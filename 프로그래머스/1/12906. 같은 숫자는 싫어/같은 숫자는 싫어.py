def solution(arr):
    answer = []

    for num in arr:
        if len(answer) == 0: #answer의 숫자 갯수가 0이면,
            answer.append(num)
            
        elif answer[-1] != num: # answer[-1]	answer의 마지막 값
            answer.append(num)

    return answer