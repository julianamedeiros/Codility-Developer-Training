#sets do not allow duplicates!

def solution(A):
    array = set(A)
    distinct_nums = len(array)
    return distinct_nums

print(solution([2, 1, 1, 2, 3, 1]))