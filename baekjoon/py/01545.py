# 기본 변수 세팅
n = list(input())
range = len(n)
alpha = [0] * 26
end = [0] * 26
for i in n:
    alpha[ord(i) - 97] += 1
ans = []
ans2 = []
ans3 = []
i = 0

# 만약에 특정 글자가 글자 전체 길이의 절반을 넘는다면 안티 팰린드롬이 불가능하므로 -1 출력
if max(alpha) > (range + 1) // 2:
    print(-1)
    exit(0) 

# 사전순으로 가장 앞서는 답을 만들어야 하므로 절반까지는 글자들중 a에 가까운 순서로 삽입
while len(ans) < ((range + 1) // 2):
    if alpha[i] > 0:
        ans.append(chr(i + 97))
        alpha[i] -= 1
    else:
        i += 1

# 만약에 길이가 홀수라면 코드의 편의를 위해 중간 글자는 ans2로 이동
if range % 2 == 1:
    ans2.append(ans.pop())

# 이제 중간 이후의 글자는 겹치지 않으며 사전순으로 가자앞서도록 삽입
count = 1
while alpha != end:

    # 현재까지 남아있는 글자들중 사전순으로 가장 앞서는 글자를 찾기위해 i를 이동
    while alpha[i] == 0:
        i += 1
    
    # j를 i로 설정후에 안티 팰린드롬이 성립하며 사전순으로 가장 앞서도록 j 세팅
    j = i
    while (ans[len(ans) - count] == chr(j + 97)) | (alpha[j] == 0):
        j += 1

    # j값에 맞춰 글자를 추가하고 남아있는 글자에서 삭제, 또한 카운트를 하나 증가
    alpha[j] -= 1
    ans3.append(chr(j + 97))
    count += 1

# 나눠서 구한 답 세개를 합쳐서 출력
print("".join(ans + ans2 + ans3))