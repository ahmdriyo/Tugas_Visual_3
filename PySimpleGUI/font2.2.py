import PySimpleGUI as sg
sg.theme("DrakGreen4")
sg.theme_text_color("#212121")
window = sg.Window(title= "Profile",
                   layout=[[sg.Text("FTI UNISKA", font=("Helvetica", 22))],
                          [sg.Text("FAKULTAS TEKNOLOGI INFORMASI")],
                          [sg.Text("UNISKA MAB BANJARMASIN")]],
                          size=(430,200),
                          font=("Times", 18))
window()
window.close()