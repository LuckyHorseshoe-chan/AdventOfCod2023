with open('input.txt', 'r') as f:
  lines = f.readlines()

time, distance = int(''.join(lines[0][lines[0].find(':') + 1:].split())), int(''.join(lines[1][lines[1].find(':') + 1:].split()))
ways = 0
for j in range(1, time):
  if (time - j) * j >= distance:
    ways += 1
print(ways) 