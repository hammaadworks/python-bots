from pytube import Playlist

def download_playlist_videos():
    """Downloads videos from a YouTube playlist based on user input.

    Prompts the user for a playlist URL, displays playlist information, 
    and then iterates through each video in the playlist, prompting the user 
    if they wish to download the video. If yes, the user is prompted to select
    a resolution, and the video is downloaded.

    Args:
        None
    
    Returns:
        None
    """
    url = input('Enter the Playlist URL: ')

    p = Playlist(url)
    print('\n\nStats')
    print(f"\nPlaylist : {p.title}\nNo. of Videos : {p.length}\nOwner : {p.owner}\nViews : {p.views}\n")

    for (v, i) in zip(p.videos, range(p.length)):
        print(f"Video {i+1} : {v.title}\nRatings : {v.rating}\tViews : {v.views}\n")
        y = input('Would you like to download - Y? : ')
        if y.lower() == 'y':
            res, itag = 2, 22
            res = int(input(f'Resolution Option (1 or 2 or 3):\n1: 360p\n2: 720p\n3: 1080p\nEnter Resolution Option : '))
            if res == 1:
                itag = 18
            elif res == 2:
                itag = 22
            elif res == 3:
                itag = 137
            else:
                print('Downloading Default Resolution : 720p')
            # print(v.streams.filter(file_extension='mp4'))
            try:
                v.streams.get_by_itag(itag).download()
            except AttributeError:
                print(f"Error: Could not download video {v.title} with itag {itag}. It may not be available in that resolution.")
        else:
            print()
            continue

if __name__ == "__main__":
    download_playlist_videos()