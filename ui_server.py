import tkinter as tk
from tkinter import *
from tkinter.font import BOLD
import random
import string 

window = tk.Tk()
window.title("N.G.U. Sever")
window.geometry("500x400")
window.configure(bg='#000000')
window.resizable(0, 0)

frame_info = tk.Frame(window, width = 400, height= 400, bg= '#000000')

lblHost = tk.Label(frame_info, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lblHost.pack(side=TOP, anchor=W)
lblPort = tk.Label(frame_info, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lblPort.pack(side=TOP, anchor=W)
def update_host_port(host, port):
    global lblHost,lblPort
    lblHost.config(text = "Address: " + str(host))
    lblHost.pack()
    lblPort.config(text = "Port: " + str(port))
    lblPort.pack()

frame_info_user = tk.Frame(frame_info, width = 400, height= 170, bg='#000000')
lb_user_title = tk.Label(frame_info_user, text='ACCOUNT', font = ('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
lb_user_title.pack(side=TOP, anchor=W)
text_user=''
show_text_user = tk.Text(frame_info_user, bd=-1, relief='flat', bg = '#000000', font = ('Roboto Mono', 12, 'bold'), fg = '#ffffff', width = 400, cursor="arrow")
show_text_user.insert('end', text_user)
show_text_user.bind("<Key>", lambda e: "break")
show_text_user.pack(side = TOP)
frame_info_user.propagate(0)
frame_info_user.pack(side=TOP)

frame_info_chart = tk.Frame(frame_info, width = 400, height= 170, bg='#000000')
text_chart_title = ' RANK |         ACCOUNT         | SCORE '
lb_chart_title = tk.Label(frame_info_chart, text=text_chart_title, font = ('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff')
lb_chart_title.pack(side=TOP, anchor=W)
text_chart=''
show_text_chart = tk.Text(frame_info_chart, bd=-1, relief='flat', bg = '#000000', font = ('Roboto Mono', 12, 'bold'), fg = '#ffffff', width = 400, cursor="arrow")
show_text_chart.insert('end', text_chart)
show_text_chart.bind("<Key>", lambda e: "break")
show_text_chart.pack(side = TOP)
frame_info_chart.propagate(0)
frame_info_chart.pack(side=TOP)

frame_info.propagate(0)
frame_info.place(x=0,y=0)

frame_button = tk.Frame(window, width = 100, height= 400, bg= '#000000')

btnStart = tk.Button(frame_button, text="Start", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnStart.pack(side=TOP)

btnShowDtb = tk.Button(frame_button, text="Show dtb", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnShowDtb.pack(side=TOP)

btnOpenDtb = tk.Button(frame_button, text="Open dtb", font=('Roboto Mono', 12, 'bold'), bg= '#000000', fg='#ffffff', width = 8, height= 1)
btnOpenDtb.pack(side=TOP)

btnMakeQuest = tk.Button(frame_button, text="Make Quest", font=('Roboto Mono', 10, 'bold'), bg= '#000000', fg='#ffffff', width = 10, height= 1)
btnMakeQuest.pack(side=TOP)
btnMakeQuest.config(command=lambda: btnMakeQuest_click())
text_input = text_output = None
def btnMakeQuest_click():
    global text_input, text_output
    MakeQuestWindow = Toplevel(window)
    MakeQuestWindow.title('Make Quest')
    MakeQuestWindow.geometry("402x62")
    MakeQuestWindow.configure(bg='#000000')
    MakeQuestWindow.resizable(0, 0)
    lb_input = tk.Label(MakeQuestWindow, text='Input', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_input.grid(row=0,column=0)
    text_input = tk.Entry(MakeQuestWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=20)
    text_input.grid(row=0,column=1)
    lb_output = tk.Label(MakeQuestWindow, text='Output', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff')
    lb_output.grid(row=1,column=0)
    text_output = tk.Text(MakeQuestWindow, font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', insertbackground='#ffffff', width=20, height=1)
    text_output.config(state='disabled')
    text_output.grid(row=1,column=1)
    bt_convert = tk.Button(MakeQuestWindow, text='Convert', font=('Roboto Mono', 14, 'bold'), bg= '#000000', fg='#ffffff', command=lambda: bt_convert_click())
    bt_convert.place(x=302, y=10)
def bt_convert_click():
    global text_input, text_output
    data = text_input.get()
    data = convert_quest(data)
    text_output.config(state='normal')
    text_output.delete('1.0', 'end')
    text_output.insert('end', data)
    text_output.config(state='disabled')
    text_output.grid(row=1,column=1)

def convert_quest(cv_input):
    x = 16 - len(cv_input)
    cv_output = random_char(x) + cv_input
    cv_output = ''.join(random.sample(cv_output,len(cv_output)))
    cv_output = cv_output.upper()
    return cv_output

def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))

frame_button.propagate(0)
frame_button.place(x=400,y=0)
def disable_button():
    global btnStart
    btnStart.config(state=tk.DISABLED)

#window.mainloop()
