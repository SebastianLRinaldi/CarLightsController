import serial.tools.list_ports
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)


#---------------------------------------------
# GUI to turn ON/OFF LED connected to Arduino
#---------------------------------------------
import tkinter as tk
from led_control_folder.led_maxtrix import LedMatrix, led_runner
from pyfirmata import Arduino
#===============================================



#===============================================
# Functions
#-----------
def ledON():
    car_lights.all_on()
    
def ledOFF():
    car_lights.all_off()

def exhaustLights():
    car_lights.exhaustLightsMatrix()

def RightRearLights():
    car_lights.RightRearLightsMatrix()

def LeftRearLights():
    car_lights.LeftRearLightsMatrix()

def RightFrontLights():
    car_lights.RightFrontLightsMatrix()

def LeftFrontLights():
    car_lights.LeftFrontLightsMatrix()

def FogLights():
    car_lights.FogLightsMatrix()

def DayTimeLights():
    car_lights.DayTimeLightsMatrix()






#==============================================
# Arduino board connected to serial port COM3
board = Arduino('COM3')
print("byBass Stall")


#===============================================
# Matrix Controler
DIN = 11
CS = 7
CLK = 13
car_lights = LedMatrix(board, DIN, CS, CLK)
car_lights.setup()


# Root widget to create window
win = tk.Tk()
# initialize window with title & minimum size
win.title("L E D")
win.minsize(200,60)

# Label widget
label = tk.Label(win, text="click to Run Car")
label.grid(column=1, row=1)

# # Button widget
ONbtn = tk.Button(win, bd=4, text="LED ON", command=ledON)
ONbtn.grid(column=1, row=2)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=2)

ONbtn = tk.Button(win, bd=4, text="exhaustLights", command=exhaustLights)
ONbtn.grid(column=1, row=3)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=3)

ONbtn = tk.Button(win, bd=4, text="RightRearLights", command=RightRearLights)
ONbtn.grid(column=1, row=4)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=4)

ONbtn = tk.Button(win, bd=4, text="LeftRearLights", command=LeftRearLights)
ONbtn.grid(column=1, row=5)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=5)

ONbtn = tk.Button(win, bd=4, text="RightFrontLights", command=RightFrontLights)
ONbtn.grid(column=1, row=6)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=6)

ONbtn = tk.Button(win, bd=4, text="LeftFrontLights", command=LeftFrontLights)
ONbtn.grid(column=1, row=7)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=7)

ONbtn = tk.Button(win, bd=4, text="FogLights", command=FogLights)
ONbtn.grid(column=1, row=8)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=8)

ONbtn = tk.Button(win, bd=4, text="DayTimeLights", command=DayTimeLights)
ONbtn.grid(column=1, row=9)
OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
OFFbtn.grid(column=2, row=9)

# start & open window continously
win.mainloop()