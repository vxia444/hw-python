n = int(input())
max_set = set()

for _ in range(n):
    common_intersections = input().split("-")
    n1 = common_intersections[0].split(",")
    n2 = common_intersections[1].split(",")
    
    set1 = {x for x in range(int(n1[0]), int(n1[1])+1)}
    set2 = {x for x in range(int(n2[0]), int(n2[1])+1)}

    common1 = set1.intersection(set2)
    
    if len(common1) > len(max_set):
        max_set = common1

print(f"Най-дългото сечение е {max_set} с дължина {len(max_set)}")
