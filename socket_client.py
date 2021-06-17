import socket

ClientSocket = None

add_score = 0
question_num = 0
question = ""

host = None
port = None

def update_host_port(host1, port1):
    global host, port
    host = host1
    port = port1

def connect_to_server():
    global ClientSocket, host, port
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

def received_msg():
    while True:
        data_from_server = ClientSocket.recv(1024)
        if not data_from_server:
            continue
        else:
            data = data_from_server.decode()
            data = data.split()
            if data[0] == 'login':
                return int(data[1])
            elif data[0] == 'play':
                add_score = int(data[1])
                question_num = int(data[2])
                question = data[3]
                hint = data[4]
                return 0, add_score, question_num, question, hint
            elif data[0] == 'lastques':
                return 1, data[1]
            elif data[0] == 'endgame':
                return data[1]
        
def sent_msg(answerword):
    ClientSocket.send(answerword.encode())

#ClientSocket.close()