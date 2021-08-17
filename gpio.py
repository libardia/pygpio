import os

GPIO_PATH = '/sys/class/gpio'

class Handles:
    export = open(GPIO_PATH + '/export', 'w', 0)
    unexport = open(GPIO_PATH + '/unexport', 'w', 0)

handles = Handles()

def open(pin):
    handles.export.write(str(pin))
    handles.export.flush()

def close(pin):
    handles.unexport.write(str(pin))
    handles.unexport.flush()
