from tkinter import*
import random
import tkinter.messagebox
import tempfile
import os

class summary:

    def __init__(self,window):
            self.window=window
            self.window.title("DISCHARGE SUMMARY")
            self.window.geometry("1350x850+0+0")
            self.window.config(background="white")

            abc =Frame(self.window, bg="white", bd=15, relief=RIDGE, width=1350, height=710)
            abc.grid()
            abc2 =Frame(abc, bd=5, width=1320, height=600, bg="Cornsilk",relief=RIDGE)
            abc2.grid(row=1 ,column=0, rowspan=6, sticky=W)
            abc1 =Frame(abc, bd=5, width=1320, height=30,  bg="Cornsilk", relief=RIDGE) #310
            abc1.grid(row=0,column=0 , sticky=W)

            abc3 =Frame(abc, bd=5, width=1320, height=50,  bg="lightgray", relief=RIDGE) #310
            abc3.grid(row=7 ,column=0 , sticky=W)

            #====================================================================================================
            self.lblspace=Label(abc1, text="DISCHARGE SUMMARY",font=('arial',10,'bold'),bd=1,bg="Cornsilk",fg="black",
                                width=163,justify=CENTER).grid(row=0,column=0)

            self.txtReceipt = Text(abc2, height=37, width=184, bd=10, font=('arial',9,'bold'))
            self.txtReceipt.grid(row=0,column=0)
            #=================================================================================================
            
            #===================================================================================================
            def show():
                self.txtReceipt.insert(END,'-----------MEDISURGE MULTISPECIALITY HOSPITAL----------' + "\n\n")
                self.txtReceipt.insert(END,'IPD NO:' + "\n ")
                self.txtReceipt.insert(END,'BILL NO:'+ "\n ")
                self.txtReceipt.insert(END,'NAME:'+ "\n")
                self.txtReceipt.insert(END,'AGE/GEN.'+ "\n")
                self.txtReceipt.insert(END,'BILL DATE'+ " \n")
                self.txtReceipt.insert(END,'DATE OF ADM-DISCHARGE:'+ "\n")
                self.txtReceipt.insert(END,'BED NO:'+ "\n")
                self.txtReceipt.insert(END,'DR:'+ "\n")
                self.txtReceipt.insert(END,'CONT. No:'+ "\n")
                self.txtReceipt.insert(END,'ADDRESS:'+ "\n")
                self.txtReceipt.insert(END,'ADHAR NO:' + "\n")
                self.txtReceipt.insert(END,'TREATING DOCTORS:' + "\n")
                self.txtReceipt.insert(END,'PAST HISTORY:' + "\n")
                self.txtReceipt.insert(END,'FINAL DIAGNOSIS:' + "\n")
                self.txtReceipt.insert(END,'HISTORY AND PRESENTING COMPLAIN:' + "\n")
                self.txtReceipt.insert(END,'HISTORY GIVEN:' + "\n")
                self.txtReceipt.insert(END,'ON ARRIVAL VITALS:' + "\n")
                self.txtReceipt.insert(END,'HOSPITALISATION COURSE:' + "\n")
                self.txtReceipt.insert(END,'OPERATION DETAILS:' + "\n")
                self.txtReceipt.insert(END,'NAME OF OPERATION:' + "\n")
                self.txtReceipt.insert(END,'NAME OF SURGEON:' + "\n")
                self.txtReceipt.insert(END,'NAME OF ANAESTHESIOLOGIST:' + "\n")
                self.txtReceipt.insert(END,'TYPE OF ANAESTHESIA:' + "\n")
                self.txtReceipt.insert(END,'OPERATIVE NOTE:' + "\n")
                self.txtReceipt.insert(END,'MEDICATION ON HOSPITALISATION:' + "\n")
                self.txtReceipt.insert(END,'INVESTIGATION:-ALL REPORTS ATTACHED WITH FILE:' + "\n")
                self.txtReceipt.insert(END,'MEDICATION ON DISCHARGE:' + "\n")
                self.txtReceipt.insert(END,'FOLLOW-UP:' + "\n")
                self.txtReceipt.insert(END,'CONDITION OF PATIENT ON DISCHARGE:' + "\n")
                self.txtReceipt.insert(END,'WHEN TO OBTAIN URGENT ADVICE:' + "\n")
                self.txtReceipt.insert(END,'RELATIVE SIGN:\t\t\t\t\tDOCTOR SIGN & STAMP:\t\t\t' + "\n")
                self.txtReceipt.insert(END,'RELATION :' + "\n")
                self.txtReceipt.insert(END,'RELATIVE NAME :' + "\n")
                self.txtReceipt.insert(END,'MO:' + "\n")


            #=====================Functions======================================================================
            def iprint():
                q=self.txtReceipt.get("1.0", "end-1c")
                filename = tempfile.mktemp(".txt")
                open (filename, "w"). write(q)
                os.startfile(filename, "print")

            def iexit():
                iexit = tkinter.messagebox.askyesno("DISCHARGE SUMMARY","Confirm if you want to Exit.")
                if iexit  > 0:
                    window.destroy()
                    return

            def ireset():
                self.txtReceipt.delete("1.0",END)



            #=====================================================================================================
            self.btnDone = Button(abc3,padx=1,pady=1,bd=5,fg="black",font=('arial',10,'bold'), width=7, height=1,
            bg="gray", text="Summary",command=show).grid(row=0,column=0)
            self.btnReset = Button(abc3,padx=1,pady=1,bd=5,fg="black",font=('arial',10,'bold'), width=7, height=1,
            bg="gray", text="Reset",command=ireset).grid(row=0,column=1)
            self.btnExit = Button(abc3,padx=1,pady=1,bd=5,fg="black",font=('arial',10,'bold'), width=7, height=1,
            bg="gray", text="Exit", command=iexit).grid(row=0,column=2)
            self.btnPrint = Button(abc3,padx=1,pady=1,bd=5,fg="black",font=('arial',10,'bold'), width=7, height=1,
            bg="gray", text="Print", command=iprint).grid(row=0,column=3)

if __name__ =='__main__':
            window = Tk()
            application = summary(window)
            window.mainloop()
