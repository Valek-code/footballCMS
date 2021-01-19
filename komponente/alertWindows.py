
from tkinter import *
from tkinter import ttk

# stvara prozor za slanje obavjesti korisniku ( npr. success or fail te druge povratne informacije )
def alertWindow(_text):
    Alert_Win = Tk()
    Alert_Win.title("Alert")
    Alert_Win.geometry("500x100")

    _label = Label(Alert_Win, text=f"{_text}")
    _label.pack()