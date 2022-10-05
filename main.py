
#importing tkinter library
import tkinter as tk
#importing ttk module from Tkinter library
from tkinter import ttk
#importing font,colorchooser,filedialog,messagebox
from tkinter import font,colorchooser,filedialog,messagebox
#importing os
import os
#creating main_application window
main_application=tk.Tk()
#setting the geometry of main application window
main_application.geometry('1200x800')
#naming the title of main_window
main_application.title('D-Lite Text Editor ')
#giving icon to our D-Lite Text Editor
main_application.wm_iconbitmap('icon.ico')

########################main_menu#########################################

#creating main menu
main_menu=tk.Menu()
#file icon
#Creating icon object with the help of PhotoImage class tk
new_icon=tk.PhotoImage(file='icons2/new.png')
open_icon=tk.PhotoImage(file='icons2/open.png')
save_icon=tk.PhotoImage(file='icons2/save.png')
save_as_icon=tk.PhotoImage(file='icons2/save_as.png')
exit_icon=tk.PhotoImage(file='icons2/exit.png')
#creating file menu
#tearoff will prevent tearoff of dropdown menubar
file=tk.Menu(main_menu,tearoff=0)


#creating edit menu
edit=tk.Menu(main_menu,tearoff=False)
#Edit icon
cut_icon=tk.PhotoImage(file='icons2/cut.png')
paste_icon=tk.PhotoImage(file='icons2/paste.png')
copy_icon=tk.PhotoImage(file='icons2/copy.png')
clear_all_icon=tk.PhotoImage(file='icons2/clear_all.png')
find_icon=tk.PhotoImage(file='icons2/find.png')

#creating view menu
view=tk.Menu(main_menu,tearoff=False)
#creating icon objects for tool bar and status bar
tool_bar_icon=tk.PhotoImage(file='icons2/tool_bar.png')
status_bar_icon=tk.PhotoImage(file='icons2/status_bar.png')



#creating colour theme menu
color_theme=tk.Menu(main_menu,tearoff=False)
light_default_icon=tk.PhotoImage(file='icons2/light_default.png')
light_plus_icon = tk.PhotoImage(file='icons2/light_plus.png')
dark_icon = tk.PhotoImage(file='icons2/dark.png')
red_icon = tk.PhotoImage(file='icons2/red.png')
monokai_icon = tk.PhotoImage(file='icons2/monokai.png')
night_blue_icon = tk.PhotoImage(file='icons2/night_blue.png')
esthetique_icon = tk.PhotoImage(file='icons2/esthetique.png')
monalisa_icon = tk.PhotoImage(file='icons2/monalisa.png')
quilea_icon = tk.PhotoImage(file='icons2/quilea.png')
zubayr_icon = tk.PhotoImage(file='icons2/zubayr.png')






theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon,esthetique_icon,monalisa_icon,quilea_icon,zubayr_icon)

color_dict = {
    'Light Default ' : ('#000000', '#ffffff'),
    'Light Plus' : ('#474747', '#e0e0e0'),
    'Dark' : ('#c4c4c4', '#2d2d2d'),
    'Red' : ('#2d2d2d', '#ffe8e8'),
    'Monokai' : ('#d3b774', '#474747'),
    'Night Blue' :('#ededed', '#6b9dc2'),
    'Esthetique':('#091540','#F8F7F9'),
    'Monalisa':('#FF9090','#3F2F2F'),
    'Quilea':('#F2E8CF','#162719'),
    'Zubayr':('#262322','#F2E5D7')
}


#cascade
main_menu.add_cascade(label='File',menu=file)
main_menu.add_cascade(label='Edit',menu=edit)
main_menu.add_cascade(label='View',menu=view)
main_menu.add_cascade(label='Colour Theme',menu=color_theme)
#%%%%%%%%%%%%%%%%%%%%%%%end_main menu%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%




########################toolbar#########################################
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
#setting a default value in fontbox
font_box.current(font_tuple.index('Arial'))
#setting the geometry of font box
font_box.grid(row=0, column=0, padx=5)

