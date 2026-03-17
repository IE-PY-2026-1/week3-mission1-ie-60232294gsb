# 파일이름 : 60232294 신지웅 3주차 과제
# 작 성 자 : 신지웅
# 미션 1
# 1. 사용자 입력
name3 = str(input("이름을 입력하시오:"))
writing3 = int(input("당신의 글쓰기 점수를 입력하시오:"))
python3 = int(input("당신의 파이썬 점수를 입력하시오:"))
last_avg3 = float(input("당신의 지난학기 평균을 입력하시오:"))
diff3 = average3 - last_avg3

# 2. 계산
average3 = (writing3 + python3)/2

# 3. 출력
print(f"\n{name3} 학생의 글쓰기 점수는 {writing3}, 파이썬 점수는 {python3} 입니다.")
print(f"평균은 {average3} 이고, 지난 학기와의 차이는 {diff3} 입니다.")
