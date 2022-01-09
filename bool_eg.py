


a = True
b = False
c = True
d = False

if a and b:
    print("T and F")

if a or b:
    print("T or F")

if a and c:
    print("T and T")

if b or d:
    print("F or F")

mon = 32
tue = 40
wed = 65

if tue > mon and tue < wed:
    print("Tuesday is good for shopping.")

if wed > mon and wed > tue:
    print("Wednesday is hottest")

if wed > mon \
        or wed > mon + tue\
        or mon > tue + wed\
        or tue > wed + mon:
    print("High diff in temperature.")

# booleans - w3school
