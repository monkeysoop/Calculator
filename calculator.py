from tkinter import *
from matplotlib import pyplot as plt
import math
import random
import time

a=[]

#Main logic

def parantheses(f):
    count=0
    while ("(" in f or ")" in f) and count<100:
        for i in range(len(f)):
            if f[i]==")":
                x=[]
                for k in range(i-1,0,-1):
                    if f[k]=="(":
                        break
                    x.append(f[k])
                    f.pop(k)
                x.reverse()
                x=absolute(x)
                x=mod(x)
                x=logarithm(x)
                x=factorial(x)
                x=sincos(x)
                x=power(x)
                x=multiply(x)
                x=add(x)
                x=x[0]
                for i in range(len(f)):
                    if f[i]==")":
                        f[i]=x
                        for k in range(i,-1,-1):
                            if f[k]=="(":
                                f.pop(k)
                                break
                        break
                break
        count+=1
    return f
def absolute(f):
    count=0
    while "[" in f and count<100:
        for i in range(len(f)):
            if f[i]=="[":
                x=[]
                for k in range(i+1,len(f)):
                    if f[k]=="]":
                        break
                    x.append(f[k])
                l=len(x)
                x=mod(x)
                x=logarithm(x)
                x=factorial(x)
                x=sincos(x)
                x=power(x)
                x=multiply(x)
                x=add(x)
                x=x[0]
                x=abs(float(x))
                del f[i:i+l+2]
                f.insert(i,str(x))
                break
        count+=1
    return f
def mod(f):
    count=0
    while "mod" in f and count<100:
        for i in range(len(f)):
            if f[i]=="mod":
                f[i+2]=str((float(f[i+1])%float(f[i+2])))
                f.pop(i)
                f.pop(i)
                break
        count+=1
    return f
def logarithm(f):
    count=0
    while ("log" in f) and count<100:
        for i in range(len(f)):
            if f[i]=="log":
                f[i+2]=str(math.log(float(f[i+2]),float(f[i+1])))
                f.pop(i)
                f.pop(i)
                break
        count+=1
    return f
def factorial(f):
    count=0
    while ("!" in f) and count<100:
        for i in range(len(f)):
            if f[i]=="!":
                f[i-1]=str(math.factorial(float(f[i-1])))
                f.pop(i)
                break
        count+=1
    return f
