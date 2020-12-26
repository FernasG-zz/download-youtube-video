from pytube import YouTube

def sliceStreamString(string, info):
    pos = int(string.find(info)) 
    c = pos+5

    if pos != -1:
        while string[c] != '"':
            c += 1

    return string[pos+5:c]

def getVideoStreams(link):
    yt = YouTube(link)
    streams = yt.streams.filter(type="video", file_extension="mp4")
    data = []

    videoInfo = {
        "author": yt.author,
        "title": yt.title,
        "data": data
    }

    for video in streams:
        new = {
            "res": sliceStreamString(str(video), "res"),
            "tag": sliceStreamString(str(video), "tag"),
            "fps": sliceStreamString(str(video), "fps")
        }
        data.append(new)

    return videoInfo


