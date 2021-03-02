import requests
import time
import concurrent.futures
import json
import os
import urllib.request

with open('task_urls.json') as json_urls:
    json_data = json.load(json_urls)
    json_data2 = json_data['items']
    list_urls = [i['url'] for i in json_data2]

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
    executor.map(download_image, list_urls)
if len(os.listdir('web_images')) == 0:
    os.rmdir('web_images')
t2 = time.perf_counter()
print(f'Finished in {t2-t1} seconds')