from yt_dlp import YoutubeDL
import os
import config
import utils
import threading
import time
import subprocess

def is_ffmpeg_installed():
    """Check if ffmpeg is available in the system PATH"""
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except FileNotFoundError:
        return False

def get_ydl_opts(output_folder, resolution="720p", audio_only=False):
    """Generate yt-dlp options based on configuration"""
    opts = {
        'format': 'best' if not is_ffmpeg_installed() else f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'progress_hooks': [utils.progress_bar],
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
    }
    
    if audio_only and is_ffmpeg_installed():
        opts['format'] = 'bestaudio/best'
        opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    elif audio_only:
        print("⚠️ FFmpeg is not installed - downloading audio as video file")
        opts['format'] = 'bestaudio[ext=m4a]/bestaudio'
    
    return opts

def download_video(video_url, output_folder, resolution="720p", audio_only=False):
    """Download a single video using yt-dlp"""
    try:
        ydl_opts = get_ydl_opts(output_folder, resolution, audio_only)
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            print(f"✅ Download complete: {info_dict.get('title', 'Unknown')}")
    except Exception as e:
        print(f"❌ Error downloading {video_url}: {e}")

def download_playlist(playlist_url, output_folder, resolution="720p", audio_only=False):
    """Download a playlist using yt-dlp"""
    try:
        ydl_opts = get_ydl_opts(output_folder, resolution, audio_only)
        ydl_opts['noplaylist'] = False
        
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=True)
            print(f"\n🔗 Playlist Title: {info_dict.get('title', 'Unknown')}")
            print(f"🎥 Total Videos: {len(info_dict.get('entries', []))}\n")
    except Exception as e:
        print(f"❌ Error downloading playlist {playlist_url}: {e}")
