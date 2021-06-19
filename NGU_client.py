from tkinter.constants import END
import ui_client as ui_clt
import socket_client as sk_clt
from tkinter import messagebox

host = '127.0.0.1'
port = 9090
sk_clt.update_host_port(host, port)

sk_clt.connect_to_server()

ui_clt.frame_start.pack()

ui_clt.bt_start.config(command = lambda : bt_start_click())
def bt_start_click():
    
    ui_clt.frame_start.forget()
    ui_clt.frame_login.pack()

def check_not_null(a, b):
    if a=='' or b=='': 
        messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", "Không được bỏ trống USERNAME, PASSWORD!!")
        return 0
    return 1

ui_clt.bt_sign_up.config(command = lambda : bt_signup_click())
def bt_signup_click():
    get_user = ui_clt.entry_user.get()
    get_pass = ui_clt.entry_pass.get()
    if check_not_null(get_user,get_pass):
        msg = 'login signup ' + get_user + ' ' + get_pass
        sk_clt.sent_msg(msg)
        a = sk_clt.received_msg()
        if a == 1:
            messagebox.showinfo("(ヘ･_･)ヘ┳━┳", "Đăng kí thành công, mời bạn đăng nhập lại !!")
        else:
            messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", "Tài khoản đã tồn tại !!")
            ui_clt.entry_user.delete(0,END)
            ui_clt.entry_pass.delete(0,END)

ui_clt.bt_login.config(command = lambda : bt_login_click())
def bt_login_click():
    get_user = ui_clt.entry_user.get()
    get_pass = ui_clt.entry_pass.get()
    if check_not_null(get_user,get_pass):
        msg = 'login login ' + get_user + ' ' + get_pass
        sk_clt.sent_msg(msg)
        a = sk_clt.received_msg()
        if a == 1:
            ui_clt.frame_login.forget()
            ui_clt.frame_play.pack()
            first_question()
        else:
            messagebox.showinfo("(ﾉ´･ω･)ﾉ ﾐ ┻━┻", "Sai tài khoản hoặc mật khẩu rồi!!")
            ui_clt.entry_user.delete(0,END)
            ui_clt.entry_pass.delete(0,END)

def first_question():
    ui_clt.score = 0
    (check, add_score, question_num, question, hint) = sk_clt.received_msg()
    ui_clt.update_quest_score(add_score, question_num, question, hint)
    
ui_clt.btw_enter.config(command = lambda : btw_enter_click())
def btw_enter_click():
    global add_score, question_num, question
    answerword = ui_clt.get_answerword()
    answerword = 'answer ' + answerword
    sk_clt.sent_msg(answerword)
    data = sk_clt.received_msg()
    check_last = data[0]
    if check_last == 0:
        (add_score, question_num, question, hint) = (data[1], data[2], data[3], data[4])
        ui_clt.update_quest_score(add_score, question_num, question, hint)
    else: last_question(data[1])

def last_question(add_score):
    ui_clt.update_last_quest(add_score)
    user_score = ui_clt.score
    msg = 'endgame ' + str(user_score)
    sk_clt.sent_msg(msg)
    data_rank = sk_clt.received_msg()
    ui_clt.start_end_game(data_rank)

ui_clt.bt_play_again.config(command = lambda : bt_play_again_click())
def bt_play_again_click():
    sk_clt.sent_msg('playagain')
    ui_clt.frame_end_game.pack_forget()
    ui_clt.frame_play.pack()
    first_question()

ui_clt.bt_exit.config(command = lambda : bt_exit_click())
def bt_exit_click():
    sk_clt.sent_msg('exit')
    #sk_clt.ClientSocket.close()
    ui_clt.frame_end_game.pack_forget()
    ui_clt.frame_start.pack()

ui_clt.window.mainloop()