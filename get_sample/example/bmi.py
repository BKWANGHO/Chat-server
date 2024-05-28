from example.utils import Member


class BMI():
    def __init__(self) -> None:
        '''utils.py / Members(), myRandom() 를 이용하여 BMI 지수를 구하는 계산기를 작성합니다.'''
        

    def getBMI(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.0
        this.weight = 80.5
        res = round(this.weight / this.height**2 *10000,2)
        
        return res