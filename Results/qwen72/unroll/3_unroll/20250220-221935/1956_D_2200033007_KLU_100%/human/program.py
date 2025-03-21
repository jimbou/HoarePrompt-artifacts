#from functools import cache
from typing import List, Tuple
 
n = int(input())
arr = list(map(int, input().split()))
 
 
res_dict = {}
def get_max_possible_value(start_index: int, end_index: int) -> int:
    key = (start_index, end_index)
    if key in res_dict:
        return res_dict[key]
    if start_index == end_index:
        res_dict[key] = max(1, arr[start_index])
        return max(1, arr[start_index])
    res = (end_index - start_index + 1) ** 2
    for i in range(start_index + 1, end_index):
        new_res = get_max_possible_value(start_index, i - 1) + get_max_possible_value(i + 1, end_index) + arr[i]
        res = max(res, new_res)
    res = max(res, arr[start_index] + get_max_possible_value(start_index + 1, end_index))
    res = max(res, arr[end_index] + get_max_possible_value(start_index, end_index - 1))
    res_dict[key] = res
    return res
 
 
def get_changes(start_index: int, end_index: int) -> List[Tuple[int, int]]:
    max_value = get_max_possible_value(start_index, end_index)
    length = end_index - start_index + 1
    if length == 1:
        if arr[start_index] > 0:
            return []
        return [(start_index, start_index)]
    if max_value == length ** 2:
        res = []
 
        def make_stairs(i:int) -> None:
            is_already_stairs = True
            for j in range(i + 1):
                if arr[start_index + j] != j:
                    is_already_stairs = False
            if is_already_stairs:
                return
            if i == 0:
                res.append((start_index, start_index))
                arr[start_index] = 1
                return
            if arr[start_index + i] == i:
                make_stairs(i - 1)
            else:
                make_stairs(i - 1)
                res.append((start_index, start_index + i))
                for j in range(start_index, start_index + i + 1):
                    arr[j] = i
                make_stairs(i - 1)
        make_stairs(length - 1)
        res.append((start_index, end_index))
        return res
 
    else:
        for i in range(start_index + 1, end_index):
            temp_res = get_max_possible_value(start_index, i - 1) + get_max_possible_value(i + 1, end_index) + arr[i]
            if temp_res == max_value:
                return get_changes(start_index, i - 1) + get_changes(i + 1, end_index)
        if arr[start_index] + get_max_possible_value(start_index + 1, end_index) == max_value:
            return get_changes(start_index + 1, end_index)
        elif arr[end_index] + get_max_possible_value(start_index, end_index - 1) == max_value:
            return get_changes(start_index, end_index - 1)
 
 
 
res = get_max_possible_value(0, n - 1)
changes = get_changes(0, n - 1)
print(res, len(changes))
for a, b in changes:
    print(a + 1, b + 1)