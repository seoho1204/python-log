def solution(numbers):
    sum=0
    cnt=0
    for i in numbers:
        sum+=i
        cnt+=1
    answer=sum/cnt
    # answer=sum(numbers)/len(numbers)
    return answer