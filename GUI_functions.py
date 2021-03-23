import PySimpleGUI as sg

def loginwindow():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Please enter credentials')],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
            [sg.Submit('Register Account')]]

    loginpage = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = loginpage.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break
        if event == 'Register Account':
            registerwindow()
        print('You entered ', values[0])

    loginpage.close()



def registerwindow():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Please enter credentials')],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('First name', size=(15, 1)), sg.InputText()],
            [sg.Text('Last name', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
            [sg.Submit('back')],
            [sg.Submit('OK')]]

    registerpage = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = registerpage.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'back':
            registerpage.close()
            startwindow()
        print('You entered ', values[0])

    registerpage.close()



def startwindow():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('CAYMAN ISLANDS NATIONAL BANK™', text_color='Magenta', size=(31, 1), font='Helvetica 20')],
            [sg.Text('We value your privacy, since 1998', text_color='Magenta', justification='center', size=(62, 1), font='Helvetica 10')],  
            [sg.Button('Login', size=(62, 2))],
            [sg.Button('Register', size=(62, 2))],
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]


    startpage = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = startpage.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Register':
            startpage.close()
            registerwindow() 
        if event == 'Login':
            startpage.close()
            loginwindow()       
        print('You entered ', values[0])

    startpage.close()

startwindow()