# 기본 변수 세팅
l, c = map(int, input().split())
ap = list(input().split())
ap.sort()
s = []
vi = [False] * c
vo = {"a", "e", "i", "o", "u"}

# 경우의수 탐색을위한 dfs 함수
def dfs(k):

    # 만약 탐색중인 문자열길이가 목표 문자열 길이와 같다면
    if len(s) == l:

        # 모음수를 카운팅
        vowel = 0
        for i in s:
            if i in vo:
                vowel += 1

        # 모음수가 1개이상, 자음수가 2개 이상이라면 출력
        if (vowel >= 1) & (len(s) - vowel >= 2):
            print("".join(s))
            return
    
    # 다음 문자 추가
    for i in range(k, c):
        if vi[i]:
            continue
        vi[i] = True
        s.append(ap[i])
        dfs(i + 1)
        s.pop()
        vi[i] = False

# dfs 실행
dfs(0)