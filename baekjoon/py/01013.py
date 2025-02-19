# 라이브러리 세팅
import sys

# 맨 앞글자를 조건에 맞도록 잘라내는 함수, 만약 불가능하면 x반환, 모든 숫자를 잘라냈다면 o 반환
def cut(a):
    if a[0] == 0:
        if len(a) == 1:
            return "x"
        if a[1] == 0:
            return "x"
        return a[2:]
    else:
        if len(a) < 4:
            return "x"
        if (a[1] == 1) | (a[2] == 1):
            return "x"
        i = 3
        while a[i] == 0:
            i += 1
            if len(a) == i:
                return "x"
        while a[i] == 1:
            i += 1
            if len(a) == i:
                return "o"
        if len(a) > i + 1:
            if a[i + 1] == 0:
                if a[i - 2] == 1:
                    return a[i - 1:]
                return "x"
        return a[i:]
    
# 테스트 케이스 수 입력
for t in range(int(sys.stdin.readline())):

    # 문자열 입력
    n = list(map(int, list(sys.stdin.readline().strip())))

    # 문자열이 남아있는동안 반복
    while len(n) != 0:

        # 커팅후 n의값을 저장
        n = cut(n)  

        # 커팅 불가능이라면 NO출력
        if n == "x":
            print("NO")
            break

        # 커팅이 도중에 끝났다면 YES출력
        elif n == "o":
            print("YES")
            break

    # 문자열이 남아있지 않다면 YES출력
    else:
        print("YES")