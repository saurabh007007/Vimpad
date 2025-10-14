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
#adding command for file manu
file=tk.Menu(main_menu,tearoff=False)
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N')
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O')
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S')
file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q')

# edit icons
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')
#ADDING COMMAND FOR EDIT MENU
edit=tk.Menu(main_menu,tearoff=False)
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C')
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V')
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X')
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X')
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F')


# color theme icons
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')
#ADDING COMMAND FOR COLOR THEME MENU
color_theme=tk.Menu(main_menu,tearoff=False)
color_theme.add_radiobutton(label='Light Default',image=light_default_icon,compound=tk.LEFT)
color_theme.add_radiobutton(label='Light Plus',image=light_plus_icon,compound=tk.LEFT)
color_theme.add_radiobutton(label='Dark',image=dark_icon,compound=tk.LEFT)
color_theme.add_radiobutton(label='Red',image=red_icon,compound=tk.LEFT)
color_theme.add_radiobutton(label='Monokai',image=monokai_icon,compound=tk.LEFT)
color_theme.add_radiobutton(label='Night Blue',image=night_blue_icon,compound=tk.LEFT)
#view icons
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')
#ADDING COMMAND FOR VIEW MENU

view=tk.Menu(main_menu,tearoff=False)
view.add_checkbutton(label='Tool Bar',image=tool_bar_icon,compound=tk.LEFT)
view.add_checkbutton(label='Status Bar',image=status_bar_icon,compound=tk.LEFT)

#icon of the about
about_icon=tk.PhotoImage(file='icons2/github.png')
# Command for the about menu 
about=tk.Menu(main_menu,tearoff=False)
about.add_command(label='Developed by Saurabh Yadav(saurabh007007)',image=about_icon,compound=tk.LEFT)

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