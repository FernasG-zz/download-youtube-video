from pytube import YouTube

class downloaderManager:
    def __new__(self, link):
        yt = YouTube(link)
        videoOption = self.treatData(self, yt.streams)

        response = {
            "title": yt.title,
            "author": yt.author,
            "views": yt.views,
            "data": videoOption
        }
        return response 

    
    def treatData(self, videos):
        downloadableList = []

        for stream in videos:
            # aux = str(stream)
            print(stream["type"])

            # if aux.find("video/mp4") != -1:
            #     downloadableList.append(aux)
        
        return downloadableList                

    
    def downloadVideo(url, itag):
        pass
    
        


# def getVideos(link):
#     yt = YouTube(link)
#     print(yt.streams[1])


#     # yt.streams.filter(subtype='mp4', res='720p').order_by('resolution').first().download('./.temp')


# getVideos("https://www.youtube.com/watch?v=Vm0ivVxNaA8")