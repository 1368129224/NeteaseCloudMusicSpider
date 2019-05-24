import pkuseg

seg = pkuseg.pkuseg()
text = seg.cut('Redmi K20 已经可以定金预售了，骁龙 855、索尼 4800 万、4000mAh 电池、升降式前置、屏幕指纹识别……等个售价吧（隐约有种 K20 会比米酒卖的还好的预感')
print(text)