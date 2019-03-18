# NeteaseCloudMusicSpider

网易云音乐爬虫

使用[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)+requests原生爬虫，数据存入mysql。

目前问题：

- [x] 未找到效率高的高匿代理池

  目前暂时的解决方案：放弃使用代理。

- [x] 直接爬取频率过高会封IP

  目前暂时的解决方案：遇到-460cheating时，修改NeteaseCloudMusicApi/util/request.js中的X-Real-IP为任意国内IP。

  ......

---

目前获得的数据



共有159万条

---

项目暂停

TODO:

- [ ] 学习数据库知识
- [ ] 学习python面向对象相关知识