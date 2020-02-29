from functools import partial
from math import *
from tkinter import *
from tkinter import messagebox

import pymysql

kap=pymysql.connect(host="127.0.0.1",user="root",password="pass",db="tsovagyux")
c=kap.cursor()
patuhanx=Tk()
patuhanx.withdraw()
s=[]
patuhank=Tk()
patuhank.withdraw()

    
patuhanga=Tk()
patuhanga.withdraw()
###########grancvelu patuhan####
patuhangr=Tk()
patuhangr.withdraw()

patuhangr1=Tk()
patuhangr1.withdraw()

def mtnel():
    patuhanga.geometry("500x500")
    patuhanga.wm_title("Mutq")
    patuhanga.deiconify()
    
mutqh=messagebox.askyesno("Anhrajesht e gaxtnabar","Grel Gaxtnabar@ kam Grancvel ")
if mutqh==True :
    mtnel()
    
else:
    print("h")

def grancvell():
    log=elogin1.get()
    par=eparol1.get()
    if log=="admin" and par=="1234":
        grancvel1()

    else:
        messagebox.showerror("sms","harcum@ sxale e")
    

def grancvel1():
    patuhangr1.geometry("500x500")
    patuhangr1.wm_title("Grancvel")
    patuhangr1.deiconify()
    

def grancvel ():
    patuhangr.geometry("600x600")
    patuhangr.wm_title("Harcum")
    patuhangr.deiconify()

    

def arevtur ():
    patuhank.geometry("800x700")
    patuhank.wm_title("Arevtur")
    patuhank.deiconify()
    #amutq=Button(patuhank,text="Hastatel",command=partial(hashvark,acod), bg="red",fg="cyan",font="100")
    #amutq.place(x=650,y=10)
    

def hashvark():
    cod= ecod.get()
    gin="select * from pahest where  cod ='"+cod+"'"
    c.execute(gin)
    kap.commit()

    
    for i in c:
        print(i[2])
    lcod1=Label(patuhank,text="  Grel    "+i[1]+"_i   qanak@  " ,bg="blue",fg="cyan",font="100" )
    lcod1.place (x=10,y=50)
    ecod1=Entry(patuhank,textvariable=qash,bg="blue",fg="cyan",font="100")
    ecod1.place(x=350,y=50)
    amutq1=Button(patuhank,text="Mutq",command=partial(tpel,ecod1,i[2],i), bg="red",fg="cyan",font="100")
    amutq1.place(x=650,y=50)

#######shauyti pahesti mas##########
def shauyt1(i,x,z):
    ianun=i[1]
    iqanak=x.get()
    ivacharq=z
    igin=i[2]
    iinqnarjeq=i[3]
    ish1=igin-iinqnarjeq
    ish2=int(iqanak)*int(ish1)
    ishauyt=ish2
    imutq="insert into shahuyt (anun,qanak,vacharq,shahuyt,amsativ)values('"+ianun+"','"+iqanak+"','"+str(ivacharq)+"','"+str(ishauyt)+"',NOW())"
    c.execute(imutq)
    kap.commit()
    #print(imutq)
    #print(type(ianun),type(iqanak),type(ivacharq),type(igin),type(iinqnarjeq),type(ishauyt))
    
    
    

def tpel(x,y,i):
    q=x.get()
    z=int(q)*int(y)
    print(q,y)
    lhashvark=Label(patuhank,text=(z ,"dram" ),bg="blue",fg="cyan",font="100" )
    lhashvark.place (x=350,y=110)
    lhashvark1=Label(patuhank,text="    @ndanur hashiv@ " ,bg="blue",fg="cyan",font="100" )
    lhashvark1.place (x=10,y=110)
    shauyt1(i,x,z)
    
def cuyc ():
    #c=ptichka5.get()
    x=radio.get()
    print(x)
    
