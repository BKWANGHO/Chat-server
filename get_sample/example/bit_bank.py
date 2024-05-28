import datetime
import random        

today = datetime.datetime.now()

class Account:

    def __init__(self, name, account_number, money) -> None:
        '''
        [요구사항(RFP)]
        은행이름은 비트은행이다.
        입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
        계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성된다.
        예를들면 123-12-123456 이다.
        금액은 100 ~ 999 사이로 랜덤하게 입금된다. (단위는 만단위로 암묵적으로 판단한다)
        '''
        self.BANK_NAME = '비트은행'
        self.name = name
        self.account_number = account_number
        self.money = money

    def __str__(self):
        return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")} ' \
               f'은행 : {self.BANK_NAME}, ' \
               f'입금자: {self.name},' \
               f'계좌번호: {self.account_number},' \
               f'금액: {self.money} 만원'
    # __str__의 목적은 문자열화를 하여 서로 다른 객체 간의 정보를 전달하는 데 사용한다.
    
    # def __repr__(self):
    #     return f'날짜 : {today.strftime("%Y-%m-%d %H:%M:%S")} ' \
    #            f'은행 : {self.BANK_NAME}, ' \
    #            f'입금자: {self.name},' \
    #            f'계좌번호: {self.account_number},' \
    #            f'금액: {self.money} 만원' 
    # __repr__의 목적은 객체를 문자열화하여 객체 자체를 표현하는 데 사용한다.

    @staticmethod
    def creat_account_number(these: list):
            name = input('이름')
            money = input('입금액')
            account_number = f'{myRandom(1000, 10000)}-{myRandom(10, 100)}-{myRandom(100000, 1000000)}'
            money = money
            this = Account(name, account_number, money)
            print(f'__str__ 출력')
            print(f'{this} ... 개설되었습니다.')
            print(f'__repr__ 출력')
            print(f'{this}... 개설되었습니다.')
            these.append(this)
            return these
    
    @staticmethod
    def show_account_list(these: list):
        [ print(i) for i in these ]


    def deposit(self,these:list):
        print('계좌번호: ???? 입금액: ?? ')
        account_number = input('입금할 계좌번호')
        deposit = int(input('입금액')) # string -> int
            # 힌트 a.money + deposit
        for i, j in enumerate(these):
            if j.account_number == account_number:
                j[i].money += deposit
                break

    @staticmethod
    def find_account(ls, account_number):
        pass

    @staticmethod
    def del_account(ls, account_number):
        pass
        




def myRandom(start, end): return random.randint(start, end-1)

if __name__ == "__main__":
    these = []
    while 1 :
        menu = input('0.종료 1.계좌개설 2.계좌목록 3.입금 4.출금 5.계좌해지 6.계좌조회')
        if menu == '0':
            break
        if menu == '1':
            these = Account.creat_account_number(these)
        elif menu == '2':
            Account.show_account_list(these)
        elif menu == '3':
            Account.show_account_list(these)
        elif menu == '4':
            account_number = input('출금할 계좌번호')
            money = input('출금액')
            # 추가코드 완성
            for i, j in enumerate(ls):
                if j.account_number == account_number:
                    ls[i].money -= money
                    break
        elif menu == '5':
            Account.del_account(ls, input('탈퇴할 계좌번호'))
            for i, j in enumerate(ls):
                if j.account_number == account_number:
                    ls[i].remove()
                    break
        elif menu == '6':
            print(Account.find_account(ls, input('검색할 계좌번호') ))
            
        else:
            print('Wrong Number.. Try Again')
            continue