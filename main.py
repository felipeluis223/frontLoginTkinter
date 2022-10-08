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

# Header da interface:
heading = Label(frame, text="Sig in", fg=colorBlue, bg=colorBaseLight, font=(fontOrigin,23,"bold"))
heading.place(x=100,y=5)

# Input de "user":
user = Entry(frame, width=25, fg=colorBaseDark, border=0, bg=colorBaseLight, font=(fontOrigin, 11))
user.place(x=30, y=80)
user.insert(0, "Username")

Frame(frame, width=295, height=2, bg=colorBaseDark).place(x=25, y=107)


# Input de "password":
code = Entry(frame, width=25, fg=colorBaseDark, border=None, bg=colorBaseLight, font=(fontOrigin, 11))
code.place(x=30, y=150)
code.insert(0, "Password")

Frame(frame, width=295, height=2, bg=colorBaseDark).place(x=25, y=177)

# Botão de Login: 
Button(frame, width=39, pady=7, text="Sign in", bg=colorBlue, fg=colorBaseLight, border=0).place(x=35, y=204)



root.mainloop()
