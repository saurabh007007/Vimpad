import tkinter as tk
from tkinter import ttk,font,colorchooser,filedialog,messagebox
import os
import traceback



main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('VimPad-A Text Editor for Beginners')

########### main menu section##########
main_menu = tk.Menu()
#file icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')

file=tk.Menu(main_menu,tearoff=False)
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')

edit=tk.Menu(main_menu,tearoff=False)
color_theme=tk.Menu(main_menu,tearoff=False)
view=tk.Menu(main_menu,tearoff=False)
about=tk.Menu(main_menu,tearoff=False)


#cascade

main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Color Theme',menu=color_theme)
main_menu.add_cascade(label='About',menu=about)


# ##############main menu ending ###########

########### Toolbar menu section##########

# ##############Toolbar menu ending ###########


########### Text Editor  menu section##########

# ##############Text Editor  menu ending ###########



########### Status Bar  menu section##########

# ##############Status Bar  menu ending ###########


########### Main menu Functionality##########

# ##############Main  menu Functionality ending ###########





main_application.configure(menu=main_menu)
main_application.mainloop()