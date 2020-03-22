# NeteaseCloudMusicSpider

![](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/god.svg)

**初学Python时期的代码，逻辑流程语法皆有不足，请谅解。**

**初学Python时期的代码，逻辑流程语法皆有不足，请谅解。**

**初学Python时期的代码，逻辑流程语法皆有不足，请谅解。**



网易云音乐爬虫

使用[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)+requests原生爬虫，数据存入MySql，并进行简单的数据分析及可视化。

网易云音乐网页端是动态网页需要使用Selenium/PhantomJS进行爬取。由于时间和技术问题，项目直接从API爬取数据。采用第三方API服务，它对官方API进行了整理及封装，方便使用，[API文档](https://binaryify.github.io/NeteaseCloudMusicApi)。

感谢[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)项目及项目贡献者。

---

# 食用指南

1. 安装node js
2. `git clone https://github.com/Binaryify/NeteaseCloudMusicApi`
3. `git clone https://github.com/1368129224/NeteaseCloudMusicSpider`
4. 取消NeteaseCloudMusicApi\util\request.js第42行注释。
5. 在NeteaseCloudMusicSpider目录中`pip install -r packages.txt`
6. 复制NeteaseCloudMusicSpider\config.sample.py为config.py，并按实际修改。
7. `python run.py`

---

## 爬取成果

![数据库](<https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Pictures/163music_new.jpg>)

<center>50张评论表、歌手粉丝表、歌手表、热门歌曲表。</center>

![167705的评论](https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Pictures/167705_Comments.jpg)

<center>由于网易云音乐官方API限制，每首歌只能获取最新和最旧各5100条评论，每首歌大约10k条评论。</center>

![5771的粉丝信息](https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Pictures/5771_FansInfo.jpg)

<center>歌手粉丝表</center>

![5771的热门歌曲](https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Pictures/T_HotSongs.jpg)

<center>热门歌曲表</center>

![幻听词云](https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Wordcloud_pictures/167655.png)

<center>幻听 词云</center>

![粉丝分布热力图](https://raw.githubusercontent.com/1368129224/NeteaseCloudMusicSpider/master/Pictures/5771_HeatMap.jpg)

<center><a href="https://github.com/1368129224/NeteaseCloudMusicSpider/blob/master/Wordcloud_pictures/Heat_map/5771.html">粉丝分布热力图</a></center>

