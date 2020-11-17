# Huffman coding, creates n prefix codes

import heapq
from collections import defaultdict

def solution(n):
    dict = defaultdict(int)
    list = []
    count = 1
    for number in range(n):
        dict[number] += count
        count +=1

    heap = [[weight, [symbol, '']] for symbol, weight in dict.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    huff = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))
    for p in huff:
        list.append(p[1])
    return list

print(solution(100))
