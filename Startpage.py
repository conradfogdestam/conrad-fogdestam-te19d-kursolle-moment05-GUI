import PySimpleGUI as sg
sg.theme_previewer()
sg.theme('DarkPurple7')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Cayman Islands National Bank')],
            [sg.Text('Login'), sg.InputText()],
            [sg.Text('Password'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()