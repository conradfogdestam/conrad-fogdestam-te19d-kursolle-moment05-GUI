import PySimpleGUI as sg
import functions

def loginwindow():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Please enter credentials')],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
            [sg.Button('Back'), sg.Submit('No account? Register here'), sg.Button('Login')],
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]

    loginpage = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = loginpage.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        if event == 'Login':
            if functions.login(values[0], values[1]) == True:
                loginpage.close()
                logged_in_window()
            else:
                sg.Popup("Login failed, try again")
        if event == 'Back':
            loginpage.close()
            startwindow()
        if event == 'No account? Register here':
            loginpage.close()
            registerwindow()
        print('username ', values[0])
        print('pass ', values[1])

    loginpage.close()



def registerwindow():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Please enter credentials')],
            [sg.Text('Username', size=(15, 1)), sg.InputText()],
            [sg.Text('First name', size=(15, 1)), sg.InputText()],
            [sg.Text('Last name', size=(15, 1)), sg.InputText()],
            [sg.Text('Password', size=(15, 1)), sg.InputText(password_char='*')],
            [sg.Button('Back'), sg.Button('Confirm Credentials and Register')], 
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]

    registerpage = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = registerpage.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        if event == 'Confirm Credentials and Register':
            functions.register(values[0], values[3])
            registerpage.close()
            startwindow()


        if event == 'Back':
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

def withdrawal_window():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Enter Amount To Withdraw')],
            [sg.Text('Amount to withdraw: ', size=(15, 1)), sg.InputText()],
            [sg.Button('Back'), sg.Button('Withdraw')],
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]

    withdrawal_page = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = withdrawal_page.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        if event == 'Withdraw':
            functions.withdrawal(functions.logged_in_user(), functions.logged_in_password(), int(values[0]))
            withdrawal_page.close()
            logged_in_window()

        if event == 'Back':
            withdrawal_page.close()
            logged_in_window()

    withdrawal_page.close()

def deposit_window():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('Enter Amount To Deposit')],
            [sg.Text('Amount to Deposit: ', size=(15, 1)), sg.InputText()],
            [sg.Button('Back'), sg.Button('Deposit')],
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]

    deposit_page = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = deposit_page.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            break

        if event == 'Deposit':
            functions.deposit(functions.logged_in_user(), functions.logged_in_password(), int(values[0]))
            deposit_page.close()
            logged_in_window()

        if event == 'Back':
            deposit_page.close()
            logged_in_window()

    deposit_page.close()

def logged_in_window():
    sg.theme('DarkPurple7')
    layout = [[sg.Text('CAYMAN ISLANDS NATIONAL BANK™', text_color='Magenta', size=(31, 1), font='Helvetica 20')],
            [sg.Text('We value your privacy, since 1998', text_color='Magenta', justification='center', size=(62, 1), font='Helvetica 10')],
            [sg.Button('View Balance', size=(62, 2))],
            [sg.Button('Make Withdrawal', size=(62, 2))],
            [sg.Button('Make Deposit', size=(62, 2))],
            [sg.Button('Check Transactions', size=(62, 2))],
            [sg.Button('Terminate Account', size=(62, 2))],
            [sg.Button('EXIT', size=(62, 2))],
            [sg.Text('© 2021 CAYMAN ISLANDS NATIONAL BANK™ CAY IS, Inc. All rights reserved.', justification='center', size=(62, 1), font='Helvetica 10')]]


    logged_in_page = sg.Window('CAYMAN ISLANDS NATIONAL BANK™', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event = logged_in_page.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break  

        if event == 'View Balance':
            sg.popup(f"Balance: ${functions.check_balance(functions.get_current_user())}", font='Helvetica 20')

        if event == 'Make Withdrawal':
            logged_in_page.close()
            withdrawal_window()
        
        if event == 'Make Deposit':
            logged_in_page.close()
            deposit_window()

        #if event == 'Check Transactions':

        if event == 'Terminate Account':
            functions.terminate_user(functions.logged_in_user(), functions.logged_in_password())
                
        if event == 'EXIT':
            logged_in_page.close()

    logged_in_page.close()