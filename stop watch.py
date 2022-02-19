from tkinter import *
from datetime import datetime

counter = 0
running = False
main = True

def counter_label(label):
    def count():
        if running:
            global counter
            tt = datetime.fromtimestamp(counter)
            if(counter > 600):
                date_object = tt.strftime('%H:%M:%S')
            elif(counter > 60):
                date_object = tt.strftime('%M:%S.%f')[:-4]
            else:
                date_object = tt.strftime('%S.%f')[:-4]
            display=date_object
   
            label['text']=display
   
            label.after(10, count) 
            counter += 0.01
    count()
    
def clocktime(label):
    
    def count():
        if main == True:
            label['text']=datetime.utcnow().strftime('%H:%M:%S')
            label.after(500, count) 
    count()
    

def Start(label):
    global running,main
    running=True
    main = False
    counter_label(label)
    
    start['state']='disabled'
    start['highlightbackground']='black'
    
    stop['state']='normal'
    stop['highlightbackground']='red'
    
    reset['state']='normal'
    reset['highlightbackground']='dark grey'
   

def Stop():
    global running,main
    start['state']='normal'
    start['highlightbackground']='green'
    
    stop['state']='disabled'
    stop['highlightbackground']='black'
    
    reset['state']='normal'
    reset['highlightbackground']='dark grey'
    
    running = False
  

def Reset(label):
    global counter,main
    counter=00000
    if running==False:      
        reset['state']='disabled'
        reset['highlightbackground']='black'
        
        main = True
        clocktime(label)
   

   
root = Tk()
root.title("Stopwatch")


root.minsize(width=100, height=150)


label = Label(root, text=datetime.utcnow().strftime('%H:%M:%S'), fg="white", font="Geneva 45 bold",bg="#282828")
label.pack()
root.attributes("-alpha", 0.90)


clocktime(label)

f = Frame(root)
root.config(bg="#282828")
f.configure(background="black")

start = Button(f, text='Start', width=7,height=3, command=lambda:Start(label),font="Geneva 15 bold",highlightbackground="green",activeforeground='black',fg='green')
reset = Button(f, text='Reset',width=7,height=3, state='disabled', command=lambda:Reset(label),font="Geneva 15 bold",borderwidth = 0,highlightbackground="black",activeforeground='black',fg='white')
stop = Button(f, text='Stop',width=7,height=3,state='disabled',command=Stop,font="Geneva 15 bold",bg="darkgrey",highlightbackground="black",activeforeground='black',fg='red')

f.pack(anchor = 'center',pady=5)
start.pack(side="left")
reset.pack(side="left")
stop.pack(side ="left")
root.mainloop()