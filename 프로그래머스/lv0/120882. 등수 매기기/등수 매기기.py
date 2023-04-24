def solution(score):
    answer = []
    set_score = []
    
    # score를 각 과목 점수에서 과목의 평균값으로 수정
    for i in range(len(score)):
        score[i] = (score[i][0] + score[i][1]) / 2
    
    # score를 높은 순서대로 정렬
    set_score = sorted(score, reverse=True)
    
    # set_score (등수)로 score[j]의 등수를 answer에 추가 | 같은 값은 가장 높은 등수대로 나오기 때문에, 공동 등수 체크 가능
    for j in range (len(set_score)):
        answer += [set_score.index(score[j]) + 1]
    
    print(answer)
    
    return answer

