import os
import random
import tkinter as tk
from tkinter import filedialog
import pygame
import vlc



class MusicPlayer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Music Player")

        # Create buttons
        self.play_button = tk.Button(self.window, text="Play", command=self.play_music)
        self.pause_button = tk.Button(self.window, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(self.window, text="Next", command=self.play_next_track)
        self.prev_button = tk.Button(self.window, text="Previous", command=self.play_previous_track)
        self.repeat_button = tk.Button(self.window, text="Repeat(Off)", command=self.toggle_repeat)
        self.random_button = tk.Button(self.window, text="Randomize (Off)", command=self.toggle_randomize)
        self.select_folder_button = tk.Button(self.window, text="Find Track In Files", command=self.select_music_folder)
        self.select_track_button = tk.Button(self.window, text="Choose Track", command=self.select_track)

        # Create volume control
        self.volume_scale = tk.Scale(self.window, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL,
                                     command=self.set_volume)

        # Create track selection
        self.track_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)

        # Create track information display
        self.track_label = tk.Label(self.window, text="No song playing.")

        # Position the GUI elements
        self.track_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.play_button.pack()
        self.pause_button.pack()
        self.stop_button.pack()
        self.next_button.pack()
        self.prev_button.pack()
        self.repeat_button.pack()
        self.random_button.pack()
        self.volume_scale.pack()
        self.select_folder_button.pack()
        self.select_track_button.pack()
        self.track_label.pack()

        # Initialize pygame mixer
        pygame.mixer.init()

        # Initialize VLC player
        self.vlc_player = vlc.MediaPlayer()

        # Set the initial volume
        self.set_volume(0.5)

        # Initialize music directory and track list
        directory = "C:/Users/artkh/Downloads/"
        self.music_directory = directory
        self.music_files = []
        self.current_track_index = 0

        # Set playback options
        self.repeat = False
        self.randomize = False


    def load_tracks(self):
        self.track_listbox.delete(0, tk.END)
        for track in self.music_files:
            self.track_listbox.insert(tk.END, os.path.basename(track))

    def play_music(self):
        if self.current_track_index < len(self.music_files):
            music_file = self.music_files[self.current_track_index]
            pygame.mixer.music.load(music_file)
            pygame.mixer.music.play()
            self.track_label.config(text="Now playing: " + os.path.basename(music_file))

    def pause_music(self):
        pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.track_label.config(text="No song playing.")

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(float(volume))

    def play_next_track(self):
        self.stop_music()
        if self.randomize:
            self.current_track_index = random.randint(0, len(self.music_files) - 1)
        elif self.repeat:
            self.current_track_index = self.current_track_index
        else:
            self.current_track_index = (self.current_track_index + 1) % len(self.music_files)
        self.play_music()

    def play_previous_track(self):
        self.stop_music()
        if self.randomize:
            self.current_track_index = random.randint(0, len(self.music_files) - 1)
        elif self.repeat:
            self.current_track_index = self.current_track_index
        else:
            self.current_track_index = (self.current_track_index - 1) % len(self.music_files)
        self.play_music()

    def toggle_repeat(self):
        self.repeat = not self.repeat
        self.repeat_button.config(text="Repeat (On)" if self.repeat else "Repeat (Off)")

    def toggle_randomize(self):
        self.randomize = not self.randomize
        self.random_button.config(text="Randomize (On)" if self.randomize else "Randomize (Off)")

    def select_track(self):
        selected_index = self.track_listbox.curselection()
        if selected_index:
            self.stop_music()
            self.current_track_index = selected_index[0]
            self.play_music()


    def select_music_folder(self):
        self.music_directory = filedialog.askdirectory(title="Select Music Directory")
        self.music_files = self.explore_directory(self.music_directory)
        self.load_tracks()
        self.current_track_index = 0

    def explore_directory(directory):
        supported_extensions = (".mp3", ".wav", ".mp4", ".webm")
        media_files = []

        for root, dirs, files in os.walk(directory):
            for file in files:
                _, ext = os.path.splitext(file)
                if ext.lower() in supported_extensions:
                    media_files.append(os.path.join(root, file))

        return media_files

    # Example usage
    directory = "C:/Users/artkh/Downloads/"  # Replace with the directory you want to search


player = MusicPlayer()
player.window.mainloop()