def cucakner ():
    global ptichka4
    global ptichka5
    
    patuhanp.geometry("900x900")
    patuhanp.wm_title("Pahest")
    patuhanp.deiconify()
    pahest="select * from pahest"
    c.execute(pahest)
    kap.commit()
    for i in c:
       lid1=Label(patuhanp,text="| id |" ,bg="blue",fg="cyan",font="100" )
       lid1.place (x=10,y=0)
       
       lid=Label(patuhanp,text=i[0] ,bg="blue",fg="cyan",font="100" )
       lid.place (x=20,y=10*3*i[0])
       xmbagrel=Button(patuhanp,text="Uxel",command=partial(mutqx,i[0]),bg="blue",fg="cyan",font="100")
       xmbagrel.place(x=790,y=10*3*i[0])
       #ptichka4=Radiobutton(patuhanp,text="Voch",variable=radio, command=cuyc , value=i[0],height=2,width=10)
       #ptichka4.place(x=750,y=10*3*i[0])
       #ptichka5=Radiobutton(patuhanp,text="Ayo",variable=radio,command=cuyc,value="i[0]",height=2,width=10)
       #ptichka5.place(x=830,y=10*3*i[0])
       lanun1=Label(patuhanp,text="|   Anun   |" ,bg="blue",fg="cyan",font="100" )
       lanun1.place (x=60,y=0)
       lanun=Label(patuhanp,text=i[1] ,bg="blue",fg="cyan",font="100" )
       lanun.place (x=75,y=10*3*i[0])
       lgin1=Label(patuhanp,text="| Vacharvox Gin |" ,bg="blue",fg="cyan",font="100" )
       lgin1.place (x=160,y=0)
       lgin=Label(patuhanp,text=i[2] ,bg="blue",fg="cyan",font="100" )
       lgin.place (x=200,y=10*3*i[0])
       la=Label(patuhanp,text="| Inqnarjeq |" ,bg="blue",fg="cyan",font="100" )
       la.place (x=320,y=0)
       linqnarjeq=Label(patuhanp,text=i[3] ,bg="blue",fg="cyan",font="100" )
       linqnarjeq.place (x=350,y=10*3*i[0])
       lqanak=Label(patuhanp,text="| Apranqi qanak |",bg="blue",fg="cyan",font="100" )
       lqanak.place (x=435,y=0)
       lqanak1=Label(patuhanp,text=i[4],bg="blue",fg="cyan",font="100" )
       lqanak1.place (x=490,y=10*3*i[0])
       lqanak=Label(patuhanp,text="| Apranqi cod@ |",bg="blue",fg="cyan",font="100" )
       lqanak.place (x=595,y=0)
       lqanak1=Label(patuhanp,text=i[5],bg="blue",fg="cyan",font="100" )
       lqanak1.place (x=650,y=10*3*i[0])

def uxel (x):
    nanun=xanun.get()
    ngin=xanun1.get()
    ninq=xanun2.get()
    nqanak=xanun3.get()
    ncod=xanun4.get()
    aanun= "update pahest set anun='"+nanun+"',gin='"+ngin+"',inqnarjeq='"+ninq+"',qanak='"+nqanak+"',cod='"+ncod+"'where id='"+str(x)+"'"
    c.execute(aanun)
    kap.commit()
    y=messagebox.askyesno("Harcum","Cucadrel pahest@")
    if y:

        cucakner()
    else :
        print("h")
    
def mutqx(x):
    arjeq="select * from pahest where id='"+str(x)+"'"
    c.execute(arjeq)
    kap.commit()
    for i in c:
        xanun.set(i[1])
        xanun1.set(i[2])
        xanun2.set(i[3])
        xanun3.set(i[4])
        xanun4.set(i[5])
    
    patuhanx.geometry("900x900")
    patuhanx.wm_title("xmbagrel")
    patuhanx.deiconify()
    bmutq=Button(patuhanx,text="mutq",command=partial(uxel,x),bg="red",fg="cyan",font="100")
    bmutq.place(x=700,y=350)

def mutq():
    
    patuhanx.geometry("900x900")
    patuhanx.wm_title("xmbagrel")
    patuhanx.deiconify()
    bmutq=Button(patuhanx,text="mutq",command=partial(xmbagrel),bg="red",fg="cyan",font="100")
    bmutq.place(x=700,y=350)
    
       
       
def xmbagrel ():
    
    
       
    anun1=xanun.get()
    anun2=xanun1.get()
    anun3=xanun2.get()
    anun4=xanun3.get()
    anun5=xanun4.get()
    aanun="insert into pahest (anun,gin,inqnarjeq,qanak,cod) values ('"+anun1+"','"+anun2+"','"+anun3+"','"+anun4+"','"+anun5+"')"
    c.execute(aanun)
    kap.commit()

    
