import RPi.GPIO as GPIO
#pin 17

def setup(channel1, channel2):
    GPIO.setmode(GPIO.BOARD)
    print('GPIO setup\n')
    GPIO.setup(channel1, GPIO.IN)
    GPIO.setup(channel2, GPIO.OUT)
    print(f'Pin set as input on channel {channel1}\n')
    print(f'Pin set as input on channel {channel1}\n')

def gpio_read(channel):
    result = GPIO.input(channel)
    print('Channel read\n')
    return result

def gpio_write(channel, mode):
    GPIO.output(channel, mode)
    print('Channel send')
