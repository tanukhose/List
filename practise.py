# from tkinter import *

# chat = Tk()

# chat.title('chat bot')

# chat.geometry('400x500')

# main_menu = Menu (chat)

# file_menu = Menu (chat)
# file_menu.add_command(label = 'new..')
# file_menu.add_command(label= 'Save As..')
# file_menu.add_command(label='Exit')



# help_menu = Menu (chat)
# help_menu.add_command(label = 'do u want help..')


# main_menu.add_cascade(label='File',menu= file_menu)
# main_menu.add_command(label='Edit')
# main_menu.add_command(label='Quit')
# main_menu.add_cascade(label='help',menu= help_menu)
# chat.config(menu=main_menu)




# chatWindow = Text(chat,bd=1,bg='red',width=50,height=8)
# chatWindow.place(x=6,y=6,height=385,width=370)

# messageWindow = Text(chat,bg='pink',width=30,height=4,)
# messageWindow.place(x=128,y=400,height=88,width=260)

# Button = Button(chat,text = 'send',bg = 'blue',activebackground = 'light blue', width = 12, height = 5,font=('Arial',20))
# Button.place(x=6, y=400, height = 88, width = 120)


# scrollbar = Scrollbar(chat,command=chatWindow.yview())
# scrollbar.place(x = 375, y = 5, height = 385)

# chat.mainloop()


































































# from tkinter import *

# root = Tk()



# root.title('chat bot')

# root.geometry('400x500')


# main_menu = Menu (root)

# chatWindow = Text(root,bd=1,bg='red',width=50,height=8)
# chatWindow.place(x=6,y=6,height=385,width=370)

# messageWindow = Text(root,bg='pink',width=30,height=4,)
# messageWindow.place(x=10,y=400,height=70,width=360)

# Button = Button(root,text = 'send',bg = 'blue',activebackground = 'light blue', width = 12, height = 5,font=('Arial',20))
# Button.place(x=250, y=400, height = 70, width = 120)


# scrollbar = Scrollbar(root,command=chatWindow.yview())
# scrollbar.place(x = 375, y = 5, height = 385)

# root.mainloop()







































# from tkinter import *

# root = Tk()



# root.title('chat bot')

# root.geometry('400x500')



# def send():
#     send="you :"+e.get()
#     txt.insert(END,"\n"+send)
#     if (e.get()=="hello"):
#         txt.insert(END,"\n"+"computer : hii")
#     elif (e.get()=="hi"):
#         txt.insert(END,"\n"+"computer : hello ")
#     elif (e.get()=="how are you"):
#         txt.insert(END,"\n"+"computer : fine and you ")
#     elif (e.get()=="i am also fine"):
#         txt.insert(END,"\n"+"computer : nice to hear  ")
#     else:
#         txt.insert(END,"\n"+"computer : sorry i did not get it  ")
#     e.delete(0,END)
# txt=Text(root)
# txt.grid(row=0,column=0,columnspan=2)
# e=Entry(root,width=100)
# send=Button(root,text="send",command=send).grid(row=1,column=1)
# e.grid(row=1,column=0)
# root.title('chatbox')
# root.mainloop()     