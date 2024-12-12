import yt_dlp

def download_youtube_video(url, save_path="."):
    try:
        ydl_opts = {
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'format': 'best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
            print(f"Download complete: {file_path}")
            return file_path
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_directory = input("Enter the directory to save the video (leave blank for current directory): ").strip() or "."
    download_youtube_video(video_url, save_directory)
