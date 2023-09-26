#!/usr/bin/env python3

import pystray
from PIL import Image, ImageDraw
import schedule
import os
import threading
from datetime import datetime, time
from time import sleep
from plyer import notification

# Miner control functions
def start_miner():
    global manually_stopped
    current_time = datetime.now().time()
    
    if manually_stopped:
        notification.notify(
            title="Miner Control",
            message="The miner was manually stopped and won't start until tomorrow.",
            timeout=10
        )
        return

    if time(17, 0) <= current_time <= time(20, 0): 
        notification.notify(
            title="Miner Control",
            message="It's not the scheduled time to start the miner. Electricity costs are too high.",
            timeout=10
        )
        return
    
    if current_time > time(20, 0) or current_time < time(17, 0):
        os.chdir('/home/miner/miner/t-rex/') 
        os.system('./xna.sh') 
    else:
        stop_miner()

def stop_miner(manual=False):
    global manually_stopped
    if manual:
        manually_stopped = True
    os.system('pkill -f t-rex')

# Schedule tasks
schedule.every().day.at("20:00").do(start_miner)
schedule.every().day.at("17:00").do(stop_miner)
schedule.every().day.at("09:00").do(lambda: setattr(globals(), 'manually_stopped', False))

keep_running = True
manually_stopped = False

# Scheduler thread
def scheduler():
    while keep_running:
        schedule.run_pending()
        sleep(60)

t = threading.Thread(target=scheduler)
t.start()

# System tray icon functions and creation
def create_image():
    width, height = 64, 64
    color1 = (0, 0, 0)
    color2 = (255, 255, 255)
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
    dc.rectangle((0, height // 2, width // 2, height), fill=color2)
    return image

def on_activate_start(icon, item):
    start_miner()

def on_activate_stop(icon, item):
    stop_miner(manual=True)

def on_activate_exit(icon, item):
    global keep_running
    print("Exit activated") 
    stop_miner()
    keep_running = False
    t.join()
    icon.stop()

image = create_image()
menu = (pystray.MenuItem('Start Miner', on_activate_start),
        pystray.MenuItem('Stop Miner', on_activate_stop),
        pystray.MenuItem('Exit', on_activate_exit))
icon = pystray.Icon("miner_control", image, "Miner Control", menu)
icon.run()