def sincos(f):
    count=0
    while ("sin" in f or "cos" in f or "tan" in f or "ctn" in f or "asin" in f or "acos" in f or "atan" in f or "actn" in f) and count<100:
        for i in range(len(f)-1):
            if f[i]=="sin":
                f[i+1]=str(math.sin(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="cos":
                f[i+1]=str(math.cos(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="tan":
                f[i+1]=str(math.tan(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="ctn":
                f[i+1]=str(1/math.tan(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="asin":
                f[i+1]=str(math.asin(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="acos":
                f[i+1]=str(math.acos(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="atan":
                f[i+1]=str(math.atan(float(f[i+1])))
                f.pop(i)
                break
            elif f[i]=="actn":
                f[i+1]=str(math.actn(1/float(f[i+1])))
                f.pop(i)
                break
        count+=1
    return f
def power(f):
    count=0
    while ("**" in f or "√" in f) and count<100:
        for i in range(len(f)-1):
            if f[i]=="**":
                f[i+1]=str(float(f[i-1])**float(f[i+1]))
                f.pop(i)
                f.pop(i-1)
                break
            elif f[i]=="√":
                f[i+1]=str(float(f[i+1])**(1/float(f[i-1])))
                f.pop(i)
                f.pop(i-1)
                break
        count+=1
    return f
def multiply(f):
    count=0
    while ("*" in f or "/" in f) and count<100:
        for i in range(len(f)-1):
            if f[i]=="*":
                f[i+1]=str(float(f[i-1])*float(f[i+1]))
                f.pop(i)
                f.pop(i-1)
                break
            elif f[i]=="/":
                f[i+1]=str(float(f[i-1])/float(f[i+1]))
                f.pop(i)
                f.pop(i-1)
                break
        count+=1
    return f
def add(f):
    count=0
    while ("+" in f or "-" in f) and count<100:
        for i in range(len(f)-1):
            if f[i]=="+"and f[i+1]!="-" and f[i+1]!="+":
                f[i+1]=str(float(f[i-1])+float(f[i+1]))
                f.pop(i)
                f.pop(i-1)
                break
            elif f[i]=="-" and f[i+1]!="-" and f[i+1]!="+":
                f[i+1]=str(float(f[i-1])-float(f[i+1]))
                f.pop(i)
                f.pop(i-1)
                break
        count+=1
    return f

#Run

def run(a):
    #"""
    a=parantheses(a) 
    a=absolute(a)
    a=mod(a)
    a=logarithm(a)
    a=factorial(a)
    a=sincos(a)
    a=power(a)
    a=multiply(a)
    a=add(a)
    a=float(a[len(a)-1])
    print("output: ",a,sep="")
    """
    try:
        a=absolute(a)
        a=parantheses(a)
        a=logarithm(a)
        a=factorial(a)
        a=sincos(a)
        a=power(a)
        a=multiply(a)
        a=add(a)
        a=float(a[len(a)-1])
        print("output: ",a,sep="")
    
    except:
        print("syntax error")
        exit()
    """
def graph(s):
    global a
    xcords=[]
    ycords=[]
    s=s[2:]
    time5=time.time()
    for x in range(-100,101):
        news=list(s)
        for i in range(len(news)):
            if news[i]=="x":
                news[i]=x
        news=''.join(map(str, news))
        translate(news)
        try:
            a=parantheses(a)
            a=absolute(a)
            a=mod(a)
            a=logarithm(a)
            a=factorial(a)
            a=sincos(a)
            a=power(a)
            a=multiply(a)
            a=add(a)
            a=float(a[len(a)-1])
            ycords.append(a)
            xcords.append(x)
        except:
            pass
        a=[]
    time6=time.time()
    print("Time taken for graphing:",time6-time5)
    plt.figure('Graph')
    plt.plot(xcords,ycords)
    plt.xlim(xmin=-100,xmax=100)
    plt.ylim(ymin=-100,ymax=100)
    plt.show()

def translate(s):
    for i in range(len(s)):
            if s[i]=="|":
                if s.count("[")==s.count("]"):
                    s=s[:i]+"["+s[i+1:]
                else:
                    s=s[:i]+"]"+s[i+1:]
    while "++" in s or "+-" in s or "-+" in s or "--" in s:
        for i in range(len(s)):
            try:
                if s[i]=="+" and s[i+1]=="+":
                    string_list=list(s)
                    string_list[i]="+"
                    string_list[i+1]=" "
                    s="".join(string_list)
                    break
                elif s[i]=="-" and s[i+1]=="-":
                    string_list=list(s)
                    string_list[i]="+"
                    string_list[i+1]=" "
                    s="".join(string_list)
                    break
                elif s[i]=="+" and s[i+1]=="-":
                    string_list=list(s)
                    string_list[i]="-"
                    string_list[i+1]=" "
                    s="".join(string_list)
                    break
                elif s[i]=="-" and s[i+1]=="+":
                    string_list=list(s)
                    string_list[i]="-"
                    string_list[i+1]=" "
                    s="".join(string_list)
                    break
            except:
                pass
        s=s.replace(" ","")
    for i in range(len(s)):
        try:
            if s[i]=="(" and s[i-1]!="f":
                a.append("(")
            elif s[i]==")" and (i==len(s)-1 or (i<=len(s)-2 and s[i+1]!="=")):
                a.append(")")
            elif s[i]=="[":
                a.append("[")
            elif s[i]=="]":
                a.append("]")
            elif s[i]=="*" and s[i-1]!="*" and (i==len(s)-1 or (i<=len(s)-2 and s[i+1]!="*")):
                a.append("*")
            elif s[i]=="*" and s[i+1]=="*":
                a.append("**")
            if s[i]=="√":
                a.append("√")
            elif s[i]=="/":
                a.append("/")
            elif i!=0 and (s[i-1]=="!" or s[i-1]=="]" or s[i-1]==")" or s[i-1]=="0" or s[i-1]=="1" or s[i-1]=="2" or s[i-1]=="3" or s[i-1]=="4" or s[i-1]=="5" or s[i-1]=="6" or s[i-1]=="7" or s[i-1]=="8" or s[i-1]=="9" or s[i-1]=="√" or (s[i-1]=="*" and s[i-2]=="*")) and s[i]=="+":
                a.append("+")
            elif i!=0 and (s[i-1]=="!" or s[i-1]=="]" or s[i-1]==")" or s[i-1]=="0" or s[i-1]=="1" or s[i-1]=="2" or s[i-1]=="3" or s[i-1]=="4" or s[i-1]=="5" or s[i-1]=="6" or s[i-1]=="7" or s[i-1]=="8" or s[i-1]=="9" or s[i-1]=="√" or (s[i-1]=="*" and s[i-2]=="*")) and s[i]=="-":
                a.append("-")
            elif s[i]=="!":
                a.append("!")
            elif s[i]=="e":
                a.append(str(math.e))
            elif s[i]=="π":
                a.append(str(math.pi))
            elif s[i]=="s" and i<=len(s)-3 and s[i+1]=="i" and s[i+2]=="n" and s[i-1]!="a":
                a.append("sin")
            elif s[i]=="c" and i<=len(s)-3 and s[i+1]=="o" and s[i+2]=="s" and s[i-1]!="a":
                a.append("cos")
            elif s[i]=="t" and i<=len(s)-3 and s[i+1]=="a" and s[i+2]=="n" and s[i-1]!="a":
                a.append("tan")
            elif s[i]=="c" and i<=len(s)-3 and s[i+1]=="t" and s[i+2]=="n" and s[i-1]!="a":
                a.append("ctn")
            elif s[i]=="s" and i<=len(s)-3 and s[i+1]=="i" and s[i+2]=="n" and s[i-1]=="a":
                a.append("asin")
            elif s[i]=="c" and i<=len(s)-3 and s[i+1]=="o" and s[i+2]=="s" and s[i-1]=="a":
                a.append("acos")
            elif s[i]=="t" and i<=len(s)-3 and s[i+1]=="a" and s[i+2]=="n" and s[i-1]=="a":
                a.append("atan")
            elif s[i]=="c" and i<=len(s)-3 and s[i+1]=="t" and s[i+2]=="n" and s[i-1]=="a":
                a.append("actn")
            elif s[i]=="l" and i<=len(s)-3 and s[i+1]=="o" and s[i+2]=="g":
                a.append("log")
            elif s[i]=="m" and i<=len(s)-3 and s[i+1]=="o" and s[i+2]=="d":
                a.append("mod")
            elif s[i]=="y" and s[i+1]=="=":
                a.append("y=")
            elif s[i]=="x":
                a.append("x")
            elif (s[i]=="." and "." not in a[len(a)-1]) or s[i]=="0" or s[i]=="1" or s[i]=="2" or s[i]=="3" or s[i]=="4" or s[i]=="5" or s[i]=="6" or s[i]=="7" or s[i]=="8" or s[i]=="9":
                try:
                    if str(a[len(a)-1][len(a[len(a)-1])-1])=="." or str(a[len(a)-1][len(a[len(a)-1])-1])=="0" or int(a[len(a)-1][len(a[len(a)-1])-1]):
                        a[len(a)-1]+=str(s[i])
                except:
                    if s[i-1]=="-":
                        if len(a)>0:
                            if a[len(a)-1]!="-":
                                if s[i]=="0" and s[i+1]==".":
                                    a.append("-"+str(int(s[i])))
                                else:
                                    a.append(str(int(s[i])*-1))
                            else:
                                a.append(str(int(s[i])))
                        else:
                            try:
                                if s[i+1]=="." and s[i]=="0":
                                    a.append("-"+str(int(s[i])))
                                else:
                                    a.append(str(int(s[i])*-1))
                            except:
                                a.append(str(int(s[i])*-1))
                    elif s[i-1]=="+":
                        if s[i]!=".":
                            a.append(str(int(s[i])))
                    else:
                        if s[i]!=".":
                            a.append(str(int(s[i])))
        except:
            pass
    
#Buttons

def paranthese_open_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"(")
def paranthese_close_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,")")
def AC_button():
    global a
    a=[]
    s= ''.join(map(str, a))
    equation.set(s)
def C_button():
    global a
    s=row0.get()
    translate(s)
    try:
        a.pop(len(a)-1)
    except:
        pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def power_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"**()")
    row0.icursor(cursorindex+3)
def root_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"()√")
    row0.icursor(cursorindex+1)
def divide_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"/")
def multiply_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"*")
def minus_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"-")
def add_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"+")
def equal_button():
    global a
    time1=time.time()
    s=row0.get()
    if s[0:2]=="y=":
        graph(s)
    else:
        time3=time.time()
        translate(s)
        time4=time.time()
        print("Time taken to translate",round(time4-time3,5),"sec")
        print("input: ",*a,sep="")
        run(a)
        s= ''.join(map(str, a))
        equation.set(s)
        a=[]
        row0.icursor("end")
    time2=time.time()
    print("Time taken:",round(time2-time1,5),"sec")
def number_button(number):
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,number)
def exit_button():
    exit()
def sin_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"sin()")
    row0.icursor(cursorindex+4)
def cos_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"cos()")
    row0.icursor(cursorindex+4)
def tan_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"tan()")
    row0.icursor(cursorindex+4)
