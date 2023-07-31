from tkinter import *

langas = Tk()
issaugotas_vardas = StringVar()


# Veiksmų funkcijos
def spausdinti():
    vardas = vardas_entry.get()
    issaugotas_vardas.set(vardas)
    rezultatas_label['text'] = f"Sveiki, {vardas}"
    status_label['text'] = "Sukurta"


def isvalyti():
    rezultatas_label['text'] = ""
    vardas_entry.delete(0, END)
    status_label['text'] = "Išvalyta"


def atkurti():
    vardas = issaugotas_vardas.get()
    vardas_entry.insert(END, vardas)
    spausdinti()
    status_label['text'] = "Atkurta"


def iseiti():
    exit()


# Grafiniai objektai
vardas_label = Label(langas, text="Įveskite vardą")
vardas_entry = Entry(langas)
patvirtinti_button = Button(langas, text="Patvirtinti", command=spausdinti)
rezultatas_label = Label(langas, text="")
status_label = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)

# Mygtukų priskyrimas
langas.bind("<Return>", lambda e: spausdinti())

# Meniu formavimas
meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=iseiti)

# Objektų sudėjimas į lentelę
vardas_label.grid(row=0, column=0)
vardas_entry.grid(row=0, column=1)
patvirtinti_button.grid(row=0, column=2)
rezultatas_label.grid(row=1, columnspan=3)
status_label.grid(row=2, columnspan=3, sticky=W + E)
langas.mainloop()
