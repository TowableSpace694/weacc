import csv
from pyecharts.charts import Line
def get_data(path):
    f = csv.reader(open(path,'r',encoding='utf-8'))
    flist = list(f)[1:]
    age = []
    girl = []
    boy = []
    for x in flist:
        age.append(x[0])
        girl.append(x[1])
        boy.append(x[2])
    return age,girl,boy
print(get_data('男女身高.csv'))
def renderline(age,girl,boy,name):
    line = Line()
    line.add_xaxis(age)
    line.add_yaxis('girl',girl)
    line.add_yaxis('boy',boy)
    line.render(name +'.html')
empt1 = get_data('男女身高.csv')
renderline(empt1[0],empt1[1],empt1[2],'nmaeee')