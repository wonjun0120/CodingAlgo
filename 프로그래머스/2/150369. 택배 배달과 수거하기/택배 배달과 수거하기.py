def solution(cap, n, deliveries, pickups):
    distance = 0
    last_delivery = n - 1  # 가장 먼 배달이 필요한 집
    last_pickup = n - 1  # 가장 먼 수거가 필요한 집

    while last_delivery >= 0 or last_pickup >= 0:
        # 가장 먼 배달, 수거할 위치 찾기
        while last_delivery >= 0 and deliveries[last_delivery] == 0:
            last_delivery -= 1
        while last_pickup >= 0 and pickups[last_pickup] == 0:
            last_pickup -= 1
        
        # 이번 이동에서 갈 수 있는 최적 거리 (배달과 수거 중 더 먼 곳)
        max_distance = max(last_delivery, last_pickup) + 1  # 인덱스가 0-based 이므로 +1

        # 배달 및 수거할 개수
        capacity = cap
        for i in range(last_delivery, -1, -1):  # 먼 곳부터 배달
            if capacity == 0:
                break
            if deliveries[i] > 0:
                if deliveries[i] <= capacity:
                    capacity -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= capacity
                    capacity = 0

        capacity = cap  # 트럭을 비우고 다시 채움
        for i in range(last_pickup, -1, -1):  # 먼 곳부터 수거
            if capacity == 0:
                break
            if pickups[i] > 0:
                if pickups[i] <= capacity:
                    capacity -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= capacity
                    capacity = 0

        # 이동 거리 추가 (왕복)
        distance += max_distance * 2

    return distance
