import random
import subprocess


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