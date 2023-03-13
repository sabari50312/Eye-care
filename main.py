try: 
    import os
    import sys
    import time
    from tkinter import *
    from tkinter import messagebox
 
    import platform
    CLEAR= 'clear' if platform.system()=="Linux" else 'cls'
    os.system(CLEAR)
    print("Press Ctrl+c at any point to exit :)")
    TIME=float(input('Enter the timer interval (in min): '))*60
    FIRST=1
    while True:

        if not FIRST:
            print("Press Ctrl+c at any point to exit :)")
            x=input('Continue? (<y> to continue/ <time in min to change timer>): ')
            if x.isnumeric():
                TIME=float(x)*60
            # TIME=float(input('Enter the timer interval (in min): '))*60
        i=0
        os.system(CLEAR)
        while i<=int(TIME):
            print(f"Timer started for {int(TIME//60):02d}:{int(TIME%60):02d} minutes")
            print("Press Ctrl+c at any point to exit :)")
            print("Elapsed time: ", 60%1, "min", i, "seconds")
            time.sleep(1)
            i+=1
            os.system(CLEAR)
        FIRST=0

        messagebox.showinfo("Time's up!", "Take a break from your screen and press ok when you return :)")

except KeyboardInterrupt:
    os.system(CLEAR)
    print("Quitting program bye bye :)")
    time.sleep(0.5)
    sys.exit(0)

except ValueError:
    # os.system(CLafEAR)
    print('Please enter only valid numbers!! :( ')
    time.sleep(1)
    os.system(CLEAR)
    os.system("python main.py")

except ModuleNotFoundError:
    print('Encountered an issue with dependencies. Please run "pip install -r requirements.txt" in terminal and try again:)')