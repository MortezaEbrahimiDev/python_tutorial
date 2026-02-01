# imports and global variables
import tkinter as tk
from tkinter import messagebox as messagebox
from datetime import datetime


alarm_time=None
def set_alarm():
    global alarm_time
    current_time=datetime.now()
    alarm_time=current_time.replace(hour=int(hour_alarm_entry.get()),minute=int(minuts_alarm_entry.get()),second=0,microsecond=0)
    latest_alarm_label.config(text=alarm_time.strftime("%H:%M:%S"))





window=tk.Tk()
window.title("Alarm Clock App")
window.resizable(width=True,height=True)
# window.geometry("400*300")


time_label=tk.Label(window,text="12:30:30",font=('tahoma',32))
time_label.pack()


tk.Label(window,text="Hour").pack()
hour_alarm_entry=tk.Entry(window)
hour_alarm_entry.pack()




tk.Label(window,text="minuts").pack()
minuts_alarm_entry=tk.Entry(window)
minuts_alarm_entry.pack()



tk.Button(window,text="Set alarm",command=set_alarm).pack()


latest_alarm_label=tk.Label(window,text="12:31")
latest_alarm_label.pack()
# function for get current time
def get_current_time():
    res= datetime.now()
    time_label.config(text=res.strftime("%H:%M:%S"))
    compare_alarm_with_current_time(res)
    window.after(1000,get_current_time)


def compare_alarm_with_current_time(current_time):
    global alarm_time
    if  alarm_time is not None and  current_time>=alarm_time:
        messagebox.showinfo("allllllarm")
        print('anjam shod')
        alarm_time=None

# function set alarm timer

# function for compare time with alarm


# ui designer

# run app
get_current_time()
window.mainloop()