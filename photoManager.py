from PIL import Image, ImageTk

def load_image(image_path):
    # Open an image file
    img = Image.open(image_path)
    # Convert image into PhotoImage object
    photo = ImageTk.PhotoImage(img)
    return photo

def resize_image(image_path, new_size=(200, 200)):
    # Open the image file
    img = Image.open(image_path)

    # Resize the image without cropping
    resized_img = img.resize(new_size)
    
    # Convert the image to PhotoImage format for Tkinter
    photo = ImageTk.PhotoImage(resized_img)
    
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

    

