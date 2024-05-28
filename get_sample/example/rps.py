# from example.utils import myRandom
import random

import utils

# class RPS:

#     def __init__(self) -> None:
#         print(f'utils.py myRandom() 를 이용하여 가위바위보 객체를 생성합니다')

#     def play(self):
#         c = myRandom(1, 3)
#         p = input('가위', '바위', '보')
#         # 1: 가위, 2: 바위, 3: 보
#         rps = ['가위', '바위', '보']
#         if p == rps[c-1]:
#             print(f'컴퓨터: {rps[c-1]}, 당신: {p}, 비겼습니다')
#         elif p == rps[c % 3]:
#             print(f'컴퓨터: {rps[c-1]}, 당신: {p}, 당신이 이겼습니다')
#         else:
#             print(f'컴퓨터: {rps[c-1]}, 당신: {p}, 컴퓨터가 이겼습니다')



if __name__ == "__main__":
    c = utils.myRandom(1, 4)
    p = input('1, 2, 3:')
    # 1: 가위, 2: 바위, 3: 보
    if p == '1':
        you = '가위'  
    elif p == '2':
        you = '바위'
    else:
        you = '보'

    rps = ['가위', '바위', '보']
    if you == rps[c-1]:
        print(f'컴퓨터: {rps[c-1]}, 당신: {you}, 비겼습니다')
    elif you == rps[c%3]:
        print(f'컴퓨터: {rps[c-1]}, 당신: {you}, 당신이 이겼습니다')
    else:
        print(f'컴퓨터: {rps[c-1]}, 당신: {you}, 컴퓨터가 이겼습니다')
    