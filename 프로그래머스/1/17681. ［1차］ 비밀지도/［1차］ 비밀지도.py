def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        a, b = arr1[i], arr2[i]
        a = str(bin(a))[2:]
        b = str(bin(b))[2:]
        
        while len(a) < n:
            a = '0' + a
        while len(b) < n:
            b = '0' + b
                
        row = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                row += '#'
            else:
                row += ' '
        answer.append(row)
    
    return answer