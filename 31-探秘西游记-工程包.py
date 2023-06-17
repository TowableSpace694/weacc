import jieba
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.charts import WordCloud
#开发模式 
#统计函数
def cut_book(path,dic_path):
    #打开文件
    f = open(path,'r',encoding='gbk',errors='ignore')
    #读取文件
    txt = f.read()
    #加载自定义词典
    jieba.load_userdict(dic_path)
    #分词
    words = jieba.lcut(txt)
    res0 = {}
    res1 = {}
    li = ['悟空', '悟能', '悟净', '泼猴', '八戒']
    for i in words:
        res0[i] = res0.get(i,0) + 1
        if i in ['悟空', '悟能', '悟净', '泼猴', '八戒']:
            res1[i] = res1.get(i, 0) + 1
    f.close()
    return res0,res1
#饼图
def render_pie(data):
    #create pie
    p = Pie()
    p.add('',data)
    p.set_global_opts(title_opts=opts.TitleOpts(title='唐僧最喜欢哪个徒弟?'))
    p.render('xyj.html')
#热词
def word_cloud(data):
    c = WordCloud()
    c.add('byd',data,word_size_range=[6,80])
    c.set_global_opts(title_opts=opts.TitleOpts(title='11454'))
    c.render('wqe.html')
#主函数

def main():
    data = cut_book('西游记.txt','user_dict.txt')[1]
    data2 = cut_book('西游记.txt', 'user_dict.txt')[0]
    temp1 = []
    temp2 = []
    for i in data:
        temp1.append((i,data[i]))
        render_pie(temp1)
    for x in data2:
        if int(data2[x]) >= 5 and len(x) >= 2:
            temp2.append((x, data2[x]))
        word_cloud(temp2)
if __name__ == '__main__':
    main()