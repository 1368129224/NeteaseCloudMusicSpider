import random
import subprocess
import time
import signal


class api():
    def __changeIP(self):
        try:
            with open(r"G:\163music\util\request.js", "r+", encoding="utf8") as f:
                f.seek(2782)
                random.seed(a=None)
                ip = repr(random.randint(100, 255)) + '.' + \
                     repr(random.randint(100, 255))
                f.write(ip)
            return ip
        except Exception as e:
            print(e)
            return None

    def startApi(self):
        self.__changeIP()
        self.__api = subprocess.Popen(
            'node app.js',
            cwd=r"G:\163music",
            stdout=None,
            stderr=None
        )
        print('pid: {} api started'.format(self.__api.pid))

    def stopApi(self):
        self.__api.terminate()

if __name__ == '__main__':
    # test
    api = api()
    api.startApi()
    time.sleep(10)
    api.stopApi()