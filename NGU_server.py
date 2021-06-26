from tkinter import Toplevel
from tkinter.constants import END
import ui_server as ui_sv
import socket_server as sk_sv
import dtb
from _thread import *
from time import sleep

host = '127.0.0.1'
port = 9090
ui_sv.update_host_port(host, port)
sk_sv.update_host_port(host, port)

ui_sv.btnStart.config(command=lambda : start_server())
def start_server():
    ui_sv.disable_button()
    start_new_thread(sk_sv.start_server, ())

ui_sv.btnShowDtb.config(command=lambda: btnShowDtb_click())
def btnShowDtb_click():
    ui_sv.text_user = ''
    data_acc = dtb.get_acc_server()
    for data in data_acc:
        ui_sv.text_user += ' ' + str(data[0]) +'\n'
    ui_sv.text_user = ui_sv.text_user[:len(ui_sv.text_user)-1]
    ui_sv.show_text_user.delete('1.0', 'end')
    ui_sv.show_text_user.insert('end', ui_sv.text_user)
    ui_sv.show_text_user.pack()
    ui_sv.text_chart = ''
    data_chart = dtb.get_chart_server()
    for data in data_chart:
        t = '#' + str(data[0])
        ui_sv.text_chart += t.center(6)
        t = str(data[1])
        ui_sv.text_chart += t.center(27)
        t = str(data[2])
        ui_sv.text_chart += t.center(7) + '\n'
    ui_sv.text_chart = ui_sv.text_chart[:len(ui_sv.text_chart)-1]
    ui_sv.show_text_chart.delete('1.0', 'end')
    ui_sv.show_text_chart.insert('end', ui_sv.text_chart)
    ui_sv.show_text_chart.pack()

ui_sv.btnOpenDtb.config(command=lambda: btnOpenDtb_click())
def btnOpenDtb_click():
    import os
    os.startfile("dtb.db")

ui_sv.window.mainloop()