def cotan_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"ctn()")
    row0.icursor(cursorindex+4)
def xsquare_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"**(2)")
def xsquareroot_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"(2)√")
def reciprocal_button():
    global a
    s=row0.get()
    translate(s)
    for i in range(len(a)-1,-1,-1):
        try:
            if float(a[i]):
                a[i]=str(1/float(a[i]))
                break
        except:
            pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def factorial_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"!")
def e_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"e")
def pi_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"π")
def inverse_button():
    global a
    s=row0.get()
    translate(s)
    for i in range(len(a)-1,-1,-1):
        try:
            if float(a[i]):
                a[i]=str(float(a[i])*-1)
                break
        except:
            pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def log_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"log()()")
    row0.icursor(cursorindex+4)
def abs_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"|")
def mod_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"mod()()")
    row0.icursor(cursorindex+4)
def doubleleftarrow_button():
    row0.icursor(0)
def leftarrow_button():
    cursorindex=row0.index(INSERT)
    row0.icursor(cursorindex-1)
def rightarrow_button():
    cursorindex=row0.index(INSERT)
    row0.icursor(cursorindex+1)
def doublerightarrow_button():
    row0.icursor("end")
def torad_button():
    global a
    s=row0.get()
    translate(s)
    for i in range(len(a)-1,-1,-1):
        try:
            if float(a[i]):
                a[i]=str(float(a[i])/180*math.pi)
                break
        except:
            pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def EE_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"()*10**()")
    row0.icursor(cursorindex+1)
