# NeteaseCloudMusicSpider

![](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/god.svg)

网易云音乐爬虫

使用[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)+requests原生爬虫，数据存入MySql，并进行简单的数据分析及可视化。



网易云音乐网页端是动态网页需要使用Selenium/PhantomJS进行爬取。由于时间和技术问题，项目直接从API爬取数据。采用第三方API服务，它对官方API进行了整理及封装，方便使用，[API文档](https://binaryify.github.io/NeteaseCloudMusicApi)。

感谢[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)项目及项目贡献者。

---

* Document

  * 一些文档(暂未更新)
    * 163music.pdman.json:由[PDMan](https://gitee.com/robergroup/pdman)创建的数据库模型
    * catlist.txt:歌单分类
    * loccodes.txt:行政区划分代码
    * template.html:HeatMap模板
    * 开发文档.md(暂未更新)


* Helper
	* ApiHelper.py为api控制类。

	* SqlHelper.py为数据库链接字符串。

	* models.py为数据库建表相关。

	  其中T_Artists、T_HotSongs为所有歌手共用，{}_Comments参数为歌曲ID，{}_FansInfo参数为歌手ID。
	
	  * T_Artists
	
	    id|name
	
	  * T_HotSongs
	
	    id|rating|name|aid
	  
	  * {}_Comments
	  
	    cid|sid|likeCount|uid|uname|content
	  
	  
	  * {}_FansInfo
	  
	    id|nickname|gender|level|city|followeds|follows|playlists
	  
	
* Spiders

  * mongodb.py爬取数据储存到mongodb(暂时弃置)。

  * mysq.py爬取数据储存到MySql。

    具体请查阅源文件。

    * get_artist_id(name, api)
    * get_songs(artist_info, api)
    * request_comment(url, song_info, api)
    * get_comments_multi_thread(song_info, api)
    * get_fans_infos_multi_thread(aid, api)
    * request_info(aid, uid, api)

* Wordcloud
  
  * mysql.py
  
    分词、绘制词云及热力图。
  
    具体请查阅源文件。
  
    * get_comments(id)
    * get_ids(aid)
    * partition(comments)
    * word_count(word_list)
    * draw_picture(word_counts, sid)
    * request_loccodes()
    * get_loccodes()
    * get_city(aid)
    * getlnglat(citys)
    * generate_map(aid, loc_counts)

  * picture.png词云遮罩。

* Wordcloud_pictures

    * Heat_map

      * {}.html歌手粉丝分布热力图静态网页，参数为歌手ID。
    * {}.png歌曲评论词云图，参数为歌曲ID。

* old早期代码(弃置)。


* run项目入口。

* test测试文件。

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

