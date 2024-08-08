from tkinter import *
root = Tk()
myCanvas = Canvas(root)
myCanvas.pack()


def on_circle_click(event):
    print("Circle clicked!")



def create_circle(x, y, r, canvas): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    circle_id = canvas.create_oval(x0, y0, x1, y1, fill="blue", outline="black")
    # Bind the click event to the circle
    canvas.tag_bind(circle_id, "<ButtonPress-1>", on_circle_click)

create_circle(150, 150, 20, myCanvas)
create_circle(20, 25, 10, myCanvas)
root.mainloop()