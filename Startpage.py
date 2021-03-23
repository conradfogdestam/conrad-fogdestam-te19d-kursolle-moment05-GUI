import PySimpleGUI as sg

layout = [[sg.Text('CAYMAN ISLANDS NATIONAL BANK™')],
        [sg.Button('Login','center', size=(20, 2))],
        [sg.Button('Register', size=(20, 2))] + [sg.Stretch()],
        [sg.Cancel()]]

window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()