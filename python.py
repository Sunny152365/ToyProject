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
