import json
import sys

hobby_data = dict()
with open('hobby.csv', 'r', encoding='utf-8') as f1,\
    open('user.csv', 'r', encoding='utf-8') as f2:
    for line1 in f1:
        line2 = f2.readline().strip()
        if not line2:
            line2 = None
        if line1 not in hobby_data:
            hobby_data[line1.strip()] = line2
    content = f2.read()
  

with open('hobby_result.json','w', encoding='utf-8') as f3:
    data=json.dumps(hobby_data, ensure_ascii=False)
    f3.write(data)
with open('hobby_result.json','r', encoding='utf-8') as f4:
    content=f4.read()
    result=json.loads(content)

print(result)