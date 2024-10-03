
from dotenv import load_dotenv
import os

load_dotenv()

from Scripts import constants
from tkinter import *
import tkinter.font as tkFont
from Scripts import selenium_Funct

constants.username = os.getenv("USER_NAME")
constants.password = os.getenv("PASS")
constants.commaseparated = "Field1;Field2;field3"
constants.upto_page = 1


def start_automate(e3, e4, root):
    constants.username = os.getenv("USER_NAME")
    constants.password = os.getenv("PASS")
    constants.commaseparated = e3.get()
    constants.upto_page = e4.get()
    selenium_Funct.main()
    root.destroy()


def guibuild():
    root = Tk()
    root.configure(background='lightblue')

    root.geometry("1300x1100")
    root.title("LinkedIn Conection Bot")
    link = "https://github.com/prabaljainn/Linkedin_Connection_Bot.git"
    text = Text(root, height=1, padx=10, borderwidth=1, bg="cyan")
    text.insert(1.0, link)
    text.configure(state="normal")
    text.grid(row=0, column=0)
    text.configure(inactiveselectbackground=text.cget("selectbackground"))

    # canvas = Canvas(root, width=448, height=226)
    # canvas.grid(row=1, column=0, )
    # img = ImageTk.PhotoImage(Image.open("linkin.png"))
    # canvas.create_image(20, 20, anchor=NW, image=img)
    fontstyle = tkFont.Font(family="Ubuntu", size=18)
    
    labe_head = Label(root, text="LinkedIn Bot", fg="blue", font=fontstyle).grid(row=1, column=0)
    # labe_des = Label(root, text="A bot to Target Mass connections for Purpose", fg="blue", font=fontstyle).grid(row=2, column=0)
    
    # label_username = Label(root, text="Enter Username ").grid(row=4, column=0)
    # e1 = Entry(root, width=50, borderwidth=10, bg="white", fg='black')
    # e1.insert(0, constants.username)
    # e1.grid(row=6, column=0, columnspan=3, padx=10, pady=7)
    
    # label_password = Label(root, text="Enter Password").grid(row=8, column=0)
    # e2 = Entry(root, show="*", width=50, borderwidth=10, bg="white", fg='black')
    # e2.insert(0, constants.password)
    # e2.grid(row=10, column=0, columnspan=3, padx=10, pady=7)
    
    label = Label(root, text="Now Below enter your intrests separated by ;").grid(row=11, column=0)
    label2 = Label(root, text="for eg. to search for TCS , Accenture and Wipro Enter: ").grid(row=12, column=0)
    label3 = Label(root, text="TCS;Accenture;Wipro").grid(row=13, column=0)
    e3 = Entry(root, width=50, borderwidth=3, bg="white", fg='black')
    e3.insert(0, constants.commaseparated)
    e3.grid(row=15, column=0, columnspan=3, padx=10, pady=7)
    e4 = Entry(root, width=50, borderwidth=3, bg="white", fg='black')
    labelx = Label(root, text="How many pages you want to automate, for the First time use enter 1").grid(row=18,
                                                                                                          column=0)
    e4.insert(0, constants.upto_page)
    e4.grid(row=20, column=0, columnspan=3, padx=10, pady=7)
    label_username = Label(root, text="On the Same Directory Excel File will be Exported of Connected Users").grid(
        row=22, column=0)

    buttonsubmit = Button(root, text="Start The Automation!!", fg='blue', height=5, width=40,
                          command=lambda: start_automate(e3, e4, root)).grid(row=24,
                                                                                     columnspan=3,
                                                                                     column=0,
                                                                                     padx=10,
                                                                                     pady=7)

    link = "https://www.linkedin.com/in/prabaljainn"
    text = Text(root, height=1, padx=10, borderwidth=1, bg="cyan")
    text.insert(1.0, link)
    text.configure(state="normal")
    text.grid(row=30, column=0)
    text.configure(inactiveselectbackground=text.cget("selectbackground"))

    link = "https://github.com/prabaljainn"
    text = Text(root, height=1, padx=10, borderwidth=1, bg="cyan")
    text.insert(1.0, link)
    text.configure(state="normal")
    text.grid(row=32, column=0)
    text.configure(inactiveselectbackground=text.cget("selectbackground"))
    Button(root, text="Quit", command=root.destroy).grid(row=34)

    root.mainloop() 
