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

* Helper
	* ApiHelper为api控制类。

	* SqlHelper为数据库链接字符串。

	* models为数据库建表相关。

* Document
  * 一些文档(暂未更新)

* Spiders
  * mongodb爬取数据储存到mongodb。
  * mysql(暂未完成)爬取数据储存到mysql。

* wordcloud_test
  * test分词及词云制作测试。



run、test(测试)项目入口

---

## 以下早期代码

### ~~爬取分类下的热门歌单，获取热门歌单内的歌曲，统计歌曲出现次数~~

* ~~[Document](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/Document)存放一些文档~~

* ~~[Helper](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/Helper)包括数据库链接字符串和[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)控制类~~

* ~~[getPlaylistInfo](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getPlaylistInfo)爬取热门歌单及歌单信息~~

* ~~[getPlaylistSongs](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getPlaylistSongs)爬取歌单内的所有歌曲ID~~

* ~~[getSongName](https://github.com/1368129224/NeteaseCloudMusicSpider/tree/master/getSongName)按歌曲ID爬取歌曲名~~
  ~~数据库结构：~~

  ![数据库结构](https://github.com/1368129224/NeteaseCloudMusicSpider/blob/master/picture/20190414103943.jpg?raw=true)



