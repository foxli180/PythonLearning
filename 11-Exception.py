s=input("input your age:")
if s=="":
    raise Exception("Input must not be emputy")

try:
    i=int(s)
except Exception as err:
    print(err)
finally:
    print("Bye!")
