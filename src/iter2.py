inps = []
inp = ""
TRIGGER = "done"

while inp.lower() != TRIGGER:
  if inp:
    inps.append(inp)
  inp = input('input: ')
print(inps)
