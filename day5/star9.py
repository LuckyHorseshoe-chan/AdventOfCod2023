with open('input.txt', 'r') as f:
  lines = f.readlines()

dic, new_dic = {}, {}
key_strings = [
    'seed-to-soil map:\n', 
    'soil-to-fertilizer map:\n', 
    'fertilizer-to-water map:\n', 
    'water-to-light map:\n',
    'light-to-temperature map:\n',
    'temperature-to-humidity map:\n',
    'humidity-to-location map:\n'
]
first, last = False, False

for line in lines:
  if line.find('seeds') > -1:
    first = True
    for x in line[line.find(':') + 1:].split():
        dic[int(x)] = -1
    continue
  if line in key_strings:
    continue
  if first:
    first = False
    continue
  if line == 'humidity-to-location map:\n':
    last = True
    continue
  if not len(line.split()) and not last:
    for key in dic.keys():
      if dic[key] == -1:
        new_dic[key] = -1
      else:
        new_dic[dic[key]] = -1
    dic = new_dic
    new_dic = {}
    continue
  dst, src, rng = [int(x) for x in line.split()]
  for key in dic.keys():
    if key >= src and key <= src + rng:
      dic[key] = dst + key - src
for key in dic.keys():
  if dic[key] == -1:
    dic[key] = key
print(min(dic.values()))