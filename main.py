import string
from random import randint, choice
from tkinter import *


##########################################################################################

def generate_password():
    size_coming = password_size_entry.get()

    if int(size_coming) >= 6:
        password_min = int(size_coming)
        password_max = int(size_coming) + 1
    else:
        password_min = 6
        password_max = 15

    all_chars = string.ascii_letters + string.punctuation + string.digits
    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)


##########################################################################################

window = Tk()
window.title("Password generator")
# window.geometry("720x480")
window.config(background="white", pady=30, padx=30)

##########################################################################################

# main frames
width = 720 / 2
height = 480
left_frame = Frame(window, width=width, height=height, bg="white")
right_frame = Frame(window, width=width, height=height, bg="white")

##########################################################################################
# left frame

# image
image = PhotoImage(file="logo.png").zoom(20).subsample(32)
canvas = Canvas(left_frame, height=280, bg="white", bd=0, highlightthickness=0)
canvas.create_image(width / 2, 140, image=image)
canvas.pack(expand=YES)

# title
label_left_title = Label(left_frame, text="Password generator", font=("Helvetica", 20), bg="white", fg="black")
label_left_title.pack(expand=YES)

##########################################################################################
# right frame

# right internal frames
right_top_frame = Frame(right_frame, width=width, height=height / 2, bg="white")
right_bottom_frame = Frame(right_frame, width=width, height=height / 2, bg="white")

# password size label
password_size_label = Label(right_top_frame, text="Type the size of your password", font=("Helvetica", 15),
                            bg="white", fg="black")
password_size_label.grid(row=0, column=0)

# password size entry
password_size_entry = Entry(right_top_frame, font=("Helvetica", 20), bg="white", fg="black")
password_size_entry.grid(row=1, column=0)

# button
generate_button = Button(right_bottom_frame, text="Generate", font=("Helvetica", 20), bg="white", fg="black",
                         command=generate_password)
generate_button.pack(pady=10, expand=YES)

# entry
password_entry = Entry(right_bottom_frame, font=("Helvetica", 20), bg="white", fg="black")
password_entry.pack(pady=10)

##########################################################################################
# launch frames

right_top_frame.pack(expand=YES)
right_bottom_frame.pack(expand=YES)
left_frame.grid(row=0, column=0)
right_frame.grid(row=0, column=1)

window.mainloop()
