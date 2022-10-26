from tkinter import *
import User.users as model
import Notes.actions as actionsNotes
from tkinter import messagebox as MessageBox
import root as root


class Actions:
    root.root
    root.root.minsize(500,500)
    root.root.title("Notes tkinter")
    root.root.resizable(0,0)
    root.root.grid_columnconfigure(1, weight=1)
    root.root.grid_rowconfigure(0, weight=0)
    root.root.config(bg="#2F83BA")

    #* Variables
    name = StringVar()
    lastname = StringVar()
    email = StringVar()
    password = StringVar()

    def home(self):
        #* Definir campo login
        

        loginEmail = Label(root.loginFrame,text="Email")
        loginEmail.grid(row=1, column=0,sticky=W)
        loginEntryEmail = Entry(root.loginFrame,textvariable=Actions.email)
        loginEntryEmail.grid(row=1, column=1)

        loginPassword = Label(root.loginFrame,text="Password")
        loginPassword.grid(row=2, column=0,sticky=W)
        loginEntryPassword = Entry(root.loginFrame,textvariable=Actions.password)
        loginEntryPassword.grid(row=2, column=1)

        botonEnter=Button(root.loginFrame,text="Enter",relief="groove",command=Actions().loginMethod)
        botonCreateCount=Button(root.loginFrame,text="Create Count",relief="ridge",command=Actions().create)

        labelVacio = Label(root.loginFrame,text="")
        
        #*
        loginLabel = Label(root.root ,text="WELCOME")
        loginLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=50)

        loginLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)
        root.loginFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.loginFrame.config(bg="#2F83BA")

        loginEmail.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        loginEntryEmail.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        loginPassword.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        loginEntryPassword.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        labelVacio.grid(row=4)
        labelVacio.config(bg="#2F83BA")

        botonEnter.grid(row=5,column=1,sticky=E,padx=5,pady=10)
        botonEnter.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)
        
        botonCreateCount.grid(row=5,column=0,sticky=SW,padx=5,pady=10)
        botonCreateCount.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        
        root.createFrame.grid_remove()
        root.root.mainloop()

    def create(self):
        #* Crear cuenta
        

        createName = Label(root.createFrame,text="Name")
        createName.grid(row=1, column=0,sticky=W)
        createEntryName = Entry(root.createFrame,textvariable=Actions.name)
        createEntryName.grid(row=1, column=1)

        createLastname = Label(root.createFrame,text="Last Name")
        createLastname.grid(row=2, column=0,sticky=W)
        createEntryLastname = Entry(root.createFrame,textvariable=Actions.lastname)
        createEntryLastname.grid(row=2, column=1)

        createEmail = Label(root.createFrame,text="Email")
        createEmail.grid(row=3, column=0,sticky=W)
        createEntryEmail = Entry(root.createFrame,textvariable=Actions.email)
        createEntryEmail.grid(row=3, column=1)

        createPassword = Label(root.createFrame,text="Password")
        createPassword.grid(row=4, column=0,sticky=W)
        createEntryPassword = Entry(root.createFrame,textvariable=Actions.password)
        createEntryPassword.grid(row=4, column=1)

        botonRegister=Button(root.createFrame,text="Register",relief="groove",command=Actions().registerMethod)
        botonBack=Button(root.createFrame,text="Back",relief="groove",command=Actions().home)

        #*
        createLabel = Label(root.root,text="Register")
        createLabel.config(fg="#fff",bg="#2F83BA",font=("arial",30),padx=20,pady=30)
        createLabel.grid(row=0,column=0, columnspan=3, sticky=NSEW)

        root.createFrame.grid(row=1,column=0, columnspan=2, sticky=N)
        root.createFrame.config(bg="#2F83BA")

        createName.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        createEntryName.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        createLastname.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        createEntryLastname.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        createEmail.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        createEntryEmail.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        createPassword.config(bg="#2F83BA",fg="#fff",height=2,font=("arial",15),padx=10)
        createEntryPassword.config(width=20,font=("arial",13),bg="#fff",fg="#000")

        botonRegister.grid(row=6,column=1,sticky=E,padx=5,pady=10)
        botonRegister.config(width=10,bg="#BEE2FA",fg="#000",font=("arial",15),pady=3,padx=7)

        botonBack.grid(row=6,column=0,sticky=SW,padx=5,pady=10)
        botonBack.config(width=10,bg="#2F83BA",fg="#fff",font=("arial",10),pady=3,padx=7)

        root.loginFrame.grid_remove()
        root.menuFrame.grid_remove()

        root.root.mainloop()

    def registerMethod(self):
        user = model.User(Actions.name.get(),Actions.lastname.get(),Actions.email.get(),Actions.password.get())
        register = user.register()

        if(register[0]>=1):
            Actions.email.set("")
            Actions.password.set("")
            Actions().home()
        else:
            MessageBox.showwarning("Alerta", "ERROR")

    def loginMethod(self):
        try:
            #ingresamos los valos que vamos a ocupar
            user=model.User("", "", Actions.email.get(), Actions.password.get())
            login = user.identify()

            #tiene que ser con el email porque la contraseña esta hasheada
            if(Actions.email.get()==login[3]):
                Actions.email.set("")
                Actions.password.set("")
                root.loginFrame.destroy()
                actionsNotes.ActionsNotes().menu(login)
        except Exception as e:
            MessageBox.showwarning("Alerta", "ERROR")
            Actions.email.set("")
            Actions.password.set("")
            
