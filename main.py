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

# Tipo da fontes:
fontOrigin = "Microsoft YaHei UI Light"

# Imagem de fundo:
img = PhotoImage(file="./imgs/login.png")
Label(root, image = img, bg=colorBaseLight).place(x=50, y=50)

# Container do Login:
frame = Frame(root, width=350, height=350, bg=colorBaseLight)
frame.place(x=480, y=70)

# Header da interface:
heading = Label(frame, text="Sig in", fg="#57a1f8", bg=colorBaseLight, font=(fontOrigin,23,"bold"))
heading.place(x=100,y=5)

user = Entry(frame, width=25, fg="#000000", border=2, bg=colorBaseLight, font=(fontOrigin, 11))
user.place(x=30, y=80)


root.mainloop()
