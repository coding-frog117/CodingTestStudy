from itertools import permutations


# DFS 등의 그래프 탐색을 통해 가능한 아이디를 탐색하는 방법이 있지만,
# 여기서는 파이썬의 permutations 모듈을 통해 브루트포스 전수탐색

# 해당 user가 ban일 수 있는지 아닌지 판정
def is_valid(user, ban):
    if len(user) != len(ban):
        return False

    for i, j in zip(user, ban):
        if j == "*":
            continue
        if i != j:
            return False

    return True


def solution(user_id, banned_id):
    answer = []

    # 가능한 user_id 리스트 permutation으로 전부 뽑아놓고 탐색
    for id_list in permutations(user_id, len(banned_id)):
        is_banned = True

        for u_id, ban_id in zip(id_list, banned_id):
            if not is_valid(u_id, ban_id):
                is_banned = False

        if is_banned:
            if not set(id_list) in answer:
                answer.append(set(id_list))

    return len(answer)