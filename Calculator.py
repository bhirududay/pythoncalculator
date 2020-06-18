import tkinter as tk
import math


#-----------------------------creating a window--------------------------------
window = tk.Tk()
window.title('Calculator')
window.geometry('680x297')
window.resizable(width=False, height=False)



#--------input and display bar---------------

bar = tk.Entry(window, width=110, borderwidth=3)
bar.grid(row=0, column=0, padx=5, pady=5, columnspan=7)



#------------------0-9 number buttons function---------------------------------
def num(n):
    current = bar.get()
    bar.delete(0, tk.END)
    bar.insert(0, str(current)+str(n))

#---------------------operator button function--------------------------------    
def getnum(opr):
    global num1, operator
    num1 = float(bar.get())
    bar.delete(0, tk.END)
    operator = opr

#----------------------equal button function-----------------------------------
def equal(n):
    if(n =='add'):
        ans = num1 + float(bar.get())
    elif(n=='sub'):
        ans = num1 - float(bar.get())
    elif(n=='mul'):
        ans = num1 * float(bar.get())
    elif(n=='div'):
        ans = num1 / float(bar.get())
    bar.delete(0, tk.END)
    bar.insert(0, str(ans))

#------------------------clear button function--------------------------------
def clr():
    bar.delete(0, tk.END)

#-------------------degree/radians button function----------------------------
t=0
unit='degree'
def angle():
    global unit,t
    dr = ['degree', 'radian']
    t=t^1
    unit = dr[t]
    button_angle.configure(text=unit)
    
#----------------------------tan button function-------------------------------
def tan():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree' and angle%90!=0 or angle==0):
        bar.insert(0, round(math.tan(math.radians(angle)),6))
        
    elif((unit == 'radian' and round(math.degrees(angle), 3)%90!=0) or angle==0):
        bar.insert(0, round(math.tan(angle),6))
        
    else:
        bar.insert(0, 'INVALID')

#----------------------------cos button function-------------------------------
def cos():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree'):
        bar.insert(0, round(math.cos(math.radians(angle)),6))
    else:
        bar.insert(0, round(math.cos(angle),6))

#----------------------------sin button function-------------------------------
def sin():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree'):
        bar.insert(0, round(math.sin(math.radians(angle)),6))
    else:
        bar.insert(0, round(math.sin(angle),6))

#----------------------------cot button function-------------------------------
def cot():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree' and angle%180!=0):
        bar.insert(0, round(1/math.tan(math.radians(angle)),6))    
    
    elif((unit == 'radian' and round(math.degrees(angle), 3)%180!=0)):
        bar.insert(0, round(1/math.tan(angle),6))
    
    else:
        bar.insert(0, 'INVALID')

#--------------------------cosec button function-------------------------------
def cosec():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree' and angle%180!=0):
        bar.insert(0, round(1/math.sin(math.radians(angle)),6))    
    
    elif((unit == 'radian' and round(math.degrees(angle), 3)%180!=0)):
        bar.insert(0, round(1/math.sin(angle),6))
    
    else:
        bar.insert(0, 'INVALID')

#----------------------------sec button function-------------------------------
def sec():
    angle = float(bar.get())
    bar.delete(0, tk.END)
    if(unit == 'degree' and angle%90!=0 or angle==0):
        bar.insert(0, round(1/math.cos(math.radians(angle)),6))    
    
    elif((unit == 'radian' and round(math.degrees(angle), 3)%90!=0)):
        bar.insert(0, round(1/math.cos(angle),6))
    
    else:
        bar.insert(0, 'INVALID')

#----------------------------memory button function----------------------------
def memory():
    global mem
    mem = float(bar.get())
    mem = format(mem, '.20f')
    button_mu.configure(text=str(mem)[0:11])

#--------------------------memory use button function--------------------------
def memuse():
    bar.delete(0, tk.END)
    bar.insert(0, mem)



