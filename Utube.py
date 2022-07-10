from pytube import Playlist

url = input('Enter the Playlist URL: ')


p = Playlist(url)
print('\n\nStats')
print(f"\nPlaylist : {p.title}\nNo. of Videos : {p.length}\nOwner : {p.owner}\nViews : {p.views}\n")

for (v,i) in zip(p.videos,range(p.length)):
    print(f"Video {i+1} : {v.title}\nRatings : {v.rating}\tViews : {v.views}\n")
    y=input('Would you like to download - Y? : ')
    if(y=='y' or y=='Y'):
        res,itag=2,22
        res = int(input(f'Resolution Option (1 or 2 or 3):\n1: 360p\n2: 720p\n3: 1080p\nEnter Resolution Option : '))
        if res==1:
            itag=18
        elif res==2:
            itag=22
        elif res==3:
            itag=137
        else: 
            print('Downloading Default Resolution : 720p')
        # print(v.streams.filter(file_extension='mp4'))
        v.streams.get_by_itag(itag).download()
    else:
        print()
        continue