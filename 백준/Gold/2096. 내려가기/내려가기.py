import sys
input = sys.stdin.readline

N = int(input().strip())
M = 3

first = list(map(int, input().split()))
max_dp = first[:]
min_dp = first[:]

for _ in range(1, N):
    row = list(map(int, input().split()))
    new_max = [0]*M
    new_min = [0]*M

    for j in range(M):
        cand = []
        if j-1 >= 0: cand.append(j-1)
        cand.append(j)
        if j+1 < M: cand.append(j+1)

        new_max[j] = row[j] + max(max_dp[k] for k in cand)
        new_min[j] = row[j] + min(min_dp[k] for k in cand)

    max_dp, min_dp = new_max, new_min

print(max(max_dp), min(min_dp))
