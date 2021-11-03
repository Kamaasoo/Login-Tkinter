# Login interface with Tkinter

#Imports 
from tkinter import * 
from tkinter import messagebox

# Functions
def mensagem(name, texto):
  messagebox.showinfo(name, texto)
  quit()

#  Window settings.
window = Tk()
window.title("Kmsz Login")

window['bg'] = "#1f211f"
window.geometry("210x200+290+290")

window.resizable(False, False)
window.iconbitmap("icon.ico")

# Widgets

#Cascades
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
 
menu.add_cascade(label = "Help",
  menu = filemenu
 )

filemenu.add_command(label='Exit',
  command = window.quit
  )

# Labels
label_user = Label(window,
  text = "User:",
  font = "Arial 12 italic",
  fg = "white",
  bg = "#1f211f"
).grid( row = 0, column = 0, sticky = W )

label_password = Label(window,
  text = "Password:",
  font = "Arial 12 italic",
  fg = "white",
  bg = "#1f211f"
).grid( row = 1, column = 0, sticky = W )

#Entrys 
entry_user = Entry(window).grid( row = 0, column = 1)
entry_password = Entry(window).grid ( row = 1, column = 1)

#Buttons
button_login = Button(window,
  text = "Login",
  font = "Arial 12 italic",
  command = lambda: mensagem("Login Access", "Successfully logged in")
  ).grid(row = 2, column = 1, sticky = E)

# Loop window
window.mainloop()
