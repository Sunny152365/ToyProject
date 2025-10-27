Basic List Grammer

# 리스트 생성
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']

# 리스트에 원소 추가
movie_rank.append('배트맨')

# 리스트 특정 위치에 원소 추가
# insert(index, value)
movie_rank.insert(1, '슈퍼맨')

# 리스트에 원소 삭제
del movie_rank[1] # '스플릿' 삭제
"""
리스트에서 어떤 값을 삭제하면 남은 값들은 새로 인덱싱됩니다.
따라서 여러 값을 삭제할 때는 어떤 값이 먼저 삭제된 후 남은 원소들에 대해서 순서를 새로 고려한 후 삭제해야 한다.
"""

# 리스트 합치기
lang1 = ['C', 'C++', 'JAVA']
lang2 = ['Python', 'Go', 'C#']
langs = lang1 + lang2

# 리스트 최소값, 최대값
nums = [1, 2, 3, 4, 5, 6, 7]
min(nums)
max(nums)

# 리스트의 합
sum(nums)

# 리스트의 길이(저장된 데이터의 개수)
len(nums)

# 리스트의 평균
avg = sum(nums) / len(nums)

# 리스트 슬라이싱
price = ['20180728', 100, 130, 140, 150, 160, 170]
price_slicing = price[1:]

# 리스트 슬라이싱 응용, 홀수만 출력
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_slicing_odd = num[::2] # [0::2]과 동일한 의미

# 리스트 슬라이싱 응용, 짝수만 출력
num_slicing_even = num[1::2]

# 리스트 슬라이싱 응용, 역순으로 출력
num_slicing_reverse = num[::-1]

# 리스트 바인딩 출력
interest = ['삼성전자', 'LG전자', 'SK Hynix'. 'Naver']
print(interest[0], interest[3])

