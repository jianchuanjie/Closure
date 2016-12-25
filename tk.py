from tkinter.filedialog import askopenfilename
from tkinter.messagebox import *
from tkinter import *
import numpy
import sys
from collections import OrderedDict
import closure


def inarray(s):
    m = []
    count = 0
    for i in s.split():
        count += 1
        m.append(int(i))

    return numpy.array(m).reshape(int(count**0.5), int(count**0.5))


def outarray(ans):
    for i in range(len(ans)):
        print(ans[i])


def openfile_rc(event=None):
    file = open(askopenfilename())
    a = file.read()
    b = inarray(a)
    outarray(closure.reflexive_closure(b))


def openfile_sc(event=None):
    file = open(askopenfilename())
    a = file.read()
    b = inarray(a)
    outarray(closure.symmetric_closure(b))


def openfile_tc(event=None):
    file = open(askopenfilename())
    a = file.read()
    b = inarray(a)
    outarray(closure.transitive_closure(b))


def rc():
    me = Toplevel(root)
    me.title('Reflexive_closure')
    me.config(height=10, width=20)
    msg = Button(me, text='open file', command=openfile_rc)
    msg.pack(expand=YES)
    msg.config(height=2, width=50)


def sc():
    me = Toplevel(root)
    me.title('Symmetric_closure')
    msg = Button(me, text='open', command=openfile_sc)
    msg.pack(expand=YES)
    msg.config(padx=10, pady=10, bd=5)


def tc():
    me = Toplevel(root)
    me.title('Transitive_closure')
    msg = Button(me, text='open', command=openfile_tc)
    msg.pack(expand=YES)
    msg.config(padx=10, pady=10)


closure_select = OrderedDict()
closure_select['reflexive_closure'] = rc
closure_select['symmetric_closure'] = sc
closure_select['transitive_closure'] = tc


root = Tk()
root.title("Closure")
root.config(height=50, width=100)
Label(root, text='Please select the operation you want', width=40).pack()
for (key, value) in closure_select.items():
    Button(root, text=key, command=value).pack(side=TOP)

root.mainloop()


if input('anykey to quit'):
    sys.exit()
