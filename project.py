import os
import datetime
import time
import clock
import urllib.request
from xml.etree import ElementTree
from tkinter import *
y=93
stop=0
def second():
    global sectk
    global sc
    sectk=Tk()
    sectk.title("Секундомер")
    sc=Canvas(sectk,width=300,height=300)
    st=Button(sectk,text="Старт",width=15,height=2,bg="#00FF00",fg="#0000ff",font="Arial 20 bold",command=start)
    st2=Button(sectk,text="Стоп",width=15,height=2,bg="#00FF00",fg="red",font="Arial 20 bold",command=stop)
    kt=Button(sectk,text="Круг",width=15,height=2,bg="#00FF00",fg="#0000ff",font="Arial 20 bold",command=krug)
    sc.pack()
    st.pack()
    st2.pack()
    kt.pack()
def start():
    global stop
    global a
    global t
    stop=0
    try:
        sc.delete(t)
    except:
        pass
    try:
        h=0
        m=0
        s=0
        ms=0
        while True:
            if ms<10:
                ms2="0"+str(ms)
            else:
                ms2=ms
            if s<10:
                s2="0"+str(s)
            else:
                s2=s
            if m<10:
                m2="0"+str(m)
            else:
                m2=m
            if h<10:
                h2="0"+str(h)
            else:
                h2=h
            a=str(h2)+":"+str(m2)+":"+str(s2)+":"+str(ms2)
            t=sc.create_text(150,60,text=a,fill="#0000ff",font="Arial 20 bold")
            sectk.update()
            ms+=1
            if ms==100:
                ms=0
                s+=1
            if s==60:
                s=0
                m+=1
            if m==60:
                m=0
                h+=1
            if stop==1:
                break
            time.sleep(0.01)
            sc.delete(t)
    except:
        pass
def krug():
    global y
    if y>=317:
        y=93
        sc.delete("all")
        k=sc.create_text(150,y,text=a,fill="red",font="Arial 20 bold")
        y+=28
    elif stop==1:
        pass
    else:
        k=sc.create_text(150,y,text=a,fill="red",font="Arial 20 bold")
        y+=28
def stop():
    global t
    global stop
    global y
    stop=1
    sc.delete(t)
    t=sc.create_text(150,60,text=a,fill="#0000ff",font="Arial 20 bold")
def calc():
    os.startfile("C:\windows\system32\calc.exe")
def date():
    try:
        tkdate=Tk()
        tkdate.title("Дата и время")
        dc=Canvas(tkdate,width=300,height=200,bg="lightgreen")
        dc.pack()
        while True:
            now=time.strftime("%m:%d:%Y\n  %H:%M:%S")
            d=dc.create_text(150,100,text=now,fill="red",font="Arial 25 bold")
            tkdate.update()
            dc.delete(d)
    except:
        pass
def ngtime():
    try:
        ngtk=Tk()
        ngtk.title("Время до нового года")
        nc=Canvas(ngtk,width=800,height=200,bg="#f7a502")
        nc.pack()
        while True:
            delta=str(datetime.datetime(2018,1,1,00,00,00)-datetime.datetime.now())
            f=delta.find(".")
            delta=delta[0:f]
            f=delta.find(":")
            delta=delta[:f]+" hours, "+delta[f+1:]
            f=delta.find(":")
            delta=delta[:f]+" minutes, "+delta[f+1:]
            delta=delta+" seconds."
            n=nc.create_text(400,100,text=delta,fill="#ffffff",font="Arial 24 bold")
            ngtk.update()
            nc.delete(n)
    except:
        pass
def time1():
    chooze=Tk()
    chooze.title("Выбор города")
    moscow=Button(chooze,text="Москва",command=clock.moscow)
    london=Button(chooze,text="Лондон",command=clock.london)
    tokyo=Button(chooze,text="Токио",command=clock.tokyo)
    new_york=Button(chooze,text="Нью-йорк",command=clock.new_york)
    paris=Button(chooze,text="Париж",command=clock.paris)
    moscow.pack()
    london.pack()
    tokyo.pack()
    new_york.pack()
    paris.pack()
def opr():
    m=int(time.strftime("%m"))
    d=int(time.strftime("%d"))
    opr=Tk()
    opr.title("Ближайшие праздники")
    oprc=Canvas(opr,height=400,width=1000,bg="#007faa")
    oprc.pack()
    if m==9 and d>=2 or 10<=m<=12:
        hol="Новый Год"
    elif m==1 and 1<=d<=6:
        hol="Рождество (7 января)"
    elif m==1 and 7<=d<=10:
        hol="День рождения Игоря (11 января)"
    elif m==1 and 11<=d<=26:
        hol="День рождения Макса (27 января)"
    elif m==1 and d>=27 or m==2 and 1<=d<=13:
       hol="День святого Валентина (14 февраля)"
    elif m==2 and 14<=d<=22:
        hol="День защитника Oтечества (23 февраля)"
    elif m==2 and d>=23 or m==3 and 1<=d<=7:
        hol="Международный женский день (8 марта) "
    elif m==3 and d>=8 or m==4 or m==5 and 1<=d<=8:
        hol="День победы (9 мая)"
    elif m==5 and d>=9 or 6<=m<=8:
        hol="траурный день (1 сентября)"
    elif m==9 and d==1:
        hol="День рождения Саши (2 сентября)"
    oprc.create_text(500,200,text="Ближайший праздник: "+hol,fill="yellow",font="Arial 25 bold")
def val():
    valute=Tk()
    valute.title("Курс валют")
    valc=Canvas(valute,height=500,width=500)
    valc.pack()
    for line in ElementTree.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")).findall("Valute"):
        if line.get("ID")=="R01235":
            dollar=valc.create_text(50,20,text=float(line.find("Value").text.replace(",",".")))
        if line.get("ID")=="R01239":
            euro=valc.create_text(50,40,text=float(line.find("Value").text.replace(",",".")))
val()
