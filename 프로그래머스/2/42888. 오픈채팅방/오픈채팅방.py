def solution(record):
    uid2name = {}
    msg = []
    for rec in record:
        rec = rec.split()
        if len(rec) == 2:
            status, uid = rec
            m = "님이 나갔습니다."
            msg.append((uid, m))
            
        if len(rec) == 3:
            status, uid, nickname = rec
            uid2name[uid] = nickname
                
            if status == "Enter":
                m = "님이 들어왔습니다."
                msg.append((uid, m))
        
    return [uid2name[n] + m for n, m in msg]
    
    