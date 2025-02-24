import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import config
import downloader
import utils

class YTDownloader:
    def __init__(self,root):
        self.root = root
        self.root.title("Youtube Playlist Downloader ")
        self.root.geometry("500x300")

        self.url_label = tk.Label(root, text="Playlist URL: ")
        self.url_label.pack()

        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        self.folder_label = tk.Label(root, text="Save Location: ")
        self.folder_label.pack()

        self.folder_entry = tk.Entry(root, width=40)
        self.folder_entry.pack()

        self.browse_button = tk.Button(root, text="Browse", command=self.browse_folder)

        self.browse_button.pack()

        self.resolution_label = tk.Label(root, text="Resolution:  ")
        self.resolution_label.pack()

        self.resolution_var = tk.StringVar(value="720p")
        self.resolution_dropdown = tk.OptionMenu(root, self.resolution_var,"1080p","720p","480p","360p")
        self.resolution_dropdown.pack()

        self.audio_only_var = tk.BooleanVar()
        self.audio_check = tk.Checkbutton(root, text="Download Audio Only", variable= self.audio_only_var)

        self.audio_check.pack()

        self.download_button = tk.Button(root,text="Download", command=self.start_download)
        self.download_button.pack()
    
    def browse_folder(self):
        folder = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0,folder)
    
    def start_download(self):
        playlist_url = self.url_entry.get()
        output_folder = self.folder_entry.get() or config.DOWNLOAD_FOLDER
        resolution = self.resolution_var.get()
        audio_only = self.audio_only_var.get()

        if not playlist_url:
            messagebox.showerror("Error","Please enter a playlist URL")
            return

        utils.create_download_folder(output_folder)

        threading.Thread(target=downloader.download_playlist, args=(playlist_url, output_folder, resolution, audio_only)).start()
