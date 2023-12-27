from helper import downloadPlaylist


if __name__ == "__main__":
    url = input("Enter the playlist URL: ")
    folderName = input("Enter the folder name: ")

    downloadPlaylist(url, outputFolder=f"videos/{folderName}")
