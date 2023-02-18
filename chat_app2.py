import socket
import threading
import time
from tkinter import *

root=Tk()
root.geometry("700x720")
root.config(bg="white")

def func():
    t = threading.Thread(target=recv)
    t.start()

def recv():
    server_socket = socket.socket()
    port = 4050
    maxconnection = 99

    server_socket.bind(('', port))
    server_socket.listen(maxconnection)
    connection_socket, addr = server_socket.accept()

    while True:
        sendermessage = connection_socket.recv(2048).decode()
        if not sendermessage == "":
            time.sleep(5)
            lstbox.insert(0, "Client : " + sendermessage)

s = 0

def sendmsg():

    global s
    if s == 0:
        s = socket.socket()
        port = 3050
        s.connect(('localhost', port))
        msg = messagebox.get()
        lstbox.insert(0, "You : " + msg)
        s.send(msg.encode())
    else:
        msg = messagebox.get()
        lstbox.insert(0, "You : " + msg)
        s.send(msg.encode())


def threadsendmsg():
    th = threading.Thread(target=sendmsg)
    th.start()

startchatimage = PhotoImage(file="start.png")

buttons = Button(root, image=startchatimage, command=func, borderwidth=0)
buttons.place(x=90, y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message, font=('Calibre', 10, 'normal'), border=2, width=50)
messagebox.place(x=90, y = 650)

sendmessageimg = PhotoImage(file = "send.png")

sendmessagebutton = Button(root, image=sendmessageimg, command=threadsendmsg, borderwidth=0)
sendmessagebutton.place(x=610, y=630)

lstbox = Listbox(root, height=15, width=56)
lstbox.place(x=89, y=250)

root.mainloop()

