import time
from getPlaylistSongs import runPlaylistSong


if __name__ == '__main__':
    start_time = time.perf_counter()
    try:
        runPlaylistSong.runPlaylistSong()
    except Exception as e:
        print(e)
    print('last time: {}'.format(time.perf_counter() - start_time))