import tkinter as tk

# Create a tkinter window
window = tk.Tk()

# Create a light state variable
light_state = tk.IntVar()

# Create a evil guy state variable
evil_guy_state = tk.IntVar()

# Create a function to toggle the light
def toggle_light():
    if light_state.get() == 1:
        light_state.set(0)
    else:
        light_state.set(1)
        if evil_guy_state.get() == 0:
            evil_guy_state.set(1)
            door_state.set(0)
            door_label.config(image=door_open_image)
            door_label.after(5000, lambda: door_label.config(image=door_closed_image))
            door_label.config(image=door_closed_image)  # Move this line outside of the lambda function

# Create a label for the door
door_state = tk.IntVar()
door_open_image = tk.PhotoImage(file="MAIN.PY/Impress.py/door_open.jpg")
door_closed_image = tk.PhotoImage(file="images/door_closed.jpg")
door_label = tk.Label(window, image=door_closed_image)
door_label.pack()

# Create a checkbutton for the light
light_switch = tk.Checkbutton(window, text="Light Switch", variable=light_state, command=toggle_light)
light_switch.pack()

# Start the tkinter mainloop
window.mainloop()