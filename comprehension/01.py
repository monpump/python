# # 리스트 컴프리핸션
# total = []
# for i in range(1,11):
#     total.append(i)

print([i+5 for i in range(1,11) ])

import random

total = []
print([ random.randint(1,10) for i in range(5)])

