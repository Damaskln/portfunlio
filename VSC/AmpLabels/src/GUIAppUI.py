import PySimpleGUI as sg
import openpyxl 
import os

def getFiles(directory: str, extension: str) -> list:
    try:
        file_list = os.listfir(directory)
    except:
        file_list = []
    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(directory, f)) and f.lower().endswith(extension)
    ]
    return fnames

def pysimpleguiamplabels():
    defaultoutputpath = "./output"
    selection_column = [
        [
            sg.Checkbox(
                "Single Amp Cart",
                default=False,
                key="-SINGLE_AMP_CART-",
                enable_events=True,
            )
        ],
        [
            sg.Checkbox(
                "Double Amp Cart",
                default=False,
                key="-DOUBLE_AMP_CART-",
                enable_events=True,
            )
        ],
        [
            sg.Checkbox(
                "Triple Amp Cart",
                default=False,
                key="-TRIPLE_AMP_CART-",
                enable_events=True,
            )
        ],
    ]
    button_column = [
        [sg.Text("Choose First Amp Patch")],
        [
            sg.In(size=(30, 1), enable_events=True, key="-INPUTONE-"),
            sg.FileBrowse(
                initial_folder="./",
                button_text="Amp Cart One",
                file_types=(
                    (
                        "Excel Spreadsheets"
                        "*.xlsx .xls .xlsm"
                    ),
                ),
                key="-FILEONE-"
            )
        ],
        [sg.Text("Choose Second Amp Patch")],
        [
            sg.In(size=(30, 1), enable_events=True, key="-INPUTTWO-"),
            sg.FileBrowse(
                initial_folder="./",
                button_text="Amp Cart One",
                file_types=(
                    (
                        "Excel Spreadsheets"
                        "*.xlsx .xls .xlsm"
                    ),
                ),
                key="-FILETWO-"
            )
        ],
    ]
    missing_amp_column = [
        [
            sg.Text("Missing amps")
        ],
        [
            sg.In(
                size=(30, 1),
                enable_events= True,
                key="-MISSINGAMPS-",
                default_text=defaultoutputpath
            ),
            sg.FolderBrowse(initial_folder="./", key="-BROWSE2-")
        ],
        [
            sg.Listbox(
                values=getFiles(defaultoutputpath, ".output")
            )
        ],
    ]
    generate_column = [
        [
            sg.Button("Give me the list", enable_events=True, key="-GENERATE-")
        ],
    ]
    tab1_layout=[
        [
            sg.Column(selection_column),
            sg.VSeparator(),
            sg.Column(button_column),
            sg.VSeparator(),
            sg.Column(generate_column, justification='center')
        ],
    ]
    layout = [
        [  
            sg.TabGroup(
                [
                    [
                        sg.Tab("Please solve my problems", tab1_layout),
                    ]
            ]
            )
        ],
    ]  
    
#    ###################
#    #event handlers
#     amppatchselector = {}
#     while True:
#         event, values= window.read()
#         if event == sg.TIMEOUT_KEY:
#             continue
#         if event == "Exit" or event == sg.WINDOW_CLOSED:
#             break
#         if event == "-GENERATE-":
#             outfolder = os.path.join("output")
#             if not os.path.exists("output"):
#                 os.makedirs("output")
#             if values 

    window = sg.Window("Amps Label", layout, return_keyboard_events=True)

   
    window.close()

pysimpleguiamplabels()

