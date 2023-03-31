import json
import os
import time
import sys
import platform

DEFAULT_CONFIG={
    "timeInterval":600,
    "askForTimeUpdate":True,
}

try:
    print("Trying")
    F=open('config.json','r')
    CONFIG=json.load(F)
except json.decoder.JSONDecodeError: #If error then load default config
    CONFIG=DEFAULT_CONFIG
except FileNotFoundError: #If file does not exist
    CONFIG=DEFAULT_CONFIG

CLEAR= 'cls' if platform.system()=="Windows" else 'clear'

def configure(config):
    W=open('config.json','w')
    while True:
        os.system(CLEAR)
        try:
            print("1. Time Interval", "2. Ask for new time on timer end", sep="\n")
            choice=int(input("Enter config to change (0/1/2) [0 to save and exit]:"))

            if choice == 1:
                interval=config['timeInterval']
                print(f"Current time interval: {int(interval//60):02d}:{int(interval%60):02d} minutes")
                interval=float(input('Enter the timer interval [in min]: '))*60
                if interval:
                    config['timeInterval'] =interval
                print("Updating . . .")
                time.sleep(0.3)

            elif choice == 2:
                print("Current option:", config['askForTimeUpdate'])
                ask=bool(int(input("Enter whether you want to be asked for time update on timer end: [0/1]: ")))
                config['askForTimeUpdate'] =ask;
                print("Updating . . .")
                time.sleep(0.3)

            elif choice == 0:
                raise (KeyboardInterrupt)
            
        except ValueError:
            print("Please enter only [0/1/2] !!")
            time.sleep(1)

        except KeyboardInterrupt:
                os.system(CLEAR)
                # F=open('config.json','w')
                json.dump(CONFIG,W)
                print("Saving and exiting bye bye :)")
                time.sleep(0.5)
                sys.exit(0)
    
def getConfig(config=CONFIG):

    return (config['timeInterval'],config['askForTimeUpdate'])

if __name__ == "__main__":
    configure(CONFIG)
