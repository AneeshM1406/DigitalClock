from tkinter import Label, Tk  
from time import strftime 
  
app = Tk() 
app.title('Clock') 

def call_time(): 
    string = strftime('%I:%M:%S %p') 
    label.config(text = string) 
    label.after(1000, call_time) 
  
label = Label(app, font = ('arial', 40, 'bold'), bg = 'blue', fg = 'white') 
label.pack(anchor = 'center') 

call_time() 
  
app.mainloop()
