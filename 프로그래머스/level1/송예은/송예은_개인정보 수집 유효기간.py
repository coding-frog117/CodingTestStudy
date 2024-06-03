def solution(today, terms, privacies):
    answer = []
    termsSet = {}
    t_year,t_mon,t_day = list(map(int,today.split('.')))
    
    # terms의 유효기간을 해시에 저장
    for i in terms:
        name,num = i.split()
        termsSet[name] = int(num)
    
    for idx,i in enumerate(privacies):
        date,name = i.split()
        # 각 개인정보 수집일을 연,월,일로 나눈다
        year,mon,day = list(map(int,date.split('.')))
        
        period = termsSet[name]
        # month를 추가하면서 확인, 12가 넘어가면 year올려줌
        mon += period
            
        if mon > 12:
            n,mod = divmod(mon,12)
            year += n
            if mod != 0:
                mon = mod
                
        print(year,mon,day)
        # 유효기간 최대일과 today 날짜 비교
        if t_year > year:
            answer.append(idx+1)
        elif t_year == year and t_mon > mon:
            answer.append(idx+1)
        elif t_year == year and t_mon == mon and t_day >= day:
            answer.append(idx+1)
        
    return answer