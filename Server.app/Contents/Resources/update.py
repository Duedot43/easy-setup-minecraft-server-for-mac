import os
extra = ("b")
from tkinter import messagebox
import tkinter as tk
root=tk.Tk() 
  
# setting the windows size 
root.geometry("600x400") 
   
# declaring string variable 
# for storing name and password 
name_var=tk.StringVar() 
passw_var=tk.StringVar() 
  
   
# defining a function that will 
# get the name and password and  
# print them on the screen 
def submit(): 
  
    name=name_entry.get() 
    
      
    print("The name is : " + name) 
    
    print(name)
    name_var.set("")
    if name == "MH37W-N47XK-V7XM9-C7227-GCQG9":
    

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
    
        if name != "MH37W-N47XK-V7XM9-C7227-GCQG9":
            print("fail")
   

    root.quit()
    
     
      
      
# creating a label for  
# name using widget Label 
name_label = tk.Label(root, text = 'Product Key', 
                      font=('calibre', 
                            10, 'bold')) 
   
# creating a entry for input 
# name using widget Entry 
name_entry = tk.Entry(root, 
                      textvariable = name_var,font=('calibre',10,'normal')) 
   

   
# creating a button using the widget  
# Button that will call the submit function  
sub_btn=tk.Button(root,text = 'Submit', 
                  command = submit) 
   
# placing the label and entry in 
# the required position using grid 
# method 
name_label.grid(row=0,column=0) 
name_entry.grid(row=0,column=1) 

sub_btn.grid(row=2,column=1) 
   
# performing an infinite loop  
# for the window to display 
root.mainloop() 


if name_entry == "MH37W-N47XK-V7XM9-C7227-GCQG9":
    

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
    
if name_entry != "MH37W-N47XK-V7XM9-C7227-GCQG9":
    print("fail")
   

