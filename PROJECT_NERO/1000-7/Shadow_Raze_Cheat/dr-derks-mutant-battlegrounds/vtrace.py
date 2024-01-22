# coding=utf-8
# Copyright 2019 The SEED Authors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Functions to compute V-trace off-policy actor critic targets.

For details and theory see:

"IMPALA: Scalable Distributed Deep-RL with
Importance Weighted Actor-Learner Architectures"
by Espeholt, Soyer, Munos et al.

See https://arxiv.org/abs/1802.01561 for the full paper.
"""
import collections
import tensorflow as tf

VTraceReturns = collections.namedtuple('VTraceReturns', 'vs pg_advantages')


def from_importance_weights(
    target_action_log_probs, behaviour_action_log_probs,
    discounts, rewards, values, bootstrap_value,
    clip_rho_threshold=1.0, clip_pg_rho_threshold=1.0, lambda_=1.0,
    name='vtrace_from_importance_weights'):
  r"""V-trace from log importance weights.

  Calculates V-trace actor critic targets as described in

  "IMPALA: Scalable Distributed Deep-RL with
  Importance Weighted Actor-Learner Architectures"
  by Espeholt, Soyer, Munos et al.

  In the notation used throughout documentation and comments, T refers to the
  time dimension ranging from 0 to T-1. B refers to the batch size and
  NUM_ACTIONS refers to the number of actions. This code also supports the
  case where all tensors have the same number of additional dimensions, e.g.,
  `rewards` is [T, B, C], `values` is [T, B, C], `bootstrap_value` is [B, C].

  Args:
    target_action_log_probs: A float32 tensor of shape [T, B] with
      log-probabilities of taking the action by the current policy
    behaviour_action_log_probs: A float32 tensor of shape [T, B] with
      log-probabilities of taking the action by the behavioural policy
    discounts: A float32 tensor of shape [T, B] with discounts encountered when
      following the behaviour policy.
    rewards: A float32 tensor of shape [T, B] containing rewards generated by
      following the behaviour policy.
    values: A float32 tensor of shape [T, B] with the value function estimates
      wrt. the target policy.
    bootstrap_value: A float32 of shape [B] with the value function estimate at
      time T.
    clip_rho_threshold: A scalar float32 tensor with the clipping threshold for
      importance weights (rho) when calculating the baseline targets (vs).
      rho^bar in the paper. If None, no clipping is applied.
    clip_pg_rho_threshold: A scalar float32 tensor with the clipping threshold
      on rho_s in \rho_s \delta log \pi(a|x) (r + \gamma v_{s+1} - V(x_s)). If
      None, no clipping is applied.
    lambda_: Mix between 1-step (lambda_=0) and n-step (lambda_=1). See Remark 2
      in paper. Defaults to lambda_=1.
    name: The name scope that all V-trace operations will be created in.

  Returns:
    A VTraceReturns namedtuple (vs, pg_advantages) where:
      vs: A float32 tensor of shape [T, B]. Can be used as target to
        train a baseline (V(x_t) - vs_t)^2.
      pg_advantages: A float32 tensor of shape [T, B]. Can be used as the
        advantage in the calculation of policy gradients.
  """
  #tf.print("target_action_log_probs: ", target_action_log_probs)
  #tf.print("behaviour_action_log_probs: ", behaviour_action_log_probs)

  log_rhos = target_action_log_probs - behaviour_action_log_probs
  #tf.print("log_rhos: ", log_rhos)

  log_rhos = tf.convert_to_tensor(log_rhos, dtype=tf.float32)
  discounts = tf.convert_to_tensor(discounts, dtype=tf.float32)
  rewards = tf.convert_to_tensor(rewards, dtype=tf.float32)
  values = tf.convert_to_tensor(values, dtype=tf.float32)
  bootstrap_value = tf.convert_to_tensor(bootstrap_value, dtype=tf.float32)

  if clip_rho_threshold is not None:
    clip_rho_threshold = tf.convert_to_tensor(clip_rho_threshold, dtype=tf.float32)

  if clip_pg_rho_threshold is not None:
    clip_pg_rho_threshold = tf.convert_to_tensor(clip_pg_rho_threshold, dtype=tf.float32)

  # Make sure tensor ranks are consistent.
  rho_rank = log_rhos.shape.ndims  # Usually 2.

  values.shape.assert_has_rank(rho_rank)
  bootstrap_value.shape.assert_has_rank(rho_rank - 1)
  discounts.shape.assert_has_rank(rho_rank)
  rewards.shape.assert_has_rank(rho_rank)

  if clip_rho_threshold is not None:
    clip_rho_threshold.shape.assert_has_rank(0)

  if clip_pg_rho_threshold is not None:
    clip_pg_rho_threshold.shape.assert_has_rank(0)

  with tf.name_scope(name):
    rhos = tf.exp(log_rhos)
    #tf.print("rhos: ", rhos)
    if clip_rho_threshold is not None:
      clipped_rhos = tf.minimum(clip_rho_threshold, rhos, name='clipped_rhos')
    else:
      clipped_rhos = rhos

    #tf.print("clipped_rhos: ", clipped_rhos)

    cs = tf.minimum(1.0, rhos, name='cs')
    #tf.print("cs b: ", cs)
    cs *= tf.convert_to_tensor(lambda_, dtype=tf.float32)
    #tf.print("cs a: ", cs)

    # Append bootstrapped value to get [v1, ..., v_t+1]
    #tf.print("values[1:]: ", values[1:])
    #tf.print("tf.expand_dims(bootstrap_value, 0): ", tf.expand_dims(bootstrap_value, 0))
    values_t_plus_1 = tf.concat([values[1:], tf.expand_dims(bootstrap_value, 0)], axis=0)
    #tf.print("values_t_plus_1: ", values_t_plus_1)

    #print("rewards: ", rewards)
    #print("values_t_plus_1: ", values_t_plus_1)
    #print("values: ", values)
    deltas = clipped_rhos * (rewards + discounts * values_t_plus_1 - values)
    #tf.print("deltas: ", deltas)

    acc = tf.zeros_like(bootstrap_value)
    vs_minus_v_xs = []
    for i in range(int(discounts.shape[0]) - 1, -1, -1):
      discount, c, delta = discounts[i], cs[i], deltas[i]
      #tf.print("discount: ", discount)
      #tf.print("c: ", c)
      #tf.print("delta: ", delta)
      acc = delta + discount * c * acc
      vs_minus_v_xs.append(acc)

    vs_minus_v_xs = vs_minus_v_xs[::-1]
    #tf.print("vs_minus_v_xs: ", vs_minus_v_xs)

    # Add V(x_s) to get v_s.
    vs = tf.add(vs_minus_v_xs, values, name='vs')
    #tf.print("vs: ", vs)

    # Advantage for policy gradient.
    vs_t_plus_1 = tf.concat([vs[1:], tf.expand_dims(bootstrap_value, 0)], axis=0)
    if clip_pg_rho_threshold is not None:
      #tf.print("rhos: ", rhos)
      clipped_pg_rhos = tf.minimum(clip_pg_rho_threshold, rhos, name='clipped_pg_rhos')
      #tf.print("clipped_pg_rhos: ", clipped_pg_rhos)
    else:
      clipped_pg_rhos = rhos

    pg_advantages = (clipped_pg_rhos * (rewards + discounts * vs_t_plus_1 - values))
    #tf.print("pg_advantages: ", pg_advantages)
    #tf.print("")

    # Make sure no gradients backpropagated through the returned values.
    return VTraceReturns(vs=tf.stop_gradient(vs), pg_advantages=tf.stop_gradient(pg_advantages))
