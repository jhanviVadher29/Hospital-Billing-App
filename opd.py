from tkinter import*
import random
import tkinter.messagebox
from datetime import datetime
import time
import tempfile
import io
import os

class customer1:

    def __init__(self,window):
            self.window=window
            self.window.title("OPD Billing System")
            self.window.geometry("1350x850+0+0")
            self.window.config(background="lightsalmon")


            abc =Frame(self.window, bg="plum", bd=15, relief=RIDGE, width=1350, height=850)
            abc.grid()

            abc1 =Frame(abc, bd=10, width=450, height=100, padx=2, bg="violet",relief=RIDGE)
            abc1.grid(row=0 ,column=0 ,columnspan=2, sticky=W)
            abc2 =Frame(abc, bd=20, width=600, height=850, padx=20, bg="plum", relief=RIDGE) #310
            abc2.grid(row=2 ,column=0 , sticky=W)
            abc3 =Frame(abc, bd=5, width=600, height=850, padx=1, bg="mediumorchid", relief=RIDGE)
            abc3.grid(row=2 ,column=1 , sticky=W)


            abc4 =Frame(abc3, bd=30, width=300, height=850, padx=5, bg="plum", relief=RIDGE)
            abc4.grid(row=0 ,column=0 , sticky=W)
            abc5 =Frame(abc4, bd=5, width=300, height=120, padx=5, bg="plum", relief=RIDGE) #370
            abc5.grid(row=1 ,column=0 , columnspan=3, sticky=W)



            billNoV=StringVar()
            opdNoV=StringVar()
            nameV=StringVar()
            dateV=StringVar()
            bedV=StringVar()
            conDrV=StringVar()
            refDrV=StringVar()
            contNoV=StringVar()
            ageV=StringVar()
            genV=StringVar()
            amtV=StringVar()
            addV=StringVar()


            f = open ("value.txt","r")
            if f.mode == "r":
                opdNoV = f.read()
                #print(opdNoV)





            #billNoV.set(random.randint(1,1000000))
            #opdNoV.set(random.randint(1,1000000))


            #==============================================================================


            self.lblspace=Label(abc1, text="OPD BILLING SYSTEM",font=('arial',15,'bold'),pady=1,bd=1,bg="darkorchid",fg="Cornsilk",
                                width=110,justify=CENTER).grid(row=0,column=0)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Bill No:",padx=5,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=0,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=billNoV)
            self.lblCus_Ref.grid(row=0,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="OPD No:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=1,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=opdNoV)
            self.lblCus_Ref.grid(row=1,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Date:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=2,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=dateV)
            self.lblCus_Ref.grid(row=2,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Name:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=3,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=nameV)
            self.lblCus_Ref.grid(row=3,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Gender:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=4,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=genV)
            self.lblCus_Ref.grid(row=4,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Age:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=5,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=ageV)
            self.lblCus_Ref.grid(row=5,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Contact No:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=6,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=contNoV)
            self.lblCus_Ref.grid(row=6,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Cons. Dr:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=7,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=conDrV)
            self.lblCus_Ref.grid(row=7,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Ref. Dr:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=8,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=refDrV)
            self.lblCus_Ref.grid(row=8,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Address:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=9,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=addV)
            self.lblCus_Ref.grid(row=9,column=1,pady=5,padx=1)

            self.lblCus_Ref=Label(abc2,font=('arial',14,'bold'),text="Amount:",padx=1,fg="Cornsilk",bg="darkorchid",bd=2)
            self.lblCus_Ref.grid(row=10,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc2,font=('arial',14,'bold'),width=30,textvariable=amtV)
            self.lblCus_Ref.grid(row=10,column=1,pady=5,padx=1)


            #=============================================================================================================================#
            self.txtReceipt = Text(abc4, height=30, width=70, bd=10, font=('arial',9,'bold'))
            self.txtReceipt.grid(row=0,column=0)

            #=========================SHOW function================================================================================#
            def show():
                self.txtReceipt.insert(END,'------MEDISURGE MULTISPECIALITY HOSPITAL------'+"\n ")
                self.txtReceipt.insert(END,'DATE'+ dateV.get() + "\n")
                self.txtReceipt.insert(END,'BILL NO:'+ billNoV.get() + "\n ")
                self.txtReceipt.insert(END,'OPD NO:' + opdNoV + "\n ")
                self.txtReceipt.insert(END,'---------------------------------------------'+ "\n ")
                self.txtReceipt.insert(END,'NAME:' + nameV.get() + "\n")
                self.txtReceipt.insert(END,'GEN.' + genV.get() + "\n")
                self.txtReceipt.insert(END,'Age:' + ageV.get() + "\n")
                self.txtReceipt.insert(END,'CONT. No:' + contNoV.get() + "\n")
                self.txtReceipt.insert(END,'ADDRESS:' + addV.get() + "\n")
                self.txtReceipt.insert(END,'---------------------------------------------'+ "\n ")
                self.txtReceipt.insert(END,'Consultant DR:' + conDrV.get() + "\n")
                self.txtReceipt.insert(END,'Referring DR:' + conDrV.get() + "\n")
                self.txtReceipt.insert(END,'Amount:'+ amtV.get() + "\n")

                opdNoV = int(opdNoV) + 1
                with open("value.txt",'w') as f:
                    if f.mode == "w":
                        f.write(str(opdNoV))
                        f.close()



            def ireset():
                self.txtReceipt.delete("1.0",END)
                billNoV.set("")
                opdNoV.set("")
                nameV.set("")
                dateV.set("")
                bedV.set("")
                conDrV.set("")
                refDrV.set("")
                contNoV.set("")
                ageV.set("")
                genV.set("")
                amtV.set("")
                addV.set("")


            def iprint():
                q=self.txtReceipt.get("1.0", "end-1c")
                filename = tempfile.mktemp(".txt")
                open (filename, "w"). write(q)
                os.startfile(filename, "print")

            def iexit():
                iexit = tkinter.messagebox.askyesno("IPD Billing System","Confirm if you want to Exit.")
                if iexit  > 0:
                    window.destroy()
                    return





            #=============================================================================================================================#


            self.btnPrint = Button(abc5,padx=1,pady=1,bd=5,fg="Cornsilk",font=('arial',14,'bold'), width=7, height=2,
            bg="darkorchid", text="DONE",command=show).grid(row=0,column=0)
            self.btnReset = Button(abc5,padx=1,pady=1,bd=5,fg="Cornsilk",font=('arial',14,'bold'), width=7, height=2,
            bg="darkorchid", text="Reset",command=ireset).grid(row=0,column=1)
            self.btnExit = Button(abc5,padx=1,pady=1,bd=5,fg="Cornsilk",font=('arial',14,'bold'), width=7, height=2,
            bg="darkorchid", text="Exit",command=iexit).grid(row=0,column=2)
            self.btnPrint = Button(abc5,padx=1,pady=1,bd=5,fg="Cornsilk",font=('arial',14,'bold'), width=7, height=2,
            bg="darkorchid", text="Print",command=iprint).grid(row=0,column=3)








if __name__ =='__main__':
            window = Tk()
            application = customer1(window)
            window.mainloop()
