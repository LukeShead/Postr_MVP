import tkinter as tk
import tkinter.ttk as ttk
import post_test

window = tk.Tk()
frame = tk.Frame()


# Basic text being displayed (cannot be edited in app)
greeting = tk.Label(
    text = "Luke is Amazing",
    foreground = "white",
    background = "grey",
    width = 50,
    height = 1,
    master = frame)

# Basic button for testing, can be clicked on
# Hoping to get functions to run on it
button = tk.Button(
    text = "Upload tweet",
    width = 25,
    height = 5,
    background = "grey",
    foreground = "white",
    master = frame
)


# Getting the input from the user.
entry = tk.Entry(
    foreground = "yellow",
    background = "blue",
    width = 50,
    master = frame
)

# Text box testing as well
text_box = tk.Text()
entry.insert(0, "text goes here")

# Pack is the function that implements the type of widget into the window
greeting.pack()
entry.pack()
button.pack()
frame.pack()

# Set the window to start handling events
event = []

# Clicking on the button will get the message within the text box
# From here we will run the function to post the text onto the page
def handle_click(event):
    message = entry.get()
    post_test.post_tweet(message)
    # Debug print, can be removed later
    print(message)

# Binding left moust click (button-1) to the button to activate the event
button.bind("<Button-1>", handle_click)


window.mainloop()
