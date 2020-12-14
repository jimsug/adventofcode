import re, itertools

demo = False
with open("2020/day_14/demo.txt" if demo else "2020/day_14/input.txt") as f:
  input = [i.split(" = ") for i in f.read().strip().split("\n")]

total = 0
mem = {}
for verb, arg in input:
  if verb == 'mask':
    mask = arg
  else:
    addr = int(re.findall('\[(\d+)\]', verb)[0])
    try:
      current = mem[addr]
    except KeyError:
      current = ['0'] * 36

    op = bin(int(arg))[2:].zfill(36) if int(arg)>0 else ''.join(['0'] * 36)

    for c in range(1, len(mask) + 1):
      if mask[-c] in '01':
        current[-c] = mask[-c]
      elif c <= len(op):
        current[-c] = op[-c]

    mem[addr] = current

if len(mem) > 0:
  for key, val in mem.items():
    total+=int(''.join(val), 2)
print('Part 1:', total)
print('----')

total = 0
mem = {}
for verb, arg in input:
  if verb == 'mask':
    mask = arg
  else:
    addr = bin(int(re.findall('\[(\d+)\]', verb)[0]))[2:].zfill(36)
    try:
      current = mem[addr]
    except KeyError:
      current = ['0'] * 36


    maskedAddr = ['0'] * len(addr)
    for i in range(1, len(maskedAddr)+1):
      if mask[-i] == '0':
        maskedAddr[-i] = addr[-i]
      else:
        maskedAddr[-i] = mask[-i]

    maskedAddr = ''.join(maskedAddr)
    allAddresses = []

    for i in itertools.product('01', repeat=maskedAddr.count('X')):
      thisAddress = maskedAddr
      flippedAddress = []
      nextSlice = 0
      for j in range(maskedAddr.count('X')):
        indexOf = thisAddress.index('X')
        flippedAddress.append(thisAddress[:indexOf])
        flippedAddress.append(i[j])
        thisAddress = thisAddress[indexOf+1:]

      flippedAddress.append(thisAddress)
      allAddresses.append(''.join(flippedAddress))

    for address in allAddresses:
      mem[int(address, 2)] = int(arg)

if len(mem) > 0:
  for key, val in mem.items():
    total+=val
print('Part 2:', total)
