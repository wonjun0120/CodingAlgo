def str2int(s):
    hh, mm = s.split(":")
    return int(hh) * 60 + int(mm)

def time2fee(fees, time):
    btime, bfee, utime, ufee = fees
    
    if btime >= time:
        return bfee
    
    time -= btime
    a, b = divmod(time, utime)
    if b > 0:
        a += 1
    return bfee + (a * ufee)

def solution(fees, records):
    carfee = {}
    
    for rec in records:
        time, car, status = rec.split()
        time = str2int(time)
        car = int(car)
        
        if car not in carfee:
            carfee[car] = (time, 0)
        
        else:
            intime, tot = carfee[car]
            
            if status == "IN":
                carfee[car] = (time, tot)
            else:
                tot += (time - intime)
                carfee[car] = (-1, tot)

    answer = []
    for car in sorted(carfee.keys()):
        intime, tot = carfee[car]
        if intime != -1:
            tot += (str2int("23:59") - intime)
        fee = time2fee(fees, tot)
        answer.append(fee)
    return answer