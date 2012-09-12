from copy import deepcopy
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
dy = deepcopy(x)

y['username'] = 'Test'
y['machines'].remove('bar')
print(x)
print(y)
print(dy)
