def str2num(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    res_dic = {}

    for rec in records:
        time_str, car, status = rec.split()
        t = str2num(time_str)

        if car not in res_dic:
            res_dic[car] = (t if status == "IN" else None, status, 0)
        else:
            btime, bstatus, tot = res_dic[car]
            if status == "IN":
                res_dic[car] = (t, "IN", tot)
            elif status == "OUT":
                duration = t - btime  
                res_dic[car] = (None, "OUT", tot + duration)

    END = 23 * 60 + 59
    for car, (btime, bstatus, tot) in list(res_dic.items()):
        if bstatus == "IN":
            res_dic[car] = (None, "OUT", tot + (END - btime))

    base_time, base_fee, unit_time, unit_fee = fees

    def calc_fee(total):
        if total <= base_time:
            return base_fee
        extra = total - base_time
        units = (extra + unit_time - 1) // unit_time
        return base_fee + units * unit_fee

    cars = sorted(res_dic.keys())
    return [calc_fee(res_dic[car][2]) for car in cars]