def asin_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"asin()")
    row0.icursor(cursorindex+5)
def acos_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"acos()")
    row0.icursor(cursorindex+5)
def atan_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"atan()")
    row0.icursor(cursorindex+5)
def actn_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"actn()")
    row0.icursor(cursorindex+5)
def Rand_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,str(random.random()))
def todeg_button():
    global a
    s=row0.get()
    translate(s)
    for i in range(len(a)-1,-1,-1):
        try:
            if float(a[i]):
                a[i]=str(float(a[i])*180/math.pi)
                break
        except:
            pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def x_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"x")
def y_button():
    cursorindex=row0.index(INSERT)
    row0.insert(cursorindex,"y=")
def rounding_button():
    global a
    s=row0.get()
    translate(s)
    for i in range(len(a)-1,-1,-1):
        try:
            if float(a[i]):
                a[i]=str(round(float(a[i]),2))
                break
        except:
            pass
    s= ''.join(map(str, a))
    s=s.replace("[","|")
    s=s.replace("]","|")
    equation.set(s)
    a=[]
def backspace_button():
    cursorindex=row0.index(INSERT)
    entry=row0.get()
    entry=entry[0:cursorindex-1]+entry[cursorindex:]
    equation.set(entry)
    row0.icursor(cursorindex-1)
def graphexit_button():
    plt.close()


root=Tk()
root.resizable(True,True)
root.title("Calculator")
root.configure(background='black')
equation = StringVar()

row0=Entry(root,width=34,borderwidth=0,highlightthickness=0,bg="#000000",foreground="white",insertbackground="white",textvariable=equation)
row0.grid(columnspan=6)

#1111111111111111111111111111111:
CEbutton=Button(root,text="CE",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=AC_button).grid(row=1,column=0)
Xbutton=Button(root,text="X",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=x_button).grid(row=1,column=1)
ybutton=Button(root,text="y=",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=y_button).grid(row=1,column=2)
Randbutton=Button(root,text="Rand",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=Rand_button).grid(row=1,column=3)
Graphexitbutton=Button(root,text="GExit",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=graphexit_button).grid(row=1,column=4)
exitbutton=Button(root,text="Exit",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=exit_button).grid(row=1,column=5)

#2222222222222222222222222222222:
logbutton=Button(root,text="log",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=log_button).grid(row=2,column=0)
asinbutton=Button(root,text="asin",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=asin_button).grid(row=2,column=1)
acosbutton=Button(root,text="acos",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=acos_button).grid(row=2,column=2)
atanbutton=Button(root,text="atan",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=atan_button).grid(row=2,column=3)
actnbutton=Button(root,text="actn",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=actn_button).grid(row=2,column=4)
Roundingbutton=Button(root,text="Round",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=rounding_button).grid(row=2,column=5)