def kardal ():
    arjeq="select * from pahest"
    c.execute(arjeq)
    kap.commit()
    for i in c:
        xanun.set(i[1])
        xanun1.set(i[2])
        xanun2.set(i[3])
        xanun3.set(i[4])
        xanun4.set("1050")
        print(xanun.get(),xanun1.get(),xanun2.get(),xanun3.get())


############shauyti pahest###########
patuhansh=Tk()
patuhansh.withdraw()        
def shahuyt ():
    patuhansh.geometry("1200x900")
    patuhansh.wm_title("Shahuyt")
    patuhansh.deiconify()
    pahest1="select * from shahuyt"
    c.execute(pahest1)
    kap.commit()
    profit=0
    for i in c:
       profit=profit+i[4] 
       lid11=Label(patuhansh,text="| id |" ,bg="blue",fg="cyan",font="100" )
       lid11.place (x=10,y=0)
       
       lid1=Label(patuhansh,text=i[0] ,bg="blue",fg="cyan",font="100" )
       lid1.place (x=20,y=10*3*i[0])
       lanun1=Label(patuhansh,text="|   Anun   |" ,bg="blue",fg="cyan",font="100" )
       lanun1.place (x=60,y=0)
       lanun=Label(patuhansh,text=i[1] ,bg="blue",fg="cyan",font="100" )
       lanun.place (x=60,y=10*3*i[0])
       lgin1=Label(patuhansh,text="|Gnvac Apranqi Qanak|" ,bg="blue",fg="cyan",font="100" )
       lgin1.place (x=160,y=0)
       lgin=Label(patuhansh,text=i[2] ,bg="blue",fg="cyan",font="100" )
       lgin.place (x=160,y=10*3*i[0])
       la=Label(patuhansh,text="|@ndanur Vacharq@|" ,bg="blue",fg="cyan",font="100" )
       la.place (x=374,y=0)
       linqnarjeq=Label(patuhansh,text=i[3] ,bg="blue",fg="cyan",font="100" )
       linqnarjeq.place (x=374,y=10*3*i[0])
       lqanak=Label(patuhansh,text="| Shahuyt |",bg="blue",fg="cyan",font="100" )
       lqanak.place (x=573,y=0)
       lqanak1=Label(patuhansh,text=i[4],bg="blue",fg="cyan",font="100" )
       lqanak1.place (x=573,y=10*3*i[0])
       lqanak=Label(patuhansh,text="|Apranqi Vacharqi Jam,Amsativ|",bg="blue",fg="cyan",font="100" )
       lqanak.place (x=676,y=0)
       lqanak1=Label(patuhansh,text=i[5],bg="blue",fg="cyan",font="100" )
       lqanak1.place (x=720,y=10*3*i[0])
       lqanak=Label(patuhansh,text="|   @ndanur Shauyt   |",bg="blue",fg="cyan",font="100" )
       lqanak.place (x=965,y=0)
       lqanak1=Label(patuhansh,text=profit,bg="blue",fg="cyan",font="100" )
       lqanak1.place (x=965,y=10*3*i[0])
       global s
       x=int(i[0])
       s.append(i[4])
    print(s)

        
ianun=StringVar()
iqanak=StringVar()
ivacharq=StringVar()
igin=StringVar()
iinqnarjeq=StringVar()
ishauyt1=StringVar()
############menu############

patuhan=Tk()
patuhan.geometry("900x900")
patuhan.wm_title("menu")
menubar=Menu(patuhan)
file=Menu(menubar)

file.add_command(label="Xmbagrel",command=mutq)
file.add_command(label="Sksel arevtur@",command=arevtur)
file.add_command(label="Tesnel pahest@",command=cucakner)
file.add_command(label="Tesnel orva arevtur@",command=shahuyt)

