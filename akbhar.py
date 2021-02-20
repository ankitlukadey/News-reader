import json
import time
import requests
url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=38830f25257a425595fd67f852675219')
response=requests.get(url)
news=json.loads(response.text)
from win32com.client import Dispatch
speak=Dispatch("SAPI.SpVoice")
i=1
speak.Speak(time.asctime(time.localtime(time.time())))
for new in news['articles']:
       speak.Speak(f"news number{i}")
       speak.Speak(new['title'])
       print({i},new['title'])
       print(new['url'])
       i=i+1
speak.Speak("Thank you")