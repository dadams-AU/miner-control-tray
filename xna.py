#!/usr/bin/env python3

import schedule
import os
import threading
from datetime import datetime, time
from time import sleep

os.system('clear')

keep_running = True  # Shared flag to control the scheduler thread


def start_miner():
    current_time = datetime.now().time()
    if current_time <= time(17, 0) or current_time >= time(20, 0):
        os.chdir('/home/miner/miner/rigel/')
        os.system('./xna.sh')
    else:
        print("It's not the scheduled time to start the miner. Wait until 8 PM.")


def stop_miner():
    os.system('pkill -f rigel')


schedule.every().day.at("20:00").do(start_miner)
schedule.every().day.at("17:00").do(stop_miner)


def scheduler():
    global keep_running
    while keep_running:
        schedule.run_pending()
        sleep(60)


t = threading.Thread(target=scheduler)
t.start()

print("Rigel Miner Controller")
print("Press (k) to manually kill the miner.")
print("Press (s) to manually start the miner.")
print("Press (q) to quit this script.")

while True:
    choice = input("\n\nPlease enter your choice and press Enter: ")

    if choice == 'k':
        stop_miner()
    elif choice == 's':
        start_miner()
    elif choice == 'q':
        stop_miner()
        keep_running = False  # Signal the scheduler to stop
        t.join()  # Wait for the scheduler thread to finish
        break
