import subprocess
import webbrowser
import time
import requests

class SOP():
    def __init__(self, api_port=8000, app_port=8080, type='2d_line'):
        self.api_port = api_port
        self.app_port = app_port
        self.api_url = f'http://127.0.0.1:{api_port}/api/meter/'
        self.type = type
        self.items = []

        self.p1 = subprocess.Popen(['python', './api/manage.py', 'runserver', f'{api_port}'], shell=True)
        self.p2 = subprocess.Popen(['cd', './app', '&', 'npm', 'run', 'serve', '--', '--port', f'{app_port}'], shell=True)
        time.sleep(5)

        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        url = f'http://127.0.01:{app_port}'
        webbrowser.register(chrome_path, None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get(chrome_path).open(url)

    def meter(self, iter, value, periods=1):
        # update own metrics
        item = {'iter': iter, 'value': value}
        self.items.append(item)

        # post new value to drf server on given periods
        if iter % periods == 0:
            res = requests.post(self.api_url, data=item)

    def get_result(self):
        return self.items
