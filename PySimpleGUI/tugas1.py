import PySimpleGUI as sg
sg.theme("DrakGreen4")
sg.theme_text_color("#eaeaea")
window = sg.Window(title="Profile saya",
    layout=[
        [sg.Text("NPM : 2210010085")],
        [sg.Text("Nama : Ahmad Riyo Kusuma")],
        [sg.Text("Kelas : 5O Pagi Bjm")],
        [sg.Text("Makul : Pemograman Visual 3")],
    ],
    size=(500,200),
    font=("Sans", 15))

window()
window.close()