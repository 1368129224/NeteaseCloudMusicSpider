import pymysql
import os
from pyecharts.charts import Pie, Funnel, Line
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
        Pie(init_opts=opts.InitOpts(width='1900px', height='900px', page_title='粉丝性别分布'.format(aid)))
            .add('性别分布', data)
            .set_global_opts(title_opts=opts.TitleOpts(title="性别分布"))
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
        Funnel(init_opts=opts.InitOpts(width='1900px', height='900px', page_title='粉丝等级分布'.format(aid)))
            .add(
            "等级分布",
            data,
            sort_="ascending",
            label_opts=opts.LabelOpts(position="inside"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="粉丝等级分布"))
    )
    c.render(os.path.join(BASE_PATH, 'Pyecharts_htmls\{}_粉丝等级分布.html'.format(aid)))

def top20_fans(aid):
    # 男女粉丝的粉丝数TOP10
    db = pymysql.connect(**getMySqlTx())
    cursor = db.cursor()
    m_data = []
    f_data = []
    cursor.execute("SELECT followeds FROM {}_FansInfo WHERE gender = 1 GROUP BY followeds ORDER BY followeds DESC LIMIT 21;".format(aid))
    for i,item in enumerate(cursor.fetchall()):
        if i != 0:
            m_data.append(item[0])
    cursor.execute("SELECT followeds FROM {}_FansInfo WHERE gender = 2 GROUP BY followeds ORDER BY followeds DESC LIMIT 20;".format(aid))
    for item in cursor.fetchall():
        f_data.append(item[0])
    db.close()
    c = (
        Line(init_opts=opts.InitOpts(width='1900px', height='900px', page_title='男女粉丝的粉丝数TOP20'.format(aid)))
            .add_xaxis([str(i) for i in range(1, 21)])
            .add_yaxis("男性", m_data)
            .add_yaxis("女性", f_data)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="男女粉丝的粉丝数TOP20"),
                toolbox_opts=opts.ToolboxOpts(is_show=True),
                tooltip_opts=opts.TooltipOpts(is_show=True)
        )
    )
    c.render(os.path.join(BASE_PATH, 'Pyecharts_htmls\{}_男女粉丝的粉丝数TOP20.html'.format(aid)))

