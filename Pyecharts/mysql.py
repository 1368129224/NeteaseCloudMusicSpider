import pymysql
import os
from pyecharts.charts import Pie, Funnel
from pyecharts import options as opts
from Helper.SqlHelper import getMySqlTx
from Helper import BASE_PATH


def gender(aid):
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    data = []
    cursor.execute("SELECT gender,COUNT(*) FROM {}_FansInfo GROUP BY gender".format(aid))
    for item in cursor.fetchall():
        if item[0] == '0':
            data.append(('保密', item[1]))
        elif item[0] == '1':
            data.append(('男', item[1]))
        else:
            data.append(('女', item[1]))
    db.close()
    c = (
        Pie()
            .add('性别分布', data)
            .set_global_opts(title_opts=opts.TitleOpts(title="性别分布"))
            .set_global_opts(opts.InitOpts(width='1440px'))
            .set_global_opts(opts.InitOpts(height='900px'))
    )
    c.render(os.path.join(BASE_PATH, 'Pyecharts_htmls\{}_性别分布.html'.format(aid)))

def level(aid):
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    data = []
    cursor.execute("SELECT `level`,COUNT(*) FROM {}_FansInfo GROUP BY `level`".format(aid))
    for item in cursor.fetchall():
        data.append((str(item[0]) + '级', item[1]))
    db.close()
    c = (
        Funnel()
            .add(
            "等级分布",
            data,
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="粉丝等级分布"))
            .set_global_opts(opts.InitOpts(width='1440px'))
            .set_global_opts(opts.InitOpts(height='900px'))
    )
    c.render(os.path.join(BASE_PATH, 'Pyecharts_htmls\{}_粉丝等级分布.html'.format(aid)))

