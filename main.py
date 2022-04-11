from pytube import YouTube
from tkinter import Tk, filedialog
import os

link = input("Enter the link of YouTube video you want to download:  ")
try:
    yt = YouTube(link)
except:
    print(f'Video {link} is unavaialable, skipping.')

class Details:
   def info(self):
    print("Title: ",yt.title)
    print(yt.thumbnail_url)
    print("Number of views: ",yt.views," views")
    print("Length of video: ",yt.length," seconds")
    print("Rating of video: ",yt.rating)

dest = Details()
dest.info()

#to set destination folder
class destination:
    root = Tk()  # pointing root to Tk() to use it as Tk() in program.
    root.withdraw()  # Hides small tkinter window.
    ''
    root.attributes('-topmost', True)  # Opened windows will be active. above all windows despite of selection.
    ''
    open_file = filedialog.askdirectory()  # Returns opened path as str
    print(open_file)

#Starting download
#print("Downloading...")
#Getting the highest resolution possible
class MP4:
    ys = yt.streams.get_highest_resolution()
    print("Default Resolution : '",ys.resolution,"'")


class MP3:
    ys = yt.streams.filter(only_audio=True).first()


Unit = input("Please choose your desired format 'MP4' or 'MP3': ")
if Unit.upper()=='MP4':
    try:
        MP4.ys.download(destination.open_file)
        print("Download completed!!")
    except:
        print("Failed to download ",yt.title)


elif Unit.upper()=='MP3':
    try:
        out_file = MP3.ys.download(destination.open_file)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Download completed!!")
    except:
        print("Failed to download ",yt.title)

