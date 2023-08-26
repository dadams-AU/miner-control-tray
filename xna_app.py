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
    current_time = datetime.now().time()
    if current_time <= time(17, 0) or current_time >= time(20, 0):
        os.chdir('/home/miner/miner/t-rex/') # location of your trex software
        os.system('./xna.sh') # sh file for your mining preferences, algo, username, etc or put the whole thing here
    else:
        notification.notify(
            title="Miner Control",
            message="It's not the scheduled time to start the miner. Wait until 8 PM.",
            timeout=10
        )

def stop_miner():
    os.system('pkill -f t-rex')

schedule.every().day.at("20:00").do(start_miner) # time of peak electricty costs
schedule.every().day.at("17:00").do(stop_miner)

keep_running = True

def scheduler():
    while keep_running:
        schedule.run_pending()
        sleep(60)

t = threading.Thread(target=scheduler)
t.start()

# Create system tray icon
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
    stop_miner()

def on_activate_exit(icon, item):
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
