import PySimpleGUI as sg
sg.theme("DarkRed1")
sg.theme_text_color("#424bdd")
window = sg.Window(title="Profile",
            layout=[[sg.Text("NPM : 2210010085 ")],
                    [sg.Text("Nama : AHMAD RIYO KUSUMA ")],
                    [sg.Text("Kelas : 5O Regular Banjarmasin ")]],
            size=(400,200),
            font=("Arial", 18))
window()
window.close()