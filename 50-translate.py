import string
s = 'abcdefghijklmnopqrstuvwxyz'
table = s.maketrans('cs', 'kz')
s.translate(table)
print(s)

