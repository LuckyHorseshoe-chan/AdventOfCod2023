with open('input.txt', 'r') as f:
  lines = f.readlines()

time, distance = [int(x) for x in lines[0][lines[0].find(':') + 1:].split()], [int(x) for x in lines[1][lines[1].find(':') + 1:].split()]
res = 1
for i in range(len(time)):
  ways = 0
  for j in range(1, time[i]):
    if (time[i] - j) * j >= distance[i]:
      ways += 1
  res *= ways
print(res) # 303600