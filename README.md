# NeteaseCloudMusicSpider

![](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/god.svg)

网易云音乐爬虫

使用[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)+requests原生爬虫，数据存入mysql。

目前问题：

- [x] 未找到效率高的高匿代理池

  目前暂时的解决方案：放弃使用代理。

- [x] 直接爬取频率过高会封IP

  目前暂时的解决方案：遇到-460cheating时，修改NeteaseCloudMusicApi/util/request.js中的X-Real-IP为任意国内IP。

  ......

---

## 食用指南

1. 在```/```创建**mysql.txt**，填写以下信息：
``` 
host=127.0.0.1
port=3306
user=root
passwd=passw0rd
database=163music
charset=utf8mb4
connect_timeout=180
```
2. 修改```Helper.SqlHelper.py```中的文件名为**mysql.txt**
3. 在数据库中创建```163music```database
4. enjoy!

---


### 爬取分类下的热门歌单，获取热门歌单内的歌曲，统计歌曲出现次数

* [Document](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/Document)存放一些文档

* [Helper](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/Helper)包括数据库链接字符串和[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)控制类

* [getPlaylistInfo](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getPlaylistInfo)爬取热门歌单及歌单信息

* [getPlaylistSongs](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getPlaylistSongs)爬取歌单内的所有歌曲ID

* [getSongName](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getSongName)按歌曲ID爬取歌曲名
  数据库结构：

  ![数据库结构](https://github.com/1368129224/NeteaseCloudMusicSpider/blob/master/picture/20190414103943.jpg?raw=true)

---


### 获取用户信息（早期代码，比较凌乱）

[Userinfo](https://github.com/1368129224/NeteaseCloudMusicSpider/blob/master/Userinfo.py)，目前获得的数据。

![数据](https://github.com/1368129224/NeteaseCloudMusicSpider/blob/master/picture/1552876455910.png?raw=true)

共有159万条

---

项目暂停

TODO:

- [ ] 学习数据库知识
- [ ] 学习python面向对象相关知识