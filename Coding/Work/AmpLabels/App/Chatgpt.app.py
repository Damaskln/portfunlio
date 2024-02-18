import tkinter as tk
from tkinter import ttk, filedialog

# Constants for file paths
SINGLE_PATH = "C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Single"
DOUBLE_PATH = "C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Double"
TRIPLE_PATH = "C:\\Users\\koeni\\Desktop\\VSC\\AmpLabels\\Excel sheets for Mabellaker\\Triple"

# Variables to store selected file paths
selected_file1 = None
selected_file2 = None

def checkbox_changed(checkbox):
    for cb in checkboxes:
        if cb != checkbox:
            cb.deselect()

def on_checkbox_click(event):
    checkbox_changed(event.widget)

def open_file(file_path, target_variable):
    global selected_file1, selected_file2
    filepath = filedialog.askopenfilename(initialdir=file_path, title=f"Select Config File in {file_path}")
    with open(filepath, 'r') as file:
        print(file.read())
    # Update the selected file path based on the target variable
    if target_variable == "file1":
        selected_file1 = filepath
    elif target_variable == "file2":
        selected_file2 = filepath

def create_checkbutton(parent, text, row, column, command):
    checkbutton = tk.Checkbutton(parent, text=text)
    checkbutton.grid(row=row, column=column)
    checkbutton.bind("<Button-1>", command)
    return checkbutton

def create_separator(parent, row):
    separator = ttk.Separator(parent)
    separator.grid(row=row, columnspan=5, padx=(10), pady=10, sticky="ew")

root = tk.Tk()
root.title("Main Window")

frame = ttk.Frame(root)
frame.pack()

widgets_frame = ttk.LabelFrame(frame, text="Choose your fighter")
widgets_frame.grid(row=0, column=0, padx=20, pady=20)

checkboxes = []

checkbutton1 = create_checkbutton(widgets_frame, "Single Cart", 0, 0, on_checkbox_click)
checkbutton2 = create_checkbutton(widgets_frame, "Double Cart", 0, 2, on_checkbox_click)
checkbutton3 = create_checkbutton(widgets_frame, "Triple Cart", 0, 4, on_checkbox_click)

for i in range(0, 5):
    create_separator(widgets_frame, 1)

button1 = ttk.Button(widgets_frame, text="Amp cart 1", command=lambda: open_file(SINGLE_PATH, "file1"))
button1.grid(row=2, column=1, pady=10)
button2 = ttk.Button(widgets_frame, text="Amp cart 2", command=lambda: open_file(DOUBLE_PATH, "file2"))
button2.grid(row=2, column=3, pady=10)

viewerframe = ttk.Frame(frame)
viewerframe.grid(row=1, column=0, pady=10)
viewerScroll = ttk.Scrollbar(viewerframe)
viewerScroll.pack(side="right", fill="y")

cols = ("IP", "Hang", "Box")
viewer = ttk.Treeview(viewerframe, show="headings", yscrollcommand=viewerScroll.set, columns=cols, height=13)
viewer.column("IP", width=30)
viewer.column("Hang", width=80)
viewer.column("Box", width=60)
viewer.pack()
viewerScroll.config(command=viewer.yview)

checkbuttons = [checkbutton1, checkbutton2, checkbutton3]

root.mainloop()