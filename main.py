from tkinter import *
from tkinter import messagebox

# Configurações da interface:
root = Tk()
root.title("Login")
root.geometry("925x500+300+200")
root.configure(bg="#fff")
root.resizable(False, False)

# Paleta de cores da interface:
colorBaseLight = "#ffffff"
colorBaseDark = "#000000"
colorBlue = "#57a1f8"

# Tipo da fontes:
fontOrigin = "Microsoft YaHei UI Light"

# Imagem de fundo:
img = PhotoImage(file="./imgs/login.png")
Label(root, image = img, bg=colorBaseLight).place(x=50, y=50)

# Container do Login:
frame = Frame(root, width=350, height=350, bg=colorBaseLight)
frame.place(x=480, y=70)

# Função de Login:
def signIn():
    username = user.get()
    password = code.get()

    if username == "admin" and password == "123456":
        screen = Toplevel(root)
        screen.title("App")
        screen.geometry("925x500+325+200")
        screen.config(bg=colorBaseLight)
            
        Label(screen, text="Hello admin", bg="#fff", font=("Calibri(Body)", 50, "bold")).pack(expand=True)

        screen.mainloop()

    elif username != "admin" and password != "123456":
        messagebox.showerror("Invalid", "invalid username and password...")
    
    elif username != "admin":
        messagebox.showerror("Invalid", "invalid username...")

    elif password != "123456":
        messagebox.showerror("Invalid", "invalid password...")



# Header da interface:
heading = Label(frame, text="Sig in", fg=colorBlue, bg=colorBaseLight, font=(fontOrigin,23,"bold"))
heading.place(x=100,y=5)

# Função:
def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


# Input de "user":
user = Entry(frame, width=25, fg=colorBaseDark, border=0, bg=colorBaseLight, font=(fontOrigin, 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)
Frame(frame, width=295, height=2, bg=colorBaseDark).place(x=25, y=107)



# Função:
def on_enterPassword(e):
    code.delete(0, "end")

def on_leavePassword(e):
    password = code.get()
    if password == '':
        code.insert(0, 'Password')

# Input de "password":
code = Entry(frame, width=25, fg=colorBaseDark, border=None, bg=colorBaseLight, font=(fontOrigin, 11))
code.place(x=30, y=150)
code.insert(0, "Password")
code.bind("<FocusIn>", on_enterPassword)
code.bind("<FocusOut>", on_leavePassword)
Frame(frame, width=295, height=2, bg=colorBaseDark).place(x=25, y=177)

# Botão de Login: 
Button(frame, width=39, pady=7, text="Sign in", bg=colorBlue, fg=colorBaseLight, border=0, command=signIn).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", bg=colorBaseLight, fg=colorBaseDark, font=(fontOrigin, 9))
label.place(x=65, y=275)

signUp = Button(frame, width=6, text="Sign up", border=0, bg=colorBaseLight, cursor="hand2", fg=colorBlue)
signUp.place(x=215, y=270)

root.mainloop()
