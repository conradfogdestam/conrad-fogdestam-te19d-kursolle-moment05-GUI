import PySimpleGUI as sg

layout = [[sg.Text('Rename files or folders')],
          [sg.Text('Username', size=(15, 1)), sg.InputText()],
          [sg.Text('Password', size=(15, 1)), sg.InputText()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()