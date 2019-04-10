import time
from getPlaylistSongs import runPlaylistSong
from getPlaylistInfo import runPlaylistInfo


if __name__ == '__main__':
    start_time = time.perf_counter()
    try:
        runPlaylistInfo.runPlaylistInfo()
        runPlaylistSong.runPlaylistSong()
    except Exception as e:
        print(e)
    print('last time: {}'.format(time.perf_counter() - start_time))