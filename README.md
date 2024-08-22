This Python script allows you to download videos, audio files, or entire playlists from YouTube using the pytubefix library. It provides two main methods for downloading: a quick method using command-line arguments and an interactive method for more flexibility.

Requirements : Python 3.x, pytubefix library

To install the required library, run: "pip install pytubefix"

Usage :
1. Quick Download Using Command-Line Arguments
You can download a YouTube video directly by passing the video link as a command-line argument. This will download the video in the highest resolution available.

  Command: "python downloader.py <YouTube Video URL>"

2. Interactive Download
If you don't provide a link as a command-line argument, the script will enter an interactive mode where you can specify the type of download you want (video, audio, or playlist) and provide the necessary details.

Steps:

--Select Download Type:

Video: Enter 0

Music (audio only): Enter 1

Playlist: Enter 2

--Enter the YouTube Link: Provide the URL of the video or playlist.

--Specify Download Destination: ... | You can enter a specific directory path.
If left empty, the files will be downloaded to the current directory.
Example:
python downloader.py


Sample Input During Execution:

Download video(0), music(1), or playlist(2)?: 1

Enter the link here: https://www.youtube.com/watch?v=dQw4w9WgXcQ

Enter destination, or leave empty for the current one: /path/to/destination

Playlist Download :

When downloading a playlist, all videos will be downloaded as audio files and saved in a subdirectory named Playlist under the specified destination.

Error Handling :

If any error occurs during the execution, the script will catch the exception and print an error message to the console.


Notes :

Ensure that the pytubefix library is installed and up-to-date to avoid compatibility issues.
The script currently supports downloading only the highest resolution for videos and audio-only streams.


License :

This script is open-source and can be used and modified freely.
