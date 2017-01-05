import Tkinter, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

number = tkSimpleDialog.askinteger("Entero", "Introduce un entero")
print number
texto = tkSimpleDialog.askstring("String", "Introduce un String")
print texto