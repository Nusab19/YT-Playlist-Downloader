import pytube


def onProgress(stream, _, bytesRemaining):
    totalSize = stream.filesize
    bytesRemaining = totalSize - bytesRemaining
    percentage = bytesRemaining / totalSize * 100
    print(f"Progress    :   {percentage:.2f}%\r", end="")


def downloadPlaylist(url: str, itag: int = None, outputFolder: str = "videos"):
    """Download a playlist from YouTube

    Arguments:
        url {str}           -- The playlist URL or video URL with playlist
        itag {int}          -- The itag of the video (default: None)
        outputFolder {str}  -- The output folder (default: "videos")

    """

    videos = getPlaylistVideoURLs(url)
    length = len(videos)
    prefixLength = len(str(length)) + 1

    print(f"\nFound {length} videos...\n")

    for index, url in enumerate(videos, 1):
        video = pytube.YouTube(url, on_progress_callback=onProgress)

        stream = None
        if itag:
            stream = video.streams.filter(progressive=True).get_by_itag(itag)

        if not stream:
            stream = video.streams.filter(progressive=True).get_highest_resolution()

        prefix = f"{index:0{prefixLength}}"
        fileSize = stream.filesize / 1024 / 1024
        resolution = stream.resolution
        print(f"No.{prefix} :   {video.title}...")
        print(f"FileSize    :   {fileSize:.2f} MB @ {resolution}")

        stream.download(output_path=outputFolder, max_retries=5, filename_prefix=prefix)

        print("\n")


def getAvailableResolutions(url):
    youtube = pytube.YouTube(url)
    itags = {i.itag: i.resolution for i in youtube.streams.all() if i.resolution}

    return itags


def getItagFromResolution(resolution: str):
    itags = {
        "144p": 278,
        "360p": 243,
        "720p": 247,
        "1080p": 248,
        "480p": 244,
        "240p": 242,
    }

    return itags.get(resolution)


def getPlaylistVideoURLs(playlistUrl):
    playlist = pytube.Playlist(playlistUrl)
    videoUrls = playlist.video_urls

    return videoUrls


def downloadVideo(url: str, outputFolder: str = "Videos", prefix: str = None):
    video = pytube.YouTube(url, on_progress_callback=onProgress)

    stream = video.streams.filter(progressive=True).get_highest_resolution()
    fileSize = stream.filesize / 1024 / 1024
    resolution = stream.resolution

    print(f"Downloading :   {prefix or ''}{video.title}...")
    print(f"FileSize    :   {fileSize:.2f} MB @ {resolution}")

    stream.download(output_path=outputFolder, max_retries=5, filename_prefix=prefix)
