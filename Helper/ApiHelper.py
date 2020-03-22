import random
import subprocess
import time
from config import NeteaseCloudMusicApi


catlist = {'流行':'LiuXing', '影视原声':'YingShiYuanYin', '华语':'HuaYu', '清晨':'QingChen', '怀旧':'HuaiJiu', '摇滚':'YaoGun', '夜晚':'YeWan', '清新':'QingXin', 'ACG':'ACG', '欧美':'OuMei', '儿童':'ErTong', '学习':'XueXi', '民谣':'MinYao', '浪漫':'LangMan', '日语':'RiYu', '工作':'GongZuo', '电子':'DianZi', '校园':'XiaoYuan', '性感':'XingGan', '韩语':'HanYu', '午休':'WuXiu', '游戏':'YouXi', '伤感':'ShangGan', '舞曲':'WuQu', '粤语':'YueYu', '小语种':'XiaoYuZhong', '下午茶':'XiaWuCha', '70后':'70Hou', '说唱':'ShuoChang', '治愈':'ZhiYu', '轻音乐':'QingYinYue', '放松':'FangSong', '地铁':'DiTie', '爵士':'JueShi', '90后':'90Hou', '驾车':'JiaChe', '孤独':'GuDu', '感动':'GanDong', '运动':'YunDong', '网络歌曲':'WangLuoGeQu', '乡村':'XiangCun', '兴奋':'XingFen', 'KTV':'KTV', '旅行':'LvXing', 'R&B/Soul':'RBSoul', '古典':'GuDian', '快乐':'KuaiLe', '散步':'SanBu', '经典':'JingDian', '翻唱':'FanChang', '安静':'AnJing', '民族':'MinZu', '酒吧':'JiuBa', '思念':'SiNian', '吉他':'JiTa', '英伦':'YingLun', '金属':'JinShu', '钢琴':'GangQin', '朋克':'PengKe', '器乐':'YueQi', '榜单':'BangDan', '蓝调':'LanDiao', '雷鬼':'LeiHuo', '00后':'00Hou', '世界音乐':'ShiJieYinYue', '拉丁':'LaDing', '另类/独立':'DuLi', 'New Age':'NewAge', '古风':'GuFeng', '后摇':'HouYao', 'Bossa Nova':'BossaNova'}

class api():
    def __changeIP(self):
        '''
        更改ip，需按照自己的环境修改修改的位置
        :return:
        '''
        try:
            with open(NeteaseCloudMusicApi + r"\util\request.js", "r+", encoding="utf8") as f:
                f.seek(2813)
                random.seed(a=None)
                ip = repr(random.randint(10, 100)) + '.' + \
                     repr(random.randint(10, 100))
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