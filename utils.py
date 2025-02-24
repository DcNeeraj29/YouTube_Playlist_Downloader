import os
import logging
from tqdm import tqdm

# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

def create_download_folder(folder_path):
    """Creates a download folder if it doesn't exist"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logging.info(f"Created folder: {folder_path}")

def progress_bar(d):
    """Progress callback for yt_dlp downloads"""
    if d['status'] == 'downloading':
        total_bytes = d.get('total_bytes')
        downloaded_bytes = d.get('downloaded_bytes')
        
        if total_bytes and downloaded_bytes:
            percent = (downloaded_bytes / total_bytes) * 100
            tqdm.write(f"Downloading... {percent:.2f}% completed", end="\r")
