with open('input.txt', 'r') as f:
  lines = f.readlines()
seeds, lines = lines[0][lines[0].find(':') + 1:].split(), lines[2:]
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
for i in range(0, len(seeds), 2):
  dic[(int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1)] = (int(seeds[i]), int(seeds[i]) + int(seeds[i+1]) - 1)

for line in lines:
  if line in key_strings:
    continue
  if line == 'humidity-to-location map:\n':
    last = True
    continue
  if not len(line.split()) and not last:
    for key in dic.keys():
        new_dic[dic[key]] = dic[key]
    dic = new_dic.copy()
    new_dic = {}
    continue
  dst, src, rng = [int(x) for x in line.split()]
  for key in dic.keys():
    if key[0] >= src and key[0] < src + rng and key[1] >= src + rng:
      new_dic[(key[0], src + rng - 1)] = (dst + key[0] - src, dst + rng - 1)
      new_dic[(src + rng, key[1])] = (src + rng, key[1])
    elif key[1] >= src and key[1] < src + rng and key[0] < src:
      new_dic[(src, key[1])] = (dst, dst + key[1] - src)
      new_dic[(key[0], src - 1)] = (key[0], src - 1)
    elif key[0] >= src and key[1] < src + rng:
      new_dic[(key[0], key[1])] = (dst + key[0] - src, dst + key[1] - src)
    elif key[0] < src and key[1] >= src + rng:
      new_dic[(src, src + rng - 1)] = (dst, dst + rng - 1)
      new_dic[(key[0], src - 1)] = (key[0], src - 1)
      new_dic[(src + rng, key[1])] = (src + rng, key[1])
    else:
      new_dic[key] = dic[key]
  dic = new_dic.copy()
  new_dic = {}
values = [v[0] for v in dic.values()]
print(min(values)) # 34039469