from tkinter import * # Import all definitions from tkinter

def processOK():
    print("OK button is clicked")

def processCancel():
    print("Cancel button is clicked")

window = Tk() # Create a window
btOK = Button(window, text = "OK", fg = "red", command = processOK)
btCancel = Button(window, text = "Cancel", bg = "yellow",
                  command = processCancel)
btOK.pack() # Place the OK button in the window
btCancel.pack() # Place the Cancel button in the window

window.mainloop() # Create an event loop