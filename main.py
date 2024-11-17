import pyscreenshot as ImageGrab
from datetime import datetime
import schedule
import keyboard
import time

def grab_image():
    print("Grabbing image...")
    img_name = f"screenshot-{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
    im = ImageGrab.grab()
    filepath = f"./screenshots/{img_name}"
    im.save(filepath)
    print("Image saved!")
    return filepath

def main():
    taking_screenshots = False
    schedule.every(1).seconds.do(grab_image)
    
    while True:
        if keyboard.is_pressed('l'):
            taking_screenshots = True
            print("Started taking screenshots...")
            time.sleep(1)  # Prevent multiple triggers

        if keyboard.is_pressed('esc'):
            taking_screenshots = False
            print("Stopped taking screenshots...")
            break

        if taking_screenshots:
            schedule.run_pending()
            time.sleep(1)  # Sleep for 1 second to prevent CPU usage

if __name__ == "__main__":
    main()