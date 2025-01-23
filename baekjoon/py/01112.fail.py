x, b = map(int, input().split())
ans = []
while x != 0:
    if b > 0:
        ans.append(x % b)
        x //= b
    else:
        if x > 0:
            ans.append(x % (-b))
            x = -(x // (-b))
        else:
            ans.append(-(b) - ((-x) % (-b)))
            x = ((-x) // (-b))
    print(ans)
    print(x)
ans.reverse()
print(ans)
print("".join(map(str, ans)))