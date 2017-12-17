from tkinter import*
from time import*
from math import*
def moscow():
    moscow=Tk()
    moscow.title("Москва")
    canvas=Canvas(moscow,width=500,height=550)
    canvas.pack()
    canvas.create_oval(10,10,490,490,fill="orange")
    canvas.create_text(250,225,text=".",font="Arial 62")
    canvas.create_text(250,520,text="Москва",font="Arial 34")
    i=0
    while i<60:
        i=i+1
        canvas.create_line(250+210*cos(-i*6*pi/180+pi/2),250-210*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=2)
        if i%5==0:
            canvas.create_line(250+215*cos(-i*6*pi/180+pi/2),250-215*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=4)
            continue
    i=0
    while i<12:
        i=i+1
        canvas.create_text(250+225*cos(-i*30*pi/180+pi/2),250-225*sin(-30*i*pi/180+pi/2),text=i,font='Arial 16')  
    while True:
        time_now=localtime()
        time_sec=int(strftime("%S",time_now))
        time_hour=int(strftime("%I",time_now))
        time_min=int(strftime("%M",time_now))
        sec_angle=6*time_sec
        min_angle=time_min*6+time_sec*0.1
        hour_angle=time_hour*30+time_min*60*(30/3600)
        line_min=canvas.create_line(250,250,250-180*cos(min_angle*pi/180+pi/2),250-180*sin(min_angle*pi/180+pi/2),width=3,fill='darkblue')
        line_hour=canvas.create_line(250,250,250-150*cos(hour_angle*pi/180+pi/2),250-150*sin(hour_angle*pi/180+pi/2),width=5,fill='green')
        line_sec=canvas.create_line(250,250,250-180*cos(sec_angle*pi/180+pi/2),250-180*sin(sec_angle*pi/180+pi/2),width=2,fill='red')
        moscow.update()
        canvas.delete(line_sec)
        canvas.delete(line_min)
        canvas.delete(line_hour)
def london():
    london=Tk()
    london.title("Лондон")
    canvas=Canvas(london,width=500,height=550)
    canvas.pack()
    canvas.create_oval(10,10,490,490,fill="orange")
    canvas.create_text(250,225,text=".",font="Arial 62")
    canvas.create_text(250,520,text="Лондон",font="Arial 34")
    i=0
    while i<60:
        i=i+1
        canvas.create_line(250+210*cos(-i*6*pi/180+pi/2),250-210*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=2)
        if i%5==0:
            canvas.create_line(250+215*cos(-i*6*pi/180+pi/2),250-215*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=4)
            continue
    i=0
    while i<12:
        i=i+1
        canvas.create_text(250+225*cos(-i*30*pi/180+pi/2),250-225*sin(-30*i*pi/180+pi/2),text=i,font='Arial 16')  
    while True:
        time_now=localtime()
        time_sec=int(strftime("%S",time_now))
        time_hour=int(strftime("%I",time_now))-3
        time_min=int(strftime("%M",time_now))
        sec_angle=6*time_sec
        min_angle=time_min*6+time_sec*0.1
        hour_angle=time_hour*30+time_min*60*(30/3600)
        line_min=canvas.create_line(250,250,250-180*cos(min_angle*pi/180+pi/2),250-180*sin(min_angle*pi/180+pi/2),width=3,fill='darkblue')
        line_hour=canvas.create_line(250,250,250-150*cos(hour_angle*pi/180+pi/2),250-150*sin(hour_angle*pi/180+pi/2),width=5,fill='green')
        line_sec=canvas.create_line(250,250,250-180*cos(sec_angle*pi/180+pi/2),250-180*sin(sec_angle*pi/180+pi/2),width=2,fill='red')
        london.update()
        canvas.delete(line_sec)
        canvas.delete(line_min)
        canvas.delete(line_hour)
def tokyo():
    tokyo=Tk()
    tokyo.title("Токио")
    canvas=Canvas(tokyo,width=500,height=550)
    canvas.pack()
    canvas.create_oval(10,10,490,490,fill="orange")
    canvas.create_text(250,225,text=".",font="Arial 62")
    canvas.create_text(250,520,text="Токио",font="Arial 34")
    i=0
    while i<60:
        i=i+1
        canvas.create_line(250+210*cos(-i*6*pi/180+pi/2),250-210*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=2)
        if i%5==0:
            canvas.create_line(250+215*cos(-i*6*pi/180+pi/2),250-215*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=4)
            continue
    i=0
    while i<12:
        i=i+1
        canvas.create_text(250+225*cos(-i*30*pi/180+pi/2),250-225*sin(-30*i*pi/180+pi/2),text=i,font='Arial 16')  
    while True:
        time_now=localtime()
        time_sec=int(strftime("%S",time_now))
        time_hour=int(strftime("%I",time_now))+6
        time_min=int(strftime("%M",time_now))
        sec_angle=6*time_sec
        min_angle=time_min*6+time_sec*0.1
        hour_angle=time_hour*30+time_min*60*(30/3600)
        line_min=canvas.create_line(250,250,250-180*cos(min_angle*pi/180+pi/2),250-180*sin(min_angle*pi/180+pi/2),width=3,fill='darkblue')
        line_hour=canvas.create_line(250,250,250-150*cos(hour_angle*pi/180+pi/2),250-150*sin(hour_angle*pi/180+pi/2),width=5,fill='green')
        line_sec=canvas.create_line(250,250,250-180*cos(sec_angle*pi/180+pi/2),250-180*sin(sec_angle*pi/180+pi/2),width=2,fill='red')
        tokyo.update()
        canvas.delete(line_sec)
        canvas.delete(line_min)
        canvas.delete(line_hour)
