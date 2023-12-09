with open('input.txt', 'r') as f:
  lines = f.readlines()
bids, nums = {}, {}
symbols = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
symbols.reverse()
for line in lines:
  card, bid = line.split() 
  bids[card] = int(bid)
  nums[card] = 0
  for i in range(len(card)):
    nums[card] += 13 ** (len(card) - 1 - i) * symbols.index(card[i])
nums = [x[0] for x in sorted(nums.items(), key=lambda x:x[1])]
five_of_a_kind, four_of_a_kind, full_house, three_of_a_kind, two_pair, one_pair, high_card = [], [], [], [], [], [], []
for num in nums:
  if len(set(num)) == 1:
    five_of_a_kind.append(num)
  elif len(set(num)) == 4:
    one_pair.append(num)
  elif len(set(num)) == 5:
    high_card.append(num)
  elif len(set(num)) == 2:
    if num.count(num[0]) == 3 or num.count(num[0]) == 2:
      full_house.append(num)
    else:
      four_of_a_kind.append(num)
  else:
    counts = [num.count(x) for x in num]
    if 3 in counts:
      three_of_a_kind.append(num)
    else:
      two_pair.append(num)
cards = high_card + one_pair + two_pair + three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind
total = 0
for i in range(len(cards)):
  total += (i + 1) * bids[cards[i]]
print(total) # 249748283