from tkinter import *
import webbrowser
import opd
import os
import random
import tkinter.messagebox
from datetime import datetime
import time
import tempfile
#import PIL
#from PIL import ImageTk, Image


window = Tk()
window.title('Homepage')
window.geometry('1410x710')
#window.iconbitmap('C:\Users\user\Desktop\images')

def callback(url):
    os.system(url)


#window = Tk()

label1= Label(window,text='MEDISURGE  MULTISPECIALITY  HOSPITAL',fg='white',bg="orange",font=('arial',16))
label1.pack()

label1= Label(window,text='Doctors you can trust when you need them the most.',fg='black',font=('arial',10))
label1.pack()

label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
#--------------------------------------------------------------------------------
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
#--------------------------------------------------------------------------------

#-------------opd image-----------------------------------------------------------
photo = PhotoImage(file="opdRe.png")
img_label = Label(image=photo)
img_label.pack()

link3 = Label(window, text="Outdoor", fg="blue", cursor="hand2")
link3.pack()
link3.bind("<Button-1>", lambda e: callback("C:\guiApp\engine\opd.py"))
#--------------------------------------------------------------------------------
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()

#--------------------------------------------------------------------------------
ipd_photo = PhotoImage(file="ipdRe.png")
ipd_label = Label(image=ipd_photo)
ipd_label.pack()

link1 = Label(window, text="Indoor", fg="blue", cursor="hand2")
link1.pack()
link1.bind("<Button-1>", lambda e: callback("C:\guiApp\engine\ipd_Billing.py"))
#---------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
label1= Label(window,text='  ',fg='black',font=('arial',8))
label1.pack()
#--------------------------------------------------------------------------------
ds_photo = PhotoImage(file="dsRe.png")
ds_label = Label(image=ds_photo)
ds_label.pack()


link2 = Label(window, text="Discharge Summary", fg="blue", cursor="hand2")
link2.pack()
link2.bind("<Button-1>", lambda e: callback("C:\guiApp\engine\dischargeSummary.py"))



#root.mainloop()
#===============================================


window.mainloop()
