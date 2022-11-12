from tkinter import *
from tkinter.ttk import Combobox
from pytube import YouTube
import os


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('300x120')
        self.root.resizable(False, False)
        self.root.configure(bg='white')
        self.root.title("YT downloader")
        self.root.iconbitmap("images\\icon.ico")
        self.path = "_downloads_\\"

        Label(self.root, text='Youtube Video Downloader', font='karla 16 bold', bg='white').pack()
        Button(self.root, text='DOWNLOAD', font='karla 15 bold', bg='#7bb2ed', activebackground='#6795c7',
               padx=2, command=self.downloader).place(x=80, y=62)
        self.link = StringVar()
        Entry(self.root, width=40, textvariable=self.link).place(x=32, y=32)
        self.variables = ['.mp3', '.mp4', '.3gpp']
        self.w = Combobox(self.root, values=self.variables, width=5)
        self.w.pack()
        self.w.set(self.variables[0])
        self.w.place(x=225, y=65)
        self.w['state'] = 'readonly'

    def downloader(self):
        if self.w.get() == ".mp4":
            YouTube(str(self.link.get())).streams.filter(file_extension='mp4').first().download(self.path)

        if self.w.get() == ".3gpp":
            YouTube(str(self.link.get())).streams.first().download(self.path)

        if self.w.get() == ".mp3":
            url = YouTube(str(self.link.get()))
            video = url.streams.filter(only_audio=True).first()
            out_file = video.download(self.path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    m = MainWindow()
    m.run()