from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

class Window:
    
    def __init__(self):
        bgd="#3e2723"
        fontcolor='#e9f4f0'
        self.root=Tk()
        self.root.geometry("400x550+250+20")
        self.root.config(bg='#d4a672')
        self.root.overrideredirect(1)
        self.header= Frame(self.root,height=120,bg="#3e2723")
        self.header.pack(fill=BOTH, pady=20)
        self.header.pack_propagate(0)

        self.titre=Label(self.header, text="CSV2BDD", bg="#3e2723",fg='#e9f4f0',font=('Verdana', 15))
        self.titre.pack(fill=X, pady=20)
        self.soustitre=Label(self.header, text="transferez vos données d'un fichier csv à une bdd mysql", bg="#3e2723",fg='#e9f4f0',font=('Verdana',8))
        self.soustitre.pack(fill=X)

        self.hostLabel=Label(self.root,text="Host",width='30',bg=bgd,fg=fontcolor)
        self.hostLabel.pack(pady='2')
        self.hostEntry=Entry(self.root,width='35')
        self.hostEntry.pack()

        self.userLabel=Label(self.root,text="User",width='30',bg=bgd,fg=fontcolor)
        self.userLabel.pack(pady='2')
        self.userEntry=Entry(self.root,width='35')
        self.userEntry.pack()

        self.pwLabel=Label(self.root,text="Password",width='30',bg=bgd,fg=fontcolor)
        self.pwLabel.pack(pady='2')
        self.pwEntry=Entry(self.root,width='35')
        self.pwEntry.pack()

        self.dbLabel=Label(self.root,text="Database Name",width='30',bg=bgd,fg=fontcolor)
        self.dbLabel.pack(pady='2')
        self.dbEntry=Entry(self.root,width='35')
        self.dbEntry.pack()

        self.tableLabel=Label(self.root,text="Table Name",width='30',bg=bgd,fg=fontcolor)
        self.tableLabel.pack(pady='2')
        self.tableEntry=Entry(self.root,width='35')
        self.tableEntry.pack()

        self.openFileBtn=Button(self.root,text="Ouvrir un fichier",width="30",bg=bgd,fg=fontcolor)
        self.openFileBtn.pack()

        self.fileLabel=Label(self.root,text="",width=30,bg='#fff')
        self.fileLabel.pack(pady='2')

        self.label=Label(self.root,text="",width=30,bg='#d4a672')
        self.label.pack(pady=10)
        
        self.transferBtn=Button(self.label,text="Transferer",bg='green',width='14')
        self.transferBtn.pack(side=LEFT)

        self.closeBtn=Button(self.label,text="Quitter",command=self.root.destroy,bg='red',width='14')
        self.closeBtn.pack(side=RIGHT)

        
    def mainloop(self):
        self.root.mainloop()

        

if __name__=="__main__":
    root=Window()
    root.mainloop()
