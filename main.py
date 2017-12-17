from tkinter import * 
import project
import time
import urllib.request
from xml.etree import ElementTree
def dollar():
    for line in ElementTree.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")).findall("Valute"):
        if line.get("ID")=="R01235":
            return float(line.find("Value").text.replace(",","."))
def euro():
    for line in ElementTree.parse(urllib.request.urlopen("http://www.cbr.ru/scripts/XML_daily.asp")).findall("Valute"):
        if line.get("ID")=="R01239":
            return float(line.find("Value").text.replace(",","."))
dollar=dollar()
euro=euro()
root=Tk()
root.title("Органайзер")
bf=Frame(root)
but=Button(bf,relief=FLAT,text="Часы",width=30,height=5,bg="#FF7F50",fg="#470027",font="Calibri 20",command=project.time)
but2=Button(bf,relief=FLAT,text="Время до Нового Года",width=30,height=5,bg="orange",fg="#470027",font="Calibri 20",command=project.ngtime)
but3=Button(bf,relief=FLAT,text="Калькулятор",width=30,height=5,bg="#00FF00",fg="#470027",font="Calibri 20",command=project.calc)
but4=Button(bf,relief=FLAT,text="Секундомер",width=30,height=5,bg="white",fg="#470027",font="Calibri 20",command=project.second)
but5=Button(bf,relief=FLAT,text="Ближайшие праздники",width=30,height=5,bg="#00bfff",fg="#470027",font="Calibri 20",command=project.opr)
but6=Button(bf,relief=FLAT,text="Дата",width=30,height=5,bg="#FF1493",fg="#470027",font="Calibri 20",command=project.date)
val=Label(root,text="Курсы валют:   Доллар "+str(dollar)+"   Евро "+str(euro),font="Arial 25",fg="#6d8ef9")
bf.pack()
but.grid(row=0,column=0)
but2.grid(row=0,column=2)
but3.grid(row=0,column=4)
but4.grid(row=2,column=0)
but5.grid(row=2,column=2)
but6.grid(row=2,column=4)
val.pack()
