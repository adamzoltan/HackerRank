from collections import Counter

char_count = Counter(input())

three_most_common = sorted(char_count.items(), key=lambda x: (-x[1],x[0]))[:3]

for n in three_most_common:
    print(n[0], n[1])