from pytube import YouTube

link = input("Link to your video: ")
yt = YouTube(link)

print("Video description:\n")
print("Title: ", yt.title)
print("Views: ", yt.views)
print("Length: ",yt.length)

print("Downloading..")

stream = yt.streams.get_highest_resolution()

stream.download('D:\Download')
print("Success! ")

