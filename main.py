import pytube

# where to save
SAVE_PATH = "C:/Users/arawa/Downloads/"

# link
link = input("Please enter the link :")

try:
	# yt = YouTube(link)
	mp4files = YouTube(link).streams.filter('mp4')
	d_video = YouTube(link).get(mp4files[-1].extension, mp4files[-1].resolution)
except:
	print("Connection Error else invalid input!") #to handle exception

# filters out all the files with "mp4" extension
# mp4files = yt.streams.filter('mp4')


# d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
	# downloading the video
	d_video = YouTube(link).get(mp4files[-1].extension,mp4files[-1].resolution)
except:
	print("Some Error!")
print('Task Completed!')
