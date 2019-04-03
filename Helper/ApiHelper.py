import subprocess
import random

def changeIP():
    try:
        with open(r"G:\163music\util\request.js", "r+", encoding="utf8") as f:
            f.seek(2782)
            random.seed(a=None)
            ip = repr(random.randint(100, 255)) + '.' + \
                repr(random.randint(100, 255))
            print(ip)
            f.write(ip)
        return ip
    except Exception as e:
        print(e)
        return None


def startApi():
    changeIP()
    p = subprocess.Popen(
        'node app.js',
        cwd=r"G:\163music",
        stdout=None,
        stderr=None)
    return p


def stopApi(p):
    p.terminate()