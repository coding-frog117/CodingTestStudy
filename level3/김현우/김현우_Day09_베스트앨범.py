def solution(genres, plays):
    # 무식한 해싱/정렬 구현 문제
    play_count = {}

    for i in range(len(genres)):
        if genres[i] in play_count.keys():
            play_count[genres[i]] += plays[i]
        else:
            play_count[genres[i]] = plays[i]

    # [속한 장르 총 재생수, 노래 재생수, 고유번호, 장르별 노래 카운트수]
    data = [[play_count[genres[i]], plays[i], -i, 0] for i in range(len(genres))]
    data.sort(reverse=True)

    # 장르별 노래 2개씩만 솎아내기
    temp, temp_count = data[0][0], 1
    for i in range(len(data)):
        if data[i][0] == temp:
            data[i][3] = temp_count
        else:
            temp = data[i][0]
            data[i][3] = temp_count = 1
        temp_count += 1

    ans = [-data[i][2] for i in range(len(data)) if data[i][3] <= 2]

    return ans