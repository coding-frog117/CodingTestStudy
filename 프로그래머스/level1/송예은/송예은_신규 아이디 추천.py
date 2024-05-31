def solution(new_id):
    # 1단계 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계 허용되지 않은 문자 제거
    for i in range(len(new_id)):
        if not new_id[i].isalpha() and not new_id[i].isdigit() and new_id[i] not in ['-','_','.'] :
            new_id = new_id.replace(new_id[i],'특')
    new_id = new_id.replace('특','')
    
    # 3단계 마침표 하나로 제거
    for i in range(len(new_id),1,-1):
        new_id = new_id.replace('.'*i,'.')
        
    # 4단계 양 끝 마침표 제거
    if new_id[0] == '.' :
        if len(new_id) > 1:
            new_id = new_id[1:]
        else:
            new_id = ''
    if new_id != '' and new_id[-1] == '.' :
        if len(new_id) > 1:
            new_id = new_id[:-1]
        else:
            new_id = ''
    
    # 5단계 빈문자열 체크
    if new_id == '':
        new_id = 'a'
    
    # 6단계 최대 길이 체크
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계 최소 길이 보정
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]
    return new_id