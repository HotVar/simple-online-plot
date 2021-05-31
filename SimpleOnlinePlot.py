import subprocess
import webbrowser
import time
import requests

class SOP():
    def __init__(self, api_port=8000, app_port=8080, type='2d_line'):
        self.api_port = api_port
        self.app_port = app_port
        self.api_url = f'http://localhost:{api_port}/'
        self.type = type
        self.values = []

        self.p1 = subprocess.Popen(['python', './api/manage.py', 'runserver', f'{api_port}'], shell=True)
        self.p2 = subprocess.Popen(['cd', './app', '&', 'npm', 'run', 'serve', '--', '--port', f'{app_port}'], shell=True)
        time.sleep(5)

        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
        url = f'http://localhost:{app_port}'
        webbrowser.register(chrome_path, None, webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get(chrome_path).open(url)
        while True:
            pass

    def meter(self, val):
        # update own metrics
        self.values.append(val)
        # post new value to drf server
        res = requests.post(self.api_url, data=val)
        print(res)

if __name__ == '__main__':
    sop = SOP()
    sop.meter()