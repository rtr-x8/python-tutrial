# https://learn.microsoft.com/ja-jp/training/modules/python-math-operators/2-what-are-operators


print(30 / 12)
print(30 // 12)
print(30 % 12)

demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

print(abs(-5))
print(abs(5))

from math import ceil, floor

print(ceil(123.45))
print(floor(123.45))

li = [1,2,3,4,5]
print(max(li))
print(min(li))
print(li[2:4])
print(li[2:400])
print(li[2:])

print([1,2,3]+[5,6,7])

asda = [3, 2, 4, 5, 1]
aaa = asda.sort()
print(asda)
aaa = asda.sort(reverse=True)
print(asda)

a = ["a", "b", "c", "d"]
print(a.index('b'))
print(a[0:a.index('c')])
