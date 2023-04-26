def solution(chicken):
    answer = 0

    coupon = chicken  # 쿠폰 = 여태 먹은 치킨의 양
    
    while coupon >= 10: # 쿠폰이 10장 이상일 때까지 While문 실행.
        
        service = coupon // 10 # 서비스 치킨은 쿠폰 10장 당 1마리
        answer += service
        coupon = coupon % 10 + service # 쿠폰은 서비스 주문 시 사용하고 남은 쿠폰 + 서비스로 시킨 치킨 마리 수 
        
        # 쿠폰이 10장 미만으로 남을 때까지 루프
        

    return answer