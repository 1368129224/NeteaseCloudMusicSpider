from pyecharts.charts import Bar, Pie, Funnel, Scatter, ThemeRiver, Line
from pyecharts import options as opts
from example.commons import Faker
from Pyecharts import mysql as pemysql
# from pyecharts.render import make_snapshot
# from snapshot_selenium import snapshot

# test
bar = (
    Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
    # 或者直接使用字典参数
    # .set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})
)

# 性别分布
pie = (
    Pie()
        .add('男女分布',[('男',122085),('女',80631),('保密',31055)])
        .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
)

# 用户等级分布
c = (
    Funnel()
        .add(
        "等级分布",
        [(0,730),(1,1471),(2,1768),(3,3914),(4,5929),(5,15821),(6,34954),(7,76019),(8,69751),(9,21495),(10,2288)],
        sort_="ascending",
        label_opts=opts.LabelOpts(position="inside"),
    )
        .set_global_opts(title_opts=opts.TitleOpts(title="用户等级分布"))
)

# 歌单数和粉丝数的关系
d = (
    Scatter()
        .add_xaxis([i for i in range(0,13)])
        .add_yaxis("粉丝数",[j for j in range(100, 1300, 100)])
        .set_global_opts(title_opts=opts.TitleOpts(title="歌单数和粉丝数关系"))
)

# 男女粉丝的粉丝数TOP10
ee = (
    Line()
        .add_xaxis([str(i) for i in range(1, 11)])
        .add_yaxis("男性", [2331948,436372,328108,254534,146967,78094,76079,67013,65588,63676])
        .add_yaxis("女性", [273930,207547,138289,132198,88809,47306,39272,36877,35043,34579])
        .set_global_opts(title_opts=opts.TitleOpts(title="男女粉丝的粉丝数TOP10"))
)

e = (
    Line()
        .add_xaxis([i for i in range(1,9)])
        .add_yaxis("A", Faker.values())
        .add_yaxis("B", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="测试"))
)

# e.render('mycharts.html')
# ee.render('test.html')
# make_snapshot(snapshot, pie.render(), "pie.png")

pemysql.gender(5771)
pemysql.level(5771)