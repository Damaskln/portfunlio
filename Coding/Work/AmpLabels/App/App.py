import openpyxl
import tkinter as tk
import subprocess
from tkinter import ttk
from tkinter import filedialog
import tkinter.filedialog as fd

def checkbox_changed(checkbox):
    global checkbuttons
    for cb in checkbuttons:
        if cb != checkbox:
            cb.deselect()
            
def on_checkbox_click(event):
    checkbox_changed(event.widget)

def openFile1():
    filepath = fd.askopenfilename(initialdir="C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Single",
                                          title="Select Single Amp-cart config" )
    file = open(filepath, 'r')
    print(file.read())
    file.close

def openFile2():
    filepath = fd.askopenfilename(initialdir="C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Double",
                                          title="Select Double Amp-cart config" )
    file = open(filepath, 'r')
    print(file.read())
    file.close
    
def openFile3():
    filepath = fd.askopenfilename(initialdir="C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Triple",
                                          title="Select Triple Amp-cart config" )
    file = open(filepath, 'r')
    print(file.read())
    file.close

root = tk.Tk()
root.title("Main Window")  

frame= ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Choose your fighter")
widgets_frame.grid(row=0, column=0, padx=20, pady=20)

checkboxes = []

checkbutton1 = tk.Checkbutton(widgets_frame, text="Single Cart")
checkbutton1.grid(row=0, column=0)
checkbutton1.bind("<Button-1>", on_checkbox_click)

checkbutton2 = tk.Checkbutton(widgets_frame, text="Double Cart")
checkbutton2.grid(row=0, column=2)
checkbutton2.bind("<Button-1>", on_checkbox_click)

checkbutton3 = tk.Checkbutton(widgets_frame, text="Triple Cart")
checkbutton3.grid(row=0, column=4)
checkbutton3.bind("<Button-1>", on_checkbox_click)

for i in range (0, 5):
    separator = ttk.Separator(widgets_frame)
    separator.grid(row=1, columnspan=5, padx=(10), pady=10, sticky="ew")


button1 = ttk.Button(widgets_frame, text="Amp cart 1",command=openFile1)
button1.grid(row=2, column=1, pady=10)
button2 = ttk.Button(widgets_frame, text="Amp cart 2",command=openFile1)
button2.grid(row=2, column=3, pady=10)

# button3 = ttk.Button(widgets_frame, text="Execute", command=pickapoo)
# button3.grid(row= 4, column= 2, pady= 10)

viewerframe = ttk.Frame(frame)
viewerframe.grid(row=1, column= 0, pady= 10)
viewerScroll = ttk.Scrollbar(viewerframe)
viewerScroll.pack(side="right", fill="y")

# This will show the labels that will be placed on the output file

cols = ("IP", "Hang", "Box")
viewer = ttk.Treeview(viewerframe, show="headings",
                      yscrollcommand=viewerScroll.set, columns=cols, height=13)
viewer.column("IP", width=30)
viewer.column("Hang", width=80)
viewer.column("Box", width=60)
viewer.pack()
viewerScroll.config(command=viewer.yview)

checkbuttons = [checkbutton1, checkbutton2, checkbutton3]

root.mainloop() 

