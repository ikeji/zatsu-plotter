from machine import Pin
from time import sleep_ms

pin1 = Pin(0,Pin.OUT)
pin2 = Pin(1,Pin.OUT)
pin3 = Pin(2,Pin.OUT)
pin4 = Pin(3,Pin.OUT)
pin5 = Pin(4,Pin.OUT)
pin6 = Pin(5,Pin.OUT)
pin7 = Pin(6,Pin.OUT)
pin8 = Pin(7,Pin.OUT)

class BYJ:
    def __init__(self, pins):
        self.pins = pins
        self.current_phase = 0

    def step(self):
        self.current_phase = (self.current_phase + 1) % 4
        self._update()
    def unstep(self):
        self.current_phase = (self.current_phase - 1 + 4) % 4
        self._update()

    def _update(self):
        for i in range(4):
            self.pins[i].value(i==self.current_phase)

# 左のモータ
byj1 = BYJ([pin1, pin2, pin3, pin4])
# 右のモータ
byj2 = BYJ([pin5, pin6, pin7, pin8])

# ヘッドを左に動かす。
def left(steps):
    for i in range(steps):
        byj1.step()
        byj2.step()
        sleep_ms(4)

# ヘッドを右に動かす。
def right(steps):
    for i in range(steps):
        byj1.unstep()
        byj2.unstep()
        sleep_ms(4)

# ヘッドを上に動かす。
def up(steps):
    for i in range(steps):
        byj1.unstep()
        byj2.step()
        sleep_ms(4)

# ヘッドを下に動かす。
def down(steps):
    for i in range(steps):
        byj1.step()
        byj2.unstep()
        sleep_ms(4)

# 四角を描画
def square():
    up(1000)
    left(1000)
    down(1000)
    right(1000)

square()
