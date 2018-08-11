import requests
import urllib
#from Tkinter import * 
import getmusit
import os
from tkinter import *
#v1 = StringVar()

def main():
    if not os.path.exists('./yun/'):
        os.makedirs('./yun/')
    root = Tk()                     # 创建窗口对象的背景色
    frm = Frame(root,bg='green',border=2)
    frm.grid()
    L1 = Label(frm, text="输入歌曲编号")
    L1.grid(row=0,column=0)
    #L1.pack( side = LEFT)
    E1 = Entry(frm , bd =5)
    E1.grid(row=0,column=1)

    L2 = Label(frm, text="输入歌曲名称")
    L2.grid(row=1,column=0)
    #L1.pack( side = LEFT)
    E2 = Entry(frm , bd =5)
    E2.grid(row=1,column=1)
    #E1.pack(side = RIGHT)
    B1= Button(frm,text='下载',command=lambda : downloadbyid(E1.get(),E2.get())) 
    B1.grid(row=1,column=2)

    frm2 = Frame(root,bg='red',border=2)
    frm2.grid()
    Lsinger = Label(frm2, text="输入歌手编号")
    Lsinger.grid(row=0,column=0)
    #L1.pack( side = LEFT)
    Esinger = Entry(frm2 , bd =5)
    Esinger.grid(row=0,column=1)

    #E1.pack(side = RIGHT)
    Bsinger= Button(frm2,text='下载',command=lambda : downsinger(Esinger.get())) 
    Bsinger.grid(row=1,column=2)

    frm3 = Frame(root,pady=20)
    frm3.grid()
    Llist = Label(frm3, text="输入歌单编号")
    Llist.grid(row=0,column=0)
    #L1.pack( side = LEFT)
    Elist = Entry(frm3 , bd =5)
    Elist.grid(row=0,column=1)

    #E1.pack(side = RIGHT)
    Blist= Button(frm3,text='下载',command=lambda : getlist(Elist.get())) 
    Blist.grid(row=1,column=2)
    #B1.pack()
    root.mainloop() 
  
def getlist(id):
    r=requests.get('https://music.163.com/api/playlist/detail/?id=%s'%(id))
    #r=requests.get('https://music.163.com//weapi/v3/playlist/detail?id=%s'%(id))
    arr=r.json()['result']['tracks']
    # arr=getmusit.playlist_detail(id)
    for it in arr:
        name=it['name']+'.mp3'
        mp3_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(it['id']) #音乐连接
        urllib.request.urlretrieve(mp3_url,'./yun/'+name)
        # if it['mvid']:
        #     urllib.request.urlretrieve(mp3_url,'./yun/'+name)
        print('download')
def downsinger(id):
    arr=getmusit.get_artist_music(id)
    # r=requests.get('https://music.163.com/api/playlist/detail/?id=%s'%(id))
    # arr=r.json()['result']['tracks']
    for it in arr:
        name=it['name'].replace('/','')+'.mp3'
        mp3_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(it['id']) #音乐连接
        urllib.request.urlretrieve(mp3_url,'./yun/'+name)
        print('download'+name)
def downloadbyid(v1,name):
    hname=name.replace('/','')+'.mp3'
    mp3_url = 'http://music.163.com/song/media/outer/url?id=%s.mp3'%(v1) #音乐连接
    urllib.request.urlretrieve(mp3_url,'./yun/'+hname)
    lyname=name+'.lrc'
    lyc=getmusit.get_music_lyric(v1)
    with open("./yun/"+lyname,"w") as f:
        f.write(lyc)
if __name__ =="__main__":
    main()