#size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.current(4)
font_size.grid(row=0,column=1,padx=5)
#bold button
#Creating bold,italic,underline button
bold_icon=tk.PhotoImage(file='icons2/bold.png')
italic_icon=tk.PhotoImage(file='icons2/italic.png')
underline_icon=tk.PhotoImage(file='icons2/underline.png')


#creating bold,italic,underline button
bold_btn=ttk.Button(tool_bar,image=bold_icon)
italic_btn=ttk.Button(tool_bar,image=italic_icon)
underline_btn=ttk.Button(tool_bar,image=underline_icon)


#setting the geometry of bold,italic and underline button
bold_btn.grid(row=0,column=2,padx=5)
italic_btn.grid(row=0,column=3,padx=5)
underline_btn.grid(row=0,column=4,padx=5)

#font color button
font_color_icon=tk.PhotoImage(file='icons2/font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

#creating align left,right,center icon
align_left_icon=tk.PhotoImage(file="icons2/align_left.png")
align_center_icon=tk.PhotoImage(file="icons2/align_center.png")
align_right_icon=tk.PhotoImage(file="icons2/align_right.png")

#creating align left,center and right button
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
#setting the geometry of align left,center and right button
align_left_btn.grid(row=0,column=6,padx=5)
align_center_btn.grid(row=0,column=7,padx=5)
align_right_btn.grid(row=0,column=8,padx=5)












#%%%%%%%%%%%%%%%%%%%%%%%end toolbar%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


########################text editor#########################################
#creating texteditor object with the help of Text class of tk
text_editor=tk.Text(main_application)
#
text_editor.config(wrap='word',relief=tk.FLAT)
#scrollbar
scroll_bar=tk.Scrollbar(main_application)
#setting the geometry of scrollbar
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)

#setting the focus of text editor
text_editor.focus_set()

#setting the geometry for text editor
text_editor.pack(fil=tk.BOTH,expand=True)

# configuring of scrollbar with text editor
scroll_bar.config(command=text_editor.yview)
#setting the scrollbar to work horizontally in text editor
text_editor.config(yscrollcommand=scroll_bar.set)
#font family and font size functionality
current_font_family='Arial'
current_font_size=12
#
def change_font(event=None):
    global current_font_family
    current_font_family= font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_fontsize(event=None):
    global current_font_size
    current_font_size= size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))


#binding of combobox of font family and font size with their function
font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)

######button functionality

#bold button functionality
#text property
# default text property:-{'family': 'Courier New', 'size': 10, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
def change_bold():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family,current_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family,current_font_size,'normal'))

#adding the functionality in bold button with the help of configure
bold_btn.configure(command=change_bold)

#italic button functionality
def change_italic():
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family,current_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family,current_font_size,'roman'))
#adding the functionality in italic button with the help of configure
italic_btn.configure(command=change_italic)




#underline button functionality
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))


# adding the functionality in underline button with the help of configure
underline_btn.configure(command=change_underline)

###font color functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

#binding font color with the functionality via change_font_color
font_color_btn.configure(command=change_font_color)

###align functionality

def align_left():
    #text content will store all the words written
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    #it will delete all the text content
    text_editor.delete(1.0,tk.END)
    #now inserting the text content in the left
    text_editor.insert(tk.INSERT,text_content,'left')

#adding functionality in align left button via align left function
align_left_btn.configure(command=align_left)

##align right functionality
def align_center():
    #text content will store all the words written
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    #it will delete all the text content
    text_editor.delete(1.0,tk.END)
    #now inserting the text content in the center
    text_editor.insert(tk.INSERT,text_content,'center')

#adding functionality in align left button via align_center function
align_center_btn.configure(command=align_center)

##align right functionality
def align_right():
    #text content will store all the words written
    text_content=text_editor.get(1.0,'end')
    #it will congigure the text content to the right
    text_editor.tag_config('right',justify=tk.RIGHT)
    #it will delete all the text content
    text_editor.delete(1.0,tk.END)
    #now inserting the text content in the right
    text_editor.insert(tk.INSERT,text_content,'right')


#adding functionality in align left button via align right function
align_right_btn.configure(command=align_right)











