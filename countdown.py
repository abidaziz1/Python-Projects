import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs) #formats the minutes and seconds into a string with the format MM:SS, ensuring that both minutes and seconds are displayed as two digits (e.g., 05:03). 
        print(timer, end="\r") #prints the timer string, overwriting the previous output in the same line due to the end="\r" argument.
        time.sleep(1)
        t-=1
    print("\nTime's up! Suck my nipple now...")

t=input("Enter the time in seconds: ")
countdown(int(t))

'''
The divmod function divides t by 60 and returns a tuple containing the quotient (mins) and the remainder (secs).

'''