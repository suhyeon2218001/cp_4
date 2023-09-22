# 학생들의 점수 리스트
a = [90, 45, 64, 9, 17, 29]

# 결과를 저장할 빈 리스트
results = []

# 학생들의 점수를 학점으로 변환하여 결과 리스트에 추가
for score in a:
    if score >= 71:
        results.append('A')
    elif score >= 41:
        results.append('B')
    elif score >= 11:
        results.append('C')
    else:
        results.append('D')

# 결과 출력
print(results)

