from helper import downloadPlaylist, downloadVideo


if __name__ == "__main__":
    url = input("Enter video/playlist URL: ")
    if "playlist" in url:
        print("Playlist Detected")
        folderName = input("Enter the folder name: ")
        downloadPlaylist(url, outputFolder=f"videos/{folderName}")

    else:
        downloadVideo(url)
