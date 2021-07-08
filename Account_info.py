import random
import time

class Account_info:
    def get_UserName(self):
        print('\n[1단계: 성함 입력]')
        num = True
        while(num):
            print('성함을 입력해주세요.')
            name = input()

            while(1):
                try:
                    print('\n입력받은 성함은', name, '입니다. 맞으면 1, 틀리면 2를 입력해주세요.')
                    name_check =  int(input())

                    if name_check == 1:
                        num = False
                        break
                    elif name_check == 2:
                        print('\n다시 입력받겠습니다.')
                        break
                    else:
                        print('\n###  1이나 2가 아닌 다른 값을 입력받았습니다.  ###')
                        continue
                except:
                    print('\n###  1이나 2가 아닌 다른 값을 입력받았습니다.  ###')

        print('\n**이름 입력 완료**')
        return name
    
    
    def make_AccountNum(self):
        print('\n[2단계: 계좌번호 생성]')
        
        print('계좌번호 생성중...')
        # 현장감을 주기 위한 시간 지연(1초)
        time.sleep(1)
        
        # ○○은행 계좌번호 앞의 여섯 자리는 동일
        first_3_3 = '110123'
        # 뒤 6자리 난수 발생
        last_6= str(random.randrange(100000,999999))

        # 기존 계좌번호 데이터에서 중복 여부 확인
        while last_6 in list(user_df['account']):
            last_6= str(random.randrange(100000,999999))

        account_num = first_3_3 + last_6

        print('고객님의 계좌번호는',account_num,'입니다. 따로 메모해 두시기 바랍니다.')
        return account_num
    
    
    def get_PinNumber(self):
        print('\n[3단계: PIN number 입력]')
        print('ATM기 이용시, 계좌 본인 확인을 위해 PIN number를 입력받습니다. 앞으로 사용할 PIN number(4자리)를 입력해주세요. (단, 첫 숫자는 0 아닌 수)')
        while(1):
            try:
                pin_num_1 = int(input()) # 오류 확인을 위해 임시로 int로 변환
                pin_num_1 = str(pin_num_1)
                if len(pin_num_1) == 4:
                    print('\nPIN number 확인을 위해 한번 더 입력해주세요.')
                    pin_num_2 = input()
                    if pin_num_2 == pin_num_1:
                        print('\n**입력 확인 완료**')
                        break
                    else:
                        print('\n입력하신 번호가 일치하지 않습니다. PIN number(4자리)를 다시 입력해주세요.')
                        continue
                else:
                    print('\n4자리보다 적거나 많게 입력하였습니다. PIN number(4자리)를 다시 입력해주세요.')
            except:  # str형 / float형 / 띄어서 입력시
                print('\n입력오류::: 0부터 9까지의 "정수"로 이루어진 4자리를 "띄어쓰기 없이" 입력해주세요.')
        return pin_num_1
    
    
    def make_CardNum(self):
        print('\n[4단계: 카드번호 생성]')
        
        print('카드번호 생성중...')
        # 현장감을 주기 위한 시간 지연(1초)
        time.sleep(1)
        
        card_num = str(random.randrange(1000000000000000,9999999999999999))
        
        # 기존 카드번호 데이터에서 중복 여부 확인
        while card_num in list(user_df['card']):
            card_num= str(random.randrange(1000000000000000,9999999999999999))

        length=4
        card_num_print = '-'.join([''.join(x) for x in zip(*[list(card_num[z::length]) for z in range(length)])])
        print('고객님의 카드번호는',card_num_print,'입니다. 따로 메모해 두시기 바랍니다.')
        
        return card_num
    
    def Initiate_Balance(self):
        balance = 0
        return balance