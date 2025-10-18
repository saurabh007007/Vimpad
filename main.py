import tkinter as tk
from tkinter import ttk,font,colorchooser,filedialog,messagebox
import os
import traceback



main_application = tk.Tk()
main_application.geometry('1200x800')
main_application.title('VimPad - A Text Editor for Beginners by Saurabh Yadav')
main_icon=tk.PhotoImage(file='icons2/s.png')
main_application.iconphoto(False,main_icon)

########### main menu section##########
main_menu = tk.Menu()
#file icons
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')
#adding command for file manu
file=tk.Menu(main_menu,tearoff=False)

# edit icons
copy_icon=tk.PhotoImage(file='icons2/copy.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
cut_icon=tk.PhotoImage(file='icons2/cut.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')
#ADDING COMMAND FOR EDIT MENU
edit=tk.Menu(main_menu,tearoff=False)

# color theme icons
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon=tk.PhotoImage(file='icons2/light_plus.png')
dark_icon=tk.PhotoImage(file='icons2/dark.png')
red_icon=tk.PhotoImage(file='icons2/red.png')
monokai_icon=tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon=tk.PhotoImage(file='icons2/night_blue.png')
#ADDING COMMAND FOR COLOR THEME MENU
color_theme=tk.Menu(main_menu,tearoff=False)

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default':('#000000','#ffffff'),
    'Light Plus':('#474747','#e0e0e0'),
    'Dark':('#c4c4c4','#2d2d2d'),
    'Red':('#2d2d2d','#ffe8e8'),
    'Monokai':('#d3b774','#474747'),
    'Night Blue':('#ededed','#6b9dc2')
}

#view icons
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')
#ADDING COMMAND FOR VIEW MENU

view=tk.Menu(main_menu,tearoff=False)


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

#font box 
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
fonts_tuples=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=20,textvariable=font_family,state='readonly')
font_box['values']=fonts_tuples
font_box.current(fonts_tuples.index('Arial'))
font_box.grid(row=0,column=0,padx=5)

#size box -toolbar 
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81,2))
font_size.current(3)
font_size.grid(row=0,column=1,padx=5)

# bold button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)
# italic button
italic_icon=tk.PhotoImage(file='icons2/italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)
# underline button
underline_icon=tk.PhotoImage(file='icons2/underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# font color button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#align left button
align_left_icon=tk.PhotoImage(file='icons2/align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)
#align center button
align_center_icon=tk.PhotoImage(file='icons2/align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)
#align right button
align_right_icon=tk.PhotoImage(file='icons2/align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)


# ##############Toolbar menu ending ###########


########### Text Editor  menu section##########
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family config and editor config 
current_font_family='Arial'
current_font_size=14
def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))
    
def change_font_size(event=None):
    global current_font_size
    current_font_size=size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))
    
     
text_editor.configure(font=('Arial',14))

# bind commbox
font_box.bind("<<ComboboxSelected>>", change_font)
font_box.bind("<<ComboboxSelected>>", change_font_size)
# BUTTONS FUNCTINALITY LIKE ITALIC ETC
#bold button functionality 
def chnage_to_bold(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.config(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

bold_btn.config(command=chnage_to_bold)
#italic button configuration
def chnage_to_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.config(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.config(font=(current_font_family,current_font_size,'roman'))
italic_btn.config(command=chnage_to_italic)

# underline functionality configuration

def change_to_underline():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.config(font=(current_font_family,current_font_size,'underline'))
    if text_property.actual()['underline']==1:
        text_editor.config(font=(current_font_family,current_font_size,'normal'))

underline_btn.config(command=change_to_underline)

# font color functionality 

def chnage_font_color():
    color_var=tk.colorchooser.askcolor()
    # print(color_var)
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=chnage_font_color)

# Align ments functionality 

# ALIGN LEFT 
def align_left():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)
# align right ]
def align_right():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)


# align center 
def align_center():
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,'end')
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

# ##############Text Editor  menu ending ###########



########### Status Bar  menu section##########

status_bar=ttk.Label(main_application,text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_change=False
def change_status_bar(even=None):
    global text_change
    if text_editor.edit_modified():
        text_change=True
        words=len(text_editor.get(1.0,'end-1c').split())
        charcters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Words:{words} Characters:{charcters}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>',change_status_bar)


# ##############Status Bar  menu ending ###########


########### Main menu Functionality##########
url =''
# new file functionality

def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)
    status_bar.config(text='New File Created')
file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

# file.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)
# oepn file functionality 

def open_file(event=None):
    global url 
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text File','*.txt'),('All files','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
        status_bar.config(text=os.path.basename(url))
    except FileNotFoundError:
        return 
    except:
        return
    # main_application.title(os.path.basename(url))
    
    
file.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)

# file commands
def save_file(event=None):
    global url
    try:
        if url:
            content=text_editor.get(1.0,tk.END)
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
            status_bar.config(text='File Saved')
        else:
            url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
            status_bar.config(text='File Saved')
    except:
        return
    
    
file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

# save as file functionality 
def save_as_file(event=None):
    global url 
    try:
        content=text_editor.get(1.0,tk.END)
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
        url.write(content)
        url.close()
        status_bar.config(text='File Saved')
    except:
        return 
    # main_application.title(os.path.basename(url))
file.add_command(label='Save As',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)
#exit functionality 
def exit_func(event=None):
    global url,text_change
    try:
        if text_change:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0,tk.END)
                    with open(url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                    main_application.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(('Text File','*.txt'),('All files','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)
# find functionality 
def find_func(event=None):
    #find function 
    def find():
        word=find_input.get().replace(' ','')
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
                
        
    # replace fundtion 
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
    
    find_dialog=tk.Toplevel()
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0,0)
    
    #frame 
    find_frame=ttk.Labelframe(find_dialog,text='Find/Replace')
    find_frame.pack(pady=20)
    
    #label 
    text_find_level=ttk.Label(find_frame,text='Find: ')
    text_replace_label=ttk.Label(find_frame,text='Replace')
    #entry boxes
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    
    #button 
    find_button=ttk.Button(find_frame,text='Find',command=find)
    replace_button=ttk.Button(find_frame,text='Replace',command=replace)
    
    #lable grid 
    text_find_level.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=2,column=1,padx=4,pady=4)
    #grid entry boxes
    find_input.grid(row=0,column=1,padx=4,pady=4)
    
    #replace input grid 
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    
    #grid button find
    find_button.grid(row=2,column=0,padx=4,pady=4)
    replace_button.grid(row=2,column=1,padx=4,pady=4)
    find_dialog.mainloop()

# edit commands 
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+X',command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)

# view check buttons /commands
show_statusbar=tk.BooleanVar()
show_toolbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar.set(True)

def hide_toolbar(event=None):
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True
        

def hide_statusbar(event=None):
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True
    
    

view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

# color theme radio buttons/commands
# chnage theme 
def change_theme(event=None):
    
    chooseen_theme=theme_choice.get()
    color_tuple=color_dict.get(chooseen_theme)
    # print(color_tuple)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,fg=fg_color)
    
    
    


count =0
for i in color_dict:
    color_theme.add_radiobutton(label=i,image=color_icons[count],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    count+=1



# ############## Main  menu Functionality ending ###########





main_application.configure(menu=main_menu)

main_application.mainloop()