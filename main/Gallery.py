import os
from os import listdir
from os.path import splitext, join, exists

import PySimpleGUI as sg

extensions: [str] = ['.jpg', '.png', '.jpeg', '.gif']
current_index:int = 0
path = 'avatars/'
image_list = []
title = []
image = []

def is_image_file(filename):
    if exists(filename):
        if splitext(filename)[1] in extensions:
            return True
    return False

def update():
    global title, image, image_list
    title.update(os.path.splitext(os.path.basename(image_list[current_index]))[0])
    image.update(image_list[current_index])

def next_image():
    global current_index
    current_index = current_index+1 if current_index < len(image_list)-1 else 0
    update()

def prev_image():
    global current_index
    current_index = current_index-1 if current_index > 0 else len(image_list)-1
    update()

def display():
    global image_list, title, image
    image_list = [join(path, f) for f in listdir(path) if is_image_file(join(path, f))]
    if len(image_list) == 0:
        image_list = ['resources/empty.png']
    # Define layout
    title = sg.Text(os.path.splitext(os.path.basename(image_list[current_index]))[0],size=(25,1))
    image = sg.Image(image_list[current_index])
    layout = [[title],
    [image],
    [sg.Button('Previous',key='prev', tooltip='Previous Image'),sg.Button('Next',key='next', tooltip='next Image')]]
    # Create the Window
    window = sg.Window('Avatar Gallery', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:	# if user closes window or clicks cancel
            break
        if event == 'next':
            next_image()
        if event == 'prev':
            prev_image()
    window.close()