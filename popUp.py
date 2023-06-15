from tkinter import *

def open_popup(app, data):
  top = Toplevel(app, padx=10, pady=10)
  top.resizable(False, False)
  top.geometry("350x120")
  top.title("Edytuj zawartość produktu")

  info_label = Label(top, text=f"Podaj nową ilość produktu '{data['product']}':")
  info_label.pack()

  def validate(input):
    try:
        float(input)
        return True
    except ValueError:
        return False

  newValue = StringVar()
  vcmd = (top.register(validate))
  value_entry = Entry(top, textvariable=newValue, validate='all', validatecommand=(vcmd, '%P'))
  value_entry.insert(10, data['count'])
  value_entry.pack()

  def close_popup():
    top.destroy()
    top.update()

  def exit_popup():
    newValue.set(-1)
    close_popup()

  exitButton = Button(top, text="Cancel", command=exit_popup, bg="red", fg="white")
  exitButton.pack(ipadx=10, ipady=10, padx=40, pady=10, expand=True, fill=BOTH, side=LEFT)
  editButton = Button(top, text="Accept", command=close_popup, bg="green", fg="white")
  editButton.pack(ipadx=10, ipady=10, padx=40, pady=10, expand=True, fill=BOTH, side=LEFT)

  top.wait_window()
  return float(newValue.get() or -1)