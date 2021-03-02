import simplejson as json
import yaml


def jsonToYamlConverter(jsonFileName, yamlFileName):
    global jsonData
    try:
        f = open(jsonFileName, 'r', encoding="utf8")
        jsonData = json.load(f)
        f.close()
    except FileNotFoundError:
        print('File not founded or it\'s misconfigured ')

    f = open(yamlFileName, 'w', encoding="utf8")
    f.write(yaml.dump(jsonData, allow_unicode=True))
    f.close()


jsonToYamlConverter('json_file.json', 'yaml_file')
