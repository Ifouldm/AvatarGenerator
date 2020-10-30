import os
import PySimpleGUI as sg
import json
import AvatarCreator
import Gallery

# Get users from JSON File
def get_users():
    fileloc = 'resources/users.json'
    userfile = open(fileloc)
    db = json.load(userfile)
    userfile.close()
    return db.get('Users')

# Produce GUI elements based on current user
def userrow(user):
    username = user.get('username')
    imexists = os.path.exists('avatars/'+username+'.png')
    row = [sg.Text(username), sg.Checkbox('', default= imexists, key=username)]
    return row

def get_selected_users():
    selected_userlist = []
    for usertext, usercb in usercheckboxs:
        selected_userlist.append(usertext.Get())
    return selected_userlist

def select_all_action():
     for _, cb in usercheckboxs:
         cb.update(value=select_all_checkbox.get())

def all_selected():
    for _, cb in usercheckboxs:
        if not cb.get:
            return False
    return True

sg.theme('GreenMono')
usercheckboxs = [userrow(username) for username in get_users()]
select_all_checkbox = sg.Checkbox('Select All',key='select_all',enable_events=True, default=all_selected())

# Main window Layout
layout = [ [sg.Text('Please select users to create avatars for.')],
            [select_all_checkbox],
            [sg.Frame('Users', layout=usercheckboxs)],
            [sg.Button('Ok'), sg.Button('Cancel')] ]
# Create the Window
window = sg.Window('Avatar Creator', layout)
# Events loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    if event == 'Ok':
        AvatarCreator.create_avatars(get_selected_users())
        Gallery.display()
        window.close()
    if event == 'select_all':
        select_all_action()

window.close()