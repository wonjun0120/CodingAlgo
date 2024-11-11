def solution(bandage, health, attacks):
    max_time = attacks[-1][0]
    cur_health = health
    cur_attack_idx = 0
    success = 0
    b_time, heal, add_heal = bandage
    
    
    for cur_time in range(max_time + 1):
        cur_attack = attacks[cur_attack_idx]
        if cur_health <= 0:
            return -1
        
        if cur_attack[0] == cur_time:
            success = 0
            cur_attack_idx += 1
            
            cur_health -= cur_attack[1]
            print(cur_time, "attack", "-" + str(cur_attack[1]), cur_health)
        
        else:
            success += 1
            cur_health = min(cur_health + heal, health)
            
            if success >= b_time:
                cur_health = min(cur_health + add_heal, health)
                success = 0
            print(cur_time, "heal", success, cur_health)
    
    if cur_health <= 0:
        return -1
    return cur_health
        