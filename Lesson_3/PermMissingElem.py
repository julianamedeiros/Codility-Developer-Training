
def solution(n):
    N = len(n) + 1
    expected_sum = N*(N+1)//2
    real_sum = sum(n)
    missing =  expected_sum - real_sum
    print(missing)


solution([3, 2, 1, 5])