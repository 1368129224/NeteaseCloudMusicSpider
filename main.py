import time
from getPlaylistSongs import runPlaylistSong
from getPlaylistInfo import runPlaylistInfo
from getSongName import runSongName
from Helper import ApiHelper


if __name__ == '__main__':
    start_time = time.perf_counter()
    iput = input('请输入分类:')
    while True:
        if iput not in ApiHelper.catlist:
            print('输入错误，请检查后重新输入!')
            iput = input('请输入分类:')
        else:
            cat = iput
            break
    try:
        runPlaylistInfo.run(cat)
        runPlaylistSong.run(cat)
        runSongName.run(cat)
    except Exception as e:
        print(e)
    print('last time: {}'.format(time.perf_counter() - start_time))