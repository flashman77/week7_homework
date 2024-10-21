import RPi.GPIO as GPIO
import time

BUZZER = 12

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)

SW1 = 5
SW2 = 6 
SW3 = 13
SW4 = 19
GPIO.setup(SW1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def Click(channel):
    print(channel)
    if channel == SW1:
        p.ChangeFrequency(262)
        p.start(30)
        time.sleep(1.0)
        p.stop()
    elif channel == SW2:
        p.ChangeFrequency(330)
        p.start(30)
        time.sleep(1.0)
        p.stop()
    elif channel == SW3:
        p.ChangeFrequency(392)
        p.start(30)
        time.sleep(1.0)
        p.stop()
    elif channel == SW4:
        p.ChangeFrequency(523)
        p.start(30)
        time.sleep(1.0)
        p.stop()

GPIO.add_event_detect(SW1, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW2, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW3, GPIO.RISING, callback=Click,bouncetime=200)
GPIO.add_event_detect(SW4, GPIO.RISING, callback=Click,bouncetime=200)
p = GPIO.PWM(BUZZER, 262)
p.start(30)
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(294) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(330) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(349) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(392) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(440) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(494) 
time.sleep(1.0)
p.stop()
time.sleep(1.0)
p.start(30)
p.ChangeFrequency(523)
time.sleep(1.0)
p.stop()
time.sleep(1.0)

try:
    while True:
        time.sleep(1.0)
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()