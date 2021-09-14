result = 'Success'
response = 'Great'

out_to_json = "{'Response':, 'result':"
out_to_json = out_to_json[:12] + result + out_to_json[12:] + response + '}'
print(out_to_json)
