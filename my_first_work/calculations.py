a = float(input())
b = float(input())
kalk = (input())
c = 0

if kalk == ("+"):
    c = a+b
    print(c)
elif kalk == ("-"):
    c = a-b
    print(c)
elif (kalk == ("/")) and (b == 0) or (a == 0):
    print("Деление на 0!")
elif kalk == ("/"):
    c = a/b
    print(c)
elif (kalk == ("div")) and (b == 0) or (a == 0):
    print("Деление на 0!")
elif kalk == ("div"):
    c = a//b
    print(c)
elif kalk == ("*"):
    c = a*b
    print(c)
elif (kalk == ("mod")) and (b == 0) or (a == 0):
    print("Деление на 0!")
elif kalk == ("mod"):
    c = a % b
    print(c)
elif kalk == ("pow"):
    c = a**b
    print(c)