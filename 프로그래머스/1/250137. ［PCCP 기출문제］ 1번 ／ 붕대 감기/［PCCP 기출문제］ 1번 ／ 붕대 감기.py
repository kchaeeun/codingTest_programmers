def solution(bandage, health, attacks):
    attack_list = []
    health_d = health
    acc = 0
    for i in attacks:
        attack_list.append(i[0])
    print(attack_list)
        
    for i in range(attacks[-1][0]+1):
        print(i)
        if i not in attack_list:    # 공격 x
            acc += 1
            if health < health_d:
                health += bandage[1]
                health = min(health, health_d)      # 최대 체력을 초과하지 않도록 
                if acc == bandage[0]:
                    health += bandage[2]
                    health = min(health, health_d)      # 최대 체력을 초과하지 않도록 
                    acc = 0
                    
            # print("Acc "+str(acc))
            # print("health: " + str(health))
        else:
            for attack in attacks:
                if attack[0] == i:
                    acc = 0
                    health -= attack[1]
                    if health <= 0:     # 공격을 받아 체력이 0 이하가 되면 즉시 중지!
                        return -1
            # print("health: "+ str(health))
            # print("축적"+str(acc))
            
    return health