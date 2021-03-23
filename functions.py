import os

file_users = 'accountfile.txt'
logged_in_user = []
logged_in_password = []

def get_current_user():
    u = str(logged_in_user[-1])
    return u

def get_current_password():
    p = str(logged_in_password[-1])
    return p

def terminate_user(user, password):
    os.remove(str(user) + 'profile.txt')
    os.remove(str(user) + 'transactions.txt')
    with open(file_users, "r") as f: # löser inn alla rader ur accountfile.txt
        lines = f.readlines()
    with open(file_users, "w") as f:#skriver in alla rader förutom  'if line.strip("\n") != str(user) + ' ' + str(password):'
        for line in lines:
            if line.strip("\n") != str(user) + ' ' + str(password):
                f.write(line)

def check_balance(username):
    with open(username + 'profile.txt', 'r') as f:
        danyboi = f.readline().split(' ')
        return int(danyboi[-1])

def withdrawal(username, password, minus):
    with open(username + 'profile.txt', 'r') as f:
        dankyboi = f.readline().split(' ')
        new = int(dankyboi[2]) - minus
    with open(username + 'profile.txt', 'w+') as f:
        f.truncate()
        f.write(username)
        f.write(' ')
        f.write(password)
        f.write(' ')
        f.write(str(new))

def deposit(username, password, plus):
    with open(username + 'profile.txt', 'r') as f:
        dankyboi = f.readline().split(' ')
        new = int(dankyboi[-1]) + plus
        with open(username + 'profile.txt', 'w+') as f:
            f.truncate()
            f.write(username)
            f.write(' ')
            f.write(password)
            f.write(' ')
            f.write(str(new))

def login(username, password):
    print('To login please input your credentials')
    logged_in_user.append(username)  # appendar username till logged_in_user så det kan användar i funktionerna sedan
    logged_in_password.append(password)  # appendar passwored till logged_in_password så det kan användar i funktionerna sedan
    for line in open(file_users, "r").readlines(): # löser igenom alla rader i accountfile.txt och letar efter match
        login_info = line.split()
        if username == login_info[0] and password == login_info[1]: # returnar true om båda är sanna
            print("LOGGED IN AS '{}'".format(username)) # låter användaren veta att dom loggats in
            return True
    print("LOGIN FAIL") # ifall username och password inte finns/ matchar
    return False

def register(username, password):
    print('Input credentials to register account: ')
    with open(username + 'transactions.txt', 'a+') as f: # skriver ner en balance på 1000 till att börja i transacions filen
        f.write('Balance $1000\n')
    with open(username + 'profile.txt', 'w+') as f: # skriver användare info i profile filen
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write(" ")
        f.write('1000')
    with open(file_users, "a") as f: # skriver till alla username och password som registreras till accountfile.txt som login funktionen använder
        f.write(username)
        f.write(" ")
        f.write(password)
        f.write("\n")
        f.close()
    print(username, password)