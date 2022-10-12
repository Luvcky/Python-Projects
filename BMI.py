from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import sv_ttk 
import tkinter as tk
class MyWindow:
    def __init__(self,win):
        self.label1 = Label(win, text="BMI Calculator", font= ("AZONIX",15))
        self.label2 = Label(win, text="Age Category: ", font= ('Bahnschrift',13))
        self.label3 = Label(win, text="Weight (kg):  ", font=('Bahnschrift',13))
        self.label4 = Label(win, text= "Height(m): ", font=('Bahnschrift',13))
        self.label5 = Label(win, text= "BMI: ", font=('Bahnschrift',13))
        self.label6 = Label(win, text= "Status: ", font=('Bahnschrift',13))
        self.results = Label(win,text="Results", font=('AZONIX',13))
        self.ey1 = ttk.Entry(font = ('Bahnschrift',13))
        self.ey2 = ttk.Entry(font=('Bahnschrift',13))
        self.ey1.bind("<KeyRelease>",self.validateint)
        self.ey2.bind("<KeyRelease>",self.validatefloat)
        self.ey3 = ttk.Entry(font=('Bahnschrift',13))
        self.ey4 = ttk.Entry(font=('Bahnschrift',13))
        self.btn1 = ttk.Button(win, text="Calculate BMI", command=self.cmd1, style='Accent.TButton')
        self.v1 = tk.StringVar()
        self.menu1 = ttk.Spinbox(win,from_=0, to=60, values=("Under 12", "12-18", "18-24", "24- 36","36-60", "60+"), textvariable=self.v1, wrap=True)
        self.label1.place(x=85,y=28)
        self.label2.place(x=18,y=82)
        self.label3.place(x= 25,y=132)
        self.label4.place(x=25,y=182)
        self.label5.place(x=55,y=352)
        self.label6.place(x=55,y=402)
        self.menu1.place(x=135,y=82)
        self.ey1.place(x=135,y=132)
        self.ey2.place(x=135,y=182)
        self.ey3.place(x=135,y=352)
        self.ey4.place(x=135, y=402)
        self.btn1.place(x=140,y=240)
        self.results.place(x=30, y = 305)
    
    def cmd1(self):
        self.ey3.delete(0, 'end')
        w = int(self.ey1.get())
        h = float(self.ey2.get())
        bmi = round(w / (h * h),1)
        s =""
        if bmi < 18.5:
            s = "Underweight"
        elif bmi > 18.5 and bmi < 24.9:
            s = "Healthy"
        elif bmi > 25:
            s = "Overweight"
        self.ey3.insert(END,str(bmi))
        self.ey4.insert(END, str(s))

    def validateint(self, *_):
        if self.ey1.get() == "":
            self.ey1.state(["!invalid"])
        else:
            try:
                int(self.ey1.get())
                self.ey1.state(["!invalid"])
            except ValueError:
                self.ey1.state(["invalid"])

    def validatefloat(self, *_):
        if self.ey2.get() == "":
            self.ey2.state(["!invalid"])
        else:
            try:
                float(self.ey2.get())
                self.ey2.state(["!invalid"])
            except ValueError:
                self.ey2.state(["invalid"])


window=tk.Tk()
sv_ttk.set_theme("dark")

sv_ttk.use_dark_theme()

mywin=MyWindow(window)
window.title('BMI Generator')
window.geometry("380x500+10+10")
window.mainloop()

        