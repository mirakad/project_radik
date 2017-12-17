from tkinter import * 
import project
import time
import urllib.request
from xml.etree import ElementTree
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
root=Tk()
root.title("Органайзер")
canv=Canvas(root,width=1000,height=1000)
but=Button(canv,relief=FLAT,text="Часы",width=30,height=5,bg="#FF7F50",fg="#470027",font="Calibri 20",command=project.time)
but2=Button(canv,relief=FLAT,text="Время до Нового Года",width=30,height=5,bg="orange",fg="#470027",font="Calibri 20",command=project.ngtime)
but3=Button(canv,relief=FLAT,text="Калькулятор",width=30,height=5,bg="#00FF00",fg="#470027",font="Calibri 20",command=project.calc)
but4=Button(canv,relief=FLAT,text="Секундомер",width=30,height=5,bg="white",fg="#470027",font="Calibri 20",command=project.second)
but5=Button(canv,relief=FLAT,text="Ближайшие праздники",width=30,height=5,bg="#00bfff",fg="#470027",font="Calibri 20",command=project.opr)
but6=Button(canv,relief=FLAT,text="Дата",width=30,height=5,bg="#FF1493",fg="#470027",font="Calibri 20",command=project.date)
canv.pack()
but.grid(row=0,column=0)
but2.grid(row=0,column=2)
but3.grid(row=0,column=4)
but4.grid(row=2,column=0)
but5.grid(row=2,column=2)
but6.grid(row=2,column=4)
