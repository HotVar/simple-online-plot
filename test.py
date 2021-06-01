import time

from SimpleOnlinePlot import SOP

if __name__ == '__main__':
    sop = SOP(api_port=8000,
              app_port=8080,
              type='2d_line',
              chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe')
    iter = 0
    val = 1.0
    while True:
        iter += 1
        val *= 0.9
        sop.meter(iter, val, periods=1)
        time.sleep(3)