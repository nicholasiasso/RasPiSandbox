from time import sleep
from gpiozero import CPUTemperature

cpu = CPUTemperature()

while True:
    print(cpu.temperature)
    sleep(1)
