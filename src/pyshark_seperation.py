a = ["cat",12,"Dog",12.6,"Fish",True]
b = ["str"]
c = ["int"]
d = ["float"]
e = ["bool"]
for i in a:
    if type(i) == str:
        b.append(i)
    elif type(i) == int:
        c.append(i)
    elif type(i) == float:
        d.append(i)
    else:
        e.append(i)
print(b)
print(c)
print(d)
print(e)
