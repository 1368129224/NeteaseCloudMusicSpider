import pymysql
from Helper import SqlHelper,ApiHelper


def main():
    for item in ApiHelper.catlist:
        print(item)
    iput = input()
    if iput in ApiHelper.catlist:
        print('y')


if __name__ == '__main__':
    main()