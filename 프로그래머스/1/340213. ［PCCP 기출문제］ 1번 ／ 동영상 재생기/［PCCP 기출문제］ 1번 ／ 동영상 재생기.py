def solution(video_len, pos, op_start, op_end, commands):
    pos_mm, pos_ss = map(int, pos.split(":"))
    cur_ss = pos_mm * 60 + pos_ss
    
    vl_mm, vl_ss = map(int, video_len.split(":"))
    max_ss = vl_mm * 60 + vl_ss
    
    ops_mm, ops_ss = map(int, op_start.split(":"))
    op_start_ss = ops_mm * 60 + ops_ss
    
    ope_mm, ope_ss = map(int, op_end.split(":"))
    op_end_ss = ope_mm * 60 + ope_ss
    
    for cmd in commands:
        if op_start_ss <= cur_ss <= op_end_ss:
            cur_ss = op_end_ss
            
        if cmd == "prev":
            cur_ss -= 10
            if cur_ss < 0:
                cur_ss = 0
            
        elif cmd == "next":
            cur_ss += 10
            if cur_ss > max_ss:
                cur_ss = max_ss
                
    if op_start_ss <= cur_ss <= op_end_ss:
        cur_ss = op_end_ss
    
    mm = cur_ss // 60
    ss = cur_ss % 60
    
    if mm < 10:
        mm = "0" + str(mm)
    if ss < 10:
        ss = "0" + str(ss)
    
    return str(mm) + ":" + str(ss)
    