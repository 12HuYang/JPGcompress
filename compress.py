from tkinter import *
import tkinter.filedialog as filedialog
import os
import cv2
from functools import partial

def openfile(frame,entrybox):
    percent=float(entrybox.get())
    path=filedialog.askdirectory()
    for widget in frame.winfo_children():
        widget.pack_forget()
    entrybox=Text(frame,height=50,width=50)
    entrybox.pack()
    if len(path)>0:
        print(path)
        files=os.listdir(path)
        for file in files:
            entrybox.insert(END,file+'\n',"wrap")
            originfile,extension=os.path.splitext(path+'/'+file)
            print(originfile,extension)
            if ('countresult' not in originfile) and ('training' not in originfile):
                if extension=='.JPG':
                    img=cv2.imread(path+'/'+file)
                    height,width,channel=img.shape
                    compressimg=cv2.resize(img,(int(width*percent),int(height*percent)),interpolation=cv2.INTER_LINEAR)
                    cv2.imwrite(originfile+'-compress-'+extension,compressimg)



root=Tk()
root.title('JPGcompresser')
root.geometry("")
frame=Frame(root,width=450,height=450)
boxframe=Frame(root)
percentageentry=Entry(frame)
percentageentry.pack(side=LEFT)
openfilebutton=Button(frame,text='open directory',command=partial(openfile,boxframe,percentageentry))
frame.pack()
boxframe.pack()
openfilebutton.pack(side=LEFT)

root.mainloop()
