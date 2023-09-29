#!/usr/bin/env python3

import pystray
from PIL import Image, ImageDraw
import schedule
import os
import threading
from time import sleep
from plyer import notification
import logging
import subprocess

logging.basicConfig(filename='miner_control.log', level=logging.INFO)

MINER_PATH = os.getenv('MINER_PATH', '/home/miner/miner/rigel/')

class MinerController:
    def __init__(self):
        self.manually_stopped = False
        self.keep_running = True
        self.t = threading.Thread(target=self.scheduler)
        self.t.start()
        schedule.every().day.at("20:00").do(self.start_miner)
        schedule.every().day.at("17:00").do(self.stop_miner)
        schedule.every().day.at("09:00").do(self.reset_manual_stop)

    def scheduler(self):
        while self.keep_running:
            schedule.run_pending()
            sleep(60)

    def start_miner(self):
        if self.manually_stopped:
            notification.notify(
                title="Miner Control",
                message="The miner was manually stopped and won't start until tomorrow.",
                timeout=10
            )
        else:
            try:
                os.chdir(MINER_PATH)
                os.system('./xna.sh')
                logging.info("Miner started.")
            except Exception as e:
                notification.notify(
                    title="Miner Control Error",
                    message=str(e),
                    timeout=10
                )

def stop_miner(self, manual=False):
    if manual:
        self.manually_stopped = True
    try:
        result = subprocess.run(["/usr/bin/pkill", "-f", "rigel"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f"stdout: {result.stdout}, stderr: {result.stderr}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to stop miner: {e}, stdout: {e.stdout}, stderr: {e.stderr}")
        notification.notify(
            title="Miner Control Error",
            message=f"Failed to stop miner: {e}",
            timeout=10
        )

    def reset_manual_stop(self):
        self.manually_stopped = False
        logging.info("Manual stop reset.")


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
    controller.start_miner()

def on_activate_stop(icon, item):
    controller.stop_miner(manual=True)

def on_activate_exit(icon, item):
    controller.keep_running = False
    print("Exit activated")
    controller.stop_miner()
    controller.t.join()
    icon.stop()

if __name__ == "__main__":
    controller = MinerController()
    image = create_image()
    menu = (pystray.MenuItem('Start Miner', on_activate_start),
            pystray.MenuItem('Stop Miner', on_activate_stop),
            pystray.MenuItem('Exit', on_activate_exit))
    icon = pystray.Icon("miner_control", image, "Miner Control", menu)
    icon.run()

