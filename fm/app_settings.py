import json
with open('settings.json') as file:
    data= json.load(file)
data['base_directory']='zeeshan-TEST'
with open('settings.json','w') as file:
    json.dump(data,file)
