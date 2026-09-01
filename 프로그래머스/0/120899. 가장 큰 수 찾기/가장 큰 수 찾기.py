def solution(array):
    answer = []
    max_num = max(array)
    max_index = array.index(max_num)
    
    answer = [max_num, max_index]
    return answer