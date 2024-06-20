s = "c2g3987rnc87w76345967obw58tq"
product = 1
for i in range(len(s)):
    if s[i].isdigit() and int(s[i]) > 5:
        product += i
if product == 1:
    print(0)
else:
    print(product)