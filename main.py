# 파일이름 : 60232294 신지웅 3주차 과제
# 작 성 자 : 신지웅
# 미션 1
# 1. 사용자 입력
name2 = str(input("이름을 입력하시오:"))
writing2 = int(input("당신의 글쓰기 점수를 입력하시오:"))
python2 = int(input("당신의 파이썬 점수를 입력하시오:"))
last_avg2 = float(input("당신의 지난학기 평균을 입력하시오:"))

# 2. 계산
average2 = (writing2 + python2)/2

# 3. 출력
print(f"\n{name2} 학생의 글쓰기 점수는 {writing2}, 파이썬 점수는 {python2} 입니다.")
print(f"평균은 {average2} 이고, 지난 학기와의 차이는 {average2 - last_avg2 } 입니다.")
