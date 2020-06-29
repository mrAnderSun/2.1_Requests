import requests
import os


url = 'https://reddit.com/r/gifs/top.json'
headers = {'User-Agent': 'test'}
params = {'t': 'today'}
resp = requests.get(url, params=params, headers=headers)
resp.raise_for_status()
#print(resp)
resp_json = resp.json()
data = resp_json['data']
for child in data['children']:
    video_url = child['data']['url']
    filename = f"{child['data']['title']}.mp4"
    filename = os.path.join("gifs", filename)
    print(f'Processing {video_url}')
    if "i.imgur.com" not in video_url:
        #print("Currently not supporting")
        continue
    video_url = video_url.replace(".gifv", ".mp4")
    print('get video')
    resp = requests.get(video_url, stream=True)
    #print("video resp", resp.status_code)
    with open(filename, 'wb') as file:
        for chunk in resp:
            file.write(chunk)
            print(f"File {filename} download")
#print(req.status_code)
#rep = requests.get(r"https://yandex.translate.ru/")

#print(rep.text)
