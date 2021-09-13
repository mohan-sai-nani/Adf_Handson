import json

def write_to_json(file, dic):
    """Writes Data to Json file"""
    try:
        with open(file, 'w', encoding='utf-8') as json_file:
            json.dump(dic, json_file)
    except:
        print("Error")

remarks, result = 'Success', 'Good'
outputtojson = ''
if result == '':
    outputtojson = {'Response': result}
else:
    outputtojson = {'Response': result, 'Reason': remarks}
write_to_json('sample.json', outputtojson)