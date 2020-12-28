from pytube import YouTube

class videoStream:
    def __init__(self, link):
        yt = YouTube(link)
        self.streams = yt.streams.filter(type="video", file_extension="mp4")
        data = []

        self.videoInfo = {
            "author": yt.author,
            "title": yt.title,
            "data": data
        }

        for video in self.streams:
            new = {
                "res": self.sliceStreamString(str(video), "res"),
                "tag": self.sliceStreamString(str(video), "tag"),
                "fps": self.sliceStreamString(str(video), "fps")
            }
            data.append(new)

    def sliceStreamString(self, string, info):
        pos = int(string.find(info)) 
        c = pos+5

        if pos != -1:
            while string[c] != '"':
                c += 1

        return string[pos+5:c]

    def downloadVideo(self, itag, file):
        self.streams.get_by_itag(itag).download(file)

        


