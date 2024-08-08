import tkinter as tk
from led_control_folder.led_maxtrix import LedMatrix, led_runner
from pyfirmata import Arduino
import serial.tools.list_ports
from photoManager import load_image, resize_image, process_image



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
        "Color":"green",
        "XPos":20,
        "YPos":150,
        "Height":30,
        "Width":75
    },
    1: {
        "Name": "LED_OFF",
        "Command": car_lights.all_off,
        "Color":"black",
        "XPos":180,
        "YPos":150,
        "Height":30,
        "Width":75
    },
    2: {
        "Name": "Exhaust Lights",
        "Command": car_lights.exhaustLightsMatrix,
        "Color":"orange",
        "XPos":100,
        "YPos":275,
        "Height":30,
        "Width":100
    },
    3: {
        "Name": "Right Rear Lights",
        "Command": car_lights.RightRearLightsMatrix,
        "Color":"red",
        "XPos":150,
        "YPos":250,
        "Height":30,
        "Width":100
    },
    4: {
        "Name": "Left Rear Lights",
        "Command": car_lights.LeftRearLightsMatrix,
        "Color":"red",
        "XPos":50,
        "YPos":250,
        "Height":30,
        "Width":100
    },
    5: {
        "Name": "Right Front Lights",
        "Command": car_lights.RightFrontLightsMatrix,
        "Color":"yellow",
        "XPos":150,
        "YPos":50,
        "Height":30,
        "Width":100
    },
    6: {
        "Name": "Left Front Lights",
        "Command": car_lights.LeftFrontLightsMatrix,
        "Color":"yellow",
        "XPos":50,
        "YPos":50,
        "Height":30,
        "Width":100
    },
    7: {
        "Name": "FogLights",
        "Command": car_lights.FogLightsMatrix,
        "Color":"black",
        "XPos":100,
        "YPos":25,
        "Height":30,
        "Width":100
    },
    8: {
        "Name": "Day Time Lights",
        "Command": car_lights.DayTimeLightsMatrix,
        "Color":"white",
        "XPos":100,
        "YPos":50,
        "Height":30,
        "Width":100
    }, 
    9: {
        "Name": "BothFrontLights",
        "Command": car_lights.BothFrontLightsMatrix,
        "Color":"pink3",
        "XPos":100,
        "YPos":75,
        "Height":30,
        "Width":100
    },
    10: {
        "Name": "BothRearLights",
        "Command": car_lights.BothRearLightsMatrix,
        "Color":"pink1",
        "XPos":100,
        "YPos":225,
        "Height":30,
        "Width":100
    },
    11: {
        "Name": "JustFrontAndRearLights",
        "Command": car_lights.JustFrontAndRearLightsMatrix,
        "Color":"cyan",
        "XPos":100,
        "YPos":150,
        "Height":30,
        "Width":150
    },
}



# Root widget to create window
win = tk.Tk()
myCanvas = tk.Canvas(win, border=5, borderwidth=0, highlightbackground="green")
#==============================================
def on_circle_click(event):
    print("Circle clicked!")

def create_circle_button(btn_name, x, y, r, command, color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    circle_id = myCanvas.create_oval(x0, y0, x1, y1, fill=color, outline="black")
    # Bind the click event to the circle
    myCanvas.tag_bind(circle_id, "<ButtonPress-1>", command)
    myCanvas.create_text(x, y, fill="MediumPurple4", text=btn_name, state='disabled', angle=45)

#==============================================
def create_buttons_with_commands():
    for btn_num in range(len(button_function_dict)):  # Create buttons 
        print(btn_num)
        btn_name = button_function_dict[btn_num]["Name"]
        btn_command = button_function_dict[btn_num]["Command"]
        btn_XPos = button_function_dict[btn_num]["XPos"]
        btn_YPos = button_function_dict[btn_num]["YPos"]
        btn_Width = button_function_dict[btn_num]["Width"]
        btn_Height = button_function_dict[btn_num]["Height"]
        btn_Color = button_function_dict[btn_num]["Color"]
        
        create_circle_button(btn_name, btn_XPos, btn_YPos, 10, btn_command, btn_Color)
        



#===============================================
# Car Image Layout Management
#-----------
image_path = "top_down_view.jpg"  # Update this path to your image file
photo = process_image(image_path, angle=90, new_size=(300,250))
# photo = resize_image(image_path, new_size=(300,250))
# label = tk.Label(win, image=photo)
# label.place(x=100, y=50, width=150, height=300)
print(f"Image width: {photo.width()}, Image height: {photo.height()}")
myCanvas.create_image(-50, 25, anchor='nw', image=photo)

myCanvas.place(x=50, y=50, width=200, height=300)



#===============================================
# GUI to turn ON/OFF LED connected to Arduino
#-----------
# initialize window with title & minimum size
win.title("C A R  L E D")
win.minsize(400, 400)

# # Label widget
# label = tk.Label(win, text="click to Run Car")
# label.grid(column=1, row=1)

# Button widget
create_buttons_with_commands()

# start & open window continously
win.mainloop()