#setting the  default text editor font family and size
text_editor.configure(font=('Arial,12'))

        #%%%%%%%%%%%%%%%%%%%%%%%end text editor%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

########################main status bar#########################################
status_bar=ttk.Label(main_application,text="Status Bar")
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        #it will check that there is achange in text content or not
        words=len(text_editor.get(1.0,'end-1c').split())#1-c will help not to count the new line character
        #replace method will replace space bw words
        characters=len(text_editor.get(1.0,'end-1c').replace(' ',""))#it will count the characters
        #it will configure the status bar with the text editor
        status_bar.config(text=f"Characters: {characters} Words :{words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)



#%%%%%%%%%%%%%%%%%%%%%%%end_main  status bar%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

########################main_menu functionality#########################################
#every file has a url and if url is empty it means that file do note xists

#new file functionality
url='' ###url variable
def new_file(event=None):
    global url
    url = ''
    text_editor.delete(1.0, tk.END)

## file commands
file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)



##open functonality
# filedailog will help to open the file
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
    try:
        with open(url, 'r') as fr:
            text_editor.delete(1.0, tk.END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_application.title(os.path.basename(url))

file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

##open functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
             url=filedialog.asksaveasfile(mode='w',defaultextension =".txt",filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
             content2=text_editor.get(1.0,tk.END)
             url.write(content2)
             url.close()
    except:
        return


file.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator="Ctrl+S",command=save_file)


##save as functionality
def save_as(event=None):
    global url
    try:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt',filetypes=(("Text File","*.txt"),("All files","*.*")))
        url.write(content)
        url.close()
    except:
        return

file.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+S",command=save_as)

##exit functionality
def exit_func(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2 = str(text_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return
file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)
def find_func(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match', '1.0', tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f"{start_pos}+{len(word)}c"
                text_editor.tag_add('match',start_pos,end_pos)
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0, tk.END)
        text_editor.insert(1.0, new_content)

    #creating toplevel window with the help of Toplevel class of tk
    find_dialogue=tk.Toplevel()
    #setting the geometry of toplevel window
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    #making sure that toplevel window will not be resized
    find_dialogue.resizable(0,0)
    ##creating label frame on topllevel window
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)
    ## creating label on label frame
    text_find_label=ttk.Label(find_frame,text="Find: ")
    text_replace_label=ttk.Label(find_frame,text="Replace")
    ##entryboxes
    find_input=ttk.Entry(find_frame,width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    #button
    find_button = ttk.Button(find_frame, text='Find', command=find)
    replace_button = ttk.Button(find_frame, text='Replace', command=replace)

    ##label grid
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)
    ###entrybox grid
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1, column=1,padx=4,pady=4)
    ## button grid
    find_button.grid(row=2, column=0, padx=8, pady=4)
    replace_button.grid(row=2, column=1, padx=8, pady=4)

    find_dialogue.mainloop()


#Adding commands in file_menu
#compound  argument will prevent overlapping of icon and dropdown menu
#accelerator argument will provide shortcut
#commands in edit menu
edit.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator="Ctrl+C",command=lambda:text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator="Ctrl+V",command=lambda:text_editor.event_generate("<Control v>"))
edit.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator="Ctrl+X",command=lambda:text_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator="Ctrl+Alt+X",command=lambda:text_editor.delete(1.0,tk.END))
edit.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator="Ctrl+F",command=find_func)

#Adding Checkbutton on view for status bar and tool bar
show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_statusbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else :
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        text_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar = True



def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else :
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar = True








view.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=False,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar )
view.add_checkbutton(label='Status Bar',onvalue=True,offvalue=False,variable=show_statusbar,image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

#color theme
def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)
count = 0
for i in color_dict:
    color_theme.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
    count += 1




#%%%%%%%%%%%%%%%%%%%%%%%end_main menu functionality%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#### bind shortcut keys
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as)
main_application.bind("<Control-q>", exit_func)
main_application.bind("<Control-f>", find_func)


#setting the main_menu using config
main_application.config(menu=main_menu)
#Entering the main_event loop
main_application.mainloop()

