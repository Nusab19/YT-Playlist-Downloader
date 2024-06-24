import os
from helper import downloadVideo

filePath = "links.txt"
if not os.path.exists(filePath):
    raise FileNotFoundError(f"Could not find {filePath}")


with open(filePath, "r", encoding="utf8") as f:
    links = f.read().split()


for index, link in enumerate(links, 1):
    prefix = "{index:03}."
    downloadVideo(link, prefix=prefix)
