
# int를 str로 바꾸고 4와 7이 포함된 문자를 찾으려고 했는데 2자리 넘어가는 경우는 어떻게 해야될지..? 

# 처음에는 4,7 포함된 숫자로 나눈 후 나머지가 0이 되는 수를 찾으려고 했지만 리스트생성이 안되서 에러남




# 검색

while True:
    flag = True              # flag 변수 : boolean 판단, 참
    for i in str(n):                    # str(n)안에 문자를 확인
        if i != '4' and i != '7':       # 만약 i에 4와 7이 없으면
            flag = False                # flag = False를 해주고, 
            n -= 1                      # 숫자를 하나씩 빼줌
    if flag:                # 만족하면
        print(n)            # 출력 
        break               # 멈춤
        

# for문에서 문자를 하나씩 확인하면서 4나 7이 있으면 17라인으로 갔다가 12라인으로 가서 for문 다시 수행
# 두 문자 다 있는 경우 17라인으로 가서 출력 

