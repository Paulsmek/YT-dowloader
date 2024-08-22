from pytubefix import YouTube
from pytubefix import Playlist
from sys import argv

try:
    # quick way to dowload using arguments
    try : 
        link0 = argv[1]
        yt = YouTube(link0)
        yd = yt.streams.get_highest_resolution()
        yd.download()

    # main way to dowload
    except Exception as e:
        # get what type of file to dowload
        ismp3 = input("Dowload video(0), music(1), or playlist(2)?: ")

        # handle link and dowload destination
        link = input("Enter the link here: ")
        destination = input("Enter destination, or leave empty for the current one: ")

        # empty destionation means current directory
        if destination == None : 
            destination = "."

        # handle video dowloading
        if int(ismp3) == 0:
            yt = YouTube(link)
            
            print("Title: ", yt.title)
            print("Views: ", yt.views)

            yd = yt.streams.get_highest_resolution()
            yd.download(mp3 = False, output_path = destination)

        elif int(ismp3) == 1: # handle music dowloading
            yt = YouTube(link)
            
            print("Title: ", yt.title)
            print("Views: ", yt.views)

            yd = yt.streams.get_audio_only()
            yd.download(mp3 = True, output_path = destination)

        else : # handle playlist dowloading
            pl = Playlist(link)
            print("Playlist owner: ", pl.owner)

            for videos in pl.videos:
                ys = videos.streams.get_audio_only()
                ys.download(mp3 = True, output_path = destination + "./Playlist")

    # handle exceptions and errors
except Exception as exp:
    print("Error occured", str(exp))