import vlc
import os
import random
from tkinter import Tk, Frame, Button, Listbox, Scrollbar, Label, StringVar, Entry

class MP3Player:
    def __init__(self):
        self.instance = vlc.Instance('--no-xlib')
        self.player = self.instance.media_player_new()
        self.media_list = self.instance.media_list_new()
        self.media_list_player = self.instance.media_list_player_new()
        self.media_list_player.set_media_player(self.player)

        self.current_track = None
        self.is_paused = False
        self.is_repeat = False
        self.is_random = False

        self.volume = 50

    def play(self):
        if self.current_track:
            self.player.play()

    def pause(self):
        if self.current_track:
            self.player.pause()
            self.is_paused = not self.is_paused

    def stop(self):
        self.player.stop()
        self.current_track = None

    def set_volume(self, volume):
        self.volume = volume
        self.player.audio_set_volume(volume)

    def toggle_repeat(self):
        self.is_repeat = not self.is_repeat

    def toggle_random(self):
        self.is_random = not self.is_random

    def load_track(self, track_path):
        media = self.instance.media_new(track_path)
        self.media_list.add_media(media)
        self.media_list_player.set_media_list(self.media_list)

    def play_track(self, track_path):
        self.load_track(track_path)
        self.current_track = track_path
        self.play()

    def play_next_track(self):
        if self.is_random:
            self.play_random_track()
        else:
            self.media_list_player.next()

    def play_previous_track(self):
        if self.is_random:
            self.play_random_track()
        else:
            self.media_list_player.previous()

    def play_random_track(self):
        if self.media_list.count() > 0:
            index = random.randint(0, self.media_list.count() - 1)
            self.media_list_player.play_item_at_index(index)

    def find_tracks(self, search_query):
        results = []
        for i in range(self.media_list.count()):
            media = self.media_list.item_at_index(i)
            if search_query.lower() in media.get_mrl().lower():
                results.append(media.get_mrl())
        return results

class MP3PlayerGUI:
    def __init__(self, player):
        self.player = player

        self.root = Tk()
        self.root.title("MP3 Player")

        self.track_list = Listbox(self.root)
        self.track_list.pack(side="left", fill="both", expand=True)
        self.track_list.bind("<<ListboxSelect>>", self.select_track)

        self.track_list_scrollbar = Scrollbar(self.root)
        self.track_list_scrollbar.pack(side="left", fill="y")

        self.track_list.config(yscrollcommand=self.track_list_scrollbar.set)
        self.track_list_scrollbar.config(command=self.track_list.yview)

        self.control_frame = Frame(self.root)
        self.control_frame.pack(side="top", pady=10)

        self.play_button = Button(self.control_frame, text="Play", command=self.player.play)
        self.play_button.pack(side="left", padx=5)

        self.pause_button = Button(self.control_frame, text="Pause", command=self.player.pause)
        self.pause_button.pack(side="left", padx=5)

        self.stop_button = Button(self.control_frame, text="Stop", command=self.player.stop)
        self.stop_button.pack(side="left", padx=5)

        self.volume_label = Label(self.control_frame, text="Volume:")
        self.volume_label.pack(side="left", padx=5)

        self.volume_entry = Entry(self.control_frame, width=3)
        self.volume_entry.insert(0, str(self.player.volume))
        self.volume_entry.pack(side="left", padx=5)

        self.volume_button = Button(self.control_frame, text="Set Volume", command=self.set_volume)
        self.volume_button.pack(side="left", padx=5)

        self.repeat_button = Button(self.control_frame, text="Repeat", command=self.player.toggle_repeat)
        self.repeat_button.pack(side="left", padx=5)

        self.random_button = Button(self.control_frame, text="Random", command=self.player.toggle_random)
        self.random_button.pack(side="left", padx=5)

        self.find_entry = Entry(self.root)
        self.find_entry.pack(side="top", pady=10)

        self.find_button = Button(self.root, text="Find Tracks", command=self.find_tracks)
        self.find_button.pack(side="top")

        self.now_playing = StringVar()
        self.now_playing_label = Label(self.root, textvariable=self.now_playing)
        self.now_playing_label.pack(side="top", pady=10)

    def select_track(self, event):
        selected_index = self.track_list.curselection()
        if selected_index:
            selected_track = self.track_list.get(selected_index[0])
            self.player.play_track(selected_track)

    def set_volume(self):
        volume = int(self.volume_entry.get())
        self.player.set_volume(volume)

    def find_tracks(self):
        search_query = self.find_entry.get()
        results = self.player.find_tracks(search_query)
        self.track_list.delete(0, "end")
        for track in results:
            self.track_list.insert("end", track)

    def update_now_playing(self):
        track_path = self.player.current_track
        if track_path:
            track_filename = os.path.basename(track_path)
            self.now_playing.set("Now Playing: " + track_filename)
        else:
            self.now_playing.set("")

    def run(self):
        self.root.mainloop()

# Usage example
player = MP3Player()
gui = MP3PlayerGUI(player)

# Add your files to the player
player.load_track("path/to/track1.mp3")
player.load_track("path/to/track2.wav")
player.load_track("path/to/track3.webm")
player.load_track("C:/Users/artkh/Downloads/zxcursed, mupp - haunt.mp4")

# Set the default track list
gui.track_list.insert("end", "path/to/track1.mp3")
gui.track_list.insert("end", "path/to/track2.wav")
gui.track_list.insert("end", "path/to/track3.webm")
gui.track_list.insert("end", "C:/Users/artkh/Downloads/zxcursed, mupp - haunt.mp4")

# Run the GUI
gui.run()