file.add_command(label="Grancvel",command=kardal)
file.add_separator()
file.add_command(label="Exit",command=patuhan.quit())
menubar.add_cascade(label="file",menu=file)
patuhan.config(menu=menubar)
#######################xmbagrelu patuhan###########
qash=StringVar()
radio=StringVar()
#radio1=StringVar()
xanun=StringVar()
xanun1=StringVar()
xanun2=StringVar()
xanun3=StringVar()
xanun4=StringVar()
lanun=Label(patuhanx,text=".         Apranqi anun          .",bg="blue",fg="cyan",font="100")
lanun.place(x=10,y=10)
lanun1=Label(patuhanx,text=".         Apranqi vacharvox gin@           .",bg="blue",fg="cyan",font="100")
lanun1.place(x=10,y=60)
lanun2=Label(patuhanx,text=".         Apranqi inqnarjek@         .",bg="blue",fg="cyan",font="100")
lanun2.place(x=10,y=110)
lanun3=Label(patuhanx,text=".         Apranqi qanak@          .",bg="blue",fg="cyan",font="100")
lanun3.place(x=10,y=160)
lanun4=Label(patuhanx,text=".         Apranqi cod@          .",bg="blue",fg="cyan",font="100")
lanun4.place(x=10,y=210)

eanun=Entry(patuhanx ,textvariable=xanun, bg="blue",fg="cyan",font="100")
eanun.place (x=450 ,y=10)
eanun1=Entry(patuhanx ,textvariable=xanun1 ,bg="blue",fg="cyan",font="100")
eanun1.place (x=450 ,y=60)
eanun2=Entry (patuhanx,textvariable=xanun2,bg="blue",fg="cyan",font="100")
eanun2.place(x=450,y=110)
eanun3=Entry (patuhanx,textvariable=xanun3 ,bg="blue",fg="cyan",font="100")
eanun3.place (x=450,y=160)
eanun4=Entry (patuhanx,textvariable=xanun4 ,bg="blue",fg="cyan",font="100")
eanun4.place (x=450,y=210)


#patuhan.mainloop()


##############arevtri patuhan################
#acod=StringVar()
xacode = StringVar()
lcod=Label(patuhank,text="     grel apranqi cod@    " ,bg="blue",fg="cyan",font="100" )
lcod.place (x=10,y=10)
ecod=Entry(patuhank,textvariable=xacode,bg="blue",fg="cyan",font="120")
ecod.place(x=350,y=10)

      #Button(patuhanx,text="mutq",command=partial(xmbagrel),bg="red",fg="cyan",font="100")

amutq=Button(patuhank,text="Hastatel",command=hashvark, bg="red",fg="cyan",font="100")
amutq.place(x=650,y=10)
###########grancvelu patuhan###########
login=StringVar
parol=StringVar
login=Label(patuhanga,text="Login" ,bg="blue",fg="cyan",font="100" )
login.place (x=10,y=10)
parol=Label(patuhanga,text="Passvord" ,bg="blue",fg="cyan",font="100" )
parol.place (x=10,y=50)
elogin=Entry(patuhanga,textvariable=login,bg="blue",fg="cyan",font="120")
elogin.place(x=110,y=10)
eparol=Entry(patuhanga,textvariable=parol,bg="blue",fg="cyan",font="120")
eparol.place(x=110,y=50)
mtnel2=Button(patuhanga,text="mutq",command=partial(xmbagrel),bg="red",fg="cyan",font="100")
mtnel2.place(x=350,y=40)
grancvel12=Button(patuhanga,text="Grancvel",command=partial(grancvel),bg="blue",fg="cyan",font="100")
grancvel12.place(x=350,y=100)
#############grancvelu parol###########
login11=StringVar()
parol11=StringVar()
login1=Label(patuhangr,text="Login" ,bg="blue",fg="cyan",font="100" )
login1.place (x=10,y=10)
parol1=Label(patuhangr,text="Passvord" ,bg="blue",fg="cyan",font="100" )
parol1.place (x=10,y=50)
mtnel21=Button(patuhangr,text="mutq",command=partial(grancvell),bg="red",fg="cyan",font="100")
mtnel21.place(x=350,y=40)
elogin1=Entry(patuhangr,textvariable=login11,bg="blue",fg="cyan",font="120")
elogin1.place(x=110,y=10)
eparol1=Entry(patuhangr,textvariable=parol11,bg="blue",fg="cyan",font="120")
eparol1.place(x=110,y=50)

patuhanp=Tk()
patuhanp.withdraw()

patuhan.mainloop()

#patuhanx.mainloop()
#patuhank.mainloop()
