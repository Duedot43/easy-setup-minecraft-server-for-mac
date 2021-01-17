import os
extra = ("b")
from tkinter import messagebox
import tkinter as tk
root=tk.Tk() 
  
    

os.system("git clone https://github.com/Duedot43/update-.git ; cd update- ; cp yes.txt ..")
updates = ()
#git hub crap i will add later
update = open('yes.txt','r')
for line in update:
    updates = line.strip()
os.system("rm -rf update- ; rm yes.txt")
if updates == '1':
    messagebox.showinfo(title='Update!', message='updating the program please wait...')

    os.system('git clone https://github.com/Duedot43/python-updates ; rm "server update.py" ; cd python-updates ; cp "server update.py" .. ; cd .. ; rm -rf python-updates')
    
