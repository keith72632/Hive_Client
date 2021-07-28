import RPi.GPIO as GPIO
#pin 17

def setup(channel):
    GPIO.setmode(GPIO.BOARD)
    print('GPIO setup\n')
    GPIO.setup(channel, GPIO.IN)
    print(f'Pin set as input on channel {channel}\n')

def gpio_read(channel):
    result = GPIO.input(channel)
    print('Channel read\n')
    return result
