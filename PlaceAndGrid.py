# import tkinter as tk

# root = tk.Tk()

# # Using Place layout for a label
# fixed_label = tk.Label(root, text="Fixed Position")
# fixed_label.place(x=50, y=40)

# # Using Grid layout for other widgets
# button1 = tk.Button(root, text="Button 1")
# button2 = tk.Button(root, text="Button 2")

# # Grid placement
# button1.grid(row=0, column=0)
# button2.grid(row=1, column=1)

# root.mainloop()


# from tkinter import Tk, Label
# from PIL import Image, ImageTk

# def load_image(image_path):
#     # Open an image file
#     img = Image.open(image_path)
#     # Convert image into PhotoImage object
#     photo = ImageTk.PhotoImage(img)
#     return photo

# def process_image(image_path, angle=0, new_size=(200, 200)):
#     # Open the image file
#     img = Image.open(image_path)
    
#     # Rotate the image
#     rotated_img = img.rotate(angle)
    
#     # Resize the image without cropping
#     resized_img = rotated_img.resize(new_size)
    
#     # Convert the image to PhotoImage format for Tkinter
#     photo = ImageTk.PhotoImage(resized_img)
    
#     return photo

# root = Tk()
# image_path = "top_down_view.jpg"  # Update this path to your image file
# photo = process_image(image_path, angle=90, new_size=(300,250))

# label = Label(root, image=photo)
# label.place(x=50, y=50, width=150, height=300)

# root.mainloop()

import tkinter as tk
from tkinter import Tk, Label
from PIL import Image, ImageTk

def load_image(image_path):
    # Open an image file
    img = Image.open(image_path)
    # Convert image into PhotoImage object
    photo = ImageTk.PhotoImage(img)
    return photo

def process_image(image_path, angle=0, new_size=(200, 200)):
    # Open the image file
    img = Image.open(image_path)
    
    # Rotate the image
    rotated_img = img.rotate(angle)
    
    # Resize the image without cropping
    resized_img = rotated_img.resize(new_size)
    
    # Convert the image to PhotoImage format for Tkinter
    photo = ImageTk.PhotoImage(resized_img)
    
    return photo


root = tk.Tk()
image_path = "top_down_view.jpg"  # Update this path to your image file
photo = process_image(image_path, angle=90, new_size=(300,250))

label = Label(root, image=photo)
label.place(x=50, y=50, width=150, height=300)

# Using Place layout for a label
fixed_label = tk.Label(root, text="Fixed Position")
fixed_label.place(x=50, y=40)

# Using Grid layout for other widgets
button1 = tk.Button(root, text="Button 1")
button2 = tk.Button(root, text="Button 2")
button1.place(x=50, y=50)
button2.place(x=50, y=60, width=15, height=30)

root.mainloop()

