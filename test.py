# .py파일 불러오기
from Account_info import Account_info
from ATMSequence import ATMSequence
import pandas as pd
import random

def MakeAccount(user_df):
    print('<<< 계좌 생성 모드 >>>')
    print('계좌를 생성합니다.')
    
    acc_info = Account_info()
    
    name = acc_info.get_UserName()
    account_num = acc_info.make_AccountNum()
    pin_num = acc_info.get_PinNumber()
    card_num = acc_info.make_CardNum()
    balance = acc_info.Initiate_Balance()
    
    new_data = {
        'account' : account_num,
        'pin' : pin_num,
        'card' : card_num,
        'name' : name,
        'balance': balance
    }

    user_df = user_df.append(new_data,ignore_index=True)
    return user_df


def SubMenu(user_df,idx):
    
    while(1):
        print('\n원하는 메뉴를 선택해주세요.')
        print('[잔액조회] => 1 입력')
        print('[  예금  ] => 2 입력')
        print('[  출금  ] => 3 입력')
        print('(종료시, 0 입력) ')
        
        user_sub = input() 
        if user_sub == '0':
            print9=('메뉴 선택을 종료합니다..')
            break
        
        elif user_sub  == '1':
            print('\n[잔액조회]')
            print('고객님 계좌의 잔액은 $',user_df.iloc[idx][:]['balance'],'입니다.')
            print('\n메뉴 선택 화면으로 돌아갑니다..')
            continue
   
        elif user_sub  == '2':
            print('\n[  예금  ]')
            while(1):
                print('예금하실 금액(단위:$, 숫자만 입력)을 입력해주세요. (예금액은 0보다 큰 정수값만 가능합니다.) (종료: -1 입력)')
                depo_input = input()

                try:
                    depo_input = int(depo_input)
                    if depo_input > 0: # 정상 입력
                        user_df.iloc[idx][:]['balance'] += depo_input
                        print('예금 후 잔액은 $',user_df.iloc[idx][:]['balance'],'입니다.')
                        print('\n메뉴 선택 화면으로 돌아갑니다..')
                        break
                    elif depo_input == 0:
                        print('입력오류::: $0은 예금하실 수 없습니다.')
                        continue
                    elif depo_input == -1:
                        print('예금을 종료합니다..')
                        break
                    elif (depo_input < 0) & (depo_input != -1):
                        print('입력오류::: 음수값은 예금하실 수 없습니다.')
                        continue
                except:
                    print('입력하신 금액은 정수값이 아닙니다.')
        
        elif user_sub  == '3':
            print('\n[  출금  ]')
            while(1):
                print('출금하실 금액(단위:$, 숫자만 입력)을 입력해주세요. (출금액은 0보다 큰 정수값만 가능합니다.) (종료: -1 입력)')
                with_input = input()

                try:
                    with_input = int(with_input)
                    if with_input > 0: # 정상 입력
                        if user_df.iloc[idx][:]['balance'] >= with_input: # 잔액 충분
                            user_df.iloc[idx][:]['balance'] -= with_input
                            print('출금 후 잔액은 $',user_df.iloc[idx][:]['balance'],'입니다.')
                            print('\n메뉴 선택 화면으로 돌아갑니다..')
                            break
                        else:
                            print('잔액이 부족하여 출금할 수 없습니다. 잔액보다 작거나 같은 금액을 입력해주세요.')
                            print('고객님 계좌의 잔액은 $',user_df.iloc[idx][:]['balance'],'입니다.')
                            continue
                    elif with_input == 0:
                        print('입력오류::: $0은 출금하실 수 없습니다.')
                        continue
                    elif with_input == -1:
                        print('출금을 종료합니다..')
                        break
                    elif (with_input < 0) & (with_input != -1):
                        print('입력오류::: 음수값은 출금하실 수 없습니다.')
                        continue
                except:
                    print('입력하신 금액은 정수값이 아닙니다.')
                    
        else:
            print('다음 값으로 입력해주세요. ( 잔액조회(1), 예금(2), 출금(3), 종료(0) )')

                    
    return user_df


def ATMcontroller(user_df):
    
    atm = ATMSequence()
    exist, idx = atm.insert_Card()
    check = False
    ready = False
    if exist == True:
        print('idx:',idx)
        check = atm.check_PINnum(idx)
        if check:
            keep_going = atm.select_Account(user_df,idx)
            if keep_going:
                ready = True

    return ready,idx  # 초기값: None으로 설정




if __name__ == "__main__":
    print('안녕하세요. ○○은행을 이용해 주셔서 감사합니다.')
    user_df = pd.DataFrame(columns = ['account','pin', 'card','name','balance'])  # user_df 저장된거로 하도록.
    try_num = 0
    while(1):
        print('\n\n계좌 만들기를 원한다면 1을, 잔액조회/예금/출금을 원한다면 2를 입력해주세요. (종료시, 0 입력) (관리자모드: 99 입력)')
        if try_num == 5:
            print('(관리자모드 - 비활성화)')
        try:
            a = int(input())
            if a == 0:
                break
            elif (a == 99) & (try_num < 5):
                while(1):
                    print('관리자 key값을 입력하시오.')
                    input_key = input()
                    if input_key == 'EWHA':
                        print('관리자모드로 전환합니다...')
                        print(user_df)
                        break
                    else:
                        print('key값이 일치하지 않습니다.') 
                        try_num += 1
                        if try_num == 5:
                            break
                        print('다시 시도하시겠습니까? (네: 1 입력, 아니오: 1이 아닌 아무거나 입력) (최대 5번 시도 가능)')
                        if input() == '1': 
                            continue
                        else:
                            break
                            
        
            elif a == 1:
                user_df = MakeAccount(user_df)
                print('\n**계좌 생성 완료** ')
                print('처음 화면으로 돌아갑니다..')
                continue
            elif a == 2:
                print('<<< ATM Controller 모드 >>>')
                while(1):
                    print('ATM기를 시작합니다. 계좌 서비스를 이용하시려면 ○○은행에서 만든 고객님 명의의 계좌가 있어야 합니다.(계속진행: 1 입력, 돌아가기: 2 입력)')
                    temp = input()
                    if temp == '1':
                        break
                    elif temp == '2':
                        break
                    else:
                        print('1 또는 2를 입력해주세요.')
                        continue
                if temp == '1':
                    ready,idx = ATMcontroller(user_df)
                    if ready:
                        user_df = SubMenu(user_df,idx)
                    #user_df  # 나중에 삭제(확인용)
                print('처음 화면으로 돌아갑니다..')
                continue
            else:
                print('\n###  1이나 2가 아닌 다른 값을 입력받았습니다.  ###')
                continue
        except:
            print('\n###  1이나 2가 아닌 다른 값을 입력받았습니다.  ###')
            continue
