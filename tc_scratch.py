import mido
import rtmidi
import time
import random

inport = mido.open_input('KOMPLETE KONTROL M32')
outport = mido.open_output('IAC Driver Bus 1')

n = [60,62,64,65,67,69,71]
n[6]
while 1 == 1:
    i = random.randint(0,6)
    msg = mido.Message('note_on', note=n[i] )
    msg2 = mido.Message('note_on', note=48)
    outport.send(msg)
    outport.send(msg2)
    in_msg = inport.poll()
    print("*******" + str(type(in_msg)))
    print(in_msg)
    if in_msg and in_msg.note == n[i]:
        print("match")
    time.sleep(1.25)
    del in_msg
