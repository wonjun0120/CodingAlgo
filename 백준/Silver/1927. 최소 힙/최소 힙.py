import sys
input = sys.stdin.readline

n = int(input())

class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, x):
        self.heap.append(x)

        idx = len(self.heap) - 1
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break
    
    def pop(self):
        if len(self.heap) == 0:
            return 0
        
        num = self.heap[0]
        
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)

        idx = 0
        while True:
            left = idx * 2 + 1
            right = idx * 2 + 2

            min_idx = idx
            if left < len(self.heap) and self.heap[left] < self.heap[min_idx]:
                min_idx = left
            if right < len(self.heap) and self.heap[right] < self.heap[min_idx]:
                min_idx = right
            
            if min_idx == idx:
                break
            self.heap[idx], self.heap[min_idx] = self.heap[min_idx], self.heap[idx]
            idx = min_idx

        return num

heap = Heap()
for _ in range(n):
    x = int(input())
    if x == 0:
        print(heap.pop())
    else:
        heap.insert(x)