import os
import random
from pygame import mixer

class MP3Player:
    def __init__(self):
        self.tracks = []
        self.current_track = None
        self.volume = 0.5
        self.playing = False

    def add_track(self, file_path):
        self.tracks.append(file_path)

    def remove_track(self, file_path):
        if file_path in self.tracks:
            self.tracks.remove(file_path)

    def play(self):
        if not self.playing and self.current_track:
            mixer.init()
            mixer.music.load(self.current_track)
            mixer.music.set_volume(self.volume)
            mixer.music.play()
            self.playing = True

    def pause(self):
        if self.playing:
            mixer.music.pause()
            self.playing = False

    def resume(self):
        if not self.playing:
            mixer.music.unpause()
            self.playing = True

    def stop(self):
        mixer.music.stop()
        self.playing = False

    def repeat(self):
        if self.current_track:
            mixer.music.play()

    def choose_track(self, track_index):
        if 0 <= track_index < len(self.tracks):
            self.stop()
            self.current_track = self.tracks[track_index]

    def next_track(self):
        if self.current_track:
            current_index = self.tracks.index(self.current_track)
            next_index = (current_index + 1) % len(self.tracks)
            self.choose_track(next_index)
            self.play()

    def previous_track(self):
        if self.current_track:
            current_index = self.tracks.index(self.current_track)
            prev_index = (current_index - 1) % len(self.tracks)
            self.choose_track(prev_index)
            self.play()

    def randomize_tracks(self):
        random.shuffle(self.tracks)

    def find_track(self, query):
        matches = []
        for track in self.tracks:
            if query.lower() in os.path.basename(track).lower():
                matches.append(track)
        return matches

    def set_volume(self, volume):
        if 0 <= volume <= 1:
            self.volume = volume
            if self.current_track:
                mixer.music.set_volume(volume)

    def get_current_track(self):
        return self.current_track


# Example usage:

player = MP3Player()
player.add_track("song1.mp3")
player.add_track("song2.wav")
player.add_track("song3.webm")
player.add_track("zxcursed, mupp - haunt.mp4")

player.choose_track(0)
player.play()

while True:
    command = input("Enter a command: ")
    if command == "pause":
        player.pause()
    elif command == "resume":
        player.resume()
    elif command == "stop":
        player.stop()
    elif command == "repeat":
        player.repeat()
    elif command == "next":
        player.next_track()
    elif command == "previous":
        player.previous_track()
    elif command == "randomize":
        player.randomize_tracks()
    elif command.startswith("find "):
        query = command.split(" ", 1)[1]
        matches = player.find_track(query)
        if matches:
            print("Matching tracks:")
            for match in matches:
                print(match)
        else:
            print("No matching tracks found.")
    elif command.startswith("volume "):
        volume = float(command.split(" ", 1)[1])
        player.set_volume(volume)
    elif command == "current":
        current_track = player.get_current_track()
        if current_track:
            print("Current track:", current_track)
        else:
            print("No track is currently playing.")
    elif command == "exit":
        player.stop()
        break
