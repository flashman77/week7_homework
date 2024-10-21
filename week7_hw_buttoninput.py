import RPi.GPIO as GPIO
import time

SW1 = 5
SW2 = 6 
SW3 = 13
SW4 = 19
SWITCH = [5,6,13,19]
count = [0,0,0,0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Click(channel):
    CH = SWITCH.index(channel)
    count[CH] += 1
    print("('SW%s click', %d)"%(CH+1,count[CH]))

GPIO.add_event_detect(SW1, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW2, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW3, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW4, GPIO.RISING, callback=Click,bouncetime=200)

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    pass

GPIO.cleanup()

