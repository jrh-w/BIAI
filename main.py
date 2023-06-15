from functools import partial
from tkinter import *
from tkinter import ttk
from camera import run_camera
from functions import addItem, getTotalPrice, item_selected
import constValues
  
app = Tk()
app.title('BIAI - AI Cash Register (PoC)')
app.geometry('800x600+50+50')
app.minsize(650, 300)
app.iconbitmap('./cash-register.ico')
app.bind('<Escape>', lambda e: app.quit())

tree = ttk.Treeview(app, columns=constValues.columns, show='headings')
scrollbar = ttk.Scrollbar(app, orient=VERTICAL, command=tree.yview)
buttonFrame = Frame(app)
sumText = Label(app, text=getTotalPrice(tree))
testButton = Button(buttonFrame, text="Add test item", command=lambda: [addItem(tree, 'produkt 4'), sumText.config(text=getTotalPrice(tree))])
cameraButton = Button(buttonFrame, text="Open Camera", command=partial(run_camera, tree, sumText))

tree.heading('product', text='Zeskanowany produkt', anchor=CENTER)
tree.column('product', anchor=CENTER)
tree.heading('count', text='Ilość')
tree.column('count', anchor=CENTER)
tree.heading('price', text='Cena')
tree.column('price', anchor=CENTER)

tree.bind('<Double-1>', lambda e: [item_selected(app, tree), sumText.config(text=getTotalPrice(tree))])

tree.grid(row=0, column=0, sticky='nsew')
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)
tree.configure(yscroll=scrollbar.set)

scrollbar.grid(row=0, column=1, sticky=NS)
sumText.grid(row=1, column=0, sticky=E)
buttonFrame.grid(row=2, column=0)
testButton.pack(ipadx=10, ipady=10, padx=40, pady=10, expand=True, fill=BOTH, side=LEFT)
cameraButton.pack(ipadx=10, ipady=10, padx=40, pady=10, expand=True, fill=BOTH, side=LEFT)

app.mainloop()