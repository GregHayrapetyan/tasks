import requests
import time
import concurrent.futures
import json
import os
import urllib.request

with open('task_urls.json') as jsonUrls:
    jsonData = json.load(jsonUrls)
    jsonData2 = jsonData['items']
    listUrls = [i['url'] for i in jsonData2]

t1 = time.perf_counter()
os.mkdir('web_images')
def download_image(img_url):
    try:
        if urllib.request.urlopen('http://google.com')==False:
            raise Exception
        else:
            img_bytes = requests.get(img_url).content
            img_name = img_url.split('/')[3]
            img_name = f'{img_name}.jpg'
            with open(f'web_images/{img_name}', 'wb') as img_file:
                img_file.write(img_bytes)
                print(f'{img_name} was downloaded...')
    except Exception:
        print('Connection is lost')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, listUrls)
if len(os.listdir('web_images')) == 0:
    os.rmdir('web_images')
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')