import tkinter as Tk
from tkinter import *
import tkinter.font as tkfont

texte = ""
class Texte():
    
    def __init__(self):
        self.texte = ""
        self.reponse = False
    
    def ecrire(self, valeur):
        if self.reponse is True:
            chaine.configure(state="normal")
            chaine.delete(0.0, END)
            chaine.configure(state="disabled")
            self.reponse = False
        self.texte = list(valeur) 
        chaine.configure(state="normal")
        chaine.insert(END, self.texte)
        chaine.configure(state="disabled")

    def supprimer_tout(self):
        chaine.configure(state="normal")
        chaine.delete(0.0, END)
        chaine.configure(state="disabled")
        
    def supprimer(self):
        if self.reponse is True:
            chaine.configure(state="normal")
            chaine.delete(0.0, END)
            chaine.configure(state="disabled")
            return
        texte = list(chaine.get(0.0, END))
        for _ in range(2):
            texte.pop(-1)
        self.texte = "".join(texte)
        chaine.configure(state="normal")
        chaine.delete(0.0, END)
        chaine.insert(END, self.texte)
        chaine.configure(state="disabled")
        
    def resoudre(self):
        try:
            texte = list(chaine.get(0.0, END))
            for i, chiffre in enumerate(texte):
                if chiffre == "x":
                    texte[i] = "*"
                elif chiffre == "÷":
                    texte[i] = "/"
            texte = "".join(texte)
            resultat = str(f'{eval(texte)} ')
            if ".0 " in resultat:
                for _ in range(3):
                    resultat = list(resultat)
                    resultat.pop(-1)
            resultat = ''.join(resultat)
            chaine.configure(state="normal")
            chaine.delete(0.0, END)
            chaine.insert(END, resultat)
            chaine.configure(state="disabled")
        except:
            chaine.configure(state="normal")
            chaine.delete(0.0, END)
            chaine.insert(END, "ERREUR: faute de frappe.")
            chaine.configure(state="disabled")
        self.reponse = True

texte = Texte()

root = Tk()
root.title("Calculatrice")
root.resizable(False, False)

frame = Frame(root)
frame.grid(row=1, column=0, columnspan=100)

scroll_bar_x = Scrollbar(frame, orient=HORIZONTAL)
chaine = Text(frame, width=53, height=3, bg="ivory", state="disabled", xscrollcommand=scroll_bar_x.set, wrap="none")
scroll_bar_x.config(command=chaine.xview)
font = tkfont.Font(font=chaine['font'])
font = tkfont.Font(family="Consolas", size=15)
chaine.configure(font=font)
chaine.pack()
scroll_bar_x.pack(fill=X)

bouton = []
for j, i in enumerate(range(9), start=1):
    bouton_i = Button(root, width=20, height=3, text=j, command=lambda temp = j: texte.ecrire(str(temp)))
    bouton.append(bouton_i)
bouton = [bouton[0], bouton[1], bouton[2], bouton[5], bouton[4], bouton[3], bouton[6], bouton[7], bouton[8]]
bouton.reverse()
a = 0
for i in range(3):
    for j in range(3):
        bouton[a].grid(row=i + 3, column=j)
        a += 1

Button(root, width=20, height=3, text="0", command=lambda : texte.ecrire("0")).grid(row=6, column=0)
Button(root, width=20, height=3, text=".", command=lambda : texte.ecrire(".")).grid(row=6, column=1)
Button(root, width=20, height=3, text="=", command=lambda : texte.resoudre(), bg="#2596be").grid(row=6, column=2)
Button(root, width=20, height=3, text="(", command=lambda : texte.ecrire("("), foreground="#2596be").grid(row=2, column=0)
Button(root, width=20, height=3, text=")", command=lambda : texte.ecrire(")"), foreground="#2596be").grid(row=2, column=1)
Button(root, width=20, height=3, text="C", command=lambda : texte.supprimer_tout(), foreground="#2596be").grid(row=2, column=2)
Button(root, width=20, height=3, text="⇍", command=lambda : texte.supprimer(), foreground="#2596be").grid(row=2, column=3)
Button(root, width=20, height=3, text="÷", command=lambda : texte.ecrire("÷"), foreground="#2596be").grid(row=3, column=3)
Button(root, width=20, height=3, text="x", command=lambda : texte.ecrire("x"), foreground="#2596be").grid(row=4, column=3)
Button(root, width=20, height=3, text="-", command=lambda : texte.ecrire("-"), foreground="#2596be").grid(row=5, column=3)
Button(root, width=20, height=3, text="+", command=lambda : texte.ecrire("+"), foreground="#2596be").grid(row=6, column=3)

root.bind("0", lambda e : texte.ecrire("0"))
root.bind("1", lambda e : texte.ecrire("1"))
root.bind("2", lambda e : texte.ecrire("2"))
root.bind("3", lambda e : texte.ecrire("3"))
root.bind("4", lambda e : texte.ecrire("4"))
root.bind("5", lambda e : texte.ecrire("5"))
root.bind("6", lambda e : texte.ecrire("6"))
root.bind("7", lambda e : texte.ecrire("7"))
root.bind("8", lambda e : texte.ecrire("8"))
root.bind("9", lambda e : texte.ecrire("9"))
root.bind(".", lambda e : texte.ecrire("."))
root.bind("(", lambda e : texte.ecrire("("))
root.bind("+", lambda e : texte.ecrire("+"))
root.bind(")", lambda e : texte.ecrire(")"))
root.bind("-", lambda e : texte.ecrire("-"))
root.bind("*", lambda e : texte.ecrire("x"))
root.bind("/", lambda e : texte.ecrire("÷"))
root.bind("<Return>", lambda e : texte.resoudre())
root.bind("=", lambda e : texte.resoudre())
root.bind("<BackSpace>", lambda e : texte.supprimer())

root.mainloop()
