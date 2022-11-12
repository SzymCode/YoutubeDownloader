from tkinter import *
from pytube import YouTube


window = Tk()
window.geometry('300x120')
window.resizable(False, False)
window.configure(bg='white')
window.title("YT downloader")
window.iconbitmap("images\\icon.ico")

Label(window, text='Youtube Video Downloader', font='karla 16 bold', bg='white').pack()
link = StringVar()
Entry(window, width=40, textvariable=link).place(x=32, y=32)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()


Button(window, text='DOWNLOAD', font='karla 15 bold', bg='#7bb2ed', padx=2, command=Downloader).place(x=80, y=62)
window.mainloop()