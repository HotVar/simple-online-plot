# simple-online-plot
#### Drawing learning curves or any metrics.<br>
<img width="70%" src="https://github.com/HotVar/simple-online-plot/blob/main/Animation.gif"/><br>
---
## Environment
* Windows 10
* Google chrome

## Setup
### pip install
```
pip install -r requirements.txt
```
### npm install
```
cd app
npm install
```

## Test running
```
python test.py
```
``` python
import time
from SimpleOnlinePlot import SOP

sop = SOP(api_port=8000,
          app_port=8080,
          type='2d_line',
          chrome_path='C:/Program Files/Google/Chrome/Application/chrome.exe')
iter = 0
train_val = 1.0
valid_val = 1.0
while True:
    iter += 1
    train_val *= 0.8
    valid_val *= 0.9
    sop.meter(iter, train_val, valid_val)
    time.sleep(3)
```
