import sys

if __name__ =="__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--cli":
        import downloader
        import config
        import utils
    
        playlist_url = input("Enter YouTube Playlist URL: ")
        utils.create_download_folder(config.DOWNLOAD_FOLDER)
        downloader.download_playlist(playlist_url, config.VIDEO_RESOLUTION, config.AUDIO_ONLY)

    else:
        import gui
        from tkinter import Tk
        
        root = Tk()
        app = gui.YTDownloader(root)
        root.mainloop()
