# NeteaseCloudMusicSpider

![](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/god.svg)

网易云音乐爬虫

爬虫部分：

使用[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)+requests原生爬虫，数据存入MongoDB，提供取数据的接口。

数据分析部分：

由[@songsiyang](https://github.com/songsiyang)负责。

感谢[NeteaseCloudMusicApi](https://github.com/Binaryify/NeteaseCloudMusicApi)项目及项目贡献者。

# 食用指南

1. 安装node js
2. `git clone https://github.com/Binaryify/NeteaseCloudMusicApi`
3. `git clone https://github.com/1368129224/NeteaseCloudMusicSpider`
4. 取消NeteaseCloudMusicApi\util\request.js第42行注释。
5. 在NeteaseCloudMusicSpider目录中`pip install -r packages.txt`
6. 复制NeteaseCloudMusicSpider\config.sample.py为config.py，并按实际修改。
7. `python main.py`