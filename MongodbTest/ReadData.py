import pymongo
import plotly
import plotly.graph_objs as go
import sys
from functools import reduce


client = pymongo.MongoClient('localhost',27017)
db = client['163music']
cl = db['userinfos']
data = []
for item in cl.find({'LISTEN': {'$gt':50}}):
    data.append(item)
print(len(data))
# print(sys.getsizeof(data))
x = []
y = []
ids = []
for item in data:
    x.append(item['LISTEN'])
    y.append(item['FOLLOWS'])
    ids.append(item['UID'])
trace = go.Scatter(
    x = x,
    y = y,
    mode = 'markers',
    text = ids
)
fig = go.Figure(data=[trace])
plotly.offline.plot(fig, auto_open = True)
# plotly.offline.plot({
#     "data": [go.Scatter(x=x, y=y)],
#     "layout": go.Layout(title="hello world")
# }, auto_open=True)

reduce()
