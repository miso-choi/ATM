class ATMSequence:
    def insert_Card(self):
        user_data = None
        num = True
        exist = False
        idx = None
        print('\n[1단계 : 카드번호 입력]')
        while(num):
            print('\n고객님의 카드번호를 입력해주세요. ( - 를 제외한 16자리를 띄어쓰기 없이 입력해주세요.)')
            try:
                user_card_num = int(input()) # 오류 확인을 위해 임시로 int로 변환
                user_card_num = str(user_card_num)
                if len(user_card_num) == 16:
                    user_data = user_df.loc[user_df['card'] == user_card_num]
                    if user_data.shape[0] == 1: # 입력받은 카드번호 존재하면
                        idx = user_df.index[user_df['card'] == user_card_num].tolist()[0]
                        print('\n**카드번호 확인 완료**')
                        exist = True
                        break
                    else:
                        print('\n입력하신 카드번호는 존재하지 않습니다. 다시 입력하려면 1, 종료하려면 2를 입력해주세요.' )
                        while(1):
                            t = input()
                            if t=='1':
                                break
                            elif t=='2':
                                num = False
                                exist = False
                                break
                            else:
                                print('1 또는 2를 입력해주세요.(다시 입력하려면 1, 종료하려면 2)')
                                continue
                else:
                    print('\n16자리보다 적거나 많게 입력하였습니다. 카드번호(16자리)를 다시 입력해주세요.')
            except:  # str형 / float형 / 띄어서 입력시
                print('\n입력오류::: 0부터 9까지의 "정수"로 이루어진 16자리를 "띄어쓰기나 - 없이" 입력해주세요.')

        return exist, idx
    
    
    def check_PINnum(self,idx):
        try_num = 0
        print('\n[2단계: PIN number 입력]')
        check = False
        while(1):
            print('\n해당 카드의 PIN number를 입력해주세요.')
            pin = input()
            if user_df.iloc[idx][:]['pin'] == pin:
                print('\n**PIN number 확인 완료**')
                check = True
                break
            else:
                print('PIN number가 일치하지 않습니다.')
                try_num += 1
                if try_num == 5:
                    check = False
                    break
                    print('다시 입력하시겠습니까? (네: 1 입력, 아니오: 1이 아닌 아무거나 입력) (최대 5번 시도 가능)')
                    if input() == '1': 
                        continue
                    else:
                        check = False
                        break
        return check

    
    def select_Account(self,user_df,idx):
        print('\n[3단계: 계좌번호 확인]')
        print('\n카드의 계좌번호는 다음과 같습니다.')
        print(user_df.iloc[idx][:]['account'])
        keep_going = False
        print('계속 진행하겠습니까? (진행: 1 입력, 처음으로: 2 입력)')
        while(1):
            a = input()
            if a == '1':
                keep_going = True
                break
            elif a == '2':
                keep_going = False
                break
            else:
                print('1 또는 2를 입력해주세요.(진행: 1 입력, 처음으로: 2 입력)')
                continue
        return keep_going
    