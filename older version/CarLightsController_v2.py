import tkinter as tk
from led_control_folder.led_maxtrix import LedMatrix, led_runner
from pyfirmata import Arduino
import serial.tools.list_ports



#===============================================
# Port Checking FOr Arduino
#-----------
ports = list(serial.tools.list_ports.comports())
for p in ports:
    print(p)


#==============================================
# Arduino board connected to serial port COM3
#-----------
board = Arduino('COM3')
print("byBass Stall")


#===============================================
# Matrix Controler
#-----------
DIN = 11
CS = 7
CLK = 13
car_lights = LedMatrix(board, DIN, CS, CLK)
car_lights.setup()


#===============================================
# Functions
#-----------
button_function_dict = {

    0: {
        "Name": "LED_ON",
        "Command": car_lights.all_on,
        "GridPosition":[1,2],
        "PlacePosition":[50,50]
    },
    1: {
        "Name": "LED_OFF",
        "Command": car_lights.all_off
    },
    2: {
        "Name": "Exhaust Lights",
        "Command": car_lights.exhaustLightsMatrix
    },
    3: {
        "Name": "Right Rear Lights",
        "Command": car_lights.RightRearLightsMatrix
    },
    4: {
        "Name": "Left Rear Lights",
        "Command": car_lights.LeftRearLightsMatrix
    },
    5: {
        "Name": "Right Front Lights",
        "Command": car_lights.RightFrontLightsMatrix
    },
    6: {
        "Name": "Left Front Lights",
        "Command": car_lights.LeftFrontLightsMatrix
    },
    7: {
        "Name": "Fog Lights",
        "Command": car_lights.FogLightsMatrix
    },
    8: {
        "Name": "Day Time Lights",
        "Command": car_lights.DayTimeLightsMatrix
    }, 
    9: {
        "Name": "BothFrontLights",
        "Command": car_lights.BothFrontLightsMatrix
    },
    10: {
        "Name": "BothRearLights",
        "Command": car_lights.BothRearLightsMatrix
    },
    11: {
        "Name": "JustFrontAndRearLights",
        "Command": car_lights.JustFrontAndRearLightsMatrix
    },

}



# Root widget to create window
win = tk.Tk()
#==============================================
def create_buttons_with_commands():
    button_commands = {}
    for btn_num in range(len(button_function_dict)):  # Create buttons 
        print(btn_num)
        button_name = button_function_dict[btn_num]["Name"]
        button_command = button_function_dict[btn_num]["Command"]
        btn = tk.Button(win, bd=4, text=button_name, command=button_command)
        btn.grid(column=1, row=btn_num+2)  # Add some padding between buttons

        # Store the command function in the dictionary
        button_commands[button_name] = button_command
#===============================================




#===============================================
# GUI to turn ON/OFF LED connected to Arduino
#-----------
# initialize window with title & minimum size
win.title("C A R  L E D")
win.minsize(200,60)

# Label widget
label = tk.Label(win, text="click to Run Car")
label.grid(column=1, row=1)



create_buttons_with_commands()
# # Button widget
# ONbtn = tk.Button(win, bd=4, text="LED ON", command=ledON)
# ONbtn.grid(column=1, row=2)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=2)

# ONbtn = tk.Button(win, bd=4, text="exhaustLights", command=exhaustLights)
# ONbtn.grid(column=1, row=3)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=3)

# ONbtn = tk.Button(win, bd=4, text="RightRearLights", command=RightRearLights)
# ONbtn.grid(column=1, row=4)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=4)

# ONbtn = tk.Button(win, bd=4, text="LeftRearLights", command=LeftRearLights)
# ONbtn.grid(column=1, row=5)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=5)

# ONbtn = tk.Button(win, bd=4, text="RightFrontLights", command=RightFrontLights)
# ONbtn.grid(column=1, row=6)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=6)

# ONbtn = tk.Button(win, bd=4, text="LeftFrontLights", command=LeftFrontLights)
# ONbtn.grid(column=1, row=7)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=7)

# ONbtn = tk.Button(win, bd=4, text="FogLights", command=FogLights)
# ONbtn.grid(column=1, row=8)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=8)

# ONbtn = tk.Button(win, bd=4, text="DayTimeLights", command=DayTimeLights)
# ONbtn.grid(column=1, row=9)
# OFFbtn = tk.Button(win, bd=4, text="LED OFF", command=ledOFF)
# OFFbtn.grid(column=2, row=9)

# start & open window continously
win.mainloop()