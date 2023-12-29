# Youtube Playlist Downloader

## Description

This is a simple python script to download youtube playlist videos. It uses the `pytube` library to download the videos.
**This is meant to be used in educational purposes only.**

## WHY?

I often find myself in a situation where I want to download a playlist from youtube. I have tried many online tools but they are either slow or have a lot of ads. So I decided to make a simple script to download the videos.

## How to use?

1. Clone the repository
2. Install the requirements using `pip install -r requirements.txt`
3. Run the script using `python main.py`
4. Enter the playlist url ( or a video url that is part of the playlist )
5. Enter the folder name to save ( default is `videos/` )
6. Wait for the script to download the videos

## Note

The script will download the videos in the best quality available. If you want to download the videos in a specific quality, you can edit the `main.py` file and change the `stream.first()` to `stream.get_by_itag(22)` where `22` is the itag of the video quality you want to download. You can find the itag of the video quality from [here](https://gist.github.com/sidneys/7095afe4da4ae58694d128b1034e01e2).

> This might be implemented in the future versions of the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Author

- Nusab Taha
- [Website](https://nusab19.pages.dev)
- [Twitter](https://twitter.com/Nusab19)
- [Linkedin](https://linkedin.com/in/NusabTaha)
