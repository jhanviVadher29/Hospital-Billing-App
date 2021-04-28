from tkinter import*
import random
import tkinter.messagebox
from datetime import datetime
import time
import tempfile
import os


class customer:

    def __init__(self,window):
            self.window=window
            self.window.title("IPD Billing System")
            self.window.geometry("1350x850+0+0")
            self.window.config(background="powder blue")


            abc =Frame(self.window, bg="powder blue", bd=20, relief=RIDGE)
            abc.grid()

            abc1 =Frame(abc, bd=5, width=450, height=100, padx=5, bg="powder blue", relief=RIDGE)
            abc1.grid(row=0 ,column=0 , columnspan=5, sticky=W)
            abc2 =Frame(abc, bd=5, width=450, height=600, padx=5, bg="cadet blue", relief=RIDGE) #310
            abc2.grid(row=1 ,column=0 , sticky=W)
            abc3 =Frame(abc, bd=5, width=450, height=600, padx=5, bg="cadet blue", relief=RIDGE)
            abc3.grid(row=1 ,column=2 , sticky=W)



            abc7 =Frame(abc, bd=5, width=300, height=300, padx=5, bg="cadet blue", relief=RIDGE)
            abc7.grid(row=1 ,column=3 , sticky=W)

            abc8 =Frame(abc7, bd=5, width=300, height=300, padx=5, bg="cadet blue", relief=RIDGE)
            abc8.grid(row=11 ,column=0 , sticky=W)

            abc9 =Frame(abc7, bd=5, width=300, height=50, padx=5, bg="cadet blue", relief=RIDGE)
            abc9.grid(row=12 ,column=0 , sticky=W)

            abc4 =Frame(abc, bd=5, width=450, height=600, padx=5, bg="cadet blue", relief=RIDGE)
            abc4.grid(row=1 ,column=4 , sticky=W)
            abc5 =Frame(abc4, bd=5, width=450, height=600, padx=5, bg="cadet blue", relief=RIDGE)
            abc5.grid(row=0 ,column=0 , sticky=W)
            abc6 =Frame(abc4, bd=5, width=112, height=120, padx=5, bg="cadet blue", relief=RIDGE) #370
            abc6.grid(row=1 ,column=0 , columnspan=4, sticky=W)





            Date1 =StringVar()
            Time1 =StringVar()
            Date1.set(time.strftime("%d/%m/%Y"))
            Time1.set(time.strftime("%H:%M:%S"))
            txtReceipt =StringVar()
            #==============================Variables===============================================
            var1=IntVar ()
            var2=IntVar ()
            var3=IntVar ()
            var4=IntVar ()
            var5=IntVar ()
            var6=IntVar ()
            var7=IntVar ()
            var8=IntVar ()
            var9=IntVar ()
            var10=IntVar ()
            var11=IntVar ()
            var12=IntVar ()
            var13=IntVar ()
            var14=IntVar ()
            var15=IntVar ()
            var16=IntVar ()
            var17=IntVar ()
            var18=IntVar ()
            var19=IntVar ()
            var20=IntVar ()
            var21=IntVar ()
            var22=IntVar ()
            var23=IntVar ()
            var24=IntVar ()
            var25=IntVar ()
            var26=IntVar ()
            var27=IntVar ()
            var28=IntVar ()
            var29=IntVar ()
            var30=IntVar ()
            var31=IntVar ()
            var32=IntVar ()
            var33=IntVar ()
            var34=IntVar ()
            var35=IntVar ()
            var36=IntVar ()
            var37=IntVar ()
            var38=IntVar ()
            var39=IntVar ()
            var40=IntVar ()
            var41=IntVar ()
            var42=IntVar ()
            var43=IntVar ()
            var44=IntVar ()
            var45=IntVar ()
            var46=IntVar ()
            var47=IntVar ()
            var48=IntVar ()
            var49=IntVar ()
            var50=IntVar ()
            var51=IntVar ()
            var52=IntVar ()
            var53=IntVar ()
            var54=IntVar ()
            var55=IntVar ()
            var56=IntVar ()
            var57=IntVar ()
            var58=IntVar ()
            var59=IntVar ()
            var60=IntVar ()
            var61=IntVar ()
            var62=IntVar ()
            var63=IntVar ()
            var64=IntVar ()
            var65=IntVar ()
            var66=IntVar ()
            var67=IntVar ()
            var68=IntVar ()
            var69=IntVar ()
            var70=IntVar ()
            var71=IntVar ()
            var72=IntVar ()
            var73=IntVar ()
            var74=IntVar ()
            var75=IntVar ()
            var76=IntVar ()
            var77=IntVar ()
            var78=IntVar ()
            var79=IntVar ()
            var80=IntVar ()
            var81=IntVar ()
            var82=IntVar ()
            var83=IntVar ()
            var84=IntVar ()
            var85=IntVar ()
            var86=IntVar ()
            var87=IntVar ()
            var88=IntVar ()
            var89=IntVar ()
            var90=IntVar ()
            var91=IntVar ()
            var92=IntVar ()
            var93=IntVar ()
            var94=IntVar ()
            var95=IntVar ()
            var96=IntVar ()
            var97=IntVar ()
            var98=IntVar ()
            var99=IntVar ()
            var100=IntVar ()
            var101=IntVar ()
            var102=IntVar ()
            var103=IntVar ()
            var104=IntVar ()
            var105=IntVar ()





            e_general=StringVar()
            e_ssp=StringVar()
            e_delux=StringVar()
            e_iccu=StringVar()
            e_trac=StringVar()
            e_ij=StringVar()
            e_intu=StringVar()
            e_art=StringVar()
            e_dlc=StringVar()
            e_ecg=StringVar()
            e_folys=StringVar()
            e_rt=StringVar()
            e_icd=StringVar()
            e_ple=StringVar()
            e_thr=StringVar()
            e_bt=StringVar()
            e_bio=StringVar()    #asc/bro/che
            e_asc=StringVar()
            e_che=StringVar()
            e_bro=StringVar()   #cpa/chp/col
            e_cpa=StringVar()
            e_chp=StringVar()
            e_col=StringVar()
            e_lp=StringVar()
            e_pft=StringVar()
            e_pic=StringVar()
            e_pig=StringVar()
            e_thr1=StringVar()
            e_tmt=StringVar()      #vc/pap/oxy/dfeb/lap/mc/alm
            e_vc=StringVar()
            e_pap=StringVar()
            e_dfeb=StringVar()
            e_lap=StringVar()
            e_mc=StringVar()
            e_alm=StringVar()
            e_che=StringVar()
            e_oxy=StringVar()
            e_mlc=StringVar()
            e_ana=StringVar()    #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
            e_ass=StringVar()
            e_cns=StringVar()
            e_cvp=StringVar()
            e_day=StringVar()
            e_dte=StringVar()
            e_dre=StringVar()
            e_poi=StringVar()
            e_hgt=StringVar()
            e_hmc=StringVar()    #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
            e_iemc=StringVar()
            e_irc=StringVar()
            e_ipc=StringVar()
            e_ic=StringVar()
            e_iv=StringVar()
            e_nc=StringVar()
            e_pl=StringVar()
            e_prc=StringVar()
            e_g=StringVar()
            e_ss=StringVar()
            e_ac=StringVar()
            e_g2=StringVar()
            e_ss2=StringVar()
            e_ac2=StringVar()
            e_g3=StringVar()
            e_ss3=StringVar()
            e_ac3=StringVar()
            e_g4=StringVar()
            e_ss4=StringVar()
            e_ac4=StringVar()
            e_g5a=StringVar()
            e_ss5a=StringVar()
            e_ac5a=StringVar()
            e_g5b=StringVar()
            e_ss5b=StringVar()
            e_ac5b=StringVar()
            e_g6=StringVar()
            e_ss6=StringVar()
            e_ac6=StringVar()
            e_g7a=StringVar()
            e_ss7a=StringVar()
            e_ac7a=StringVar()
            e_g7b=StringVar()
            e_ss7b=StringVar()
            e_ac7b=StringVar()
            e_g8=StringVar()
            e_ss8=StringVar()
            e_ac8=StringVar()
            e_g9=StringVar()
            e_ss9=StringVar()
            e_ac9=StringVar()
            price=StringVar()

            billNoV=StringVar()
            ipdNoV=StringVar()
            nameV=StringVar()
            dateV=StringVar()
            bedV=StringVar()
            conDrV=StringVar()
            contNoV=StringVar()
            opdNoV=StringVar()
            addV=StringVar()
            daDdV=StringVar()
            ageV=StringVar()
            refDrV=StringVar()
            totalV=StringVar()
            otherV=StringVar()
            addiV=StringVar()

            billNoV.set(random.randint(1,1000000))
            ipdNoV.set(random.randint(1,1000000))



            e_general.set("0")
            e_ssp.set("0")
            e_delux.set("0")
            e_iccu.set("0")
            e_trac.set("0")
            e_ij.set("0")
            e_intu.set("0")
            e_art.set("0")
            e_dlc.set("0")
            e_ecg.set("0")
            e_folys.set("0")
            e_rt.set("0")
            e_icd.set("0")
            e_ple.set("0")
            e_thr.set("0")
            e_bt.set("0")
            e_bio.set("0")
            e_asc.set("0")
            e_bro.set("0")
            e_cpa.set("0")
            e_chp.set("0")
            e_col.set("0")
            e_lp.set("0")
            e_pft.set("0")
            e_pic.set("0")
            e_pig.set("0")
            e_thr1.set("0")
            e_tmt.set("0")
            e_che.set("0")      #vc/pap/oxy/dfeb/lap/mc/alm
            e_vc.set("0")
            e_pap.set("0")
            e_oxy.set("0")
            e_dfeb.set("0")
            e_lap.set("0")
            e_mc.set("0")
            e_alm.set("0")
            e_mlc.set("0")       #mlc/ana/ass/cns/cvp/day/dte/dre/poi/hgt
            e_ana.set("0")
            e_ass.set("0")
            e_cns.set("0")
            e_cvp.set("0")
            e_day.set("0")
            e_dte.set("0")
            e_dre.set("0")
            e_poi.set("0")
            e_hgt.set("0")      #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
            e_hmc.set("0")
            e_iemc.set("0")
            e_irc.set("0")
            e_ipc.set("0")
            e_ic.set("0")
            e_iv.set("0")
            e_nc.set("0")
            e_pl.set("0")
            e_prc.set("0")
            e_g.set("0")
            e_ac.set("0")
            e_ss.set("0")
            e_g2.set("0")
            e_ac2.set("0")
            e_ss2.set("0")
            e_g3.set("0")
            e_ac3.set("0")
            e_ss3.set("0")
            e_g4.set("0")
            e_ac4.set("0")
            e_ss4.set("0")
            e_g5a.set("0")
            e_ac5a.set("0")
            e_ss5a.set("0")
            e_g5b.set("0")
            e_ac5b.set("0")
            e_ss5b.set("0")
            e_g6.set("0")
            e_ac6.set("0")
            e_ss6.set("0")
            e_g7a.set("0")
            e_ac7a.set("0")
            e_ss7a.set("0")
            e_g7b.set("0")
            e_ac7b.set("0")
            e_ss7b.set("0")
            e_g8.set("0")
            e_ac8.set("0")
            e_ss8.set("0")
            e_g9.set("0")
            e_ac9.set("0")
            e_ss9.set("0")
            price.set("0")

        #====================================chkGeneral=========================================
            def chkGeneral():
                if(var1.get() ==1):
                   self.txtgeneral.configure(state=NORMAL)
                   self.txtgeneral.focus()
                   self.txtgeneral.delete('0',END)
                   e_general.set("")
                elif var1.get() ==0:
                   self.txtgeneral.configure(state=DISABLED)
                   self.txtgeneral.set("0")

            def chkSsp():
                if(var2.get() ==1):
                   self.txtssp.configure(state=NORMAL)
                   self.txtssp.focus()
                   self.txtssp.delete('0',END)
                   e_ssp.set("")
                elif var2.get() ==0:
                   self.txtssp.configure(state=DISABLED)
                   self.txtssp.set("0")
            def chkDelux():
                if(var3.get() ==1):
                   self.txtdelux.configure(state=NORMAL)
                   self.txtdelux.focus()
                   self.txtdelux.delete('0',END)
                   e_delux.set("")
                elif var3.get() ==0:
                   self.txtdelux.configure(state=DISABLED)
                   self.txtdelux.set("0")

            def chkIccu():
                if(var4.get() ==1):
                   self.txticcu.configure(state=NORMAL)
                   self.txticcu.focus()
                   self.txticcu.delete('0',END)
                   e_iccu.set("")
                elif var4.get() ==0:
                   self.txticcu.configure(state=DISABLED)
                   self.txticcu.set("0")
            def chkTrac():
                if(var5.get() ==1):
                   self.txttrac.configure(state=NORMAL)
                   self.txttrac.focus()
                   self.txttrac.delete('0',END)
                   e_trac.set("")
                elif var5.get() ==0:
                   self.txttrac.configure(state=DISABLED)
                   self.txttrac.set("0")

            def chkIj():
                if(var6.get() ==1):
                   self.txtij.configure(state=NORMAL)
                   self.txtij.focus()
                   self.txtij.delete('0',END)
                   e_ij.set("")
                elif var6.get() ==0:
                   self.txtij.configure(state=DISABLED)
                   self.txtij.set("0")
            def chkIntu():
                if(var7.get() ==1):
                   self.txtintu.configure(state=NORMAL)
                   self.txtintu.focus()
                   self.txtintu.delete('0',END)
                   e_intu.set("")
                elif var7.get() ==0:
                   self.txtintu.configure(state=DISABLED)
                   self.txtintu.set("0")

            def chkArt():
                if(var8.get() ==1):
                   self.txtart.configure(state=NORMAL)
                   self.txtart.focus()
                   self.txtart.delete('0',END)
                   e_art.set("")
                elif var8.get() ==0:
                   self.txtart.configure(state=DISABLED)
                   self.txtart.set("0")

            def chkDlc():
                if(var9.get() ==1):
                   self.txtdlc.configure(state=NORMAL)
                   self.txtdlc.focus()
                   self.txtdlc.delete('0',END)
                   e_dlc.set("")
                elif var9.get() ==0:
                   self.txtdlc.configure(state=DISABLED)
                   self.txtdlc.set("0")

            def chkEcg():
                if(var10.get() ==1):
                   self.txtecg.configure(state=NORMAL)
                   self.txtecg.focus()
                   self.txtecg.delete('0',END)
                   e_ecg.set("")
                elif var10.get() ==0:
                   self.txtecg.configure(state=DISABLED)
                   self.txtecg.set("0")
            def chkFolys():
                if(var11.get() ==1):
                   self.txtfolys.configure(state=NORMAL)
                   self.txtfolys.focus()
                   self.txtfolys.delete('0',END)
                   e_folys.set("")
                elif var11.get() ==0:
                   self.txtfolys.configure(state=DISABLED)
                   self.txtfolys.set("0")

            def chkRt():
                if(var12.get() ==1):
                   self.txtrt.configure(state=NORMAL)
                   self.txtrt.focus()
                   self.txtrt.delete('0',END)
                   e_rt.set("")
                elif var12.get() ==0:
                   self.txtrt.configure(state=DISABLED)
                   self.txtrt.set("0")

            def chkIcd():
                if(var13.get() ==1):
                   self.txticd.configure(state=NORMAL)
                   self.txticd.focus()
                   self.txticd.delete('0',END)
                   e_icd.set("")
                elif var13.get() ==0:
                   self.txticd.configure(state=DISABLED)
                   self.txticd.set("0")

            def chkPle():
                if(var14.get() ==1):
                   self.txtple.configure(state=NORMAL)
                   self.txtple.focus()
                   self.txtple.delete('0',END)
                   e_rt.set("")
                elif var14.get() ==0:
                   self.txtple.configure(state=DISABLED)
                   self.txtple.set("0")
            def chkThr():
                if(var15.get() ==1):
                   self.txtthr.configure(state=NORMAL)
                   self.txtthr.focus()
                   self.txtthr.delete('0',END)
                   e_thr.set("")
                elif var15.get() ==0:
                   self.txtthr.configure(state=DISABLED)
                   self.txtthr.set("0")

            def chkBt():
                if(var16.get() ==1):
                   self.txtbt.configure(state=NORMAL)
                   self.txtbt.focus()
                   self.txtbt.delete('0',END)
                   e_bt.set("")
                elif var16.get() ==0:
                   self.txtbt.configure(state=DISABLED)
                   self.txtbt.set("0")
            def chkBio():
                if(var17.get() ==1):
                   self.txtbio.configure(state=NORMAL)
                   self.txtbio.focus()
                   self.txtbio.delete('0',END)
                   e_bio.set("")
                elif var17.get() ==0:
                   self.txtbio.configure(state=DISABLED)
                   self.txtbio.set("0")

            def chkAsc():
                if(var18.get() ==1):
                   self.txtasc.configure(state=NORMAL)
                   self.txtasc.focus()
                   self.txtasc.delete('0',END)
                   e_asc.set("")
                elif var18.get() ==0:
                   self.txtasc.configure(state=DISABLED)
                   self.txtasc.set("0")
            def chkBro():
                if(var19.get() ==1):
                   self.txtbro.configure(state=NORMAL)
                   self.txtbro.focus()
                   self.txtbro.delete('0',END)
                   e_bro.set("")
                elif var19.get() ==0:
                   self.txtbro.configure(state=DISABLED)
                   self.txtbro.set("0")

            def chkChe():
                if(var20.get() ==1):
                   self.txtche.configure(state=NORMAL)
                   self.txtche.focus()
                   self.txtche.delete('0',END)
                   e_che.set("")
                elif var20.get() ==0:
                   self.txtche.configure(state=DISABLED)
                   self.txtche.set("0")
            def chkCpa():
                if(var21.get() ==1):
                   self.txtcpa.configure(state=NORMAL)
                   self.txtcpa.focus()
                   self.txtcpa.delete('0',END)
                   e_cpa.set("")
                elif var21.get() ==0:
                   self.txtcpa.configure(state=DISABLED)
                   self.txtcpa.set("0")

            def chkChp():
                if(var22.get() ==1):
                   self.txtchp.configure(state=NORMAL)
                   self.txtchp.focus()
                   self.txtchp.delete('0',END)
                   e_chp.set("")
                elif var22.get() ==0:
                   self.txtchp.configure(state=DISABLED)
                   self.txtchp.set("0")
            def chkCpa():
                if(var21.get() ==1):
                   self.txtcpa.configure(state=NORMAL)
                   self.txtcpa.focus()
                   self.txtcpa.delete('0',END)
                   e_cpa.set("")
                elif var21.get() ==0:
                   self.txtcpa.configure(state=DISABLED)
                   self.txtcpa.set("0")

            def chkChp():
                if(var22.get() ==1):
                   self.txtchp.configure(state=NORMAL)
                   self.txtchp.focus()
                   self.txtchp.delete('0',END)
                   e_chp.set("")
                elif var22.get() ==0:
                   self.txtchp.configure(state=DISABLED)
                   self.txtchp.set("0")
            def chkCol():
                if(var23.get() ==1):
                   self.txtcol.configure(state=NORMAL)
                   self.txtcol.focus()
                   self.txtcol.delete('0',END)
                   e_col.set("")
                elif var23.get() ==0:
                   self.txtcol.configure(state=DISABLED)
                   self.txtcol.set("0")

            def chkPft():
                if(var25.get() ==1):
                    self.txtpft.configure(state=NORMAL)
                    self.txtpft.focus()
                    self.txtpft.delete('0',END)
                    e_pft.set("")
                elif var25.get() ==0:
                    self.txtpft.configure(state=DISABLED)
                    self.txtpft.set("0")
            def chkPic():
                if(var26.get() ==1):
                    self.txtpic.configure(state=NORMAL)
                    self.txtpic.focus()
                    self.txtpic.delete('0',END)
                    e_pic.set("")
                elif var26.get() ==0:
                    self.txtpic.configure(state=DISABLED)
                    self.txtpic.set("0")

            def chkPig():
                if(var27.get() ==1):
                    self.txtpig.configure(state=NORMAL)
                    self.txtpig.focus()
                    self.txtpig.delete('0',END)
                    e_pig.set("")
                elif var27.get() ==0:
                    self.txtpig.configure(state=DISABLED)
                    self.txtpig.set("0")
            def chkLp():
                    if(var24.get() ==1):
                       self.txtlp.configure(state=NORMAL)
                       self.txtlp.focus()
                       self.txtlp.delete('0',END)
                       e_pic.set("")
                    elif var24.get() ==0:
                       self.txtlp.configure(state=DISABLED)
                       self.txtlp.set("0")

            def chkThr1():
                    if(var28.get() ==1):
                       self.txtthr1.configure(state=NORMAL)
                       self.txtthr1.focus()
                       self.txtthr1.delete('0',END)
                       e_thr1.set("")
                    elif var28.get() ==0:
                       self.txtthr1.configure(state=DISABLED)
                       self.txtthr1.set("0")
            def chkTmt():
                    if(var29.get() ==1):
                       self.txttmt.configure(state=NORMAL)
                       self.txttmt.focus()
                       self.txttmt.delete('0',END)
                       e_tmt.set("")
                    elif var29.get() ==0:
                       self.txttmt.configure(state=DISABLED)
                       self.txttmt.set("0")
            def chkVc():
                if(var30.get() ==1):
                    self.txtvc.configure(state=NORMAL)
                    self.txtvc.focus()
                    self.txtvc.delete('0',END)
                    e_vc.set("")
                elif var30.get() ==0:
                    self.txtvc.configure(state=DISABLED)
                    self.txtvc.set("0")
            def chkPap():
                if(var31.get() ==1):
                    self.txtpap.configure(state=NORMAL)
                    self.txtpap.focus()
                    self.txtpap.delete('0',END)
                    e_pap.set("")
                elif var31.get() ==0:
                    self.txtpap.configure(state=DISABLED)
                    self.txtpap.set("0")

            def chkOxy():
                if(var32.get() ==1):
                    self.txtoxy.configure(state=NORMAL)
                    self.txtoxy.focus()
                    self.txtoxy.delete('0',END)
                    e_oxy.set("")
                elif var32.get() ==0:
                    self.txtoxy.configure(state=DISABLED)
                    self.txtoxy.set("0")
            def chkDfeb():
                if(var33.get() ==1):
                    self.txtdfeb.configure(state=NORMAL)
                    self.txtdfeb.focus()
                    self.txtdfeb.delete('0',END)
                    e_dfeb.set("")
                elif var33.get() ==0:
                    self.txtdfeb.configure(state=DISABLED)
                    self.txtdfeb.set("0")

            def chkLap():
                if(var34.get() ==1):
                    self.txtlap.configure(state=NORMAL)
                    self.txtlap.focus()
                    self.txtlap.delete('0',END)
                    e_lap.set("")
                elif var34.get() ==0:
                    self.txtlap.configure(state=DISABLED)
                    self.txtlap.set("0")

            def chkMc():
                if(var35.get() ==1):
                    self.txtmc.configure(state=NORMAL)
                    self.txtmc.focus()
                    self.txtmc.delete('0',END)
                    e_mc.set("")
                elif var35.get() ==0:
                    self.txtmc.configure(state=DISABLED)
                    self.txtmc.set("0")

            def chkAlm():
                if(var36.get() ==1):
                    self.txtalm.configure(state=NORMAL)
                    self.txtalm.focus()
                    self.txtalm.delete('0',END)
                    e_alm.set("")
                elif var36.get() ==0:
                    self.txtalm.configure(state=DISABLED)
                    self.txtalm.set("0")


            def chkMlc():
                if(var37.get() ==1):
                   self.txtmlc.configure(state=NORMAL)
                   self.txtmlc.focus()
                   self.txtmlc.delete('0',END)
                   e_mlc.set("")
                elif var37.get() ==0:
                   self.txtmlc.configure(state=DISABLED)
                   self.txtmlc.set("0")

            def chkAna():
                if(var38.get() ==1):
                   self.txtana.configure(state=NORMAL)
                   self.txtana.focus()
                   self.txtana.delete('0',END)
                   e_ana.set("")
                elif var38.get() ==0:
                   self.txtana.configure(state=DISABLED)
                   self.txtana.set("0")
            def chkAss():
                if(var39.get() ==1):
                   self.txtass.configure(state=NORMAL)
                   self.txtass.focus()
                   self.txtass.delete('0',END)
                   e_ass.set("")
                elif var39.get() ==0:
                   self.txtass.configure(state=DISABLED)
                   self.txtass.set("0")

            def chkCns():
                if(var40.get() ==1):
                   self.txtcns.configure(state=NORMAL)
                   self.txtcns.focus()
                   self.txtcns.delete('0',END)
                   e_cns.set("")
                elif var40.get() ==0:
                   self.txtcns.configure(state=DISABLED)
                   self.txtcns.set("0")
            def chkCvp():
                if(var41.get() ==1):
                   self.txtcvp.configure(state=NORMAL)
                   self.txtcvp.focus()
                   self.txtcvp.delete('0',END)
                   e_cvp.set("")
                elif var41.get() ==0:
                   self.txtcvp.configure(state=DISABLED)
                   self.txtcvp.set("0")

            def chkDay():
                if(var42.get() ==1):
                   self.txtday.configure(state=NORMAL)
                   self.txtday.focus()
                   self.txtday.delete('0',END)
                   e_day.set("")
                elif var42.get() ==0:
                   self.txtday.configure(state=DISABLED)
                   self.txtday.set("0")
            def chkDte():
                if(var43.get() ==1):
                   self.txtdte.configure(state=NORMAL)
                   self.txtdte.focus()
                   self.txtdte.delete('0',END)
                   e_dte.set("")
                elif var43.get() ==0:
                   self.txtdte.configure(state=DISABLED)
                   self.txtdte.set("0")

            def chkDre():
                if(var44.get() ==1):
                   self.txtdre.configure(state=NORMAL)
                   self.txtdre.focus()
                   self.txtdre.delete('0',END)
                   e_dre.set("")
                elif var44.get() ==0:
                   self.txtdre.configure(state=DISABLED)
                   self.txtdre.set("0")
            def chkPoi():
                if(var45.get() ==1):
                   self.txtpoi.configure(state=NORMAL)
                   self.txtpoi.focus()
                   self.txtpoi.delete('0',END)
                   e_poi.set("")
                elif var45.get() ==0:
                   self.txtpoi.configure(state=DISABLED)
                   self.txtpoi.set("0")

            def chkHgt():
                if(var46.get() ==1):
                   self.txthgt.configure(state=NORMAL)
                   self.txthgt.focus()
                   self.txthgt.delete('0',END)
                   e_hgt.set("")
                elif var46.get() ==0:
                   self.txthgt.configure(state=DISABLED)
                   self.txthgt.set("0")
            def chkPoi():
                if(var45.get() ==1):
                   self.txtpoi.configure(state=NORMAL)
                   self.txtpoi.focus()
                   self.txtpoi.delete('0',END)
                   e_poi.set("")
                elif var45.get() ==0:
                   self.txtpoi.configure(state=DISABLED)
                   self.txtpoi.set("0")

            def chkHgt():
                if(var46.get() ==1):
                   self.txthgt.configure(state=NORMAL)
                   self.txthgt.focus()
                   self.txthgt.delete('0',END)
                   e_hgt.set("")
                elif var46.get() ==0:
                   self.txthgt.configure(state=DISABLED)
                   self.txthgt.set("0")
            def chkHmc():
                if(var47.get() ==1):
                   self.txthmc.configure(state=NORMAL)
                   self.txthmc.focus()
                   self.txthmc.delete('0',END)
                   e_hmc.set("")
                elif var47.get() ==0:
                   self.txthmc.configure(state=DISABLED)
                   self.txthmc.set("0")

            def chkIemc():
                if(var48.get() ==1):
                   self.txtiemc.configure(state=NORMAL)
                   self.txtiemc.focus()
                   self.txtiemc.delete('0',END)
                   e_iemc.set("")
                elif var48.get() ==0:
                   self.txtiemc.configure(state=DISABLED)
                   self.txtiemc.set("0")
            def chkIrc():
                if(var49.get() ==1):
                   self.txtirc.configure(state=NORMAL)
                   self.txtirc.focus()
                   self.txtirc.delete('0',END)
                   e_irc.set("")
                elif var49.get() ==0:
                   self.txtirc.configure(state=DISABLED)
                   self.txtirc.set("0")

            def chkIpc():
                if(var50.get() ==1):
                   self.txtipc.configure(state=NORMAL)
                   self.txtipc.focus()
                   self.txtipc.delete('0',END)
                   e_ipc.set("")
                elif var50.get() ==0:
                   self.txtipc.configure(state=DISABLED)
                   self.txtipc.set("0")
            def chkIc():
                if(var51.get() ==1):
                   self.txtic.configure(state=NORMAL)
                   self.txtic.focus()
                   self.txtic.delete('0',END)
                   e_ic.set("")
                elif var51.get() ==0:
                   self.txtic.configure(state=DISABLED)
                   self.txtic.set("0")

            def chkIv():
                if(var52.get() ==1):
                   self.txtiv.configure(state=NORMAL)
                   self.txtiv.focus()
                   self.txtiv.delete('0',END)
                   e_iv.set("")
                elif var52.get() ==0:
                   self.txtiv.configure(state=DISABLED)
                   self.txtiv.set("0")
            def chkNc():
                if(var53.get() ==1):
                   self.txtnc.configure(state=NORMAL)
                   self.txtnc.focus()
                   self.txtnc.delete('0',END)
                   e_nc.set("")
                elif var53.get() ==0:
                   self.txtnc.configure(state=DISABLED)
                   self.txtnc.set("0")

            def chkPl():
                if(var54.get() ==1):
                   self.txtpl.configure(state=NORMAL)
                   self.txtpl.focus()
                   self.txtpl.delete('0',END)
                   e_pl.set("")
                elif var54.get() ==0:
                   self.txtpl.configure(state=DISABLED)
                   self.txtpl.set("0")
            def chkPrc():
                if(var55.get() ==1):
                   self.txtprc.configure(state=NORMAL)
                   self.txtprc.focus()
                   self.txtprc.delete('0',END)
                   e_prc.set("")
                elif var55.get() ==0:
                   self.txtprc.configure(state=DISABLED)
                   self.txtprc.set("0")

            def chkG():
                if(var56.get() ==1):
                   self.txtg.configure(state=NORMAL)
                   self.txtg.focus()
                   self.txtg.delete('0',END)
                   e_g.set("")
                elif var56.get() ==0:
                   self.txtg.configure(state=DISABLED)
                   self.txtg.set("0")
                   self.txtg.set("0")
            def chkSs():
                if(var57.get() ==1):
                   self.txtss.configure(state=NORMAL)
                   self.txtss.focus()
                   self.txtss.delete('0',END)
                   e_ss.set("")
                elif var57.get() ==0:
                   self.txtss.configure(state=DISABLED)
                   self.txtss.set("0")

            def chkAc():
                if(var58.get() ==1):
                   self.txtac.configure(state=NORMAL)
                   self.txtac.focus()
                   self.txtac.delete('0',END)
                   e_ac.set("")
                elif var58.get() ==0:
                   self.txtac.configure(state=DISABLED)
                   self.txtac.set("0")
                   self.txtac.set("0")

            def chkG2():
                if(var59.get() ==1):
                   self.txtg2.configure(state=NORMAL)
                   self.txtg2.focus()
                   self.txtg2.delete('0',END)
                   e_g2.set("")
                elif var59.get() ==0:
                   self.txtg2.configure(state=DISABLED)
                   self.txtg2.set("0")

            def chkSs2():
                if(var60.get() ==1):
                   self.txtss2.configure(state=NORMAL)
                   self.txtss2.focus()
                   self.txtss2.delete('0',END)
                   e_ss2.set("")
                elif var60.get() ==0:
                   self.txtss2.configure(state=DISABLED)
                   self.txtss2.set("0")
                   self.txtss2.set("0")
            def chkAc2():
                if(var61.get() ==1):
                   self.txtac2.configure(state=NORMAL)
                   self.txtac2.focus()
                   self.txtac2.delete('0',END)
                   e_ac2.set("")
                elif var61.get() ==0:
                   self.txtac2.configure(state=DISABLED)
                   self.txtac2.set("0")

            def chkG3():
                if(var62.get() ==1):
                   self.txtg3.configure(state=NORMAL)
                   self.txtg3.focus()
                   self.txtg3.delete('0',END)
                   e_g3.set("")
                elif var62.get() ==0:
                   self.txtg3.configure(state=DISABLED)
                   self.txtg3.set("0")
                   self.txtg3.set("0")
            def chkSs3():
                if(var63.get() ==1):
                   self.txtss3.configure(state=NORMAL)
                   self.txtss3.focus()
                   self.txtss3.delete('0',END)
                   e_ss3.set("")
                elif var63.get() ==0:
                   self.txtss3.configure(state=DISABLED)
                   self.txtss3.set("0")

            def chkAc3():
                if(var64.get() ==1):
                   self.txtac3.configure(state=NORMAL)
                   self.txtac3.focus()
                   self.txtac3.delete('0',END)
                   e_ac3.set("")
                elif var64.get() ==0:
                   self.txtac3.configure(state=DISABLED)
                   self.txtac3.set("0")
                   self.txtac3.set("0")
            def chkG4():
                if(var65.get() ==1):
                   self.txtg4.configure(state=NORMAL)
                   self.txtg4.focus()
                   self.txtg4.delete('0',END)
                   e_g4.set("")
                elif var65.get() ==0:
                   self.txtg4.configure(state=DISABLED)
                   self.txtg4.set("0")

            def chkSs4():
                if(var85.get() ==1):
                   self.txtss4.configure(state=NORMAL)
                   self.txtss4.focus()
                   self.txtss4.delete('0',END)
                   e_ss4.set("")
                elif var85.get() ==0:
                   self.txtss4.configure(state=DISABLED)
                   self.txtss4.set("0")
                   self.txtss4.set("0")
            def chkAc4():
                if(var66.get() ==1):
                   self.txtac4.configure(state=NORMAL)
                   self.txtac4.focus()
                   self.txtac4.delete('0',END)
                   e_ac4.set("")
                elif var66.get() ==0:
                   self.txtac4.configure(state=DISABLED)
                   self.txtac4.set("0")

            def chkG5a():
                if(var67.get() ==1):
                   self.txtg5a.configure(state=NORMAL)
                   self.txtg5a.focus()
                   self.txtg5a.delete('0',END)
                   e_g5a.set("")
                elif var67.get() ==0:
                   self.txtg5a.configure(state=DISABLED)
                   self.txtg5a.set("0")
                   self.txtg5a.set("0")
            def chkSs5a():
                if(var68.get() ==1):
                   self.txtss5a.configure(state=NORMAL)
                   self.txtss5a.focus()
                   self.txtss5a.delete('0',END)
                   e_ss5a.set("")
                elif var68.get() ==0:
                   self.txtss5a.configure(state=DISABLED)
                   self.txtss5a.set("0")

            def chkAc5a():
                if(var69.get() ==1):
                   self.txtac5a.configure(state=NORMAL)
                   self.txtac5a.focus()
                   self.txtac5a.delete('0',END)
                   e_ac5a.set("")
                elif var69.get() ==0:
                   self.txtac5a.configure(state=DISABLED)
                   self.txtac5a.set("0")
                   self.txtac5a.set("0")
            def chkG5b():
                if(var70.get() ==1):
                   self.txtg5b.configure(state=NORMAL)
                   self.txtg5b.focus()
                   self.txtg5b.delete('0',END)
                   e_g5b.set("")
                elif var70.get() ==0:
                   self.txtg5b.configure(state=DISABLED)
                   self.txtg5b.set("0")

            def chkSs5b():
                if(var71.get() ==1):
                   self.txtss5b.configure(state=NORMAL)
                   self.txtss5b.focus()
                   self.txtss5b.delete('0',END)
                   e_ss5b.set("")
                elif var71.get() ==0:
                   self.txtss5b.configure(state=DISABLED)
                   self.txtss5b.set("0")
                   self.txtss5b.set("0")
            def chkAc5b():
                if(var72.get() ==1):
                   self.txtac5b.configure(state=NORMAL)
                   self.txtac5b.focus()
                   self.txtac5b.delete('0',END)
                   e_ac5b.set("")
                elif var72.get() ==0:
                   self.txtac5b.configure(state=DISABLED)
                   self.txtac5b.set("0")

            def chkG6():
                if(var73.get() ==1):
                   self.txtg6.configure(state=NORMAL)
                   self.txtg6.focus()
                   self.txtg6.delete('0',END)
                   e_g6.set("")
                elif var73.get() ==0:
                   self.txtg6.configure(state=DISABLED)
                   self.txtg6.set("0")
                   self.txtg6.set("0")
            def chkSs6():
                if(var74.get() ==1):
                   self.txtss6.configure(state=NORMAL)
                   self.txtss6.focus()
                   self.txtss6.delete('0',END)
                   e_ss6.set("")
                elif var74.get() ==0:
                   self.txtss6.configure(state=DISABLED)
                   self.txtss6.set("0")

            def chkAc6():
                if(var75.get() ==1):
                   self.txtac6.configure(state=NORMAL)
                   self.txtac6.focus()
                   self.txtac6.delete('0',END)
                   e_ac6.set("")
                elif var75.get() ==0:
                   self.txtac6.configure(state=DISABLED)
                   self.txtac6.set("0")
                   self.txtac6.set("0")
            def chkG7a():
                if(var76.get() ==1):
                   self.txtg7a.configure(state=NORMAL)
                   self.txtg7a.focus()
                   self.txtg7a.delete('0',END)
                   e_g7a.set("")
                elif var76.get() ==0:
                   self.txtg7a.configure(state=DISABLED)
                   self.txtg7a.set("0")

            def chkSs7a():
                if(var77.get() ==1):
                   self.txtss7a.configure(state=NORMAL)
                   self.txtss7a.focus()
                   self.txtss7a.delete('0',END)
                   e_ss7a.set("")
                elif var77.get() ==0:
                   self.txtss7a.configure(state=DISABLED)
                   self.txtss7a.set("0")
                   self.txtss7a.set("0")
            def chkAc7a():
                if(var78.get() ==1):
                   self.txtac7a.configure(state=NORMAL)
                   self.txtac7a.focus()
                   self.txtac7a.delete('0',END)
                   e_ac7a.set("")
                elif var78.get() ==0:
                   self.txtac7a.configure(state=DISABLED)
                   self.txtac7a.set("0")

            def chkG7b():
                if(var79.get() ==1):
                   self.txtg7b.configure(state=NORMAL)
                   self.txtg7b.focus()
                   self.txtg7b.delete('0',END)
                   e_g7b.set("")
                elif var79.get() ==0:
                   self.txtg7b.configure(state=DISABLED)
                   self.txtg7b.set("0")
                   self.txtg7b.set("0")
            def chkSs7b():
                if(var80.get() ==1):
                   self.txtss7b.configure(state=NORMAL)
                   self.txtss7b.focus()
                   self.txtss7b.delete('0',END)
                   e_ss7b.set("")
                elif var80.get() ==0:
                   self.txtss7b.configure(state=DISABLED)
                   self.txtss7b.set("0")

            def chkG8():
                if(var86.get() ==1):
                   self.txtg8.configure(state=NORMAL)
                   self.txtg8.focus()
                   self.txtg8.delete('0',END)
                   e_g8.set("")
                elif var86.get() ==0:
                   self.txtg8.configure(state=DISABLED)
                   self.txtg8.set("0")
                   self.txtg8.set("0")
            def chkSs8():
                if(var87.get() ==1):
                   self.txtss8.configure(state=NORMAL)
                   self.txtss8.focus()
                   self.txtss8.delete('0',END)
                   e_ss8.set("")
                elif var87.get() ==0:
                   self.txtss8.configure(state=DISABLED)
                   self.txtss8.set("0")

            def chkAc8():
                if(var88.get() ==1):
                   self.txtac8.configure(state=NORMAL)
                   self.txtac8.focus()
                   self.txtac8.delete('0',END)
                   e_g8.set("")
                elif var88.get() ==0:
                   self.txtac8.configure(state=DISABLED)
                   self.txtac8.set("0")

            def chkG9():
                if(var82.get() ==1):
                   self.txtg9.configure(state=NORMAL)
                   self.txtg9.focus()
                   self.txtg9.delete('0',END)
                   e_g9.set("")
                elif var82.get() ==0:
                   self.txtg9.configure(state=DISABLED)
                   self.txtg9.set("0")

            def chkSs9():
                if(var83.get() ==1):
                   self.txtss9.configure(state=NORMAL)
                   self.txtss9.focus()
                   self.txtss9.delete('0',END)
                   e_ss9.set("")
                elif var83.get() ==0:
                   self.txtss9.configure(state=DISABLED)
                   self.txtss9.set("0")
                   self.txtss9.set("0")
            def chkAc9():
                if(var84.get() ==1):
                   self.txtac9.configure(state=NORMAL)
                   self.txtac9.focus()
                   self.txtac9.delete('0',END)
                   e_ac9.set("")
                elif var84.get() ==0:
                   self.txtac9.configure(state=DISABLED)
                   self.txtac9.set("0")
            def chkAc7b():
                if(var81.get() ==1):
                   self.txtac7b.configure(state=NORMAL)
                   self.txtac7b.focus()
                   self.txtac7b.delete('0',END)
                   e_ac7b.set("")
                elif var81.get() ==0:
                   self.txtac7b.configure(state=DISABLED)
                   self.txtac7b.set("0")

            #=============================================================================================================================#
            def iExit():
                iExit = tkinter.messagebox.askyesno("IPD Billing System","Confirm if you want to Exit.")
                if iExit  > 0:
                    root.destroy()
                    return
            def iprint():
                q=self.txtReceipt.get("1.0", "end-1c")
                filename = tempfile.mktemp(".txt")
                open (filename, "w"). write(q)
                os.startfile(filename, "print")

            #===================================================================================
            def costOfItem():
                item1=float(e_general.get())
                item2=float(e_ssp.get())
                item3=float(e_delux.get())
                item4=float(e_iccu.get())
                item5=float(e_trac.get())
                item6=float(e_dlc.get())
                item7=float(e_ecg.get())
                item8=float(e_folys.get())
                item9=float(e_rt.get())
                item10=float(e_icd.get())
                item11=float(e_ple.get())
                item12=float(e_thr.get())
                item13=float(e_bt.get())
                item14=float(e_bio.get())   #asc/bro/che
                item15=float(e_asc.get())
                item16=float(e_che.get())
                item17=float(e_bro.get())   #cpa/chp/col
                item18=float(e_cpa.get())
                item19=float(e_chp.get())
                item20=float(e_col.get())
                item21=float(e_lp.get())
                item22=float(e_pft.get())
                item23=float(e_pic.get())
                item24=float(e_pig.get())
                item25=float(e_thr1.get())
                item26=float(e_tmt.get())      #vc/pap/oxy/dfeb/lap/mc/alm
                item27=float(e_vc.get())
                item28=float(e_pap.get())
                item29=float(e_dfeb.get())
                item30=float(e_lap.get())
                item31=float(e_mc.get())
                item32=float(e_alm.get())
            #    item33=float(e_che.get())
                item34=float(e_oxy.get())
                item35=float(e_mlc.get())
                item36=float(e_ana.get())  #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
                item37=float(e_ass.get())
                item38=float(e_cns.get())
                item39=float(e_cvp.get())
                item40=float(e_day.get())
                item41=float(e_dte.get())
                item42=float(e_dre.get())
                item43=float(e_poi.get())
                item44=float(e_hgt.get())
                item45=float(e_hmc.get())   #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
                item46=float(e_iemc.get())
                item47=float(e_irc.get())
                item48=float(e_ipc.get())
                item49=float(e_ic.get())
                item50=float(e_iv.get())
                item51=float(e_nc.get())
                item52=float(e_pl.get())
                item53=float(e_prc.get())
                item54=float(e_g.get())
                item55=float(e_ss.get())
                item56=float(e_ac.get())
                item57=float(e_g2.get())
                item58=float(e_ss2.get())
                item59=float(e_ac2.get())
                item60=float(e_g3.get())
                item61=float(e_ss3.get())
                item62=float(e_ac3.get())
                item63=float(e_g4.get())
                item64=float(e_ss4.get())
                item65=float(e_ac4.get())
                item66=float(e_g5a.get())
                item67=float(e_ss5a.get())
                item68=float(e_ac5a.get())
                item69=float(e_g5b.get())
                item70=float(e_ss5b.get())
                item71=float(e_ac5b.get())
                item72=float(e_g6.get())
                item73=float(e_ss6.get())
                item74=float(e_ac6.get())
                item75=float(e_g7a.get())
                item76=float(e_ss7a.get())
                item77=float(e_ac7a.get())
                item78=float(e_g7b.get())
                item79=float(e_ss7b.get())
                item80=float(e_ac7b.get())
                item81=float(e_g8.get())
                item82=float(e_ss8.get())
                item83=float( e_ac8.get())
                item84=float(e_g9.get())
                item85=float(e_ss9.get())
                item86=float(e_ac9.get())
                item87=float(e_ij.get())
                item88=float(e_intu.get())
                item89=float(e_art.get())
                item90=float(otherV.get())
                item91=float(addiV.get())

                price =   (item1 * 3200) \
                        + (item2 * 4200) \
                        + (item3 * 5300) \
                        + (item4 * 7000) \
                        + (item5 * 5500) \
                        + (item6 * 3500) \
                        + (item7 * 300) \
                        + (item8 * 250) \
                        + (item9 * 250) \
                        + (item10 * 5000) \
                        + (item11 * 3000) \
                        + (item12 * 5000) \
                        + (item13 * 250) \
                        + (item14 * 6000) \
                        + (item15 * 3500) \
                        + (item16 * 4000) \
                        + (item17 * 5000) \
                        + (item18 * 20000) \
                        + (item19 * 6000) \
                        + (item20 * 5000) \
                        + (item21 * 3500) \
                        + (item22 * 1000) \
                        + (item23 * 4000) \
                        + (item24 * 3500) \
                        + (item25 * 2000) \
                        + (item26 * 1000) \
                        + (item27 * 4500) \
                        + (item28 * 3500) \
                        + (item29 * 500) \
                        + (item30 * 5000) \
                        + (item31 * 300) \
                        + (item32 * 350) \
                        + (item34 * 1500)\
                        + (item35 * 3000) \
                        + (item36 * 5000) \
                        + (item37 * 15000) \
                        + (item38 * 2000) \
                        + (item39 * 350) \
                        + (item40 * 500) \
                        + (item41 * 800) \
                        + (item42 * 300) \
                        + (item43 * 3000) \
                        + (item44 * 100) \
                        + (item45 * 1500) \
                        + (item46 * 5000) \
                        + (item47 * 3000) \
                        + (item48 * 200) \
                        + (item49 * 500) \
                        + (item50 * 100) \
                        + (item51 * 100) \
                        + (item52 * 1500) \
                        + (item53 * 1500) \
                        + (item54 * 9000) \
                        + (item55 * 11000) \
                        + (item56 * 12500) \
                        + (item57 * 15000) \
                        + (item58 * 18000) \
                        + (item59 * 21000) \
                        + (item60 * 21000) \
                        + (item61 * 24000) \
                        + (item62 * 28000) \
                        + (item63 * 28000) \
                        + (item64 * 33000) \
                        + (item65 * 37000) \
                        + (item66 * 35000) \
                        + (item67 * 40000) \
                        + (item68 * 45000) \
                        + (item69 * 45000) \
                        + (item70 * 50000) \
                        + (item71 * 56000) \
                        + (item72 * 56000) \
                        + (item73 * 60000) \
                        + (item74 * 66000) \
                        + (item75 * 66000) \
                        + (item76 * 72000) \
                        + (item77 * 80000) \
                        + (item78 * 80000) \
                        + (item79 * 87000) \
                        + (item80 * 94000) \
                        + (item81 * 94000) \
                        + (item82 * 100000) \
                        + (item83 * 112500) \
                        + (item84 * 100000) \
                        + (item85 * 112500) \
                        + (item86 * 125000) \
                        + (item87 * 2500) \
                        + (item88 * 1500) \
                        + (item89 * 2500) \
                        + (item90 * 1) \
                        + (item91 * 1)

                result1 = item1 * 3200
                result2 = item2 * 4200
                result3 = item3 * 5300
                result4 = item4 * 7000
                result5 = item5 * 5500
                result6 = item6 * 3500
                result7 = item7 * 300
                result8 = item8 * 250
                result9 = item9 * 250
                result10 = item10 * 5000
                result11 = item11 * 3000
                result12 = item12 * 5000
                result13 = item13 * 250
                result14 = item14 * 6000
                result15 = item15 * 3500
                result16 = item16 * 4000
                result17 = item17 * 5000
                result18 = item18 * 20000
                result19 = item19 * 6000
                result20 = item20 * 5000
                result21 = item21 * 3500
                result22 = item22 * 1000
                result23 = item23 * 4000
                result24 = item24 * 3500
                result25 = item25 * 2000
                result26 = item26 * 1000
                result27 = item27 * 4500
                result28 = item28 * 3500
                result29 = item29 * 500
                result30 = item30 * 5000
                result31 = item31 * 300
                result32 = item32 * 350
                result34 = item34 * 1500
                result35 = item35 * 3000
                result36 = item36 * 5000
                result37 = item37 * 15000
                result38 = item38 * 2000
                result39 = item39 * 350
                result40 = item40 * 500
                result41 = item41 * 800
                result42 = item42 * 300
                result43 = item43 * 3000
                result44 = item44 * 100
                result45 = item45 * 1500
                result46 = item46 * 5000
                result47 = item47 * 3000
                result48 = item48 * 200
                result49 = item49 * 500
                result50 = item50 * 100
                result51 = item51 * 100
                result52 = item52 * 1500
                result53 = item53 * 1500
                result54 = item54 * 9000
                result55 = item55 * 11000
                result56 = item56 * 12500
                result57 = item57 * 15000
                result58 = item58 * 18000
                result59 = item59 * 21000
                result60 = item60 * 21000
                result61 = item61 * 24000
                result62 = item62 * 28000
                result63 = item63 * 28000
                result64 = item64 * 33000
                result65 = item65 * 37000
                result66 = item66 * 35000
                result67 = item67 * 40000
                result68 = item68 * 45000
                result69 = item69 * 45000
                result70 = item70 * 50000
                result70 = item71 * 56000
                result72 = item72 * 56000
                result73 = item73 * 60000
                result74 = item74 * 66000
                result75 = item75 * 66000
                result76 = item76 * 72000
                result77 = item77 * 80000
                result78 = item78 * 80000
                result79 = item79 * 87000
                result80 = item80 * 94000
                result81 = item81 * 94000
                result82 = item82 * 100000
                result83 = item83 * 112500
                result84 = item84 * 100000
                result85 = item85 * 112500
                result86 = item86 * 125000
                result87 = item87 * 2500
                result88 = item88 * 1500
                result89 = item89 * 2500




                totalV.set(price)
                self.txtReceipt.insert(END,'IPD No: IP' + ipdNoV.get() + "\n ")
                self.txtReceipt.insert(END,'Bill NO:'+ billNoV.get() + "\n ")
                self.txtReceipt.insert(END,'Name:' + nameV.get() + "\n")
                self.txtReceipt.insert(END,'Age/Gen.' + ageV.get() + "\n")
                self.txtReceipt.insert(END,'Bill Date'+ dateV.get() + " \n")
                self.txtReceipt.insert(END,'Date of Adm-Discharge:'+ daDdV.get() + "\n")
                self.txtReceipt.insert(END,'Bed NO:'+ bedV.get() + "\n")
                self.txtReceipt.insert(END,'Dr:' + conDrV.get() + "\n")

                self.txtReceipt.insert(END,'---------------------------Amount Bill------------------------' +"\n")
                if (var1.get() > 0):
                    self.txtReceipt.insert(END, 'General Ward\t\t\t'+e_general.get() + "x3200 = " + str(result1) + "\n")
                if (var2.get() > 0):
                    self.txtReceipt.insert(END, 'Semi Special Ward\t\t'+e_ssp.get() + "x4200 = "+ str(result2) + "\n")
                if (var3.get() > 0):
                    self.txtReceipt.insert(END, 'Delux Ward\t\t\t'+e_delux.get() + "x5300 = "+ str(result3) + "\n")
                if (var4.get() > 0):
                    self.txtReceipt.insert(END, 'ICCU Ward\t\t\t'+e_iccu.get() + "x7000 = "+ str(result4) + "\n")
                if (var5.get() > 0):
                    self.txtReceipt.insert(END, 'Tracheostomy charge\t\t'+e_trac.get() + "x5500 = "+ str(result5) + "\n")
                if (var6.get() > 0):
                    self.txtReceipt.insert(END, 'IJVCVP charge\t\t\t'+e_ij.get() + "x2500 = "+ str(result87) + "\n")
                if (var7.get() > 0):
                    self.txtReceipt.insert(END, 'Intubation charge\t\t'+e_intu.get() + "x1500 = "+ str(result88) + "\n")
                if (var8.get() > 0):
                    self.txtReceipt.insert(END, 'Arterial Line \t\t\t'+e_art.get() + "x2500 = "+ str(result89) + "\n")
                if (var9.get() > 0):
                    self.txtReceipt.insert(END, 'DLC charge\t\t\t'+e_dlc.get() + "x3500 = "+ str(result6) + "\n")
                if (var10.get() > 0):
                    self.txtReceipt.insert(END, 'ECG charge\t\t\t'+e_ecg.get() + "x300 = "+ str(result7) + "\n")
                if (var11.get() > 0):
                    self.txtReceipt.insert(END, 'FOLYS charge\t\t\t'+e_folys.get() + "x250 = "+ str(result8) + "\n")
                if (var12.get() > 0):
                    self.txtReceipt.insert(END, 'RT charge\t\t\t'+e_rt.get() + "x250 = "+ str(result9) + "\n")
                if (var13.get() > 0):
                    self.txtReceipt.insert(END, 'ICD charge\t\t\t'+e_icd.get() + "x5000 = "+ str(result10) + "\n")
                if (var14.get() > 0):
                    self.txtReceipt.insert(END, 'Pleural Tapping\t\t'+e_ple.get() + "x3000 = "+ str(result11) + "\n")
                if (var15.get() > 0):
                    self.txtReceipt.insert(END, 'Thrombolise(5k)\t\t'+e_thr.get() + "x5000 = "+ str(result12) + "\n")
                if (var16.get() > 0):
                    self.txtReceipt.insert(END, 'BT charge\t\t\t'+e_bt.get() + "x250 = "+ str(result13) + "\n")
                if (var17.get() > 0):
                    self.txtReceipt.insert(END, 'Biopsy charge\t\t\t'+e_bio.get() + "x6000 = "+ str(result14) + "\n")
                if (var18.get() > 0):
                    self.txtReceipt.insert(END, 'Ascites Tapping\t\t'+e_asc.get() + "x3500 = "+ str(result15) + "\n")
                if (var19.get() > 0):
                    self.txtReceipt.insert(END, 'Bronchoscopy\t\t\t'+e_bro.get() + "x5000 = "+ str(result17) + "\n")
                if (var20.get() > 0):
                    self.txtReceipt.insert(END, 'Chemotherapy\t\t\t'+e_che.get() + "x4000 = "+ str(result16) + "\n")
                if (var21.get() > 0):
                    self.txtReceipt.insert(END, 'Chemo Planning Adm\t\t'+e_cpa.get() + "x20000 = "+ str(result18) + "\n")
                if (var22.get() > 0):
                    self.txtReceipt.insert(END, 'Chemo Protocol\t\t\t'+e_chp.get() + "x6000 = "+ str(result19) + "\n")
                if (var23.get() > 0):
                    self.txtReceipt.insert(END, 'Colonoscopy\t\t\t'+e_col.get() + "x5000 = "+ str(result20) + "\n")
                if (var24.get() > 0):
                    self.txtReceipt.insert(END, 'Lp-CSF charge\t\t\t'+e_lp.get() + "x3500 = "+ str(result21) + "\n")
                if (var25.get() > 0):
                    self.txtReceipt.insert(END, 'PFT\t\t\t\t'+e_pft.get() + "x1000 = "+ str(result22) + "\n")
                if (var26.get() > 0):
                    self.txtReceipt.insert(END, 'PICC charge\t\t\t'+e_pic.get() + "x4000 = "+ str(result23) + "\n")
                if (var27.get() > 0):
                    self.txtReceipt.insert(END, 'Pigtail charge\t\t\t'+e_pig.get() + "x3500 = "+ str(result24) + "\n")
                if (var28.get() > 0):
                    self.txtReceipt.insert(END, 'Thrombolise(2k)\t\t'+e_thr1.get() + "x2000 = "+ str(result25) + "\n")
                if (var29.get() > 0):
                    self.txtReceipt.insert(END, 'TMT charge\t\t\t'+e_tmt.get() + "x1000 = "+ str(result26) + "\n")
                if (var30.get() > 0):
                    self.txtReceipt.insert(END, 'Ventilator charge\t\t'+e_vc.get() + "x4500 = "+ str(result27) + "\n")
                if (var31.get() > 0):
                    self.txtReceipt.insert(END, 'C-Pap charge\t\t\t'+e_pap.get() + "x3500 = "+ str(result28) + "\n")
                if (var32.get() > 0):
                    self.txtReceipt.insert(END, 'Oxygen charge\t\t\t'+e_oxy.get() + "x1500 = "+ str(result34) + "\n")
                if (var33.get() > 0):
                    self.txtReceipt.insert(END, 'D-feb charge\t\t\t'+e_dfeb.get() + "x500 = "+ str(result29) + "\n")
                if (var34.get() > 0):
                    self.txtReceipt.insert(END, 'LaproScopy charge\t\t'+e_lap.get() + "x5000 = "+ str(result30) + "\n")
                if (var35.get() > 0):
                    self.txtReceipt.insert(END, 'Monitor charge\t\t\t'+e_mc.get() + "x300 = "+ str(result31) + "\n")
                if (var36.get() > 0):
                    self.txtReceipt.insert(END, 'Arterial Line Mon.\t\t'+e_art.get() + "x350 = "+ str(result32) + "\n")
                if (var37.get() > 0):
                    self.txtReceipt.insert(END, 'MLC charge\t\t\t'+e_mlc.get() + "x3000 = "+ str(result35) + "\n")
                if (var38.get() > 0):
                    self.txtReceipt.insert(END, 'Anaethiest charge\t\t'+e_ana.get() + "x5000 = "+ str(result36) + "\n")
                if (var39.get() > 0):
                    self.txtReceipt.insert(END, 'Ass. Surgeon charge\t\t'+e_ass.get() + "x15000 = "+ str(result37) + "\n")
                if (var40.get() > 0):
                    self.txtReceipt.insert(END, 'Consumable charge\t\t'+e_cns.get() + "x2000 = "+ str(result38) + "\n")
                if (var41.get() > 0):
                    self.txtReceipt.insert(END, 'CVP Monitoring\t\t\t'+e_cvp.get() + "x350 = "+ str(result39) + "\n")
                if (var42.get() > 0):
                    self.txtReceipt.insert(END, 'Day Care charge\t\t'+e_day.get() + "x500 = "+ str(result40) + "\n")
                if (var43.get() > 0):
                    self.txtReceipt.insert(END, 'Dialysis Tech. charge\t\t'+e_dte.get() + "x800 = "+ str(result41) + "\n")
                if (var44.get() > 0):
                    self.txtReceipt.insert(END, 'Dressing\t\t\t'+e_dre.get() + "x300 = "+ str(result42) + "\n")
                if (var45.get() > 0):
                    self.txtReceipt.insert(END, 'Emr. Poison Mgt.\t\t'+e_poi.get() + "x3000 = "+ str(result43) + "\n")
                if (var46.get() > 0):
                    self.txtReceipt.insert(END, 'HGT charge\t\t\t'+e_hgt.get() + "x100 = "+ str(result44) + "\n")
                if (var47.get() > 0):
                    self.txtReceipt.insert(END, 'High Mask charge\t\t'+e_hmc.get() + "x1500 = "+ str(result45) + "\n")
                if (var48.get() > 0):
                    self.txtReceipt.insert(END, 'ICU Emr Mgt charge\t\t'+e_iemc.get() + "x5000 = "+ str(result46) + "\n")
                if (var49.get() > 0):
                    self.txtReceipt.insert(END, 'Implant Removal \t\t'+e_irc.get() + "x3000 = "+ str(result47) + "\n")
                if (var50.get() > 0):
                    self.txtReceipt.insert(END, 'Infusion Pump\t\t\t'+e_ipc.get() + "x200 = "+ str(result48) + "\n")
                if (var51.get() > 0):
                    self.txtReceipt.insert(END, 'Isolation charge\t\t'+e_ic.get() + "x500 = "+ str(result49) + "\n")
                if (var52.get() > 0):
                    self.txtReceipt.insert(END, 'IV charge\t\t\t'+e_iv.get() + "x100 = "+ str(result50) + "\n")
                if (var53.get() > 0):
                    self.txtReceipt.insert(END, 'Nebulizer charge\t\t'+e_nc.get() + "x100 = "+ str(result51) + "\n")
                if (var54.get() > 0):
                    self.txtReceipt.insert(END, 'Poison Leveage charge\t\t'+e_pl.get() + "x1500 = "+ str(result52) + "\n")
                if (var55.get() > 0):
                    self.txtReceipt.insert(END, 'Procedure charge\t\t'+e_prc.get() + "x1500 = "+ str(result53) + "\n")
                if (var56.get() > 0):
                    self.txtReceipt.insert(END, 'Level1 General\t\t\t'+e_g.get() + "x9000 = "+ str(result54) + "\n")
                if (var57.get() > 0):
                    self.txtReceipt.insert(END, 'Level1 Semi Special\t\t'+e_ss.get() + "x11000 = "+ str(result55) + "\n")
                if (var58.get() > 0):
                    self.txtReceipt.insert(END, 'Level1 AC\t\t\t'+e_ac.get() + "x12500 = "+ str(result56) + "\n")
                if (var59.get() > 0):
                    self.txtReceipt.insert(END, 'Level2 General\t\t\t'+e_g2.get() + "x15000 = "+ str(result57) + "\n")
                if (var60.get() > 0):
                    self.txtReceipt.insert(END, 'Level2 Semi Special\t\t'+e_ss2.get() + "x18000 = "+ str(result58) + "\n")
                if (var61.get() > 0):
                    self.txtReceipt.insert(END, 'Level2 AC\t\t\t'+e_ac2.get() + "x21000 = "+ str(result59) + "\n")
                if (var62.get() > 0):
                    self.txtReceipt.insert(END, 'Level3 General\t\t\t'+e_g3.get() + "x21000 = "+ str(result60) + "\n")
                if (var63.get() > 0):
                    self.txtReceipt.insert(END, 'Level3 Semi Special\t\t'+e_ss3.get() + "x24000 = "+ str(result61) + "\n")
                if (var64.get() > 0):
                    self.txtReceipt.insert(END, 'Level3 AC\t\t\t'+e_ac3.get() + "x28000 = "+ str(result62) + "\n")
                if (var65.get() > 0):
                    self.txtReceipt.insert(END, 'Level4 General\t\t\t'+e_g4.get() + "x28000 = "+ str(result63) + "\n")
                if (var66.get() > 0):
                    self.txtReceipt.insert(END, 'Level4 AC\t\t\t'+e_ac4.get() + "x37000 = "+ str(result65) + "\n")
                if (var67.get() > 0):
                    self.txtReceipt.insert(END, 'Level5A General\t\t'+e_g5a.get() + "x35000 = "+ str(result66) + "\n")
                if (var68.get() > 0):
                    self.txtReceipt.insert(END, 'Level5A Semi Special\t\t'+e_ss5a.get() + "x40000 = "+ str(result67) + "\n")
                if (var69.get() > 0):
                    self.txtReceipt.insert(END, 'Level5A AC\t\t\t'+e_ac5a.get() + "x45000 = "+ str(result68) + "\n")
                if (var70.get() > 0):
                    self.txtReceipt.insert(END, 'Level5B General\t\t'+e_g5b.get() + "x45000 = "+ str(result69) + "\n")
                if (var71.get() > 0):
                    self.txtReceipt.insert(END, 'Level5B Semi Special\t\t'+e_ss5b.get() + "x50000 = "+ str(result70) + "\n")
                if (var72.get() > 0):
                    self.txtReceipt.insert(END, 'Level5B AC\t\t\t'+e_ac5b.get() + "x56000 = "+ str(result71) + "\n")
                if (var73.get() > 0):
                    self.txtReceipt.insert(END, 'Level6 General\t\t\t'+e_g6.get() + "x56000 = "+ str(result72) + "\n")
                if (var74.get() > 0):
                    self.txtReceipt.insert(END, 'Level6 Semi Special\t\t\t'+e_ss6.get() + "x60000 = "+ str(result73) + "\n")
                if (var75.get() > 0):
                    self.txtReceipt.insert(END, 'Level6 AC\t\t\t'+e_ac6.get() + "x66000 = "+ str(result74) + "\n")
                if (var76.get() > 0):
                    self.txtReceipt.insert(END, 'Level7A General\t\t\t'+e_g7a.get() + "x66000 = "+ str(result75) + "\n")
                if (var77.get() > 0):
                    self.txtReceipt.insert(END, 'Level7A Semi Special\t\t'+e_ss7a.get() + "x72000 = "+ str(result76) + "\n")
                if (var78.get() > 0):
                    self.txtReceipt.insert(END, 'Level7A AC\t\t\t'+e_ac7a.get() + "x80000 = "+ str(result77) + "\n")
                if (var79.get() > 0):
                    self.txtReceipt.insert(END, 'Level7B General\t\t'+e_g7b.get() + "x80000 = "+ str(result78) + "\n")
                if (var80.get() > 0):
                    self.txtReceipt.insert(END, 'Level7B Semi Special\t\t'+e_ss7b.get() + "x87000 = "+ str(result79) + "\n")
                if (var81.get() > 0):
                    self.txtReceipt.insert(END, 'Level7B AC\t\t\t'+e_ac7b.get() + "x94000 = "+ str(result80) + "\n")
                if (var82.get() > 0):
                    self.txtReceipt.insert(END, 'Level9 General\t\t\t'+e_g9.get() + "x100000 = "+ str(result84) + "\n")
                if (var83.get() > 0):
                    self.txtReceipt.insert(END, 'Level9 Semi Special\t\t'+e_ss9.get() + "x112500 = "+ str(result85) + "\n")
                if (var84.get() > 0):
                    self.txtReceipt.insert(END, 'Level9 AC\t\t\t'+e_ac9.get() + "x125000 = "+ str(result86) + "\n")
                if (var85.get() > 0):
                    self.txtReceipt.insert(END, 'Level4 Semi Special\t\t'+e_ss4.get() + "x33000 = "+ str(result64) + "\n")
                if (var86.get() > 0):
                    self.txtReceipt.insert(END, 'Level8 General\t\t\t'+e_g8.get() + "x94000 = "+ str(result81) + "\n")
                if (var87.get() > 0):
                    self.txtReceipt.insert(END, 'Level8 Semi Special\t\t'+e_ss8.get() + "x100000 = "+ str(result82) + "\n")
                if (var88.get() > 0):
                    self.txtReceipt.insert(END, 'Level8 AC\t\t\t'+e_ac8.get() + "x112500 = "+ str(result83) + "\n")
                self.txtReceipt.insert(END,'--------------------------------------------------------------' +"\n")
                self.txtReceipt.insert(END,'Total Amount:\t\t\t' +totalV.get() + "\n")










            #=====================================================================================
            self.txtReceipt = Text(abc5, height=19, width=43, bd=10, font=('arial',9,'bold'))
            self.txtReceipt.grid(row=0,column=0)

            #==========================================FIELDS==========================================================================#
            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Bill No:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=10,textvariable=billNoV)
            self.lblCus_Ref.grid(row=0,column=1,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="IPD No:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=2,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=8,textvariable=ipdNoV)
            self.lblCus_Ref.grid(row=0,column=3,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Name:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=4,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=25,textvariable=nameV)
            self.lblCus_Ref.grid(row=0,column=5,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Date:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=6,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=15,textvariable=dateV)
            self.lblCus_Ref.grid(row=0,column=7,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Bed:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=8,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=5,textvariable=bedV)
            self.lblCus_Ref.grid(row=0,column=9,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Cons. Dr:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=10,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=15,textvariable=conDrV)
            self.lblCus_Ref.grid(row=0,column=11,pady=3,padx=10)
#========================================================================================================================#
            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Contact No:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=10,textvariable=contNoV)
            self.lblCus_Ref.grid(row=1,column=1,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Opd No:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=2,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=8,textvariable=opdNoV)
            self.lblCus_Ref.grid(row=1,column=3,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Add:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=4,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=25,textvariable=addV)
            self.lblCus_Ref.grid(row=1,column=5,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="DA/DD:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=6,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=17,textvariable=daDdV)
            self.lblCus_Ref.grid(row=1,column=7,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Age/Sex:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=8,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=4,textvariable=ageV)
            self.lblCus_Ref.grid(row=1,column=9,pady=3,padx=10)

            self.lblCus_Ref=Label(abc1,font=('arial',12,'bold'),text="Ref Dr:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=10,sticky=W)
            self.lblCus_Ref=Entry(abc1,font=('arial',12,'bold'),width=15,textvariable=refDrV)
            self.lblCus_Ref.grid(row=1,column=11,pady=3,padx=10)
            #===========================abc2-ward============================================================================
            self.lblspace=Label(abc2, text="Ward",font=('arial',8,'bold'),pady=1,bd=2,bg="cadet Blue",fg="Cornsilk",width=30,
                                justify=CENTER).grid(row=0,column=0,columnspan=4)
            #--------------------------------------------------------------------------------------------
            self.general= Checkbutton(abc2, text="General", variable=var1, onvalue=1, offvalue=0,
                                      font=('arial',7,'bold'),bg="powder blue",width=20,command=chkGeneral).grid(row=1,sticky=W)
            self.txtgeneral= Entry(abc2, textvariable=e_general,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtgeneral.grid(row=1,column=1)
            #------------------------------------------------------------------------------------------
            self.ssp= Checkbutton(abc2, text="Semi Special", variable=var2, onvalue=1, offvalue=0,
                                      font=('arial',7,'bold'),bg="powder blue",width=20,command=chkSsp).grid(row=2,sticky=W)
            self.txtssp= Entry(abc2, textvariable=e_ssp,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtssp.grid(row=2,column=1)
            #---------------------------------------------------------------------------------------
            self.delux= Checkbutton(abc2, text="Delux", variable=var3, onvalue=1, offvalue=0,
                                      font=('arial',7,'bold'),bg="powder blue",width=20,command=chkDelux).grid(row=3,sticky=W)
            self.txtdelux= Entry(abc2, textvariable=e_delux,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtdelux.grid(row=3,column=1)
            #-----------------------------------------------------------------------------------------
            self.iccu= Checkbutton(abc2, text="ICCU", variable=var4, onvalue=1, offvalue=0,
                                      font=('arial',7,'bold'),bg="powder blue",width=20,command=chkIccu).grid(row=4,sticky=W)
            self.txticcu= Entry(abc2, textvariable=e_iccu,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txticcu.grid(row=4,column=1)
            #=================abcd2-Procedure Charges===================================================
            self.lblspace=Label(abc2, text="Procedure Charges",font=('arial',8,'bold'),pady=1,bd=2,bg="cadet Blue",fg="Cornsilk",width=30,
                                justify=LEFT).grid(row=5,column=0,columnspan=4)
            #------------------------------------------------------------------------------------------
            self.trac= Checkbutton(abc2, text="Tracheostomy Charge", variable=var5, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkTrac).grid(row=6,sticky=W)
            self.txttrac= Entry(abc2, textvariable=e_trac,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify=LEFT,state= DISABLED)
            self.txttrac.grid(row=6,column=1)
            #--------------------------------------------------------------------------------------------
            self.ij= Checkbutton(abc2, text="IJVCVP Charge", variable=var6, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkIj).grid(row=7,sticky=W)
            self.txtij= Entry(abc2, textvariable=e_ij,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify=LEFT,state= DISABLED)
            self.txtij.grid(row=7,column=1)
            #----------------------------------------------------------------------------------------------
            self.intu= Checkbutton(abc2, text="Intubation Charge", variable=var7, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkIntu).grid(row=8,sticky=W)
            self.txtintu= Entry(abc2, textvariable=e_intu,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtintu.grid(row=8,column=1)
            #----------------------------------------------------------------------------------------------
            self.art= Checkbutton(abc2, text="Arterial Line", variable=var8, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkArt).grid(row=9,sticky=W)
            self.txtart= Entry(abc2, textvariable=e_art,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtart.grid(row=9,column=1)
            #--------------------------------------------------------------------------------------------
            self.dlc= Checkbutton(abc2, text="DLC Character", variable=var9, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkDlc).grid(row=10,sticky=W)
            self.txtdlc= Entry(abc2, textvariable=e_dlc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtdlc.grid(row=10,column=1)
            #----------------------------------------------------------------------------------------------
            self.ecg= Checkbutton(abc2, text="ECG", variable=var10, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkEcg).grid(row=11,sticky=W)
            self.txtecg= Entry(abc2, textvariable=e_ecg,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtecg.grid(row=11,column=1)
            #----------------------------------------------------------------------------------------------
            self.folys= Checkbutton(abc2, text="FOLYS", variable=var11, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkFolys).grid(row=12,sticky=W)
            self.txtfolys= Entry(abc2, textvariable=e_folys,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtfolys.grid(row=12,column=1)
            #--------------------------------------------------------------------------------------------
            self.rt= Checkbutton(abc2, text="RT Charge", variable=var12, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkRt).grid(row=13,sticky=W)
            self.txtrt= Entry(abc2, textvariable=e_rt,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtrt.grid(row=13,column=1)
            #----------------------------------------------------------------------------------------------
            self.icd= Checkbutton(abc2, text="ICD Charge", variable=var13, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkIcd).grid(row=14,sticky=W)
            self.txticd= Entry(abc2, textvariable=e_icd,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txticd.grid(row=14,column=1)
            #----------------------------------------------------------------------------------------------
            self.ple= Checkbutton(abc2, text="Pleural Tapping", variable=var14, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkPle).grid(row=15,sticky=W)
            self.txtple= Entry(abc2, textvariable=e_ple,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtple.grid(row=15,column=1)
            #--------------------------------------------------------------------------------------------
            self.thr= Checkbutton(abc2, text="Thrombolise(5k)", variable=var15, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkThr).grid(row=16,sticky=W)
            self.txtthr= Entry(abc2, textvariable=e_thr,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtthr.grid(row=16,column=1)
            #----------------------------------------------------------------------------------------------
            self.bt= Checkbutton(abc2, text="BT Charge", variable=var16, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkBt).grid(row=17,sticky=W)
            self.txtbt= Entry(abc2, textvariable=e_bt,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtbt.grid(row=17,column=1)
            #----------------------------------------------------------------------------------------------
            self.bio= Checkbutton(abc2, text="Biopsy Charge", variable=var17, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkBio).grid(row=18,sticky=W)
            self.txtbio= Entry(abc2, textvariable=e_bio,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtbio.grid(row=18,column=1)
            #--------------------------------------------------------------------------------------------
            self.asc= Checkbutton(abc2, text="Ascites Tapping", variable=var18, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkAsc).grid(row=19,sticky=W)
            self.txtasc= Entry(abc2, textvariable=e_asc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtasc.grid(row=19,column=1)
            #----------------------------------------------------------------------------------------------
            self.bro= Checkbutton(abc2, text="Bronchoscopy Charge", variable=var19, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkBro).grid(row=20,sticky=W)
            self.txtbro= Entry(abc2, textvariable=e_bro,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtbro.grid(row=20,column=1)
            #----------------------------------------------------------------------------------------------
            self.che= Checkbutton(abc2, text="Chemotherapy Charge", variable=var20, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkChe).grid(row=21,sticky=W)
            self.txtche= Entry(abc2, textvariable=e_che,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtche.grid(row=21,column=1) #asc/bro/che
            #--------------------------------------------------------------------------------------------
            self.cpa= Checkbutton(abc2, text="Chemo Planning adm", variable=var21, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkCpa).grid(row=22,sticky=W)
            self.txtcpa= Entry(abc2, textvariable=e_cpa,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtcpa.grid(row=22,column=1)
            #----------------------------------------------------------------------------------------------
            self.chp= Checkbutton(abc2, text="Chemo Protocol", variable=var22, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkChp).grid(row=23,sticky=W)
            self.txtchp= Entry(abc2, textvariable=e_chp,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtchp.grid(row=23,column=1)
            #----------------------------------------------------------------------------------------------
            self.col= Checkbutton(abc2, text="Colonoscopy", variable=var23, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkCol).grid(row=24,sticky=W)
            self.txtcol= Entry(abc2, textvariable=e_col,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtcol.grid(row=24,column=1)   #cpa/chp/col

            #----------------------------------------------------------------------------------------------
            self.pft= Checkbutton(abc3, text="PFT Charge", variable=var25, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkPft).grid(row=0,sticky=W)
            self.txtpft= Entry(abc3, textvariable=e_pft,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpft.grid(row=0,column=1)
            #----------------------------------------------------------------------------------------------
            self.pic= Checkbutton(abc3, text="PICC Charge", variable=var26, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkPic).grid(row=1,sticky=W)
            self.txtpic= Entry(abc3, textvariable=e_pic,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpic.grid(row=1,column=1)   #cpa/chp/col
            #----------------------------------------------------------------------------------------------
            self.pig= Checkbutton(abc3, text="Pigtail CHARGE ", variable=var27, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkPig).grid(row=2,sticky=W)
            self.txtpig= Entry(abc3, textvariable=e_pig,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpig.grid(row=2,column=1)   #cpa/chp/col
            #----------------------------------------------------------------------------------------------
            self.lp= Checkbutton(abc3, text="LP-CSF CHARGE ", variable=var24, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkLp).grid(row=3,sticky=E+W)
            self.txtlp= Entry(abc3, textvariable=e_lp,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtlp.grid(row=3,column=1)   #cpa/chp/col

            #----------------------------------------------------------------------------------------------
            self.thr1= Checkbutton(abc3, text="Thrombolise(1k)", variable=var28, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,command=chkThr1).grid(row=4,sticky=W)
            self.txtthr1= Entry(abc3, textvariable=e_thr1,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtthr1.grid(row=4,column=1)   #cpa/chp/col
            #----------------------------------------------------------------------------------------------
            self.tmt= Checkbutton(abc3, text="TMT CHARGE ", variable=var29, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkTmt).grid(row=5,sticky=E+W)
            self.txttmt= Entry(abc3, textvariable=e_tmt,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txttmt.grid(row=5,column=1)
            #=================abc3-Machine Charges===================================================
            self.lblspace=Label(abc3, text="Machine Charges",font=('arial',8,'bold'),pady=1,bd=2,bg="cadet Blue",fg="Cornsilk",width=30,
                                justify=CENTER).grid(row=6,column=0,columnspan=4)
            #----------------------------------------------------------------------------------------------
            self.vc= Checkbutton(abc3, text="Ventilator CHARGE ", variable=var30, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkVc).grid(row=7,sticky=E+W)
            self.txtvc= Entry(abc3, textvariable=e_vc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtvc.grid(row=7,column=1)      #vc/pap/oxy/dfeb/lap/mc/alm
            #----------------------------------------------------------------------------------------------
            self.pap= Checkbutton(abc3, text="C-PapCHARGE ICU", variable=var31, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkPap).grid(row=8,sticky=E+W)
            self.txtpap= Entry(abc3, textvariable=e_pap,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpap.grid(row=8,column=1)
            #----------------------------------------------------------------------------------------------
            self.oxy= Checkbutton(abc3, text="Oxy CHARGE ICU ", variable=var32, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkOxy).grid(row=9,sticky=E+W)
            self.txtoxy= Entry(abc3, textvariable=e_oxy,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtoxy.grid(row=9,column=1)
            #----------------------------------------------------------------------------------------------
            self.dfeb= Checkbutton(abc3, text="D-Feb CHARGE ", variable=var33, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkDfeb).grid(row=10,sticky=E+W)
            self.txtdfeb= Entry(abc3, textvariable=e_dfeb,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtdfeb.grid(row=10,column=1)
            #----------------------------------------------------------------------------------------------
            self.lap= Checkbutton(abc3, text="LaproScopy CHARGE ", variable=var34, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkLap).grid(row=11,sticky=E+W)
            self.txtlap= Entry(abc3, textvariable=e_lap,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtlap.grid(row=11,column=1)
            #----------------------------------------------------------------------------------------------
            self.mc= Checkbutton(abc3, text="Monitor CHARGE ", variable=var35, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkMc).grid(row=12,sticky=E+W)
            self.txtmc= Entry(abc3, textvariable=e_mc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtmc.grid(row=12,column=1)
            #----------------------------------------------------------------------------------------------
            self.alm= Checkbutton(abc3, text="Arterial Line Monitor", variable=var36, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkAlm).grid(row=13,sticky=E+W)
            self.txtalm= Entry(abc3, textvariable=e_alm,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtalm.grid(row=13,column=1)

            #==================================abc3-Other Charges===================================================
            self.lblspace=Label(abc3, text="Other Charges",font=('arial',8,'bold'),pady=1,bd=2,bg="cadet Blue",fg="Cornsilk",width=30,
                                justify=CENTER).grid(row=14,column=0,columnspan=4)

            #----------------------------------------------------------------------------------------------
            self.mlc= Checkbutton(abc3, text="MLC CHARGE", variable=var37, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkMlc).grid(row=15,sticky=E+W)
            self.txtmlc= Entry(abc3, textvariable=e_mlc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtmlc.grid(row=15,column=1)      #mlc/ana/ass/cns/cvp/day/dte/dre/poi/hgt
            #----------------------------------------------------------------------------------------------
            self.ana= Checkbutton(abc3, text="Anaethiest CHARGE", variable=var38, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkAna).grid(row=16,sticky=E+W)
            self.txtana= Entry(abc3, textvariable=e_ana,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtana.grid(row=16,column=1)
            #----------------------------------------------------------------------------------------------
            self.ass= Checkbutton(abc3, text="Ass. Surgeon Charge", variable=var39, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkAss).grid(row=17,sticky=E+W)
            self.txtass= Entry(abc3, textvariable=e_ass,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtass.grid(row=17,column=1)
            #----------------------------------------------------------------------------------------------
            self.cns= Checkbutton(abc3, text="Consumable CHARGE ", variable=var40, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkCns).grid(row=18,sticky=E+W)
            self.txtcns= Entry(abc3, textvariable=e_cns,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtcns.grid(row=18,column=1)
            #----------------------------------------------------------------------------------------------
            self.cvp= Checkbutton(abc3, text="CVP Monitoring", variable=var41, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkCvp).grid(row=19,sticky=E+W)
            self.txtcvp= Entry(abc3, textvariable=e_cvp,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtcvp.grid(row=19,column=1)
            #----------------------------------------------------------------------------------------------
            self.day= Checkbutton(abc3, text="Day Care", variable=var42, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkDay).grid(row=20,sticky=E+W)
            self.txtday= Entry(abc3, textvariable=e_day,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtday.grid(row=20,column=1)
            #----------------------------------------------------------------------------------------------
            self.dte= Checkbutton(abc3, text="Dialysis Technician", variable=var43, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkDte).grid(row=21,sticky=E+W)
            self.txtdte= Entry(abc3, textvariable=e_dte,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtdte.grid(row=21,column=1)

            #----------------------------------------------------------------------------------------------
            self.dre= Checkbutton(abc3, text="Dressing", variable=var44, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkDre).grid(row=22,sticky=E+W)
            self.txtdre= Entry(abc3, textvariable=e_dre,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtdre.grid(row=22,column=1)
            #----------------------------------------------------------------------------------------------
            self.poi= Checkbutton(abc3, text="Emr Poison Mgt.", variable=var45, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkPoi).grid(row=23,sticky=E+W)
            self.txtpoi= Entry(abc3, textvariable=e_poi,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpoi.grid(row=23,column=1)
            #----------------------------------------------------------------------------------------------
            self.hgt= Checkbutton(abc3, text="HGT Charge", variable=var46, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkHgt).grid(row=24,sticky=E+W)
            self.txthgt= Entry(abc3, textvariable=e_hgt,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txthgt.grid(row=24,column=1)
            #----------------------------------------------------------------------------------------------
            self.hmc= Checkbutton(abc7, text="High Mask Charge", variable=var47, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkHmc).grid(row=0,sticky=E+W)
            self.txthmc= Entry(abc7, textvariable=e_hmc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txthmc.grid(row=0,column=1)
            #----------------------------------------------------------------------------------------------
            self.iemc= Checkbutton(abc7, text="ICU Emr. Mgt. CHARGE", variable=var48, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkIemc).grid(row=1,sticky=E+W)
            self.txtiemc= Entry(abc7, textvariable=e_iemc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtiemc.grid(row=1,column=1)
            #----------------------------------------------------------------------------------------------
            self.irc= Checkbutton(abc7, text="Implant Removal Charge", variable=var49, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkIrc).grid(row=2,sticky=E+W)
            self.txtirc= Entry(abc7, textvariable=e_irc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtirc.grid(row=2,column=1)
            #----------------------------------------------------------------------------------------------
            self.ipc= Checkbutton(abc7, text="Infusion pump CHARGE ", variable=var50, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkIpc).grid(row=3,sticky=E+W)
            self.txtipc= Entry(abc7, textvariable=e_ipc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtipc.grid(row=3,column=1)
            #----------------------------------------------------------------------------------------------
            self.ic= Checkbutton(abc7, text="Isolation Charge", variable=var51, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkIc).grid(row=4,sticky=E+W)
            self.txtic= Entry(abc7, textvariable=e_ic,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtic.grid(row=4,column=1)
            #----------------------------------------------------------------------------------------------
            self.iv= Checkbutton(abc7, text="IV Charge", variable=var52, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkIv).grid(row=5,sticky=E+W)
            self.txtiv= Entry(abc7, textvariable=e_iv,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtiv.grid(row=5,column=1)
            #----------------------------------------------------------------------------------------------
            self.nc= Checkbutton(abc7, text="Nebulizer Charge", variable=var53, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkNc).grid(row=6,sticky=E+W)
            self.txtnc= Entry(abc7, textvariable=e_nc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtnc.grid(row=6,column=1)

            #----------------------------------------------------------------------------------------------
            self.pl= Checkbutton(abc7, text="Poison Leveage", variable=var54, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkPl).grid(row=7,sticky=E+W)
            self.txtpl= Entry(abc7, textvariable=e_pl,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtpl.grid(row=7,column=1)      #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
            #----------------------------------------------------------------------------------------------
            self.prc= Checkbutton(abc7, text="Procedure Charges", variable=var55, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=20,justify=LEFT,command=chkPrc).grid(row=8,sticky=E+W)
            self.txtprc= Entry(abc7, textvariable=e_prc,font=('arial',8,'bold'),bd=1,width=5
                                   ,justify='left',state= DISABLED)
            self.txtprc.grid(row=8,column=1)
            #==================================abc7-Operative Charges===================================================
            self.lblspace=Label(abc7, text="Operative Charges",font=('arial',8,'bold'),pady=1,bd=2,bg="cadet Blue",fg="Cornsilk",width=30,
                                justify=CENTER).grid(row=9,column=0,columnspan=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level1:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g= Checkbutton(abc8, text="G", variable=var56, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG).grid(row=0,column=1,sticky=E+W)
            self.txtg= Entry(abc8, textvariable=e_g,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg.grid(row=0,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss= Checkbutton(abc8, text="SS", variable=var57, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs).grid(row=0,column=3,sticky=E+W)
            self.txtss= Entry(abc8, textvariable=e_ss,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss.grid(row=0,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac= Checkbutton(abc8, text="AC", variable=var58, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc).grid(row=0,column=5,sticky=E+W)
            self.txtac= Entry(abc8, textvariable=e_ac,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac.grid(row=0,column=6)

            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level2:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g2= Checkbutton(abc8, text="G", variable=var59, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG2).grid(row=1,column=1,sticky=E+W)
            self.txtg2= Entry(abc8, textvariable=e_g2,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg2.grid(row=1,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss2= Checkbutton(abc8, text="SS", variable=var60, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs2).grid(row=1,column=3,sticky=E+W)
            self.txtss2= Entry(abc8, textvariable=e_ss2,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss2.grid(row=1,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac2= Checkbutton(abc8, text="AC", variable=var61, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc2).grid(row=1,column=5,sticky=E+W)
            self.txtac2= Entry(abc8, textvariable=e_ac2,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac2.grid(row=1,column=6)

            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level3:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=2,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g3= Checkbutton(abc8, text="G", variable=var62, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG3).grid(row=2,column=1,sticky=E+W)
            self.txtg3= Entry(abc8, textvariable=e_g3,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg3.grid(row=2,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss3= Checkbutton(abc8, text="SS", variable=var63, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs3).grid(row=2,column=3,sticky=E+W)
            self.txtss3= Entry(abc8, textvariable=e_ss3,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss3.grid(row=2,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac3= Checkbutton(abc8, text="AC", variable=var64, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc3).grid(row=2,column=5,sticky=E+W)
            self.txtac3= Entry(abc8, textvariable=e_ac3,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac3.grid(row=2,column=6)

            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level4:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=3,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g4= Checkbutton(abc8, text="G", variable=var65, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG4).grid(row=3,column=1,sticky=E+W)
            self.txtg4= Entry(abc8, textvariable=e_g4,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg4.grid(row=3,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss4= Checkbutton(abc8, text="SS", variable=var85, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs4).grid(row=3,column=3,sticky=E+W)
            self.txtss4= Entry(abc8, textvariable=e_ss4,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss4.grid(row=3,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac4= Checkbutton(abc8, text="AC", variable=var66, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc4).grid(row=3,column=5,sticky=E+W)
            self.txtac4= Entry(abc8, textvariable=e_ac4,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac4.grid(row=3,column=6)

            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level5A:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=4,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g5a= Checkbutton(abc8, text="G", variable=var67, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG5a).grid(row=4,column=1,sticky=E+W)
            self.txtg5a= Entry(abc8, textvariable=e_g5a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg5a.grid(row=4,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss5a= Checkbutton(abc8, text="SS", variable=var68, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs5a).grid(row=4,column=3,sticky=E+W)
            self.txtss5a= Entry(abc8, textvariable=e_ss5a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss5a.grid(row=4,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac5a= Checkbutton(abc8, text="AC", variable=var69, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc5a).grid(row=4,column=5,sticky=E+W)
            self.txtac5a= Entry(abc8, textvariable=e_ac5a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac5a.grid(row=4,column=6)

            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level5B:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=5,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g5b= Checkbutton(abc8, text="G", variable=var70, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG5b).grid(row=5,column=1,sticky=E+W)
            self.txtg5b= Entry(abc8, textvariable=e_g5b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg5b.grid(row=5,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss5b= Checkbutton(abc8, text="SS", variable=var71, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs5b).grid(row=5,column=3,sticky=E+W)
            self.txtss5b= Entry(abc8, textvariable=e_ss5b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss5b.grid(row=5,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac5b= Checkbutton(abc8, text="AC", variable=var72, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc5b).grid(row=5,column=5,sticky=E+W)
            self.txtac5b= Entry(abc8, textvariable=e_ac5b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac5b.grid(row=5,column=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level6:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=6,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g6= Checkbutton(abc8, text="G", variable=var73, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG6).grid(row=6,column=1,sticky=E+W)
            self.txtg6= Entry(abc8, textvariable=e_g6,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg6.grid(row=6,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss6= Checkbutton(abc8, text="SS", variable=var74, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs6).grid(row=6,column=3,sticky=E+W)
            self.txtss6= Entry(abc8, textvariable=e_ss6,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss6.grid(row=6,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac6= Checkbutton(abc8, text="AC", variable=var75, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc6).grid(row=6,column=5,sticky=E+W)
            self.txtac6= Entry(abc8, textvariable=e_ac6,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac6.grid(row=6,column=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level7A:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=7,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g7a= Checkbutton(abc8, text="G", variable=var76, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG7a).grid(row=7,column=1,sticky=E+W)
            self.txtg7a= Entry(abc8, textvariable=e_g7a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg7a.grid(row=7,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss7a= Checkbutton(abc8, text="SS", variable=var77, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs7a).grid(row=7,column=3,sticky=E+W)
            self.txtss7a= Entry(abc8, textvariable=e_ss7a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss7a.grid(row=7,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac7a= Checkbutton(abc8, text="AC", variable=var78, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc7a).grid(row=7,column=5,sticky=E+W)
            self.txtac7a= Entry(abc8, textvariable=e_ac7a,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac7a.grid(row=7,column=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level7B:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=8,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g7b= Checkbutton(abc8, text="G", variable=var79, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG7b).grid(row=8,column=1,sticky=E+W)
            self.txtg7b= Entry(abc8, textvariable=e_g7b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg7b.grid(row=8,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss7b= Checkbutton(abc8, text="SS", variable=var80, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs7b).grid(row=8,column=3,sticky=E+W)
            self.txtss7b= Entry(abc8, textvariable=e_ss7b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss7b.grid(row=8,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac7b= Checkbutton(abc8, text="AC", variable=var81, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc7b).grid(row=8,column=5,sticky=E+W)
            self.txtac7b= Entry(abc8, textvariable=e_ac7b,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac7b.grid(row=8,column=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level8:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=9,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g8= Checkbutton(abc8, text="G", variable=var86, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG8).grid(row=9,column=1,sticky=E+W)
            self.txtg8= Entry(abc8, textvariable=e_g8,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg8.grid(row=9,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss8= Checkbutton(abc8, text="SS", variable=var87, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs8).grid(row=9,column=3,sticky=E+W)
            self.txtss8= Entry(abc8, textvariable=e_ss8,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss8.grid(row=9,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac8= Checkbutton(abc8, text="AC", variable=var88, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc8).grid(row=9,column=5,sticky=E+W)
            self.txtac8= Entry(abc8, textvariable=e_ac8,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac8.grid(row=9,column=6)
            #-------------------------------------------------------------------------------------------------------
            self.lblCus_Ref=Label(abc8,font=('arial',10,'bold'),text="Level9:",padx=2,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=10,column=0,sticky=W)

            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.g9= Checkbutton(abc8, text="G", variable=var82, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkG9).grid(row=10,column=1,sticky=E+W)
            self.txtg9= Entry(abc8, textvariable=e_g9,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtg9.grid(row=10,column=2)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ss9= Checkbutton(abc8, text="SS", variable=var83, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkSs9).grid(row=10,column=3,sticky=E+W)
            self.txtss9= Entry(abc8, textvariable=e_ss9,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtss9.grid(row=10,column=4)
            #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            self.ac9= Checkbutton(abc8, text="AC", variable=var84, onvalue=1, offvalue=0,
                                      font=('arial',8,'bold'),bg="powder blue",width=2,justify=LEFT,command=chkAc9).grid(row=10,column=5,sticky=E+W)
            self.txtac9= Entry(abc8, textvariable=e_ac9,font=('arial',8,'bold'),bd=1,width=2
                                   ,justify='left',state= DISABLED)
            self.txtac9.grid(row=10,column=6)

            #===========================Total============================================================================

            #--------------------------------------------------------------------------------------------



            self.lblCus_Ref=Label(abc9,font=('arial',12,'bold'),text="Emr Add Charges",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=0,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc9,font=('arial',12,'bold'),width=15,textvariable=addiV)
            self.lblCus_Ref.grid(row=0,column=1)

            self.lblCus_Ref=Label(abc9,font=('arial',12,'bold'),text="Other:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=1,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc9,font=('arial',12,'bold'),width=15,textvariable=otherV)
            self.lblCus_Ref.grid(row=1,column=1)

            self.lblCus_Ref=Label(abc9,font=('arial',12,'bold'),text="Total:",padx=1,fg="Cornsilk",bg="cadet Blue")
            self.lblCus_Ref.grid(row=2,column=0,sticky=W)
            self.lblCus_Ref=Entry(abc9,font=('arial',12,'bold'),width=15,textvariable=totalV)
            self.lblCus_Ref.grid(row=2,column=1)









            #=====================================Exit Button===================================
            def iExit():
                iExit = tkinter.messagebox.askyesno("IPD Billing System","Confirm if you want to Exit.")
                if iExit  > 0:
                    window.destroy()
                    return
            #======================================Reset Button=======================================================================================#
            def Reset():
                self.txtReceipt.delete("1.0",END)
                e_general.set("0")
                e_ssp.set("0")
                e_delux.set("0")
                e_iccu.set("0")
                e_trac.set("0")
                e_ij.set("0")
                e_intu.set("0")
                e_art.set("0")
                e_dlc.set("0")
                e_ecg.set("0")
                e_folys.set("0")
                e_rt.set("0")
                e_icd.set("0")
                e_ple.set("0")
                e_thr.set("0")
                e_bt.set("0")
                e_bio.set("0")
                e_asc.set("0")
                e_bro.set("0")
                e_cpa.set("0")
                e_chp.set("0")
                e_col.set("0")
                e_lp.set("0")
                e_pft.set("0")
                e_pic.set("0")
                e_pig.set("0")
                e_thr1.set("0")
                e_tmt.set("0")
                e_che.set("0")      #vc/pap/oxy/dfeb/lap/mc/alm
                e_vc.set("0")
                e_pap.set("0")
                e_oxy.set("0")
                e_dfeb.set("0")
                e_lap.set("0")
                e_mc.set("0")
                e_alm.set("0")
                e_mlc.set("0")       #mlc/ana/ass/cns/cvp/day/dte/dre/poi/hgt
                e_ana.set("0")
                e_ass.set("0")
                e_cns.set("0")
                e_cvp.set("0")
                e_day.set("0")
                e_dte.set("0")
                e_dre.set("0")
                e_poi.set("0")
                e_hgt.set("0")      #hmc/iemc/irc/ipc/ic/iv/nc/pl/prc
                e_hmc.set("0")
                e_iemc.set("0")
                e_irc.set("0")
                e_ipc.set("0")
                e_ic.set("0")
                e_iv.set("0")
                e_nc.set("0")
                e_pl.set("0")
                e_prc.set("0")
                e_g.set("0")
                e_ac.set("0")
                e_ss.set("0")
                e_g2.set("0")
                e_ac2.set("0")
                e_ss2.set("0")
                e_g3.set("0")
                e_ac3.set("0")
                e_ss3.set("0")
                e_g4.set("0")
                e_ac4.set("0")
                e_ss4.set("0")
                e_g5a.set("0")
                e_ac5a.set("0")
                e_ss5a.set("0")
                e_g5b.set("0")
                e_ac5b.set("0")
                e_ss5b.set("0")
                e_g6.set("0")
                e_ac6.set("0")
                e_ss6.set("0")
                e_g7a.set("0")
                e_ac7a.set("0")
                e_ss7a.set("0")
                e_g7b.set("0")
                e_ac7b.set("0")
                e_ss7b.set("0")
                e_g8.set("0")
                e_ac8.set("0")
                e_ss8.set("0")
                e_g9.set("0")
                e_ac9.set("0")
                e_ss9.set("0")

                var1.set("0")
                var2.set("0")
                var3.set("0")
                var4.set("0")
                var5.set("0")
                var6.set("0")
                var7.set("0")
                var8.set("0")
                var9.set("0")
                var10.set("0")
                var11.set("0")
                var12.set("0")
                var13.set("0")
                var14.set("0")
                var15.set("0")
                var16.set("0")
                var17.set("0")
                var18.set("0")
                var19.set("0")
                var20.set("0")
                var21.set("0")
                var22.set("0")
                var23.set("0")
                var24.set("0")
                var25.set("0")
                var26.set("0")
                var27.set("0")
                var28.set("0")
                var29.set("0")
                var30.set("0")
                var31.set("0")
                var32.set("0")
                var33.set("0")
                var34.set("0")
                var35.set("0")
                var36.set("0")
                var37.set("0")
                var38.set("0")
                var39.set("0")
                var40.set("0")
                var41.set("0")
                var42.set("0")
                var43.set("0")
                var44.set("0")
                var45.set("0")
                var46.set("0")
                var47.set("0")
                var48.set("0")
                var49.set("0")
                var50.set("0")
                var51.set("0")
                var52.set("0")
                var53.set("0")
                var54.set("0")
                var55.set("0")
                var56.set("0")
                var57.set("0")
                var58.set("0")
                var59.set("0")
                var60.set("0")
                var61.set("0")
                var62.set("0")
                var63.set("0")
                var64.set("0")
                var65.set("0")
                var66.set("0")
                var67.set("0")
                var68.set("0")
                var69.set("0")
                var70.set("0")
                var71.set("0")
                var72.set("0")
                var73.set("0")
                var74.set("0")
                var75.set("0")
                var76.set("0")
                var77.set("0")
                var78.set("0")
                var79.set("0")
                var80.set("0")
                var81.set("0")
                var82.set("0")
                var83.set("0")
                var84.set("0")
                var85.set("0")
                var86.set("0")
                var87.set("0")
                var88.set("0")
                var89.set("0")
                var90.set("0")
                var91.set("0")
                var92.set("0")
                var93.set("0")
                var94.set("0")
                var95.set("0")
                var96.set("0")
                var97.set("0")
                var98.set("0")
                var99.set("0")
                var100.set("0")
                var101.set("0")
                var102.set("0")
                var103.set("0")
                var104.set("0")
                var105.set("0")

                billNoV.set("")
                ipdNoV.set("")
                nameV.set("")
                dateV.set("")
                bedV.set("")
                conDrV.set("")
                contNoV.set("")
                opdNoV.set("")
                addV.set("")
                daDdV.set("")
                ageV.set("")
                refDrV.set("")

                def chkGeneral():
                    if(var1.get() ==1):
                       self.txtgeneral.configure(state=NORMAL)
                       self.txtgeneral.focus()
                       self.txtgeneral.delete('0',END)
                       e_general.set("")
                    elif var1.get() ==0:
                       self.txtgeneral.configure(state=DISABLED)
                       self.txtgeneral.set("0")

                def chkSsp():
                    if(var2.get() ==1):
                       self.txtssp.configure(state=NORMAL)
                       self.txtssp.focus()
                       self.txtssp.delete('0',END)
                       e_ssp.set("")
                    elif var2.get() ==0:
                       self.txtssp.configure(state=DISABLED)
                       self.txtssp.set("0")
                def chkDelux():
                    if(var3.get() ==1):
                       self.txtdelux.configure(state=NORMAL)
                       self.txtdelux.focus()
                       self.txtdelux.delete('0',END)
                       e_delux.set("")
                    elif var3.get() ==0:
                       self.txtdelux.configure(state=DISABLED)
                       self.txtdelux.set("0")

                def chkIccu():
                    if(var4.get() ==1):
                       self.txticcu.configure(state=NORMAL)
                       self.txticcu.focus()
                       self.txticcu.delete('0',END)
                       e_iccu.set("")
                    elif var4.get() ==0:
                       self.txticcu.configure(state=DISABLED)
                       self.txticcu.set("0")

                def chkTrac():
                    if(var5.get() ==1):
                       self.txttrac.configure(state=NORMAL)
                       self.txttrac.focus()
                       self.txttrac.delete('0',END)
                       e_trac.set("")
                    elif var5.get() ==0:
                       self.txttrac.configure(state=DISABLED)
                       self.txttrac.set("0")

                def chkIj():
                    if(var6.get() ==1):
                       self.txtij.configure(state=NORMAL)
                       self.txtij.focus()
                       self.txtij.delete('0',END)
                       e_ij.set("")
                    elif var6.get() ==0:
                       self.txtij.configure(state=DISABLED)
                       self.txtij.set("0")
                def chkIntu():
                    if(var7.get() ==1):
                       self.txtintu.configure(state=NORMAL)
                       self.txtintu.focus()
                       self.txtintu.delete('0',END)
                       e_intu.set("")
                    elif var7.get() ==0:
                       self.txtintu.configure(state=DISABLED)
                       self.txtintu.set("0")

                def chkArt():
                    if(var8.get() ==1):
                       self.txtart.configure(state=NORMAL)
                       self.txtart.focus()
                       self.txtart.delete('0',END)
                       e_art.set("")
                    elif var8.get() ==0:
                       self.txtart.configure(state=DISABLED)
                       self.txtart.set("0")
                def chkDlc():
                    if(var9.get() ==1):
                       self.txtdlc.configure(state=NORMAL)
                       self.txtdlc.focus()
                       self.txtdlc.delete('0',END)
                       e_dlc.set("")
                    elif var9.get() ==0:
                       self.txtdlc.configure(state=DISABLED)
                       self.txtdlc.set("0")

                def chkEcg():
                    if(var10.get() ==1):
                       self.txtecg.configure(state=NORMAL)
                       self.txtecg.focus()
                       self.txtecg.delete('0',END)
                       e_ecg.set("")
                    elif var10.get() ==0:
                       self.txtecg.configure(state=DISABLED)
                       self.txtecg.set("0")
                def chkFolys():
                    if(var11.get() ==1):
                       self.txtfolys.configure(state=NORMAL)
                       self.txtfolys.focus()
                       self.txtfolys.delete('0',END)
                       e_folys.set("")
                    elif var11.get() ==0:
                       self.txtfolys.configure(state=DISABLED)
                       self.txtfolys.set("0")

                def chkRt():
                    if(var12.get() ==1):
                       self.txtrt.configure(state=NORMAL)
                       self.txtrt.focus()
                       self.txtrt.delete('0',END)
                       e_rt.set("")
                    elif var12.get() ==0:
                       self.txtrt.configure(state=DISABLED)
                       self.txtrt.set("0")

                def chkCd():
                    if(var13.get() ==1):
                       self.txtcd.configure(state=NORMAL)
                       self.txtcd.focus()
                       self.txtcd.delete('0',END)
                       e_folys.set("")
                    elif var13.get() ==0:
                       self.txtcd.configure(state=DISABLED)
                       self.txtcd.set("0")

                def chkPle():
                    if(var14.get() ==1):
                       self.txtple.configure(state=NORMAL)
                       self.txtple.focus()
                       self.txtple.delete('0',END)
                       e_rt.set("")
                    elif var14.get() ==0:
                       self.txtple.configure(state=DISABLED)
                       self.txtple.set("0")
                def chkThr():
                    if(var15.get() ==1):
                       self.txtthr.configure(state=NORMAL)
                       self.txtthr.focus()
                       self.txtthr.delete('0',END)
                       e_thr.set("")
                    elif var15.get() ==0:
                       self.txtthr.configure(state=DISABLED)
                       self.txtthr.set("0")

                def chkBt():
                    if(var16.get() ==1):
                       self.txtbt.configure(state=NORMAL)
                       self.txtbt.focus()
                       self.txtbt.delete('0',END)
                       e_bt.set("")
                    elif var16.get() ==0:
                       self.txtbt.configure(state=DISABLED)
                       self.txtbt.set("0")
                def chkBio():
                    if(var17.get() ==1):
                       self.txtbio.configure(state=NORMAL)
                       self.txtbio.focus()
                       self.txtbio.delete('0',END)
                       e_bio.set("")
                    elif var17.get() ==0:
                       self.txtbio.configure(state=DISABLED)
                       self.txtbio.set("0")

                def chkAsc():
                    if(var18.get() ==1):
                       self.txtasc.configure(state=NORMAL)
                       self.txtasc.focus()
                       self.txtasc.delete('0',END)
                       e_asc.set("")
                    elif var18.get() ==0:
                       self.txtasc.configure(state=DISABLED)
                       self.txtasc.set("0")
                def chkBro():
                    if(var19.get() ==1):
                       self.txtbro.configure(state=NORMAL)
                       self.txtbro.focus()
                       self.txtbro.delete('0',END)
                       e_bro.set("")
                    elif var19.get() ==0:
                       self.txtbro.configure(state=DISABLED)
                       self.txtbro.set("0")

                def chkChe():
                    if(var20.get() ==1):
                       self.txtche.configure(state=NORMAL)
                       self.txtche.focus()
                       self.txtche.delete('0',END)
                       e_che.set("")
                    elif var20.get() ==0:
                       self.txtche.configure(state=DISABLED)
                       self.txtche.set("0")
                def chkCpa():
                    if(var21.get() ==1):
                       self.txtcpa.configure(state=NORMAL)
                       self.txtcpa.focus()
                       self.txtcpa.delete('0',END)
                       e_cpa.set("")
                    elif var21.get() ==0:
                       self.txtcpa.configure(state=DISABLED)
                       self.txtcpa.set("0")

                def chkChp():
                    if(var22.get() ==1):
                       self.txtchp.configure(state=NORMAL)
                       self.txtchp.focus()
                       self.txtchp.delete('0',END)
                       e_chp.set("")
                    elif var22.get() ==0:
                       self.txtchp.configure(state=DISABLED)
                       self.txtchp.set("0")
                def chkCpa():
                    if(var21.get() ==1):
                       self.txtcpa.configure(state=NORMAL)
                       self.txtcpa.focus()
                       self.txtcpa.delete('0',END)
                       e_cpa.set("")
                    elif var21.get() ==0:
                       self.txtcpa.configure(state=DISABLED)
                       self.txtcpa.set("0")

                def chkChp():
                    if(var22.get() ==1):
                       self.txtchp.configure(state=NORMAL)
                       self.txtchp.focus()
                       self.txtchp.delete('0',END)
                       e_chp.set("")
                    elif var22.get() ==0:
                       self.txtchp.configure(state=DISABLED)
                       self.txtchp.set("0")
            def chkCol():
                if(var23.get() ==1):
                   self.txtcol.configure(state=NORMAL)
                   self.txtcol.focus()
                   self.txtcol.delete('0',END)
                   e_col.set("")
                elif var23.get() ==0:
                   self.txtcol.configure(state=DISABLED)
                   self.txtcol.set("0")

            def chkPft():
                if(var25.get() ==1):
                   self.txtpft.configure(state=NORMAL)
                   self.txtpft.focus()
                   self.txtpft.delete('0',END)
                   e_pft.set("")
                elif var25.get() ==0:
                   self.txtpft.configure(state=DISABLED)
                   self.txtpft.set("0")
            def chkPic():
                if(var26.get() ==1):
                   self.txtpic.configure(state=NORMAL)
                   self.txtpic.focus()
                   self.txtpic.delete('0',END)
                   e_pic.set("")
                elif var26.get() ==0:
                   self.txtpic.configure(state=DISABLED)
                   self.txtpic.set("0")

            def chkPig():
                if(var27.get() ==1):
                   self.txtpig.configure(state=NORMAL)
                   self.txtpig.focus()
                   self.txtpig.delete('0',END)
                   e_pig.set("")
                elif var27.get() ==0:
                   self.txtpig.configure(state=DISABLED)
                   self.txtpig.set("0")
            def chkLp():
                if(var24.get() ==1):
                   self.txtlp.configure(state=NORMAL)
                   self.txtlp.focus()
                   self.txtlp.delete('0',END)
                   e_pic.set("")
                elif var24.get() ==0:
                   self.txtlp.configure(state=DISABLED)
                   self.txtlp.set("0")

            def chkThr1():
                if(var28.get() ==1):
                   self.txtthr1.configure(state=NORMAL)
                   self.txtthr1.focus()
                   self.txtthr1.delete('0',END)
                   e_thr1.set("")
                elif var28.get() ==0:
                   self.txtthr1.configure(state=DISABLED)
                   self.txtthr1.set("0")
            def chkTmt():
                if(var29.get() ==1):
                   self.txttmt.configure(state=NORMAL)
                   self.txttmt.focus()
                   self.txttmt.delete('0',END)
                   e_tmt.set("")
                elif var29.get() ==0:
                   self.txttmt.configure(state=DISABLED)
                   self.txttmt.set("0")

            def chkVc():
                if(var30.get() ==1):
                   self.txtvc.configure(state=NORMAL)
                   self.txtvc.focus()
                   self.txtvc.delete('0',END)
                   e_vc.set("")
                elif var30.get() ==0:
                   self.txtvc.configure(state=DISABLED)
                   self.txtvc.set("0")
            def chkPap():
                if(var31.get() ==1):
                   self.txtpap.configure(state=NORMAL)
                   self.txtpap.focus()
                   self.txtpap.delete('0',END)
                   e_pap.set("")
                elif var31.get() ==0:
                   self.txtpap.configure(state=DISABLED)
                   self.txtpap.set("0")

            def chkOxy():
                if(var32.get() ==1):
                   self.txtoxy.configure(state=NORMAL)
                   self.txtoxy.focus()
                   self.txtoxy.delete('0',END)
                   e_oxy.set("")
                elif var32.get() ==0:
                   self.txtoxy.configure(state=DISABLED)
                   self.txtoxy.set("0")
            def chkDfeb():
                if(var33.get() ==1):
                    self.txtdfeb.configure(state=NORMAL)
                    self.txtdfeb.focus()
                    self.txtdfeb.delete('0',END)
                    e_dfeb.set("")
                elif var33.get() ==0:
                    self.txtdfeb.configure(state=DISABLED)
                    self.txtdfeb.set("0")

            def chkLap():
                if(var34.get() ==1):
                    self.txtlap.configure(state=NORMAL)
                    self.txtlap.focus()
                    self.txtlap.delete('0',END)
                    e_lap.set("")
                elif var34.get() ==0:
                    self.txtlap.configure(state=DISABLED)
                    self.txtlap.set("0")

            def chkMc():
                if(var35.get() ==1):
                    self.txtmc.configure(state=NORMAL)
                    self.txtmc.focus()
                    self.txtmc.delete('0',END)
                    e_mc.set("")
                elif var35.get() ==0:
                    self.txtmc.configure(state=DISABLED)
                    self.txtmc.set("0")

            def chkAlm():
                if(var36.get() ==1):
                    self.txtalm.configure(state=NORMAL)
                    self.txtalm.focus()
                    self.txtalm.delete('0',END)
                    e_alm.set("")
                elif var36.get() ==0:
                    self.txtalm.configure(state=DISABLED)
                    self.txtalm.set("0")


            def chkMlc():
                if(var37.get() ==1):
                    self.txtmlc.configure(state=NORMAL)
                    self.txtmlc.focus()
                    self.txtmlc.delete('0',END)
                    e_mlc.set("")
                elif var37.get() ==0:
                    self.txtmlc.configure(state=DISABLED)
                    self.txtmlc.set("0")

            def chkAna():
                if(var38.get() ==1):
                    self.txtana.configure(state=NORMAL)
                    self.txtana.focus()
                    self.txtana.delete('0',END)
                    e_ana.set("")
                elif var38.get() ==0:
                    self.txtana.configure(state=DISABLED)
                    self.txtana.set("0")
            def chkAss():
                if(var39.get() ==1):
                    self.txtass.configure(state=NORMAL)
                    self.txtass.focus()
                    self.txtass.delete('0',END)
                    e_ass.set("")
                elif var39.get() ==0:
                    self.txtass.configure(state=DISABLED)
                    self.txtass.set("0")

            def chkCnc():
                if(var40.get() ==1):
                    self.txtcnc.configure(state=NORMAL)
                    self.txtcnc.focus()
                    self.txtcnc.delete('0',END)
                    e_cnc.set("")
                elif var40.get() ==0:
                    self.txtcnc.configure(state=DISABLED)
                    self.txtcnc.set("0")
            def chkCvp():
                if(var41.get() ==1):
                    self.txtcvp.configure(state=NORMAL)
                    self.txtcvp.focus()
                    self.txtcvp.delete('0',END)
                    e_cvp.set("")
                elif var41.get() ==0:
                    self.txtcvp.configure(state=DISABLED)
                    self.txtcvp.set("0")

            def chkDay():
                if(var42.get() ==1):
                    self.txtday.configure(state=NORMAL)
                    self.txtday.focus()
                    self.txtday.delete('0',END)
                    e_day.set("")
                elif var42.get() ==0:
                    self.txtday.configure(state=DISABLED)
                    self.txtday.set("0")
            def chkDte():
                if(var43.get() ==1):
                    self.txtdte.configure(state=NORMAL)
                    self.txtdte.focus()
                    self.txtdte.delete('0',END)
                    e_dte.set("")
                elif var43.get() ==0:
                    self.txtdte.configure(state=DISABLED)
                    self.txtdte.set("0")

            def chkDre():
                    if(var44.get() ==1):
                       self.txtdre.configure(state=NORMAL)
                       self.txtdre.focus()
                       self.txtdre.delete('0',END)
                       e_dre.set("")
                    elif var44.get() ==0:
                       self.txtdre.configure(state=DISABLED)
                       self.txtdre.set("0")
            def chkPoi():
                if(var45.get() ==1):
                    self.txtpoi.configure(state=NORMAL)
                    self.txtpoi.focus()
                    self.txtpoi.delete('0',END)
                    e_poi.set("")
                elif var45.get() ==0:
                    self.txtpoi.configure(state=DISABLED)
                    self.txtpoi.set("0")

            def chkHgt():
                if(var46.get() ==1):
                    self.txthgt.configure(state=NORMAL)
                    self.txthgt.focus()
                    self.txthgt.delete('0',END)
                    e_hgt.set("")
                elif var46.get() ==0:
                    self.txthgt.configure(state=DISABLED)
                    self.txthgt.set("0")
            def chkPoi():
                if(var45.get() ==1):
                    self.txtpoi.configure(state=NORMAL)
                    self.txtpoi.focus()
                    self.txtpoi.delete('0',END)
                    e_poi.set("")
                elif var45.get() ==0:
                    self.txtpoi.configure(state=DISABLED)
                    self.txtpoi.set("0")

            def chkHgt():
                if(var46.get() ==1):
                    self.txthgt.configure(state=NORMAL)
                    self.txthgt.focus()
                    self.txthgt.delete('0',END)
                    e_hgt.set("")
                elif var46.get() ==0:
                    self.txthgt.configure(state=DISABLED)
                    self.txthgt.set("0")
            def chkHmc():
                if(var47.get() ==1):
                    self.txthmc.configure(state=NORMAL)
                    self.txthmc.focus()
                    self.txthmc.delete('0',END)
                    e_hmc.set("")
                elif var47.get() ==0:
                    self.txthmc.configure(state=DISABLED)
                    self.txthmc.set("0")

            def chkIemc():
                if(var48.get() ==1):
                    self.txtiemc.configure(state=NORMAL)
                    self.txtiemc.focus()
                    self.txtiemc.delete('0',END)
                    e_iemc.set("")
                elif var48.get() ==0:
                    self.txtiemc.configure(state=DISABLED)
                    self.txtiemc.set("0")
            def chkIrc():
                if(var49.get() ==1):
                    self.txtirc.configure(state=NORMAL)
                    self.txtirc.focus()
                    self.txtirc.delete('0',END)
                    e_irc.set("")
                elif var49.get() ==0:
                    self.txtirc.configure(state=DISABLED)
                    self.txtirc.set("0")

            def chkIpc():
                if(var50.get() ==1):
                    self.txtipc.configure(state=NORMAL)
                    self.txtipc.focus()
                    self.txtipc.delete('0',END)
                    e_ipc.set("")
                elif var50.get() ==0:
                    self.txtipc.configure(state=DISABLED)
                    self.txtipc.set("0")
            def chkIc():
                if(var51.get() ==1):
                    self.txtic.configure(state=NORMAL)
                    self.txtic.focus()
                    self.txtic.delete('0',END)
                    e_ic.set("")
                elif var51.get() ==0:
                    self.txtic.configure(state=DISABLED)
                    self.txtic.set("0")

            def chkIv():
                if(var52.get() ==1):
                    self.txtiv.configure(state=NORMAL)
                    self.txtiv.focus()
                    self.txtiv.delete('0',END)
                    e_iv.set("")
                elif var52.get() ==0:
                    self.txtiv.configure(state=DISABLED)
                    self.txtiv.set("0")
            def chkNc():
                if(var53.get() ==1):
                    self.txtnc.configure(state=NORMAL)
                    self.txtnc.focus()
                    self.txtnc.delete('0',END)
                    e_nc.set("")
                elif var53.get() ==0:
                    self.txtnc.configure(state=DISABLED)
                    self.txtnc.set("0")

            def chkPl():
                if(var54.get() ==1):
                    self.txtpl.configure(state=NORMAL)
                    self.txtpl.focus()
                    self.txtpl.delete('0',END)
                    e_pl.set("")
                elif var54.get() ==0:
                    self.txtpl.configure(state=DISABLED)
                    self.txtpl.set("0")
            def chkPrc():
                if(var55.get() ==1):
                    self.txtprc.configure(state=NORMAL)
                    self.txtprc.focus()
                    self.txtprc.delete('0',END)
                    e_prc.set("")
                elif var55.get() ==0:
                    self.txtprc.configure(state=DISABLED)
                    self.txtprc.set("0")

            def chkG():
                if(var56.get() ==1):
                    self.txtg.configure(state=NORMAL)
                    self.txtg.focus()
                    self.txtg.delete('0',END)
                    e_g.set("")
                elif var56.get() ==0:
                    self.txtg.configure(state=DISABLED)
                    self.txtg.set("0")
                    self.txtg.set("0")
            def chkSs():
                if(var57.get() ==1):
                    self.txtss.configure(state=NORMAL)
                    self.txtss.focus()
                    self.txtss.delete('0',END)
                    e_ss.set("")
                elif var57.get() ==0:
                    self.txtss.configure(state=DISABLED)
                    self.txtss.set("0")

            def chkAc():
                if(var58.get() ==1):
                    self.txtac.configure(state=NORMAL)
                    self.txtac.focus()
                    self.txtac.delete('0',END)
                    e_ac.set("")
                elif var58.get() ==0:
                    self.txtac.configure(state=DISABLED)
                    self.txtac.set("0")


            def chkG2():
                if(var59.get() ==1):
                    self.txtg2.configure(state=NORMAL)
                    self.txtg2.focus()
                    self.txtg2.delete('0',END)
                    e_g2.set("")
                elif var59.get() ==0:
                    self.txtg2.configure(state=DISABLED)
                    self.txtg2.set("0")

            def chkSs2():
                if(var60.get() ==1):
                    self.txtss2.configure(state=NORMAL)
                    self.txtss2.focus()
                    self.txtss2.delete('0',END)
                    e_ss2.set("")
                elif var60.get() ==0:
                    self.txtss2.configure(state=DISABLED)
                    self.txtss2.set("0")

            def chkAc2():
                if(var61.get() ==1):
                    self.txtac2.configure(state=NORMAL)
                    self.txtac2.focus()
                    self.txtac2.delete('0',END)
                    e_ac2.set("")
                elif var61.get() ==0:
                    self.txtac2.configure(state=DISABLED)
                    self.txtac2.set("0")

            def chkG3():
                if(var62.get() ==1):
                    self.txtg3.configure(state=NORMAL)
                    self.txtg3.focus()
                    self.txtg3.delete('0',END)
                    e_g3.set("")
                elif var62.get() ==0:
                    self.txtg3.configure(state=DISABLED)
                    self.txtg3.set("0")
                    self.txtg3.set("0")
            def chkSs3():
                if(var63.get() ==1):
                    self.txtss3.configure(state=NORMAL)
                    self.txtss3.focus()
                    self.txtss3.delete('0',END)
                    e_ss3.set("")
                elif var63.get() ==0:
                    self.txtss3.configure(state=DISABLED)
                    self.txtss3.set("0")

            def chkAc3():
                if(var64.get() ==1):
                    self.txtac3.configure(state=NORMAL)
                    self.txtac3.focus()
                    self.txtac3.delete('0',END)
                    e_ac3.set("")
                elif var64.get() ==0:
                    self.txtac3.configure(state=DISABLED)
                    self.txtac3.set("0")
                    self.txtac3.set("0")
            def chkG4():
                if(var65.get() ==1):
                    self.txtg4.configure(state=NORMAL)
                    self.txtg4.focus()
                    self.txtg4.delete('0',END)
                    e_g4.set("")
                elif var65.get() ==0:
                    self.txtg4.configure(state=DISABLED)
                    self.txtg4.set("0")

            def chkSs4():
                if(var85.get() ==1):
                    self.txtss4.configure(state=NORMAL)
                    self.txtss4.focus()
                    self.txtss4.delete('0',END)
                    e_ss4.set("")
                elif var85.get() ==0:
                    self.txtss4.configure(state=DISABLED)
                    self.txtss4.set("0")

            def chkAc4():
                if(var66.get() ==1):
                    self.txtac4.configure(state=NORMAL)
                    self.txtac4.focus()
                    self.txtac4.delete('0',END)
                    e_ac4.set("")
                elif var66.get() ==0:
                    self.txtac4.configure(state=DISABLED)
                    self.txtac4.set("0")

            def chkG5a():
                if(var67.get() ==1):
                    self.txtg5a.configure(state=NORMAL)
                    self.txtg5a.focus()
                    self.txtg5a.delete('0',END)
                    e_g5a.set("")
                elif var67.get() ==0:
                    self.txtg5a.configure(state=DISABLED)
                    self.txtg5a.set("0")
                    self.txtg5a.set("0")
            def chkSs5a():
                if(var68.get() ==1):
                    self.txtss5a.configure(state=NORMAL)
                    self.txtss5a.focus()
                    self.txtss5a.delete('0',END)
                    e_ss5a.set("")
                elif var68.get() ==0:
                    self.txtss5a.configure(state=DISABLED)
                    self.txtss5a.set("0")

            def chkAc5a():
                if(var69.get() ==1):
                    self.txtac5a.configure(state=NORMAL)
                    self.txtac5a.focus()
                    self.txtac5a.delete('0',END)
                    e_ac5a.set("")
                elif var69.get() ==0:
                    self.txtac5a.configure(state=DISABLED)
                    self.txtac5a.set("0")
                    self.txtac5a.set("0")
            def chkG5b():
                if(var70.get() ==1):
                    self.txtg5b.configure(state=NORMAL)
                    self.txtg5b.focus()
                    self.txtg5b.delete('0',END)
                    e_g5b.set("")
                elif var70.get() ==0:
                    self.txtg5b.configure(state=DISABLED)
                    self.txtg5b.set("0")

            def chkSs5b():
                if(var71.get() ==1):
                    self.txtss5b.configure(state=NORMAL)
                    self.txtss5b.focus()
                    self.txtss5b.delete('0',END)
                    e_ss5b.set("")
                elif var71.get() ==0:
                    self.txtss5b.configure(state=DISABLED)
                    self.txtss5b.set("0")
                    self.txtss5b.set("0")
            def chkAc5b():
                if(var72.get() ==1):
                    self.txtac5b.configure(state=NORMAL)
                    self.txtac5b.focus()
                    self.txtac5b.delete('0',END)
                    e_ac5b.set("")
                elif var72.get() ==0:
                    self.txtac5b.configure(state=DISABLED)
                    self.txtac5b.set("0")

            def chkG6():
                if(var73.get() ==1):
                    self.txtg6.configure(state=NORMAL)
                    self.txtg6.focus()
                    self.txtg6.delete('0',END)
                    e_g6.set("")
                elif var73.get() ==0:
                    self.txtg6.configure(state=DISABLED)
                    self.txtg6.set("0")
                    self.txtg6.set("0")
            def chkSs6():
                if(var74.get() ==1):
                    self.txtss6.configure(state=NORMAL)
                    self.txtss6.focus()
                    self.txtss6.delete('0',END)
                    e_ss6.set("")
                elif var74.get() ==0:
                    self.txtss6.configure(state=DISABLED)
                    self.txtss6.set("0")

            def chkAc6():
                if(var75.get() ==1):
                    self.txtac6.configure(state=NORMAL)
                    self.txtac6.focus()
                    self.txtac6.delete('0',END)
                    e_ac6.set("")
                elif var75.get() ==0:
                    self.txtac6.configure(state=DISABLED)
                    self.txtac6.set("0")
                    self.txtac6.set("0")
            def chkG7a():
                if(var76.get() ==1):
                    self.txtg7a.configure(state=NORMAL)
                    self.txtg7a.focus()
                    self.txtg7a.delete('0',END)
                    e_g7a.set("")
                elif var76.get() ==0:
                    self.txtg7a.configure(state=DISABLED)
                    self.txtg7a.set("0")

            def chkSs7a():
                if(var77.get() ==1):
                    self.txtss7a.configure(state=NORMAL)
                    self.txtss7a.focus()
                    self.txtss7a.delete('0',END)
                    e_ss7a.set("")
                elif var77.get() ==0:
                    self.txtss7a.configure(state=DISABLED)
                    self.txtss7a.set("0")
                    self.txtss7a.set("0")
            def chkAc7a():
                if(var78.get() ==1):
                    self.txtac7a.configure(state=NORMAL)
                    self.txtac7a.focus()
                    self.txtac7a.delete('0',END)
                    e_ac7a.set("")
                elif var78.get() ==0:
                    self.txtac7a.configure(state=DISABLED)
                    self.txtac7a.set("0")

            def chkG7b():
                if(var79.get() ==1):
                    self.txtg7b.configure(state=NORMAL)
                    self.txtg7b.focus()
                    self.txtg7b.delete('0',END)
                    e_g7b.set("")
                elif var79.get() ==0:
                    self.txtg7b.configure(state=DISABLED)
                    self.txtg7b.set("0")
                    self.txtg7b.set("0")
            def chkSs7b():
                if(var80.get() ==1):
                    self.txtss7b.configure(state=NORMAL)
                    self.txtss7b.focus()
                    self.txtss7b.delete('0',END)
                    e_ss7b.set("")
                elif var80.get() ==0:
                    self.txtss7b.configure(state=DISABLED)
                    self.txtss7b.set("0")

            def chkG8():
                if(var86.get() ==1):
                    self.txtg8.configure(state=NORMAL)
                    self.txtg8.focus()
                    self.txtg8.delete('0',END)
                    e_g8.set("")
                elif var86.get() ==0:
                    self.txtg8.configure(state=DISABLED)
                    self.txtg8.set("0")
                    self.txtg8.set("0")
            def chkSs8():
                if(var87.get() ==1):
                    self.txtss8.configure(state=NORMAL)
                    self.txtss8.focus()
                    self.txtss8.delete('0',END)
                    e_ss8.set("")
                elif var87.get() ==0:
                    self.txtss8.configure(state=DISABLED)
                    self.txtss8.set("0")

            def chkAc8():
                if(var88.get() ==1):
                    self.txtac8.configure(state=NORMAL)
                    self.txtac8.focus()
                    self.txtac8.delete('0',END)
                    e_g8.set("")
                elif var88.get() ==0:
                    self.txtac8.configure(state=DISABLED)
                    self.txtac8.set("0")

            def chkG9():
                if(var82.get() ==1):
                    self.txtg9.configure(state=NORMAL)
                    self.txtg9.focus()
                    self.txtg9.delete('0',END)
                    e_g9.set("")
                elif var82.get() ==0:
                    self.txtg9.configure(state=DISABLED)
                    self.txtg9.set("0")

            def chkSs9():
                if(var83.get() ==1):
                    self.txtss9.configure(state=NORMAL)
                    self.txtss9.focus()
                    self.txtss9.delete('0',END)
                    e_ss9.set("")
                elif var83.get() ==0:
                    self.txtss9.configure(state=DISABLED)
                    self.txtss9.set("0")
                    self.txtss9.set("0")
            def chkAc9():
                if(var84.get() ==1):
                    self.txtac9.configure(state=NORMAL)
                    self.txtac9.focus()
                    self.txtac9.delete('0',END)
                    e_ac9.set("")
                elif var84.get() ==0:
                    self.txtac9.configure(state=DISABLED)
                    self.txtac9.set("0")
            def chkAc7b():
                if(var81.get() ==1):
                   self.txtac7b.configure(state=NORMAL)
                   self.txtac7b.focus()
                   self.txtac7b.delete('0',END)
                   e_ac7b.set("")
                elif var81.get() ==0:
                   self.txtac7b.configure(state=DISABLED)
                   self.txtac7b.set("0")




            #=============================================================================================================================#
            self.txtReceipt = Text(abc5, height=19, width=48, bd=10, font=('arial',9,'bold'))
            self.txtReceipt.grid(row=0,column=0)
            #=============================================================================================================================#
            self.btnTotal = Button(abc6,padx=14,pady=7,bd=5,fg="black",font=('arial',12,'bold'), width=5, height=2,
                                   bg="powder blue", text="Total",command=costOfItem).grid(row=0,column=0)
            self.btnReset = Button(abc6,padx=14,pady=7,bd=5,fg="black",font=('arial',12,'bold'), width=5, height=2,
                                   bg="powder blue", text="Reset",command=Reset).grid(row=0,column=1)
            self.btnExit = Button(abc6,padx=14,pady=7,bd=5,fg="black",font=('arial',12,'bold'), width=5, height=2,
                                   bg="powder blue", text="Exit",command=iExit).grid(row=0,column=2)
            self.btnPrint = Button(abc6,padx=14,pady=7,bd=5,fg="black",font=('arial',12,'bold'), width=5, height=2,
                                   bg="powder blue", text="Print",command=iprint).grid(row=0,column=3)



if __name__ =='__main__':
            window = Tk()
            application = customer(window)
            window.mainloop()
