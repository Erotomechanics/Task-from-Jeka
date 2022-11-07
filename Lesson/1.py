d = {}
for i in range(int(input())):
    s = input().split()
    d.setdefault(s[0], s[1])
s1 = input()
for k,v in d.items():
    if v == s1:
        print(k)
    elif k == s1:
        print(v)
