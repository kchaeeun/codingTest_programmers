def solution(bandage, health, attacks):
    answer = 0
    cnt = 0
    basic_heal = health
    attack_d = {}
    for a in attacks:
        attack_d[a[0]] = a[1]
        
    for i in range(1,attacks[-1][0]+1):
        if i in attack_d.keys():
            health -= attack_d[i]
            cnt = 0
            print(health)
            
            if health <= 0:
                return -1
        else:
            health += bandage[1]
            cnt += 1
            if cnt == bandage[0]:       # 기술이 성공하면(끝나면) 다시 붕대를 감아서 성공시간이 0으로 초기화
                health += bandage[2]
                cnt = 0
            if health > basic_heal:
                health = basic_heal
            print(health)
            
    return health