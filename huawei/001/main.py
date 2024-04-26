s = "A={1,3,5},B={2,4,6},R=1"

a, b, r = s.split("},")
a = list(map(int, a[3:].split(",")))
b = list(map(int, b[3:].split(",")))
r = int(r[2:])

print(a, b, r)
ans = []

i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] > b[j]:
        j += 1
    elif b[j]-a[i] <= r:
        ans.append(a[i], b[j])
        i += 1
