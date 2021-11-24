from tkinter import *
import random

root = Tk()
root.title('papier/kamień/nożyce')
root.geometry("330x240")


random_number = random.randint(1, 3)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"



def rock():
    label_user_choice['text'] = "Rock"
    
    if computer_choice == "R":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = "Rock"
    elif computer_choice == "P":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = "Paper"
    elif computer_choice == "S":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = "Scissors"

def scissors():
    label_user_choice['text'] = "Scissors"
    
    if computer_choice == "S":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = "Scissors"
    elif computer_choice == "R":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = "Rock"
    elif computer_choice == "P":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = "Paper"

def paper():
    label_user_choice['text'] = "Paper"
    
    if computer_choice == "P":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = "Paper"
    elif computer_choice == "S":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = "Scissors"
    elif computer_choice == "R":
        label_result['text'] = "Player wins!"
        label_computer_choice['text'] = "Rock"

def reset():
    global computer_choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_choice = "R"
    elif random_number == 2:
        computer_choice = "P"
    elif random_number == 3:
        computer_choice = "S"
        
    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""  
    label_result['text'] = ""

label_title = Label(root, text='Rock/Paper/scissors', pady=12)
label_title.pack()

rock_button = Button(root, text = "Rock", padx=33.3, command= rock)
rock_button.pack()

paper_button = Button(root, text='paper', padx=33.3,command=paper )
paper_button.pack()

scissors_button = Button(root, text='scissors',padx=33.3, command= scissors)
scissors_button.pack()

label_computer_choice = Label(root, text="")
label_computer_choice.pack()

label_user_choice = Label(root, text="")
label_user_choice.pack()

label_result = Label(root, text="")
label_result.pack()

button_reset = Button(root, text="Reset",padx=25, command=reset)
button_reset.pack()

mainloop()
