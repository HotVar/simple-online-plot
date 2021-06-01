import time

from SimpleOnlinePlot import SOP

if __name__ == '__main__':
    sop = SOP()
    iter = 0
    val = 1.0
    while True:
        iter += 1
        val *= 0.9
        sop.meter(iter, val, periods=3)
        time.sleep(3)