#3333333333333333333333333333333:
modbutton=Button(root,text="mod",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=mod_button).grid(row=3,column=0)
sinbutton=Button(root,text="sin",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=sin_button).grid(row=3,column=1)
cosbutton=Button(root,text="cos",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=cos_button).grid(row=3,column=2)
tanbutton=Button(root,text="tan",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=tan_button).grid(row=3,column=3)
cotanbutton=Button(root,text="ctan",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=cotan_button).grid(row=3,column=4)
modbutton=Button(root,text="mod",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=mod_button).grid(row=3,column=5)
Backspacebbutton=Button(root,text="⌫",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=backspace_button).grid(row=3,column=5)

#444444444444444444444444444444:
doubleleftarrowbutton=Button(root,text="<<",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=doubleleftarrow_button).grid(row=4,column=0)
leftarrowbutton=Button(root,text="<",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=leftarrow_button).grid(row=4,column=1)
paranthese_openbutton=Button(root,text="(",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=paranthese_open_button).grid(row=4,column=2)
paranthese_closebutton=Button(root,text=")",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=paranthese_close_button).grid(row=4,column=3)
rightarrowbutton=Button(root,text=">",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=rightarrow_button).grid(row=4,column=4)
doublerightarrowbutton=Button(root,text=">>",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=doublerightarrow_button).grid(row=4,column=5)

#555555555555555555555555555555:
pibutton=Button(root,text="π",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=pi_button).grid(row=5,column=0)
reciprocalbutton=Button(root,text="1/x",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=reciprocal_button).grid(row=5,column=1)
inversebutton=Button(root,text="+/-",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=inverse_button).grid(row=5,column=2)
squarerootbutton=Button(root,text="√",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=root_button).grid(row=5,column=3)
powerbutton=Button(root,text="^",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=power_button).grid(row=5,column=4)
dividebutton=Button(root,text="/",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=divide_button).grid(row=5,column=5)

#666666666666666666666666666666:
ebutton=Button(root,text="e",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=e_button).grid(row=6,column=0)
factorialbutton=Button(root,text="!",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=factorial_button).grid(row=6,column=1)
onebutton=Button(root,text="1",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("1")).grid(row=6,column=2)
twobutton=Button(root,text="2",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("2")).grid(row=6,column=3)
threebutton=Button(root,text="3",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("3")).grid(row=6,column=4)
multiplybutton=Button(root,text="*",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=multiply_button).grid(row=6,column=5)

#777777777777777777777777777777:
EEbutton=Button(root,text="EE",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=EE_button).grid(row=7,column=0)
absbutton=Button(root,text="|   |",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=abs_button).grid(row=7,column=1)
fourbutton=Button(root,text="4",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("4")).grid(row=7,column=2)
fivebutton=Button(root,text="5",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("5")).grid(row=7,column=3)
sixbutton=Button(root,text="6",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("6")).grid(row=7,column=4)
plusbutton=Button(root,text="+",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=add_button).grid(row=7,column=5)

#888888888888888888888888888888:
xsquarebutton=Button(root,text="x^2",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=xsquare_button).grid(row=8,column=0)
xsquarrootbutton=Button(root,text="2√",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=xsquareroot_button).grid(row=8,column=1)
sevenbutton=Button(root,text="7",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("7")).grid(row=8,column=2)
eightbutton=Button(root,text="8",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("8")).grid(row=8,column=3)
ninebutton=Button(root,text="9",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("9")).grid(row=8,column=4)
minusbutton=Button(root,text="-",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=minus_button).grid(row=8,column=5)

#999999999999999999999999999999:
radbutton=Button(root,text="Rad",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=torad_button).grid(row=9,column=0)
degbutton=Button(root,text="Deg",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=todeg_button).grid(row=9,column=1)
zerobutton=Button(root,text="0",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button("0")).grid(row=9,column=2)
dotbutton=Button(root,text=".",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#040404",foreground="white",command=lambda: number_button(".")).grid(row=9,column=3)
Cbutton=Button(root,text="C",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=C_button).grid(row=9,column=4)
equalbutton=Button(root,text="=",width=2,height=1,borderwidth=0,highlightthickness=0,padx=14,pady=14,bg="#ff9E09",foreground="white",command=equal_button).grid(row=9,column=5)

root.resizable(False, False)
root.mainloop()