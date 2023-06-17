import json
import requests
from requests import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from pyecharts.charts import Line
import webbrowser
from pyecharts import options as opts
import os 
#主窗口
#天气查询定义函数
openwindows = False
strc = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0']
def renderline(time,maxc,minc):
    print('[Main]Renderline running')
    line = Line()
    line.add_xaxis(time)
    line.add_yaxis('最高温度', maxc, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max')]))
    line.add_yaxis('最低温度', minc, markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='min')]))
    line.render('temp.html')
    webbrowser.open_new_tab('temp.html')
    print('[Main]已完成进程-RenderLine,Opennewtab')


def weacc(city='河北', day=0):
    try:
        sc2.destroy()
        sct.destroy()
    except:
        pass
    global weacc
    weacc = Tk()
    weacc.geometry('250x250')
    weacc.title('weac重建')
    weacct1 = Label(weacc, text='你要查询哪天?')
    weacct1.grid(row=0, column=0, padx=(75, 0), pady=(10,0))
    weaccb1 = Button(weacc, text='查询今天', command=lambda: we(city,0))
    weaccb1.grid(row=1, column=0, padx=(75,0), pady=(10,0))
    weaccb2 = Button(weacc, text='查询明天', command=lambda: we(city,1))
    weaccb2.grid(row=2, column=0, padx=(75, 0), pady=(10, 0))
    weaccb3 = Button(weacc, text='查询后天', command=lambda: we(city,2))
    weaccb3.grid(row=3, column=0, padx=(75, 0), pady=(10, 0))
    weaccb4=Button(weacc, text='温度变化', command=lambda:line_pie(city))
    weaccb4.grid(row=4, column=0, padx=(75, 0), pady=(10, 0))
    weacc.mainloop()
def line_pie(city):
    print('[Main]line_pie runing')
    empt_data = []
    empt_maxc = []
    empt_minc = []
    dicts = we(city,1,True)
    print(dicts)
    for i in range(7):
        empt_data.append(dicts[i]['date'][8:] + '\n' +dicts[i]['wea'])
        print(dicts[i]['date'])
        empt_maxc.append(int(dicts[i]['tem_day']))
        empt_minc.append(int(dicts[i]['tem_night']))
    print(empt_data)
    print(empt_maxc)
    renderline(empt_data,empt_maxc,empt_minc)
def weaccback():
    weacc(getcity)
def sc():
    def insc():
        global getcity
        getcity = scte1.get()
        url = "https://www.yiketianqi.com/free/week?unescape=1&appid=37881928&appsecret=KdmM2njA&city=" + getcity
        respnes = requests.get(url)
        result = respnes.text
        print('查询中...')
        dicts2 = json.loads(result)
        for i in getcity:
            if i in strc:
                messagebox.showerror('提示','错误城市请重试')
                textms = '错误城市'
                break
            else:
                textms = getcity
                global sc2
                sc2 = Tk()
                sc2.geometry('250x250')
                sc2.title('搜索结果')
                sctt1 = Label(sc2, text='搜索结果:')
                sctt1.grid(row=0, column=0, padx=(75, 0), pady=(10, 0))
                sc2b2 = Button(sc2, text=textms, command=weaccback)
                sc2b2.grid(row=1, column=0, padx=(75, 0), pady=(10, 0))
                sctt1.mainloop()
                break
    global sct
    sct = Tk()
    sct.geometry('250x250')
    sct.title('weac重建-搜索')
    sctt1 = Label(sct, text='你要搜索哪个城市?')
    sctt1.grid(row=0, column=0, padx=(50, 0), pady=(10, 0))
    scte1 = Entry(sct)
    scte1.grid(row=1, column=0, padx=(50, 0), pady=(10, 0))
    sctb2 = Button(sct, text='搜索', command=lambda: insc())
    sctb2.grid(row=2, column=0, padx=(50, 0), pady=(10, 0))
    sctb2.mainloop()
    
def we(city='河北', day=0,inside=False):
    try:
        weacc.destroy()
    except:
        pass
    #得到天气7days
    url = "https://www.yiketianqi.com/free/week?unescape=1&appid=37881928&appsecret=KdmM2njA&city=" + city
    respnes = requests.get(url)
    result = respnes.text
    print('查询中...')
    dicts2 = json.loads(result)
    print('[Main_we]Cityid:' + str(city))
    print('[Main_we]day:' + str(day))
    print('[Main_we]Inside_Mode:' + str(inside))
    print('[Main_we]' + str(dicts2))
    dicts = dicts2['data']
    if inside:
        print('return')
        return dicts
    print('Done!')
    print(dicts)
    #build窗口
    weac = Tk()
    weac.geometry('200x200')
    weac.title('weac重建')
    t1 = '日期:' + dicts[day]['date']
    t2 = '天气:' + dicts[day]['wea']
    t3 = '最高温度:' + dicts[day]['tem_day']
    t4 = '最低温度:' + dicts[day]['tem_night']
    t5 = '风速+风向:' + dicts[day]['win'] + dicts[day]['win_speed']
    weact1 = Label(weac, text=t1)
    weact1.grid(row=0, column=0,padx =(10,0))
    weact2 = Label(weac, text=t2)
    weact2.grid(row=1, column=0, padx=(10, 0))
    weact3 = Label(weac, text=t3)
    weact3.grid(row=2, column=0, padx=(10, 0))
    weact3 = Label(weac, text=t4)
    weact3.grid(row=3, column=0, padx=(10, 0))
    weact4 = Label(weac, text=t5)
    weact4.grid(row=4, column=0, padx=(10, 0))
    weac.mainloop()


windows = Tk()
windows.title('weac重建计划')
windows.geometry('300x300')
# windows.grid_rowconfigure(1, weight=1)  # row为1，缩放比为1
# windows.grid_columnconfigure(0, weight=1)  # column为0，缩放比为1
Maint1 = Label(windows, text='Main')
Maint1.grid(row=0, column=0,padx = (100,0))
Mainb1 = Button(windows, text='查询',command =weacc)
Mainb1.grid(row=1, column=0, padx=(100, 0),pady=(20,0))
Mainb1 = Button(windows, text='搜索',command = lambda:sc())
Mainb1.grid(row=2, column=0, padx=(100, 0),pady=(20,0))
Mainb1 = Button(windows, text='查询本地(根据ip判断)', command =weacc)
Mainb1.grid(row=3,column=0,padx=(100,0),pady=(20,0))
windows.mainloop()
