import sys
import heapq
input = sys.stdin.readline

n = int(input())

papers = []
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

papers.append(paper)
white, blue = 0, 0

while len(papers) >= 1:
    paper = papers.pop()
    paper_sum = sum(map(sum, paper))

    if paper_sum == 0:
        white += 1
    
    elif paper_sum == len(paper) ** 2:
        blue += 1
    
    else:
        half = len(paper) // 2
        papers.append([row[:half] for row in paper[:half]])
        papers.append([row[half:] for row in paper[:half]])
        papers.append([row[:half] for row in paper[half:]])
        papers.append([row[half:] for row in paper[half:]])

print(white)
print(blue)