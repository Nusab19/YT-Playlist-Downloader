import pytube


def getVideoItags(url):
    youtube = pytube.YouTube(url)
    itags = {i.itag: i.resolution for i in youtube.streams.all()
             if i.resolution}

    return itags


def getItagFromResolution(resolution: str):
    itags = {'144p': 278, '360p': 243, '720p': 247,
             '1080p': 248, '480p': 244, '240p': 242}

    return itags.get(resolution)


def getPlaylistVideoURLs(playlistUrl):
    playlist = pytube.Playlist(playlistUrl)
    videoUrls = playlist.video_urls

    return videoUrls


def on_progress(stream, chunk, bytesRemaining):
    totalSize = stream.filesize
    bytesRemaining = totalSize - bytesRemaining
    percentage = bytesRemaining / totalSize * 100
    print(f"Progress:   {percentage:.2f}%\r", end="")


def downloadPlaylist(url: str, itag: int = None, outputFolder: str = "videos"):
    """Download a playlist from YouTube

    Arguments:
        url {str} -- The playlist URL or video URL with playlist
        itag {int} -- The itag of the video (default: {None})
        outputFolder {str} -- The output folder (default: {"videos"})

    """

    videos = getPlaylistVideoURLs(url)
    length = len(videos)
    prefixLength = len(str(length))

    print(f"Found {length} videos...\n\n")

    for index, url in enumerate(videos, 1):
        video = pytube.YouTube(url, on_progress_callback=on_progress)

        stream = None
        if itag:
            stream = video.streams.filter(progressive=True).get_by_itag(itag)

        if not stream:
            stream = video.streams.filter(
                progressive=True).get_highest_resolution()

        prefix = f"{index:0{prefixLength}}"
        print(f"Downloading: {prefix} - {video.title}...")
        print(f"FileSize: {stream.filesize / 1024 / 1024:.2f} MB")

        stream.download(output_path=outputFolder,
                        max_retries=5, filename_prefix=prefix)

        print("\n")