def paris():
    paris=Tk()
    paris.title("Париж")
    canvas=Canvas(paris,width=500,height=550)
    canvas.pack()
    canvas.create_oval(10,10,490,490,fill="orange")
    canvas.create_text(250,225,text=".",font="Arial 62")
    canvas.create_text(250,520,text="Париж",font="Arial 34")
    i=0
    while i<60:
        i=i+1
        canvas.create_line(250+210*cos(-i*6*pi/180+pi/2),250-210*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=2)
        if i%5==0:
            canvas.create_line(250+215*cos(-i*6*pi/180+pi/2),250-215*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=4)
            continue
    i=0
    while i<12:
        i=i+1
        canvas.create_text(250+225*cos(-i*30*pi/180+pi/2),250-225*sin(-30*i*pi/180+pi/2),text=i,font='Arial 16')  
    while True:
        time_now=localtime()
        time_sec=int(strftime("%S",time_now))
        time_hour=int(strftime("%I",time_now))-2
        time_min=int(strftime("%M",time_now))
        sec_angle=6*time_sec
        min_angle=time_min*6+time_sec*0.1
        hour_angle=time_hour*30+time_min*60*(30/3600)
        line_min=canvas.create_line(250,250,250-180*cos(min_angle*pi/180+pi/2),250-180*sin(min_angle*pi/180+pi/2),width=3,fill='darkblue')
        line_hour=canvas.create_line(250,250,250-150*cos(hour_angle*pi/180+pi/2),250-150*sin(hour_angle*pi/180+pi/2),width=5,fill='green')
        line_sec=canvas.create_line(250,250,250-180*cos(sec_angle*pi/180+pi/2),250-180*sin(sec_angle*pi/180+pi/2),width=2,fill='red')
        paris.update()
        canvas.delete(line_sec)
        canvas.delete(line_min)
        canvas.delete(line_hour)
def new_york():
    new_york=Tk()
    new_york.title("Нью=Йорк")
    canvas=Canvas(new_york,width=500,height=550)
    canvas.pack()
    canvas.create_oval(10,10,490,490,fill="orange")
    canvas.create_text(250,225,text=".",font="Arial 62")
    canvas.create_text(250,520,text="Нью-Йорк",font="Arial 34")
    i=0
    while i<60:
        i=i+1
        canvas.create_line(250+210*cos(-i*6*pi/180+pi/2),250-210*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=2)
        if i%5==0:
            canvas.create_line(250+215*cos(-i*6*pi/180+pi/2),250-215*sin(-6*i*pi/180+pi/2),250+190*cos(-6*i*pi/180+pi/2),250-190*sin(-6*i*pi/180+pi/2),width=4)
            continue
    i=0
    while i<12:
        i=i+1
        canvas.create_text(250+225*cos(-i*30*pi/180+pi/2),250-225*sin(-30*i*pi/180+pi/2),text=i,font='Arial 16')  
    while True:
        time_now=localtime()
        time_sec=int(strftime("%S",time_now))
        time_hour=int(strftime("%I",time_now))-8
        time_min=int(strftime("%M",time_now))
        sec_angle=6*time_sec
        min_angle=time_min*6+time_sec*0.1
        hour_angle=time_hour*30+time_min*60*(30/3600)
        line_min=canvas.create_line(250,250,250-180*cos(min_angle*pi/180+pi/2),250-180*sin(min_angle*pi/180+pi/2),width=3,fill='darkblue')
        line_hour=canvas.create_line(250,250,250-150*cos(hour_angle*pi/180+pi/2),250-150*sin(hour_angle*pi/180+pi/2),width=5,fill='green')
        line_sec=canvas.create_line(250,250,250-180*cos(sec_angle*pi/180+pi/2),250-180*sin(sec_angle*pi/180+pi/2),width=2,fill='red')
        new_york.update()
        canvas.delete(line_sec)
        canvas.delete(line_min)
        canvas.delete(line_hour)
