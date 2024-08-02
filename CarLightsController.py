import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)


#---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino
#---------------------------------------------
import tkinter as tk
from pyfirmata import Arduino
#===============================================
# # Functions
# #-----------
def ledON():
    board.digital[3].write(1)
def ledOFF():
    board.digital[3].write(0)
# #===============================================
# # Arduino board connected to serial port COM3
board = Arduino('COM3')
print("byBass Stall")

# Root widget to create window
win = tk.Tk()
# initialize window with title & minimum size
win.title("L E D")
win.minsize(200,60)

# Label widget
label = tk.Label(win, text="click to turn ON/OFF")
label.grid(column=1, row=1)

# # Button widget
ONbtn = tk.Button(win, bd=4, text="LED ON", command=ledON)
ONbtn.grid(column=1, row=2)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=2)

# start & open window continously
win.mainloop()