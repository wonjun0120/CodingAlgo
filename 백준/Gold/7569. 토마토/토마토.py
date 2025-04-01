import sys
import collections

input = sys.stdin.readline

M, N, H = map(int, input().split())

stores = []
stack = collections.deque([])

is_complete = True
for h in range(H):
    layer = []
    for n in range(N):
        li = list(input().strip().split())
        for m, el in enumerate(li):
            if el == '1': stack.append((h, n, m, 0))
            if el == '0': is_complete = False

        layer.append(li)
        

    stores.append(layer)

if len(stores) < 1:
    print(-1)

if is_complete: 
    print(0)

else:
    answer = -1
    while stack:
        ch, cn, cm, time = stack.popleft()

        for dh, dn, dm in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            nh = dh + ch
            nn = dn + cn
            nm = dm + cm

            if nh < 0 or nh >= H: continue
            if nn < 0 or nn >= N: continue
            if nm < 0 or nm >= M: continue

            if stores[nh][nn][nm] == '-1': continue
            if stores[nh][nn][nm] == '1': continue
            if stores[nh][nn][nm] == '0': 
                answer = max(answer, time+1)
                stores[nh][nn][nm] = '1'
                stack.append((nh, nn, nm, time+1))

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if stores[h][n][m] == '0':
                    print(-1)
                    sys.exit(0)

    print(answer)

            

