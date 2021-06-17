import ui_server as ui_sv
import socket_server as sk_sv
from time import sleep

host = '127.0.0.1'
port = 9090
ui_sv.update_host_port(host, port)
sk_sv.update_host_port(host, port)

ui_sv.btnStart.config(command=lambda : start_server())

def start_server():
    sk_sv.start_server()
    ui_sv.disable_button()

ui_sv.window.mainloop()