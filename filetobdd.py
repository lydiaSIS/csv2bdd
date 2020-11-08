from connexion import Connection
from window import Window
from tkinter import filedialog
import xlrd
import csv
import os

root=Window()
FILETYPES = [ ("CSV files", "*.csv"),("EXCEL files", "*.xlsx") ]
directory=os.getcwd()
def openfile(event):
    #root.filename
    filename=filedialog.askopenfilename(initialdir=directory, title="Open file", filetypes=FILETYPES)
    global nom
    nom=os.path.split(filename)
    print(nom[-1])
    root.fileLabel.configure(text=nom[-1])
    
def connect():
    host=root.hostEntry.get()
    user=root.userEntry.get()
    pw=root.pwEntry.get()
    db=root.dbEntry.get()
    
    try:
        global connect
        connect=Connection(host,user,pw,db)
        print('connexion réussie')
        
    except:
        print('connexion échouée')

def transfert(event):
    connect()
    t=root.tableEntry.get()
    connect.query('SHOW COLUMNS FROM {0}'.format(t))
    cols=connect.mycursor.fetchall()
    for cl in cols:
        print(cl[0])
    
    with open(nom[-1],'r') as filesrce:
        reader=csv.reader(filesrce,delimiter=';')
        for row in reader:
            row=tuple(row)
            print(row)
            connect.query("INSERT INTO {0} VALUES {1}".format(t,row))
            connect.commit()
            #for i in range(len(row)):
                #connect.query('INSERT INTO {0} VALUES({1})'.format(t,row))
                
    connect.close()
    
    

root.openFileBtn.bind('<Button>',openfile)
root.transferBtn.bind('<Button>',transfert)

root.mainloop()
