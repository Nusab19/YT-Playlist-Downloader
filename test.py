import pytube

def download_youtube_video(url, itag, output_path):
    # Create a YouTube object
    youtube = pytube.YouTube(url)

    # Find the stream with the specified itag
    stream = youtube.streams.filter(file_extension=("mp4", "mp3"), progressive=True).get_by_itag(itag)

    # If the stream is not found, get the highest resolution stream
    if stream is None:
        stream = youtube.streams.filter(file_extension=("mp4", "mp3"), progressive=True).get_highest_resolution()

    # Download the stream
    stream.download(output_path=output_path)

# Example usage
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
itag = 22  # Example itag for 720p resolution
output_path = "/path/to/save/video"
download_youtube_video(video_url, itag, output_path)