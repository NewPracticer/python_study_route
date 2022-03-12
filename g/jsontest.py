import json

json_str = '{"name":"iqiyi","age":18}'

student = json.loads(json_str)
print(type(student))
print(student)

test = [ {'name':'qiyue','age':18,'flag':True},
            {'name':'qiyue','age':18}
          ]
json_str = json.dumps(test)
print(json_str)

# JSON 、 JSON对象、 JSON字符串
