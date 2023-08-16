import random
from  tkinter  import *
from  tkinter  import messagebox
root = Tk()
root.resizable(0,0)
root.configure(bg='blanchedalmond')
root.geometry("700x500")
root.title("Muffin")
p1 = PhotoImage(file = 'Muffin.png')
root.iconphoto(False, p1)
spacesize = Label(root, text="                           ",bg='blanchedalmond').grid(row = 1,column = 0)
spacesize2 = Label(root, text=" ",bg='blanchedalmond').grid(row = 0,column = 1)
spacesize3 = Label(root, text=" ",bg='blanchedalmond').grid(row = 2,column = 1)
spacesize4 = Label(root, text=" ",bg='blanchedalmond').grid(row = 4,column = 1)
spacesize5 = Label(root, text=" ",bg='blanchedalmond').grid(row = 6,column = 1)
spacesize6 = Label(root, text=" ",bg='blanchedalmond').grid(row = 8,column = 1)
spacesize6 = Label(root, text=" ",bg='blanchedalmond').grid(row = 10,column = 1)
spacesize7 = Label(root, text="               ",bg='blanchedalmond').grid(row = 1,column = 2)
def inputbutton():
    tyxaioixar = ""
    characteres = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*><.,"
    syskeui = e.get()
    mikos = d.get()
    if mikos.isdigit() and not len(syskeui)==0:
        mikos = int(mikos)
        for i in range(mikos) :
            tyxaioixar = tyxaioixar + random.choice(characteres)
        fakelos = open("mynewpass.txt", "a+")
        fakelos.writelines(syskeui+": "+tyxaioixar+"\n") 
        fakelos.close()
        messagebox.showinfo("","Congrats!                                        \n\nHere is your new password!\n\n"+syskeui+": "+tyxaioixar)
    elif not mikos.isdigit():
        lathos = Label(root, text="Wrong input, \nPlease insert a number.").grid(row=20, column=2)
    elif len(syskeui)==0:
        lathos2 = Label(root, text="No input, \nPlease insert why is the password for.").grid(row=20, column=2)
def inputbutton2(event):
    inputbutton()
e= Entry(root, bg="beige", borderwidth=5)
e.grid(row=3,column=1)
d= Entry(root, bg="beige", borderwidth=5)
d.grid(row=3,column=3)
okbutton= Button(root, text="Ok!", font=('Arial', 12),bg="beige",padx=20, pady=15, borderwidth=5,command=inputbutton).grid(row=9, column=2)
root.bind("<Return>",inputbutton2)
def close_win(event):
   root.destroy()
exitbutton = Button(root,text="Exit", font=('Arial', 12),bg="beige",padx=35, pady=10,borderwidth=5, command=root.quit).grid(row=13, column=2)
root.bind("<Escape>",close_win)
whatfor = Label(root, text="What is the password for?", font=('Arial', 12),bg='blanchedalmond')
whatfor.grid(row=1, column=1)
pwdsize = Label(root, text="How long should the password be?", font=('Arial', 12),bg='blanchedalmond')
pwdsize.grid(row=1, column=3)
root.mainloop()