from turtle import *
import time
speed(0)
for i in range(0, 10000, 1): 
    forward(3 + i / 1000)
    left(60)
    forward(5 + i * 0.9)
    left(60)
time.sleep(4)