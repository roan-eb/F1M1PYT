import time
import webbrowser
import random

for i in range (1000, 0, -1):
        print(i)
        time.sleep(0.002)

sites = random.choice(['www.youtube.com/watch?v=dQw4w9WgXcQ'])
visit = "https://{}".format(sites)
webbrowser.open(visit) 