import sys
input = sys.stdin.readline

n, k = [int(x) for x in input().strip().split()]
hours = []
minsec = []

if k == 0:
    hours = [h for h in range(11, n + 1) if str(k) not in str(h)]
    minsec = [i for i in range(11, 60) if str(k) not in str(i)]
else:
    hours = [h for h in range(n + 1) if str(k) not in str(h)]
    minsec = [i for i in range(60) if str(k) not in str(i)]

hours = len(hours)
minsec = (60 * 60) - (len(minsec) * len(minsec))
tot = n + 1 - hours
print(
    (minsec * hours) + (tot * 60 * 60)
)
