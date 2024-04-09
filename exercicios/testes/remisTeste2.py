n = int(input())
resp = set(input().split())

for i in range(1,n):
    s = set(input().split())
    resp = resp.difference(s)
ret = list(resp)

for i in range(len(ret)):
    ret[i] = int(ret[i])
ret.sort()
print(ret)