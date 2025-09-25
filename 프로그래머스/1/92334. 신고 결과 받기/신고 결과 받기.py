def solution(id_list, report, k):
    answer = []
    
    report_dic = {name : set() for name in id_list}
    
    for r in report:
        a, b = r.split()
        report_dic[b].add(a)
    
    email_count = {name: 0 for name in id_list}
    
    for user, reported in report_dic.items():
        if len(reported) >= k:
            
            for report_user in reported:
                email_count[report_user] += 1
        
    return [email_count[user] for user in id_list]