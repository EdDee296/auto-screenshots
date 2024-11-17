from pynput import mouse

def on_click(x, y, button, pressed):
    if button == mouse.Button.right and pressed:
        print("Right-click detected. Terminating program.")
        # Stop the listener
        return False
    elif button == mouse.Button.left and pressed:
        print(f"Mouse left-clicked at ({x}, {y})")

# Set up the listener
with mouse.Listener(on_click=on_click) as listener:
    print("Listening for mouse clicks... Right-click to stop.")
    listener.join()
