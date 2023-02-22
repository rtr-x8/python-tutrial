a = "aaa"
a += "bbb"
print("a", a)

b = """アイウエオ
aaa
fff
ddd"""
print(b)

t = "i have a pen"
print(t.title())

c = """i have a
pen"""
print(c.split())
print(c.split('\n'))

print("moon" in "this is a moon")

print("i have a moon".find("i"))
print("i have a moon".find("c"))

print("I HAVE A PEN".lower())
print("I HAVE A PEN".lower().upper())

t = "this is a 40 percent apple."
for item in t.split():
    if item.isnumeric():
        print(item)

print("abc".startswith('a'))
print("abc".startswith('b'))
print("abc".endswith('c'))

print("have" in "I Have A Pen")
print("have" in "I Have A Pen".lower())

mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" %mass_percentage)

print("""aa: %s, bb: %s, cc: %s""" % ("1", "2", "3"))

print("aaa: {0}, bbb: {0}, ccc: {1}".format(1,2))

test = "test"
print(f"test var value is {test}")
test = round(100/6, 1)
print(f"test var value is {round(100/6, 1)}")

name = 'Ganymede'
planet = 'Mars'
gravity = '1.43'
template = """Gravity Facts about {name}
----------------------------------------
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

print(template)
print(template.format(name=name, planet=planet, gravity=gravity))