#-------------------------buttons creations-----------------------------------
button_0 = tk.Button(text=0, padx=88, pady=20, command=lambda: num(0))
button_1 = tk.Button(text=1, padx=40, pady=20, command=lambda: num(1))
button_2 = tk.Button(text=2, padx=40, pady=20, command=lambda: num(2))
button_3 = tk.Button(text=3, padx=40, pady=20, command=lambda: num(3))
button_4 = tk.Button(text=4, padx=40, pady=20, command=lambda: num(4))
button_5 = tk.Button(text=5, padx=40, pady=20, command=lambda: num(5))
button_6 = tk.Button(text=6, padx=40, pady=20, command=lambda: num(6))
button_7 = tk.Button(text=7, padx=40, pady=20, command=lambda: num(7))
button_8 = tk.Button(text=8, padx=40, pady=20, command=lambda: num(8))
button_9 = tk.Button(text=9, padx=40, pady=20, command=lambda: num(9))
button_p = tk.Button(text='.', padx=42, pady=20, command=lambda: num('.'))
button_pi = tk.Button(text='pi', padx=38, pady=20, command=lambda: num(math.pi))
button_add = tk.Button(text='+', padx=39, pady=20, command=lambda: getnum('add'))
button_sub = tk.Button(text='-', padx=40, pady=20, command=lambda: getnum('sub'))
button_mul = tk.Button(text='x', padx=40, pady=20, command=lambda: getnum('mul'))
button_div = tk.Button(text='/', padx=40, pady=20, command=lambda: getnum('div'))
button_clr = tk.Button(text='clr', padx=36, pady=20, command=clr)
button_equ = tk.Button(text='=', padx=39, pady=20, command=lambda: equal(operator))
button_angle = tk.Button(text='degree', padx=25, pady=20, command=angle)
button_tan = tk.Button(text='tan', padx=34, pady=20, command=tan)
button_sin = tk.Button(text='sin', padx=34, pady=20, command=sin)
button_cos = tk.Button(text='cos', padx=33, pady=20, command=cos)
button_cosec = tk.Button(text='cosec', padx=26, pady=20, command=cosec)
button_sec = tk.Button(text='sec', padx=33, pady=20, command=sec)
button_cot = tk.Button(text='cot', padx=33, pady=20, command=cot)
button_mem = tk.Button(text='M', padx=36, pady=20, command=memory)
button_mu = tk.Button(text=('                     '), padx=10, pady=20, command=memuse)



#---------------------------button inserting----------------------------------
button_1.grid(row=3, column=0, padx=1, pady=1)
button_2.grid(row=3, column=1, padx=1, pady=1)
button_3.grid(row=3, column=2, padx=1, pady=1)
button_4.grid(row=2, column=0, padx=1, pady=1)
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6.grid(row=2, column=2, padx=1, pady=1)
button_7.grid(row=1, column=0, padx=1, pady=1)
button_8.grid(row=1, column=1, padx=1, pady=1)
button_9.grid(row=1, column=2, padx=1, pady=1)
button_add.grid(row=2, column=3, padx=1, pady=1)
button_sub.grid(row=2, column=4, padx=1, pady=1)
button_mul.grid(row=3, column=3, padx=1, pady=1)
button_div.grid(row=3, column=4, padx=1, pady=1)
button_clr.grid(row=1, column=3, padx=1, pady=1)
button_equ.grid(row=4, column=3, padx=1, pady=1)
button_angle.grid(row=1, column=4, padx=1, pady=1)
button_0.grid(row=4, column=0, columnspan=2)
button_p.grid(row=4, column=2)
button_pi.grid(row=4, column=4, padx=1, pady=1)
button_tan.grid(row=1, column=5, padx=1, pady=1)
button_sin.grid(row=2, column=5, padx=1, pady=1)
button_cos.grid(row=3, column=5, padx=1, pady=1)
button_cosec.grid(row=1, column=6, padx=1, pady=1)
button_cot.grid(row=2, column=6, padx=1, pady=1)
button_sec.grid(row=3, column=6, padx=1, pady=1)
button_mem.grid(row=4, column=5, padx=1, pady=1, columnspan=1)
button_mu.grid(row=4, column=6, padx=1, pady=1)


#-----------------------------looping------------------------------------------
window.mainloop()