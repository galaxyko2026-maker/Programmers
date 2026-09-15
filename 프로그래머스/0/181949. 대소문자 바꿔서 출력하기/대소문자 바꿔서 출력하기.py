str = input()

for s in str:
    if s.isupper():
        print(s.lower(), end="")  
        # end=""는 출력하고 나서 줄바꿈하지 말고 바로 옆에 이어 붙이라는 의미
    else:
        print(s.upper(), end="")



# str = input()
# print(str.swapcase())   #.swapcase():swap = 바꾸다, case = 대문자/소문자