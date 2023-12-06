with open('input.txt', 'r') as f:
  lines = f.readlines()

points = [0 for i in range(len(lines))]
for line in lines:
  win_nums = set(line[line.find(':') + 1:line.find('|')].split())
  nums = set(line[line.find('|') + 1:].split())
  w = len(list(nums & win_nums))
  if w:
    points[i] += 2 ** (w - 1)
print(sum(points))