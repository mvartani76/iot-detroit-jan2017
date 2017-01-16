import spidev
from time import sleep

spi = spidev.SpiDev()
spi.open(0,0)
channel_select = [0x01, 0x80, 0x00]

while True:
	adc_data = spi.xfer2(channel_select)
	adc = ((adc_data[1]<<8)&0x300)|(adc_data[2]&0xFF)
	print(round((adc / 1023.0) * 100))
	sleep(0.5)