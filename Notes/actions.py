from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import ttk
import Notes.notes as modelNotes
import root as root


class ActionsNotes:

    root.root
    root.root.minsize(1200, 800)
    root.root.title("Profesores")
    root.root.resizable(1, 0)
    root.root.grid_columnconfigure(1, weight=1)
    root.root.grid_rowconfigure(0, weight=0)
    root.root.config(bg="#2F83BA")

    Profesor = StringVar()
    AM = StringVar()
    AP = StringVar()
    RFC = StringVar()
    Sueldo = StringVar()
    Materias = StringVar()
    Sexo = StringVar()
    TelC = StringVar()
    TelCasa = StringVar()
    Pasatiempos = StringVar()
    NombreCreador = StringVar()
    TesisAM = StringVar()
    TesisAP = StringVar()
    TesisNombre = StringVar()
    products = []

    #!definir campos de pantallas add
    createNoteDescEntry = Text(root.createNoteFrame)
    updateNoteDescEntry = Text(root.updateNoteFrame2)
    productsBox = ttk.Treeview(root.showNoteFrame, height=19, columns=(
        "#0", "#1","#2","#3","#4","#5","#6","#7","#8","#9","#10","#11"), selectmode="extended")

    def createNote(self):
        # * Create Note

        createProfesorName = Label(root.createNoteFrame, text="Nombre")
        createProfesorName.grid(row=1, column=0, sticky=W)
        createProfesorNameEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.Profesor)
        createProfesorNameEntry.grid(row=1, column=1, sticky=W)

        createAM = Label(root.createNoteFrame, text="Apellido Materno")
        createAM.grid(row=2, column=0, sticky=W)
        createAMEntry = Entry(root.createNoteFrame,
                              textvariable=ActionsNotes.AM)
        createAMEntry.grid(row=2, column=1, sticky=W)

        createAP = Label(root.createNoteFrame, text="Apellido Paterno")
        createAP.grid(row=3, column=0, sticky=W)
        createAPEntry = Entry(root.createNoteFrame,
                              textvariable=ActionsNotes.AP)
        createAPEntry.grid(row=3, column=1, sticky=W)

        createRFC = Label(root.createNoteFrame, text="RFC")
        createRFC.grid(row=4, column=0, sticky=W)
        createRFCEntry = Entry(root.createNoteFrame,
                               textvariable=ActionsNotes.RFC)
        createRFCEntry.grid(row=4, column=1, sticky=W)

        createSueldo = Label(root.createNoteFrame, text="Sueldo")
        createSueldo.grid(row=5, column=0, sticky=W)
        createSueldoEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.Sueldo)
        createSueldoEntry.grid(row=5, column=1, sticky=W)

        createSexo = Label(root.createNoteFrame, text="Sexo")
        createSexo.grid(row=6, column=0, sticky=W)
        createSexoEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.Sexo)
        createSexoEntry.grid(row=6, column=1, sticky=W)

        createMaterias = Label(root.createNoteFrame, text="Materias")
        createMaterias.grid(row=7, column=0, sticky=W)
        createMateriasEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.Materias)
        createMateriasEntry.grid(row=7, column=1, sticky=W)

        createTelC = Label(root.createNoteFrame, text="Telefono Celular")
        createTelC.grid(row=8, column=0, sticky=W)
        createTelCEntry = Entry(root.createNoteFrame,
                                textvariable=ActionsNotes.TelC)
        createTelCEntry.grid(row=8, column=1, sticky=W)

        createTelCasa = Label(root.createNoteFrame, text="Telefono Casa")
        createTelCasa.grid(row=9, column=0, sticky=W)
        createTelCasaEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.TelCasa)
        createTelCasaEntry.grid(row=9, column=1, sticky=W)

        createPasatiempo = Label(root.createNoteFrame, text="Pasatiempos")
        createPasatiempo.grid(row=10, column=0, sticky=W)
        createPasatiempoEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.Pasatiempos)
        createPasatiempoEntry.grid(row=10, column=1, sticky=W)

        createTesistas = Label(root.createNoteFrame, text="Tesistas")
        createTesistas.grid(row=11, column=1, sticky=W)

        createTesisNombreCreador = Label(root.createNoteFrame, text="Nombre")
        createTesisNombreCreador.grid(row=12, column=0, sticky=W)
        createTesisNombreCreadorEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.NombreCreador)
        createTesisNombreCreadorEntry.grid(row=12, column=1, sticky=W)

        createTesisAM = Label(root.createNoteFrame, text="Apellido Materno")
        createTesisAM.grid(row=13, column=0, sticky=W)
        createTesisAMEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.TesisAM)
        createTesisAMEntry.grid(row=13, column=1, sticky=W)

        

        createTesisName = Label(root.createNoteFrame,
                                text="Nombre de la tesis")
        createTesisName.grid(row=14, column=0, sticky=W)
        createTesisNameEntry = Entry(
            root.createNoteFrame, textvariable=ActionsNotes.TesisNombre)
        createTesisNameEntry.grid(row=14, column=1, sticky=W)

        # createNoteDesc = Label(root.createNoteFrame,text="Description")
        # createNoteDesc.grid(row=2, column=0, sticky=NW)

        # ActionsNotes.createNoteDescEntry.grid(row=2, column=1)

        botonEnterNotes = Button(root.createNoteFrame, text="Enter",
                                 relief="groove", command=lambda: ActionsNotes().createNoteMethod())
        botonEnterNotesBack = Button(
            root.createNoteFrame, text="Back", relief="groove", command=lambda: ActionsNotes().menu())

        # *Estilos
        createLabel = Label(root.root, text="Create Notes")
        createLabel.config(fg="#fff", bg="#2F83BA",
                           font=("arial", 30), padx=20, pady=50)

        createLabel.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        root.createNoteFrame.grid(row=1, column=0, columnspan=2, sticky=N)
        root.createNoteFrame.config(bg="#2F83BA")

        createProfesorName.config(
            bg="#2F83BA", fg="#fff", height=1, font=("arial", 15), padx=7)
        createProfesorNameEntry.config(
            width=32, font=("arial", 13), bg="#fff", fg="#000")

        createAM.config(bg="#2F83BA", fg="#fff", height=1,
                        font=("arial", 15), padx=7)
        createAMEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createAP.config(bg="#2F83BA", fg="#fff", height=1,
                        font=("arial", 15), padx=7)
        createAPEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createRFC.config(bg="#2F83BA", fg="#fff", height=1,
                         font=("arial", 15), padx=7)
        createRFCEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createSueldo.config(bg="#2F83BA", fg="#fff",
                            height=1, font=("arial", 15), padx=7)
        createSueldoEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createSexo.config(bg="#2F83BA", fg="#fff",
                            height=1, font=("arial", 15), padx=7)
        createSexoEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createMaterias.config(bg="#2F83BA", fg="#fff",
                              height=1, font=("arial", 15), padx=7)
        createMateriasEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createTelC.config(bg="#2F83BA", fg="#fff", height=1,
                          font=("arial", 15), padx=7)
        createTelCEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createTelCasa.config(bg="#2F83BA", fg="#fff",
                             height=1, font=("arial", 15), padx=7)
        createTelCasaEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        createPasatiempo.config(bg="#2F83BA", fg="#fff",
                                height=1, font=("arial", 15), padx=7)
        createPasatiempoEntry.config(
            width=32, font=("arial", 13), bg="#fff", fg="#000")

        createTesistas.config(bg="#2F83BA", fg="#fff",
                              height=1, font=("arial", 15), padx=7)

        createTesisNombreCreador.config(
            bg="#2F83BA", fg="#fff", height=1, font=("arial", 15), padx=7)
        createTesisNombreCreadorEntry.config(
            width=32, font=("arial", 13), bg="#fff", fg="#000")

        createTesisAM.config(bg="#2F83BA", fg="#fff",
                             height=1, font=("arial", 15), padx=7)
        createTesisAMEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")


        createTesisName.config(bg="#2F83BA", fg="#fff",
                               height=1, font=("arial", 15), padx=7)
        createTesisNameEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        botonEnterNotes.grid(row=16, column=1, sticky=E, padx=5, pady=10)
        botonEnterNotes.config(width=10, bg="#BEE2FA",
                               fg="#000", font=("arial", 15), pady=3, padx=7)

        botonEnterNotesBack.grid(row=16, column=0, sticky=SW, padx=5, pady=10)
        botonEnterNotesBack.config(
            width=10, bg="#2F83BA", fg="#fff", font=("arial", 10), pady=3, padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def updateNote(self):
        # * Create Note
        updateNoteName = Label(root.updateNoteFrame, text="Name")
        updateNoteName.grid(row=1, column=0, sticky=W)
        updateNoteNameEntry = Entry(
            root.updateNoteFrame, textvariable=ActionsNotes.title)
        updateNoteNameEntry.grid(row=1, column=1, sticky=W)

        botonEnterNotes = Button(root.updateNoteFrame, text="Next",
                                 relief="groove", command=lambda: ActionsNotes().updateNoteStep2())
        botonEnterNotesBack = Button(
            root.updateNoteFrame, text="Back", relief="groove", command=lambda: ActionsNotes().menu())

        # *
        updateLabel = Label(root.root, text="update Notes")
        updateLabel.config(fg="#fff", bg="#2F83BA",
                           font=("arial", 30), padx=20, pady=50)

        updateLabel.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        root.updateNoteFrame.grid(row=1, column=0, columnspan=2, sticky=N)
        root.updateNoteFrame.config(bg="#2F83BA")

        updateNoteName.config(bg="#2F83BA", fg="#fff",
                              height=2, font=("arial", 15), padx=10)
        updateNoteNameEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        botonEnterNotes.grid(row=5, column=1, sticky=E, padx=5, pady=10)
        botonEnterNotes.config(width=10, bg="#BEE2FA",
                               fg="#000", font=("arial", 15), pady=3, padx=7)

        botonEnterNotesBack.grid(row=5, column=0, sticky=SW, padx=5, pady=10)
        botonEnterNotesBack.config(
            width=10, bg="#2F83BA", fg="#fff", font=("arial", 10), pady=3, padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def updateNoteStep2(self):

        updateNoteDesc = Label(root.updateNoteFrame2, text="New Description")
        updateNoteDesc.grid(row=2, column=0, sticky=NW)

        ActionsNotes.updateNoteDescEntry.grid(row=2, column=1)

        botonEnterNotes = Button(root.updateNoteFrame2, text="Enter",
                                 relief="groove", command=lambda: ActionsNotes().updateNoteMethod())
        botonEnterNotesBack = Button(
            root.updateNoteFrame2, text="Back", relief="groove", command=lambda: ActionsNotes().menu())

        updateLabel = Label(root.root, text="update Notes")
        updateLabel.config(fg="#fff", bg="#2F83BA",
                           font=("arial", 30), padx=20, pady=50)

        updateLabel.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        root.updateNoteFrame2.grid(row=1, column=0, columnspan=2, sticky=N)
        root.updateNoteFrame2.config(bg="#2F83BA")

        updateNoteDesc.config(bg="#2F83BA", fg="#fff",
                              height=2, font=("arial", 15), padx=10)
        ActionsNotes.updateNoteDescEntry.config(
            width=25, height=5, padx=5, font=("arial", 15), bg="#FFF", fg="#000")

        botonEnterNotes.grid(row=5, column=1, sticky=E, padx=5, pady=10)
        botonEnterNotes.config(width=10, bg="#BEE2FA",
                               fg="#000", font=("arial", 15), pady=3, padx=7)

        botonEnterNotesBack.grid(row=5, column=0, sticky=SW, padx=5, pady=10)
        botonEnterNotesBack.config(
            width=10, bg="#2F83BA", fg="#fff", font=("arial", 10), pady=3, padx=7)

        root.menuFrame.grid_remove()
        root.updateNoteFrame.grid_remove()

        root.root.mainloop()

    def showNote(self):

        note = modelNotes.Note([0])
        notes = note.show()
        
        for notess in notes:
            if(not str(notess['Telefonos']).find("casa")==-1): 
                notas = notess['Telefonos'].pop('casa')
            else:
                notas =""
            if('Tesis' in notess):
                tesis =notess['Tesis']
            else:
                tesis =notess['Tesistas']['Tesis']
                tesista = notess['Tesistas']['nombre']['pila']
                tesistaAP = notess['Tesistas']['nombre']['AP']
            ActionsNotes.productsBox.insert(
                '', 0, text=notess['_id'], values=(notess['Nombre']['pila'],notess['Nombre']['AM'],notess['Nombre']['AP'],
                            notess['RFC'],notess['Sexo'],notess['Materias'],notess['Telefonos']['celular'],
                            notas,notess['Pasatiempos'],tesis,tesista,tesistaAP))
        # ActionsNotes.productsBox.Treeview(height = 10, columns = ('#1','#2','#3','#4'))
        ActionsNotes.productsBox.grid(row=1, column=0, columnspan=5)
        ActionsNotes.productsBox.heading("#0", text="Id", anchor=CENTER)
        ActionsNotes.productsBox.heading("#1", text="Nombre", anchor=CENTER)
        ActionsNotes.productsBox.heading("#2", text="AM", anchor=CENTER)
        ActionsNotes.productsBox.heading("#3", text="AP", anchor=CENTER)
        ActionsNotes.productsBox.heading("#4", text="RFC", anchor=CENTER)
        ActionsNotes.productsBox.heading("#5", text="Sexo", anchor=CENTER)
        ActionsNotes.productsBox.heading("#6", text="Materias", anchor=CENTER)
        ActionsNotes.productsBox.heading("#7", text="Tefeno Celular", anchor=CENTER)
        ActionsNotes.productsBox.heading("#8", text="Tefeno Casa", anchor=W)
        ActionsNotes.productsBox.heading("#9", text="Pasatiempos", anchor=W)
        ActionsNotes.productsBox.heading("#10", text="Tesis Nombre", anchor=W)
        ActionsNotes.productsBox.heading("#11", text="Tesista", anchor=W)
        ActionsNotes.productsBox.heading("#12", text="Tesista AP", anchor=W)

        ActionsNotes.productsBox.column("#0", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#1", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#2", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#3", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#4", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#5", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#6", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#7", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#8", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#9", stretch=NO, width=200)
        ActionsNotes.productsBox.column("#10", stretch=NO, width=200)
        ActionsNotes.productsBox.column("#11", stretch=NO, width=80)
        ActionsNotes.productsBox.column("#12", stretch=NO, width=80)

        botonShowNotesBack = Button(
            root.showNoteFrame, text="Back", relief="groove", command=lambda: ActionsNotes().menu())

        # *
        showLabel = Label(root.root, text="Show Notes")
        showLabel.config(fg="#fff", bg="#2F83BA",
                         font=("arial", 30), padx=20, pady=50)

        showLabel.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        root.showNoteFrame.grid(row=1, column=0, columnspan=2, sticky=N)
        root.showNoteFrame.config(bg="#2F83BA")

        botonShowNotesBack.grid(row=5, column=0, sticky=SW, padx=5, pady=10)
        botonShowNotesBack.config(
            width=10, bg="#2F83BA", fg="#fff", font=("arial", 10), pady=3, padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def deleteNote(self):

        # * Create Note

        deleteNoteName = Label(root.deleteNoteFrame, text="Name")
        deleteNoteName.grid(row=1, column=0, sticky=W)
        deleteNoteNameEntry = Entry(
            root.deleteNoteFrame, textvariable=ActionsNotes.title)
        deleteNoteNameEntry.grid(row=1, column=1, sticky=W)

        botonEnterNotes = Button(root.deleteNoteFrame, text="Delete",
                                 relief="groove", command=lambda: ActionsNotes().deleteNoteMethod())
        botonEnterNotesBack = Button(
            root.deleteNoteFrame, text="Back", relief="groove", command=lambda: ActionsNotes().menu())

        # *
        deleteLabel = Label(root.root, text="Delete Notes")
        deleteLabel.config(fg="#fff", bg="#2F83BA",
                           font=("arial", 30), padx=20, pady=50)

        deleteLabel.grid(row=0, column=0, columnspan=3, sticky=NSEW)
        root.deleteNoteFrame.grid(row=1, column=0, columnspan=2, sticky=N)
        root.deleteNoteFrame.config(bg="#2F83BA")

        deleteNoteName.config(bg="#2F83BA", fg="#fff",
                              height=2, font=("arial", 15), padx=10)
        deleteNoteNameEntry.config(width=32, font=(
            "arial", 13), bg="#fff", fg="#000")

        botonEnterNotes.grid(row=5, column=1, sticky=E, padx=5, pady=10)
        botonEnterNotes.config(width=10, bg="#BEE2FA",
                               fg="#000", font=("arial", 15), pady=3, padx=7)

        botonEnterNotesBack.grid(row=5, column=0, sticky=SW, padx=5, pady=10)
        botonEnterNotesBack.config(
            width=10, bg="#2F83BA", fg="#fff", font=("arial", 10), pady=3, padx=7)

        root.menuFrame.grid_remove()

        root.root.mainloop()

    def menu(self):
        # *Remove all record
        for record in ActionsNotes.productsBox.get_children():
            ActionsNotes.productsBox.delete(record)

        # * Menu de opciones

        botonCreate = Button(root.menuFrame, text="Create",
                             relief="groove", command=lambda: ActionsNotes().createNote())
        botonShow = Button(root.menuFrame, text="Show", relief="groove",
                           command=lambda: ActionsNotes().showNote())
        botonUpdate = Button(root.menuFrame, text="Update",
                             relief="groove", command=lambda: ActionsNotes().updateNote())
        botonDelete = Button(root.menuFrame, text="Delete",
                             relief="groove", command=lambda: ActionsNotes().deleteNote())
        botonExit = Button(root.menuFrame, text="Exit",
                           relief="groove", command=exit)

        # *
        menuLabel = Label(root.root, text="Profesores Menu")
        menuLabel.config(fg="#fff", bg="#2F83BA",
                         font=("arial", 30), padx=20, pady=50)
        menuLabel.grid(row=0, column=0, columnspan=3, sticky=NSEW)

        root.menuFrame.grid(row=1, column=0, columnspan=2, sticky=N)
        root.menuFrame.config(bg="#2F83BA")

        botonCreate.grid(row=1, column=0, sticky=E, padx=5, pady=10)
        botonCreate.config(width=10, height=2, bg="#BEE2FA",
                           fg="#000", font=("arial", 20), pady=3, padx=7)

        botonShow.grid(row=1, column=1, sticky=E, padx=5, pady=10)
        botonShow.config(width=10, height=2, bg="#BEE2FA",
                         fg="#000", font=("arial", 20), pady=3, padx=7)

        botonUpdate.grid(row=2, column=0, sticky=E, padx=5, pady=10)
        botonUpdate.config(width=10, height=2, bg="#BEE2FA",
                           fg="#000", font=("arial", 20), pady=3, padx=7)

        botonDelete.grid(row=2, column=1, sticky=E, padx=5, pady=10)
        botonDelete.config(width=10, height=2, bg="#BEE2FA",
                           fg="#000", font=("arial", 20), pady=3, padx=7)

        botonExit.grid(row=4, column=1, sticky=E, padx=5, pady=10)
        botonExit.config(width=10, height=2, bg="#BEE2FA",
                         fg="#000", font=("arial", 20), pady=3, padx=7)

        root.createNoteFrame.grid_remove()
        root.showNoteFrame.grid_remove()
        root.updateNoteFrame.grid_remove()
        root.updateNoteFrame2.grid_remove()
        root.deleteNoteFrame.grid_remove()

        root.root.mainloop()

    def createNoteMethod(self):

        note = modelNotes.Note(ActionsNotes.Profesor.get(),
                               ActionsNotes.AM.get(),
                               ActionsNotes.AP.get(),
                               ActionsNotes.RFC.get(),
                               ActionsNotes.Sueldo.get(),
                               ActionsNotes.Sexo.get(),
                               ActionsNotes.Materias.get(),
                               ActionsNotes.TelC.get(),
                               ActionsNotes.TelCasa.get(),
                               ActionsNotes.Pasatiempos.get(),
                               ActionsNotes.NombreCreador.get(),
                               ActionsNotes.TesisAM.get(),
                               ActionsNotes.TesisNombre.get())
        save = note.save()
        # print(save[0])

        if (not save):
            ActionsNotes.Profesor.set(""),
            ActionsNotes.AM.set(""),
            ActionsNotes.AP.set(""),
            ActionsNotes.RFC.set(""),
            ActionsNotes.Sueldo.set(""),
            ActionsNotes.Sexo.set(""),
            ActionsNotes.Materias.set(""),
            ActionsNotes.TelC.set(""),
            ActionsNotes.TelCasa.set(""),
            ActionsNotes.Pasatiempos.set(""),
            ActionsNotes.NombreCreador.set(""),
            ActionsNotes.TesisAM.set(""),
            ActionsNotes.TesisNombre.set("")
            ActionsNotes().menu()
        else:
            MessageBox.showwarning("Alerta", "ERROR")

    def updateNoteMethod(self,):
        note = modelNotes.Note([0], ActionsNotes.title.get(
        ), ActionsNotes.updateNoteDescEntry.get("1.0", "end-1c"))
        update = note.update()

        if (update[0] >= 1):
            ActionsNotes.title.set("")
            ActionsNotes.updateNoteDescEntry.delete("1.0", END)
            ActionsNotes().menu()
        else:
            MessageBox.showwarning("Alerta", "ERROR")

    def deleteNoteMethod(self,):
        note = modelNotes.Note([0], ActionsNotes.title.get())
        delete = note.delete()

        if (delete[0] >= 1):
            ActionsNotes.title.set("")
            ActionsNotes.createNoteDescEntry.delete("1.0", END)
            ActionsNotes().menu()
        else:
            MessageBox.showwarning("Alerta", "ERROR")
