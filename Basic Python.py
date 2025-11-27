#01 인터프리터 언어 : 소스 코드를 한 줄씩 읽어서 바로 실행하는 언어
print("Hello World!")

#02 텍스트 에디터 : 라인 번호
print('안녕하세요')
a = 1
b = 1
print(a + b)

#03 변수명 만들기 : 변수명의 첫 문자는 _또는 영문자, 대소문자 구분, 숫자 사용 가능(단, 첫 문자 제외)
_myname = 'samsjang'
my_name = '홍길동'
MyName2 = 'Hong gil-dong'
counter = 1
Counter = 2

#04 변수에 값 대입하기 : 따로 자료형태 선언 없이 값 대입 시 자동으로 자료형 결정
number1 = 1
pi = 3.14
flag = True
char = 'x'
chars = 'I love Python'

#05 주석 # 
# 만든 날짜 : 2025.11.23
a = 1
b = 5
print(a+b)

#06 자료형
int_data = 1                            # 정수 선언
float_data = 3.14                       # 실수 선언
complex_data = 1 + 5j                   # 복소수 선언
str_data1 = 'I love Python'             # 문자열 선언(영문)
str_data2 = "반갑습니다."                  # 문자열 선언(한글)
list_data = [1, 2, 3]                   # 리스트 선언  
tuple_data = (1, 2, 3)                  # 튜플 선언 (요소 값 변경 불가)
dict_data = {0:'False', 1:'True'}       # 딕셔너리 선언

#07 자료형 출력(print)
a = 200
msg = "I love Python"
list_data = ['a', 'b', 'c']
dict_data = {'a':97, 'b':98}
print(a)
print(msg)
print(list_data)
print(dict_data[0])
print(dict_data)
print(dict_data['a'])
print('#', end="")
print('#')

#08 들여쓰기 : space bar 4칸, tab 1칸
listdata = ['a', 'b', 'c']
if 'a' in listdata:
    print('a가 listdata에 있습니다.')
    print(listdata)
else:
    print('a가 listdata에 존재하지 않습니다.')
    
#09 if-else문
x = 1
y = 2
if  x >= y:
    print("x가 y보다 크거나 같습니다.")
else:
    print("x가 y보다 작습니다.")
"""
조건이 참인 경우만 특정 코드를 실행하는 로직 (if문만 사용)
if 조건:
    실행 코드
"""

#10 if-elif문
x = 1
y = 2
if x > y:
    print('x가 y보다 큽니다.')
elif x < y:
    print('x가 y보다 작습니다.')
else:
    print('x와 y는 같습니다.')

"""
for문   : 범위가 지정된 자료나 반복 가능한 객체를 이용해 반복문을 수행하는 것
while문 : 특정 조건을 만족하는 경우 지속적으로 반복을 수행하는 반복문
"""

#11 for문(범위 설정 가능한 것 : 시퀀스 자료형, 반복 가능한 자료, 문자열, 리스트나 튜플, 사전, range(), 그 외에 반복 가능한 객체)
str = 'abcedf'
for a in str:
    print(a)
scope = [1,2,3,4,5]
for x in scope:
    print(x)
ascii_codes = ['a':97, 'b':98, 'c':99]
for c in a ascii_codes:
    print(c)
for d in range(10):
    print(d)
    
#12 for-continue-break문
scope = [1,2,3,4,5]
for x in scope:
    print(x)
    if x < 3:
        continue    # 다음 반복문 실행
    else:
        break       # for 반복문 탈출
scope = [1,2,3,4,5]
for x in scope:
    print(x)
    if x >= 3:
        break
    
#13 for-else문(break에 의해 중단됨이 없이 정상적으로 모두 실행되어야만 특정 코드를 실행하게 할 경우)
scope = [1,2,3]
for x in scope:
    print(x)
    #break
else:
    print('Perfect')
    
#14 while-continue-break문
x = 0
while x < 10:
    x = x + 1
    if x < 3:
        continue
    print(x)
    if x > 7:
        break
# 정수 1부터 n까지 더할 때 그 합이 10만보다 커지게 되는 n을 구하는 것
x = 1
total = 0
while 1:     # 조건 자체가 참, while 반복문을 무한 반복
    total = total + x
    if total > 100000:
        print(x)
        print(total)
        break
    x = x + 1
    
#15 None(Types.NoneType) 자료형 : 값이 없음을 나타내는 자료형
val = None
condition = 1
if condition == 1:
    val = [1,2,3]
else:
    val = 'I love Python'
    
#16 정수형 자료
int_data = 10
bin_data - 0b10
oct_data = 0o10
hex_data = 0x10
long_data = 1234567890123456789
print(int_data)
print(bin_data)
print(oct_data)
print(hex_data)
print(long_data)

#17 실수형 자료 : 소수로 나타낼 . 수있는 유리수와 원주율이나 루트와 같은 소수로 표현할 수 없는 무리수로 구성된 수 집합
f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e-4
print(f1)
print(f2)
print(f3)
print(f4)

#18 복소수형 자료 : 실수부 + 허수부j로 구성된 수
c1 = 1 + 7j
print(c1.real); print(c1.imag)
c2 = complex(2, 3)
print(c2)

#19 대입 연산자(=)
a = 1
b = 2
ret = a+b
print('a와 b를 더한 값은', end=' ')
print(ret,end=' ')
print('입니다.')

#20 사직 연산자(+,-,*,/,**)
a = 2
b = 4
ret1 = a + b          # ret1 = 2+4 = 6
ret2 = a - b          # ret2 = 2-4 = -2
ret3 = a * b          # ret3 = 2*4 = 8
ret4 = a / b          # ret4 = 2/4 = 0.5
ret5 = a ** b         # ret5 = 2**4 = 16
ret6 = a+a*b/a        # ret6 = 2+2*4/2 = 6
ret7 = (a+b)*(a-b)    # ret7 = (2+4)*(2-4) = -12
ret8 = a*b**a         # ret8 = 2*4**2 = 32

#21 연산자 축약(+=,-=,*=,/=)
a = 0
a += 1       # a = a + 1, a의 값은 1
a -= 5       # a = a - 5, a의 값은 -4
a *= 2       # a = a * 2, a의 값은 -8
a /= 4       # a = a / 4, a의 값은 -2.0

#22 True/False 자료형 : True(참, 1)과 False(거짓, 0)을 나타내는 논리 자료형
a = True
b = False
print(a == 1) # True가 출력됨
print(b != 0) # False가 출력됨

#23 관계 연산자(==, !=, >, <, >=, <=)
x = 1; y = 2
str1 = 'abc'; str2 = 'python'
print(x == y)           # False가 출력됨
print(x != y)           # True가 출력됨
print(str1 == str2)     # False가 출력됨
print(str2 == 'python') # True가 출력됨
print(str1 < str2)      # True가 출력됨(문자열의 사전순서로 비교)

#24 논리 연산자(and, or, not)
bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)  # False가 출력됨
print(bool1 and bool3)  # True가 출력됨
print(bool2 or bool3)   # True가 출력됨
print(bool2 or bool4)   # False가 출력됨
print(not bool1)        # False가 출력됨
print(not bool2)        # True가 출력됨

#25 비트 연산자(&, |, ~, ^, <<, >>)
bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2))   # 0x60이 출력됨
print(hex(bit1 | bit2))   # 0x63이 출력됨
print(hex(bit1 ^ bit2))   # 0x3이 출력됨
print(hex(bit1 >> 1))     # 0x30이 출력됨
print(hex(bit2 << 2))     # 0x188이 출력됨

#26 