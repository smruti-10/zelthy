import requests
import json
import pandas as pd
import xlsxwriter


result = requests.get('https://606f76d385c3f0001746e93d.mockapi.io/api/v1/auditlog')

# print(result.status_code)
# import pdb
# pdb.set_trace()
json_list = result.json()

id_val = []
desc_val = []
dt_val = []
act_val = []
u_id_val = []
criti_val = []
for i in json_list:
    id_val.append(i.get('id'))
    desc_val.append(i.get('description'))
    dt_val.append(i.get('date'))
    act_val.append(i.get('action'))
    u_id_val.append(i.get('user_id'))
    criti_val.append(i.get('criticality'))

writer = pd.ExcelWriter('data_from_api.xlsx', engine='xlsxwriter')

writer.save()

df = pd.DataFrame({'id': id_val,
                   'description': desc_val,
                   'date': dt_val,
                   'action': act_val,
                   'user_id': u_id_val,
                   'criticality': criti_val})

writer = pd.ExcelWriter('data_from_api.xlsx', engine='xlsxwriter')


df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()







# json_list = json.dumps(result.json())
# print(type(json_list))
#print(type(result.text))
#print(result.text)

# json_strings = result.text
# print(json_strings)
# dict_result = dict(json_strings)
# print(type(dict_result))
