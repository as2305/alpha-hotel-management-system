from customtkinter import *
import sqlite3 as sq


app = CTk()
app.geometry("500x400")
app.title("Alpha HMS")
app.attributes('-fullscreen', True)


'''def hide():
    register.place()

    def load_main():
    dialog = CTkInputDialog(text="Create UserID. DO NOT ENTER SPACE OR SPECIAL CHARACTERS", title="Register")
    login = dialog.get_input()
    global login_id
    login_id = login'''

def hide_everything():
    login.place_forget()
    login_entry.place_forget()
    label.place_forget()
    
def show_new():
    label2.place(relx=0.5, rely=0.3, anchor="center")
    
    
def login():
    database_name = login_entry.get()
    con = sq.connect(database_name+".db")
    global cur
    cur = con.cursor()
    hide_everything()
    show_new()
    create_tables()
    
def create_tables():
    hotel_info = """ CREATE TABLE INFO(Name VARCHAR(200) NOT NULL)"""
    cur.execute(hotel_info)
    
login_entry = CTkEntry(master=app, placeholder_text="UserID")
label = CTkLabel(master=app, text="Alpha Hotel Management System", font=("Arial", 20))
login = CTkButton(master=app, text="Login/Register", command=login)
label2 = CTkLabel(master=app, text="Welcome!")


login_entry.place(relx=0.5, rely=0.5, anchor="center")
login.place(relx=0.5, rely=0.6, anchor="center")
label.place(relx=0.5, rely=0.3, anchor="center") 






app.mainloop()