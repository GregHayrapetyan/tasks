with open('task_urls.json', 'r') as jsonFile:
    json_obj = jsonFile.readlines()
json_obj = [(obj.rstrip()).lstrip()[:-1] for obj in json_obj[1:-1]]
print(json_obj)

