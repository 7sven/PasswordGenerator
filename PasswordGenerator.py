import secrets
import string
import tkinter as tk
import re

pw_components = ""
pw_regex = ""
pw_components_number = 0

window = tk.Tk()
window.title("Password Generator")
window.geometry("600x400")

# gives you a password that has at least 1 of each boxes you clicked, it also checks for errors and tells the person
# whats wrong
def printpassword():
    global pw_components
    global pw_regex
    global pw_components_number
    passwordtocopy.delete("1.0", "end")
    inserted = length.get("1.0", "end")
    try:
        pw_length = int(inserted)
    except ValueError:
        passwordtocopy.insert("1.0", "Given password length was not an acceptable value")
        return
    if (len(pw_components) < 1):
        passwordtocopy.insert("1.0", "Given password components were empty")
        return
    if (pw_length < pw_components_number):
        passwordtocopy.insert("1.0", "Password length and used components not compatible")
        return
    pattern = re.compile(pw_regex)
    password = ""
    while (bool(pattern.search(password)) == False):
        password = ''.join(secrets.choice(pw_components) for _ in range(pw_length))

    passwordtocopy.insert("1.0", password)


# All add functions add the allowed content of a password
# meaning lower case, upper case, digits and punctuation such as ./( and so on
# they also include a regex element with a lookahead to see if at least one element is in the string
def addlower():
    global pw_components
    global pw_regex
    global pw_components_number
    pw_components_number += 1
    pw_regex = pw_regex + "(?=.*[a-z])"
    pw_components = pw_components + string.ascii_lowercase
    lower.configure(background="YELLOW")


def addupper():
    global pw_components
    global pw_regex
    global pw_components_number
    pw_components_number += 1
    pw_regex = pw_regex + "(?=.*[A-Z])"
    pw_components = pw_components + string.ascii_uppercase
    upper.configure(background="YELLOW")


def adddigits():
    global pw_components
    global pw_regex
    global pw_components_number
    pw_components_number += 1
    pw_regex = pw_regex + "(?=.*[0-9])"
    pw_components = pw_components + string.digits
    digits.configure(background="YELLOW")


def addpunctuations():
    global pw_components
    global pw_regex
    global pw_components_number
    pw_components_number += 1
    pw_regex = pw_regex + "(?=.*[" + string.punctuation + "])"
    pw_components = pw_components + string.punctuation
    punctuation.configure(background="YELLOW")


# clears all the pw_components and resets the button colour as well as deletes the last generated password
def reset():
    global pw_components
    global pw_components_number
    global pw_regex
    pw_regex = ""
    pw_components_number = 0
    pw_components = ""
    lower.configure(background="WHITE")
    upper.configure(background="WHITE")
    digits.configure(background="WHITE")
    punctuation.configure(background="WHITE")
    passwordtocopy.delete("1.0", "end")


# all the buttons, labels and text fields for the program
lower = tk.Button(text="lower case", command=addlower, width=10)
upper = tk.Button(text="upper case", command=addupper, width=10)
digits = tk.Button(text="digits", command=adddigits, width=10)
punctuation = tk.Button(text="punctuations", command=addpunctuations, width=10)
reset = tk.Button(text="reset", command=reset, width=10)
passwordtocopy = tk.Text(height=1, width=50)
pwlengthtxt = tk.Label(text="Type length of password below")
length = tk.Text(height=1, width=10)
showpw = tk.Button(text="get password", command=printpassword, width=10)

pwlengthtxt.pack()
length.pack()
lower.pack()
upper.pack()
digits.pack()
punctuation.pack()
reset.pack()
showpw.pack()
passwordtocopy.pack()

window.mainloop()
