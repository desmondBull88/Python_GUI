import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def addApp():
    
    for widget in frame.winfo_children():
        widget.destroy()

    
    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                           filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg='azure')
        label.pack()

        
def runApps():
    for app in apps:
        os.startfile(app)
    

canvas = tk.Canvas(root, height=500, width=500, bg='light slate gray')
canvas.pack()

frame = tk.Frame(root, bg='light gray')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

openFile = tk.Button(root, text='Open File', padx=5, pady=2.5, fg='white smoke', bg='light slate gray', command=addApp)
openFile.pack()

runApps = tk.Button(root, text='Run Apps', padx=5, pady=2.5, fg='white smoke', bg='light slate gray', command=runApps)
runApps.pack()

closeApps = tk.Button(root, text='Close Apps', padx=5, pady=2.5, fg='white smoke', bg='light slate gray')
closeApps.pack()





root.mainloop()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


with open('save.tx', 'w') as f:
    for app in apps:
        f.write(app + ',')
