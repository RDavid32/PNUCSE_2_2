n = int(input())
people_tree = {}
person_list = set()
boss_list = set()
for _ in range(n - 1):
    person, boss = input().split()
    if boss in people_tree:
        people_tree[boss].append(person)
    else:
        people_tree[boss] = [person]

    person_list.add(person)
    boss_list.add(boss)

boss = list(boss_list - person_list)[0]
people = list(boss_list | person_list)
subtree_count = {name: 0 for name in people}
depth_count = {name: 0 for name in people}

def count_subtree(person, count ):
    depth_count[person] =count
    if person in people_tree:
        for child in people_tree[person]:
            subtree_count[person] += 1 + count_subtree(child, count+1)
    return subtree_count[person]

count_subtree(boss,0)

people.sort(key = lambda x :(-subtree_count[x], depth_count[x],x))

for q in people:
    print(q)
    