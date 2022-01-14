from pytube import YouTube # Install the required module using pip
# "pip install pytube"
# Author Paul Awolesi
link = input("Enter your youtube url : ")
yt = YouTube(link)
videos = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
#this will stream all the format available for the video

video = list(enumerate(videos))
# this will be index all the format in list starting with zero
for i in video:
    print(i)
    # this will print all the available format of video with proper index

print("Enter the desired option to download the format")
dn_option = int(input("Enter the option : "))
# ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download() # for downloading the video

print(" Download successfully ")