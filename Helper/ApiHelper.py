import random
import subprocess
import time
import signal


class api():
    def __init__(self):
        self.port = random.randint(3001, 4000)

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
            'set PORT={} && node app.js'.format(self.port),
            cwd=r"G:\163music",
            stdout=None,
            stderr=None,
            shell=True
        )
        print('pid: {} api started port: {}'.format(self.__api.pid, self.port))

    def stopApi(self):
        self.__api.send_signal(signal.CTRL_C_EVENT)
        # self.__api.terminate()