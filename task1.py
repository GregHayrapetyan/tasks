import simplejson as json
import yaml


def json_to_yaml_converter(json_file_name, yaml_file_name):
    global json_data
    try:
        f = open(json_file_name, 'r', encoding="utf8")
        json_data = json.load(f)
        f.close()
    except FileNotFoundError:
        print('File not founded or it\'s misconfigured ')

    f = open(yaml_file_name, 'w', encoding="utf8")
    f.write(yaml.dump(json_data, allow_unicode=True))
    f.close()


json_to_yaml_converter('json_file.json', 'yaml_file')
