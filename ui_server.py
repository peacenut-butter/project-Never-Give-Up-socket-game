import tkinter as tk

window = tk.Tk()
window.title("N.G.U. Sever")

# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
lblHost = tk.Label(middleFrame)
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame)
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))
def update_host_port(host, port):
    global lblHost,lblPort
    lblHost.config(text = "Address: " + str(host))
    lblHost.pack()
    lblPort.config(text = "Port: " + str(port))
    lblPort.pack()

# Top frame consisting of two buttons widgets (i.e. btnStart, btnStop)
topFrame = tk.Frame(window)
btnStart = tk.Button(topFrame, text="Start")
btnStart.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))
def disable_button():
    global btnStart
    btnStart.config(state=tk.DISABLED)

#window.mainloop()
