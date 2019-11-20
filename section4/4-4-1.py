import simplejson as json

data = {}
data['people'] = []
data['people'].append({
    'name':'Kim',
    'website':'naver.com',
    'from':'Seoul'
})

data['people'].append({
    'name':'Park',
    'website':'google.com',
    'from':'Busan'
})

data['people'].append({
    'name':'Lee',
    'website':'daum.net',
    'from':'Seoul'
})

# print(data)

e = json.dumps(data)
print(type(e))
print(e)


d = json.loads(e)
print(type(d))
print(d)
