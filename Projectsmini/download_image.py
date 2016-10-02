import random
import urllib.request

def download_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_image("https://scontent-sin6-1.xx.fbcdn.net/v/t1.0-9/13920847_316068188731574_651525078299592239_n.jpg?oh=99e03338612469eca169c417947af97a&oe=5867ED31")