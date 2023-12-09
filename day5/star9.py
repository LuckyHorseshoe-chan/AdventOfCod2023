with open('input.txt', 'r') as f:
  lines = f.readlines()
seeds, lines = lines[0], lines[2:]
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
last = False
for x in seeds[seeds.find(':') + 1:].split():
  dic[int(x)] = int(x)

for line in lines:
  if line in key_strings:
    continue
  if line == 'humidity-to-location map:\n':
    last = True
    continue
  if not len(line.split()) and not last:
    for key in dic.keys():
      new_dic[dic[key]] = dic[key]
    dic = new_dic
    new_dic = {}
    continue
  dst, src, rng = [int(x) for x in line.split()]
  for key in dic.keys():
    if key >= src and key <= src + rng:
      dic[key] = dst + key - src
print(min(dic.values())) #26273516