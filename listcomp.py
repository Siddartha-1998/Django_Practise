str = " garigipati sai siddartha kowshik"
inp = input("enter what letter you need.")
c = 0
for i in str:
    if inp in i:
        c += 1
print("count of str ",c)
inp = input(":")
def fun(inp):
    str = " garigipati sai siddartha kowshik"
    c = 0
    for i in str:
        if inp in i:
            c += 1
    return c

print(fun(inp))


