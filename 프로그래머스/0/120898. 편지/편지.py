# 문자열을 받으면 문자열의 길이 만큼 2를 곱한다
def count(datas):
    cnt=0
    for data in datas:
         cnt+=1
            
    return cnt
def solution(message):
    answer = count(message)*2
    return answer