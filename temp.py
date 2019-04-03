import random
import subprocess
import time

class api():
    def __init__(self):
        self.port = random.randint(3001,4000)

    def __changeIP(self):
        pass

    def startApi(self):
        self.__changeIP()
        self.api = subprocess.Popen(
            'set PORT={} && node app.js'.format(self.port),
            cwd=r"G:\163music",
            stdout=None,
            stderr=None,
            shell=True
        )
        print('pid: {} api started port: {}'.format(self.api.pid, self.port))

    def stopApi(self):
        self.api.terminate()
        print('pid: {} api stopped'.format(self.api.pid))


api = api()
api.startApi()
time.sleep(3)
api.stopApi()

