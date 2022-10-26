from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import Notes.notes as modelNotes
import root as root

class ActionsNotes:

    root.root
    root.root.minsize(500,500)
    root.root.title("Notes tkinter")
    root.root.resizable(0,0)
    root.root.grid_columnconfigure(1, weight=1)
    root.root.grid_rowconfigure(0, weight=0)
    root.root.config(bg="#2F83BA")

    title = StringVar()
    description = StringVar()
    products=[]

    #!definir campos de pantallas add
    createNoteDescEntry = Text(root.createNoteFrame)
    updateNoteDescEntry = Text(root.updateNoteFrame2)
    productsBox = ttk.Treeview(root.showNoteFrame,height=19, columns=("#0","#1"), selectmode="extended")

    def createNote(self,user):
        #* Create Note
        
        createNoteName = Label(root.createNoteFrame,text="Name")
        createNoteName.grid(row=1, column=0,sticky=W)
        createNoteNameEntry = Entry(root.createNoteFrame,textvariable=ActionsNotes.title)
        createNoteNameEntry.grid(row=1, column=1,sticky=W)

        createNoteDesc = Label(root.createNoteFrame,text="Description")
        createNoteDesc.grid(row=2, column=0, sticky=NW)

        ActionsNotes.createNoteDescEntry.grid(row=2, column=1)

        botonEnterNotes=Button(root.createNoteFrame,text="Enter",relief="groove",command=lambda:ActionsNotes().createNoteMethod(user))
        botonEnterNotesBack=Button(root.createNoteFrame,text="Back",relief="groove",command=lambda:ActionsNotes().menu(user))

        
        #*
        createLabel = Label(root.root,text="Create Notes")
        createLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        createLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.createNoteFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.createNoteFrame.config(bg="#2F83BA")

        createNoteName.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        createNoteNameEntry.config(width=32,font=("arial",13),bg="#fff",fg="#000")

        createNoteDesc.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        ActionsNotes.createNoteDescEntry.config(width=25,height=5,padx=5,font=("arial",15),bg="#FFF",fg="#000")

        botonEnterNotes.grid(row=5,column=1,sticky=E,padx=5,pady=10)
        botonEnterNotes.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)
            
        botonEnterNotesBack.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonEnterNotesBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def updateNote(self,user):
        #* Create Note
        updateNoteName = Label(root.updateNoteFrame,text="Name")
        updateNoteName.grid(row=1, column=0,sticky=W)
        updateNoteNameEntry = Entry(root.updateNoteFrame,textvariable=ActionsNotes.title)
        updateNoteNameEntry.grid(row=1, column=1,sticky=W)

        botonEnterNotes=Button(root.updateNoteFrame,text="Next",relief="groove",command=lambda:ActionsNotes().updateNoteStep2(user))
        botonEnterNotesBack=Button(root.updateNoteFrame,text="Back",relief="groove",command=lambda:ActionsNotes().menu(user))

        #*
        updateLabel = Label(root.root,text="update Notes")
        updateLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        updateLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.updateNoteFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.updateNoteFrame.config(bg="#2F83BA")

        updateNoteName.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        updateNoteNameEntry.config(width=32,font=("arial",13),bg="#fff",fg="#000")

        botonEnterNotes.grid(row=5,column=1,sticky=E,padx=5,pady=10)
        botonEnterNotes.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)
            
        botonEnterNotesBack.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonEnterNotesBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def updateNoteStep2(self, user):

        updateNoteDesc = Label(root.updateNoteFrame2,text="New Description")
        updateNoteDesc.grid(row=2, column=0, sticky=NW)

        ActionsNotes.updateNoteDescEntry.grid(row=2, column=1)

        botonEnterNotes=Button(root.updateNoteFrame2,text="Enter",relief="groove",command=lambda:ActionsNotes().updateNoteMethod(user))
        botonEnterNotesBack=Button(root.updateNoteFrame2,text="Back",relief="groove",command=lambda:ActionsNotes().menu(user))

        updateLabel = Label(root.root,text="update Notes")
        updateLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        updateLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.updateNoteFrame2.grid(row=1,column=0, columnspan=2, sticky=N)
        root.updateNoteFrame2.config(bg="#2F83BA")

        updateNoteDesc.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        ActionsNotes.updateNoteDescEntry.config(width=25,height=5,padx=5,font=("arial",15),bg="#FFF",fg="#000")

        botonEnterNotes.grid(row=5,column=1,sticky=E,padx=5,pady=10)
        botonEnterNotes.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)
            
        botonEnterNotesBack.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonEnterNotesBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        root.menuFrame.grid_remove()
        root.updateNoteFrame.grid_remove()

        root.root.mainloop()

    def showNote(self,user):

        note = modelNotes.Note(user[0])
        notes = note.show()
        
        for notess in notes:
            ActionsNotes.productsBox.insert('',0,text=notess[1],values=(notess[2],notess[3]))
        

        ActionsNotes.productsBox.grid(row=1, column=0, columnspan=3)
        ActionsNotes.productsBox.heading("#0",text="Id", anchor=CENTER)
        ActionsNotes.productsBox.heading("#1",text="Titulo", anchor=CENTER)
        ActionsNotes.productsBox.heading("#2",text="Descripcion", anchor=W)
        ActionsNotes.productsBox.column("#0", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#1", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#2", stretch=NO, width=317)

        botonShowNotesBack=Button(root.showNoteFrame,text="Back",relief="groove",command=lambda:ActionsNotes().menu(user))
        
        #*
        showLabel = Label(root.root,text="Show Notes")
        showLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        showLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.showNoteFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.showNoteFrame.config(bg="#2F83BA")
            
        botonShowNotesBack.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonShowNotesBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)


        root.menuFrame.grid_remove()

        root.root.mainloop()
        
    def deleteNote(self,user):
        
        #* Create Note
        
        deleteNoteName = Label(root.deleteNoteFrame,text="Name")
        deleteNoteName.grid(row=1, column=0,sticky=W)
        deleteNoteNameEntry = Entry(root.deleteNoteFrame,textvariable=ActionsNotes.title)
        deleteNoteNameEntry.grid(row=1, column=1,sticky=W)

        botonEnterNotes=Button(root.deleteNoteFrame,text="Delete",relief="groove",command=lambda:ActionsNotes().deleteNoteMethod(user))
        botonEnterNotesBack=Button(root.deleteNoteFrame,text="Back",relief="groove",command=lambda:ActionsNotes().menu(user))

        
        #*
        deleteLabel = Label(root.root,text="Delete Notes")
        deleteLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        deleteLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.deleteNoteFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.deleteNoteFrame.config(bg="#2F83BA")

        deleteNoteName.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        deleteNoteNameEntry.config(width=32,font=("arial",13),bg="#fff",fg="#000")

        botonEnterNotes.grid(row=5,column=1,sticky=E,padx=5,pady=10)
        botonEnterNotes.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)
            
        botonEnterNotesBack.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonEnterNotesBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def menu(self,user):
        #*Remove all record
        for record in ActionsNotes.productsBox.get_children():
            ActionsNotes.productsBox.delete(record)

        #* Menu de opciones

        botonCreate = Button(root.menuFrame,text="Create",relief="groove",command=lambda:ActionsNotes().createNote(user))
        botonShow = Button(root.menuFrame,text="Show",relief="groove",command=lambda:ActionsNotes().showNote(user))
        botonUpdate = Button(root.menuFrame,text="Update",relief="groove",command=lambda:ActionsNotes().updateNote(user))
        botonDelete = Button(root.menuFrame,text="Delete",relief="groove",command=lambda:ActionsNotes().deleteNote(user))
        botonExit = Button(root.menuFrame,text="Exit",relief="groove",command=exit)

        #*
        menuLabel = Label(root.root,text="MENU")
        menuLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)
        menuLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)

        root.menuFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.menuFrame.config(bg="#2F83BA")

        botonCreate.grid(row=1,column=0,sticky=E,padx=5,pady=10)
        botonCreate.config(width=10,height=2 ,bg="#BEE2FA",fg="#000",font=("arial",20),pady=3,padx=7)
        
        botonShow.grid(row=1,column=1,sticky=E,padx=5,pady=10)
        botonShow.config(width=10,height=2 ,bg="#BEE2FA",fg="#000",font=("arial",20),pady=3,padx=7)
        
        botonUpdate.grid(row=2,column=0,sticky=E,padx=5,pady=10)
        botonUpdate.config(width=10,height=2 ,bg="#BEE2FA",fg="#000",font=("arial",20),pady=3,padx=7)
        
        botonDelete.grid(row=2,column=1,sticky=E,padx=5,pady=10)
        botonDelete.config(width=10,height=2 ,bg="#BEE2FA",fg="#000",font=("arial",20),pady=3,padx=7)

        botonExit.grid(row=4,column=1,sticky=E,padx=5,pady=10)
        botonExit.config(width=10,height=2 ,bg="#BEE2FA",fg="#000",font=("arial",20),pady=3,padx=7)

        root.createNoteFrame.grid_remove()
        root.showNoteFrame.grid_remove()
        root.updateNoteFrame.grid_remove()
        root.updateNoteFrame2.grid_remove()
        root.deleteNoteFrame.grid_remove()

        root.root.mainloop()

    def createNoteMethod(self, user):

        note = modelNotes.Note(user[0], ActionsNotes.title.get(), ActionsNotes.createNoteDescEntry.get("1.0","end-1c"))
        save = note.save()

        if (save[0]>=1):
            ActionsNotes.title.set("")
            ActionsNotes.createNoteDescEntry.delete("1.0",END)
            ActionsNotes().menu(user)
        else:
            MessageBox.showwarning("Alerta", "ERROR")
                
    def updateNoteMethod(self,user):
        note = modelNotes.Note(user[0], ActionsNotes.title.get(), ActionsNotes.updateNoteDescEntry.get("1.0","end-1c"))
        update = note.update()

        if (update[0]>=1):
            ActionsNotes.title.set("")
            ActionsNotes.updateNoteDescEntry.delete("1.0",END)
            ActionsNotes().menu(user)
        else:
            MessageBox.showwarning("Alerta", "ERROR")
    
    def deleteNoteMethod(self,user):
        note = modelNotes.Note(user[0],ActionsNotes.title.get())
        delete = note.delete()

        if (delete[0]>=1):
            ActionsNotes.title.set("")
            ActionsNotes.createNoteDescEntry.delete("1.0",END)
            ActionsNotes().menu(user)
        else:
            MessageBox.showwarning("Alerta", "ERROR")

