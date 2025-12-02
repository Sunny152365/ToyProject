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

#26 시퀀스 자료형(어떤 객체가 순서를 가지고 나열되어 있는 것)
strdata = 'abcde'                # 문자열은 시퀀스 자료형
listdata = [1, [2, 3], '안녕']    # 리스트는 시퀀스 자료트
tupledata = (100, 200, 300)      # 튜플(값 변경 안됨)은 시퀀스 자료형

#27 시퀀스 자료 인덱싱(인덱싱 : 시퀀스 자료형에서 인덱스를 통해 해당하는 값을 얻는 방법, 0부터 시작)
strdata = 'Time is money!!'
listdata = [1, 2,[1,2,3]]
print(strdata[5])        # 'i'가 출력됨
print(strdata[-2])       # '!'가 출력됨
print(listdata[0])       # 1이 출력됨
print(listdata[-1])      # [1,2,3]이 출력됨
print(listdata[2][-1])   # 3이 출력됨

#28 시퀀스 자료 슬라이싱(시퀀스 자료에서 일정 범위에 해당하는 부분을 취하는 방법, [시작 인덱스 : 끝 인덱스 : 스텝])
strdata = 'Time is money!!'
print(strdata[1:5])      # 'ime '가 출력됨
print(strdata[:7])       # 'Time is'가 출력됨
print(strdata[9:])       # 'oney!!'가 출력됨
print(strdata[:-3])      # 'Time is mone'가 출력됨
print(strdata[-3:])      # 'y!!'가 출력됨
print(strdata[:])        # 'Time is money!!'가 출력됨
print(strdata[::2])      # 'Tm smny!'가 출력됨

#29 시퀀스 자료 연결(+, 두 개의 시퀀스 자료형이 동일해야 함)
strdata1 = 'I love '; strdata = 'Python'; strdata3 = 'you'
listdata1 = [1,2,3]; listdata2 = [4,5,6]
print(strdata1 + strdata2)        # 'I love Python'이 출력됨
print(strdata1 + strdata3)        # 'I love you'가 출력됨
print(listdata1 + listdata2)      # [1,2,3,4,5,6]이 출력됨

#30 시퀀스 자료 반복(*)
artist = 'BTS!'
fan = 'ARMY'
dispdata = fan + '들이 외칩니다.' + artist * 3
print(dispdata)   # 'ARMY들이 외칩니다.BTS!BTS!BTS!'가 출력됨

#31 시퀀스 자료 크기(len())
strdata1 = 'I love Python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a', 'b', 'c', strdata1, strdata2]
print(len(strdata1))      # 13이 출력됨
print(len(strdata2))      # 13가 출력됨
print(len(listdata))      # 5가 출력됨
print(len(listdata[3]))   # 13가 출력됨

#32 멤버체크(in, 자료에 어떤 값이 있는지 없는지 확인) : <값> in <자료>
listdata = [1, 2, 3, 4]
ret1 = 5 in listdata    # False
ret2 = 4 in listdata    # True
print(ret1); print(ret2)
strdata = 'abcde'
ret3 = 'c' in strdata   # True
ret4 = '1' in strdata   # False
print(ret3); print(ret4)

#33 문자열(문자나 기호가 순서로 나열되어 있는 시퀀스 자료)
strdata1 = '나는 파이썬 프로그래머다'
strdata2 = "You are a programmer"
strdata3 = """I love
    python. You love
python too!
"""
strdata4 = "My son's name is John"       # ""안에서 '사용하기
strdata5 = '문자열"abc"의 길이는 3입니다.'     # ''안에서 "사용하기

#34 문자열 포맷팅
txt1 = '자바'; txt2 = '파이썬'
num1 = 5; num2 = 10
print('나는 %s보다 %s에 더 익숙합니다.'%(txt1, txt2))
print('%s은 %s보다 %d배 더 쉽습니다.'%(txt2, txt1, num1))
print('%d + %d = %d'%(num1, num2, num1+num2))
print('작년 세계 경제 성장률은 전년에 비해 %d%% 포인트 증가했다.' %num1)

from time import sleep
for i in range(100):
    msg = '\r진행률 : %d%%'%(i+1)
    print(''*len(msg), end='')
    print(msg, end='')
    sleep(0.1)

#35 이스케이프 문자
print('나는 파이썬을 사랑합니다.\n파이썬은 자바보다 훨씬 쉽습니다.')
print('Name:John Smith\tSex:Male\tAge:22')
print('이 문장은 화면폭에 비해 너무 길어 보기가 힘듭니다. \
그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했습니다.')
print('작은따옴표(\')와 큰 따옴표(")는 문자열을 정의할 때 사용합니다.')

#36 리스트([])
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1,2,3,4,5],['a','b','c']]
list1[0] = 6
print(list1)          # [6, 2, 3, 4, 5]로 출력됨
def myfunc():
    print('안녕하세요')
list4 = [1,2,myfunc]
list4[2]()            # '안녕하세요'가 출력됨, ()를 안쓰면 어떻게 되는가?

#37 튜플(()) : 요소의 값 변경 불가
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', (1,2,3,4,5), ('a','b','c'))
tuple1[0] = 6    # 오류 발생(튜플은 값 변경 불가)
def myfunc():
    print('안녕하세요')
tuple4 = (1,2,myfunc)
tuple4[2]()      # '안녕하세요'가 출력됨

#38 사전({}) : 키와 값의 쌍으로 이루어진 자료형
dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])    # 1이 출력됨
dict1['d'] = 4
print(dict1)         # {'a':1, 'b':2, 'c':3, 'd':4}가 출력됨
dict1['b'] = 7
print(dict1)         # {'a':1, 'b':7, 'c':3, 'd':4}가 출력됨
print(len(dict1))    # 4가 출력됨

#39 함수(def)
def add_number(n1, n2):
    ret = n1 + n2
    return ret

def add_txt(t1, t2):
    print(t1 + t2)
    
ans = add_number(10, 15)
print(ans)                 # 25가 출력됨
text1 = '대한민국~'
text2 = '만세!!'
add_txt(text1, text2)      # '대한민국~만세!!'가 출력됨

#40 함수 인자
def add_txt(t1, t2='파이썬'):
    print(t1 + ':' + t2)

add_txt('베스트')                   # '베스트:파이썬'이 출력됨
add_txt(t2='대한민국', t1='1등')     # '1등:대한민국'이 출력됨

def func1(*args):                 # 가변 인자 : *args는 튜플로 전달됨
    print(args)
    
def func2(width, height, **kwargs):
    print(kwargs)

func1()                                # 빈 튜플이 출력됨
func1(3, 5, 1, 5)                      # (3, 5, 1, 5)가 출력됨
func2(10, 20)                          # 빈 딕셔너리가 출력됨
func2(10, 20,depth=50, color='blue')   # {'depth': 50, 'color': 'blue'}가 출력됨

#41 지역변수와 전역변수(global) : 지역변수(함수 내에서만 유효한 변수), 전역변수(코드 전반에 걸쳐 유효한 변수)
param = 10
strdata = '전역변수'

def func1():
    strdata = '지역변수'
    print(strdata)

def func2():
    param = 1

def func3():
    global param
    param = 50
    
func1()               # '지역변수'가 출력됨
print(strdata)        # '전역변수'가 출력됨
print(param)          # 10이 출력됨
func2(param)
print(param)          # 10이 출력됨
func3()
print(param)          # 50이 출력됨

#42 함수 리턴값(return) : 리턴값이 여러 개인 경우 튜플로 반환
def reverse(x, y, z):
    return z, y, x

ret = reverse(1, 2, 3)
print(ret)                        # (3, 2, 1)이 출력됨

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3)   # 'c', 'b', 'a' 순으로 출력됨

#43 파이썬 모듈 : 다양한 기능을 미리 구현해 놓은 파이썬 파일(.py)
import time

print('5초간 프로그램을 정지합니다.')
time.sleep(5)
print('5초가 지났습니다.')

#44 파이썬 패키지(파이썬 모듈을 계층적인 디렉터리 형태로 구성한 것) : __init__.py 파일
import mypackage.mylib

ret1 = mypackage.mylib.add_txt('대한민국', '1등')
ret2 = mypackage.mylib.reverse(1, 2, 3)

#45 파이썬 모듈 임포트(import)
import time                        # 파이썬 내장 모듈인 time을 import
import mylib                       # 내가 만든 mylib을 module import
import mypackage.mylib             # mypackage에 있는 mylib module import(순서 : 패키지이름.모듈이름)

time.sleep(1)                      # time 모듈의 sleep 함수를 이용해 1초간 정지
mylib.add_txt('나는', '파이썬이다')    # mylib 모듈의 add_txt 함수 호출
mypackage.mylib.reverse(1, 2, 3)   # mypackage의 mylib 모듈의 reverse 함수 호출

#46 파이썬 모듈(from-import)
"""
from 모듈이름 import 함수이름
from 패키지이름 import 모듈이름
"""
from time import sleep
from mypackage import mylib
from mypackage.mylib import reverse

sleep(1)                             # time 모듈의 sleep 함수 호출
mylib.add_txt('나는', '파이썬이다')      # mypackage.mylib 모듈의 add_txt 함수 호출
reverse(1, 2, 3)                     # mypackage.mylib 모듈의 reverse 함수 호출

#47 파이썬 모듈(import~as) : import 이름이 긴 모듈명 as 별명
import mypackage as mp
import mypackage.mylib as ml

ret1 = mp.mylib.add_txt('대한민국', '1등')
ret2 = ml.reverse(1, 2, 3)

#48 파일 열고 닫기(open, close) : open(파일이름, 모드)
f1 = open('test.txt', 'r')
f2 = open('d:/myimages/mypictues1.jpg', 'rb')

#--------------------------------------------
# 오픈한 파일을 처리하는 코드를 작성함
#--------------------------------------------

f1.close()
f2.close()

#49 클래스(class)
class MyClass:
    var = '안녕하세요'
    def sayHello(self): # self : 인스턴스 객체 자기 자신을 의미
        print(self.var)
        
obj = MyClass()         # MyClass의 인스턴스 객체 생성
print(obj.var)          # '안녕하세요'가 출력됨
obj.sayHello()          # '안녕하세요'가 출력됨

#50 클래스 멤버(클래스 메소드 바깥에서 선언)와 인스턴스 멤버(클래스 메소드 안에서 self와 함께 선언되는 변수)
class MyClass:
    var = '안녕하세요!!'
    def sayHello(self):
        param1 = '안녕' .     # 함수 내에서만 유효한 지역변수
        self.param2 = '하이'  # 함수 내에 선언된 인스턴스 멤버
        print(param1)        # '안녕'이 출력됨
        print(self.var)      # '안녕하세요!!'가 출력됨

obj = MyClass()
print(obj.var)               # '안녕하세요!!'가 출력됨
obj.sayHello()               # '안녕'과 '안녕하세요!!'가 출력됨
#obj.param

#51 클래스 메소드
class MyClass:
    def sayHello(self):
        print('안녕하세요')
    
    def sayBye(self, name):
        print('%s! 다음에 보자!' %name)

obj = MyClass()
obj.sayHello()            # '안녕하세요'가 출력됨
obj.sayBye('철수')         # '철수! 다음에 보자!'가 출력됨

#52 클래스 생성자(def __init__(self, *args), *args : 가변 인자)
class MyClass:
    def __init__(self):
        self.var = '안녕하세요!'
        print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass()          # 'MyClass 인스턴스 객체가 생성되었습니다'가 출력됨
print(obj.var)           # '안녕하세요!'가 출력됨

#53 클래스 소멸자
class MyClass:    
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj = MyClass()          # MyClass 인스턴스 객체가 생성됨
del obj                  # 'MyClass 인스턴스 객체가 메모리에서 제거됩니다'가 출력됨

#54 클래스 상속(class 자식클래스(부모클래스):)
class Add:
    def add(self, n1, n2):
        return n1 + n2

class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))  # 3이 출력됨
print(obj.sub(1, 2))  # -1이 출력됨

#54-1 클래스 다중 상속
class Add:
    def add(self, n1, n2):
        return n1 + n2

class Multiply:
    def mul(self, n1, n2):
        return n1 * n2

class Calculator(Add, Multiply):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))   # 3이 출력됨
print(obj.mul(3, 4))   # 12이 출력됨

#55 예외처리(try~except)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')

#56 예외처리(try~except~else)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')
else: # 오류가 발생하지 않았을 때 실행
    print('예외가 발생하지 않았습니다.')

#57 예외처리(try~except~finally)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')
finally: # 오류 발생 유무와 상관없이 어떤 코드를 무조건 실행
    print('무조건 실행하는 코드')

#58 예외처리(try~except Exception as e)
try:
    print(param)
except Exception as e:
    print(e)       # name 'param' is not defined가 출력됨

#59 예외처리(try~except 특정 예외)
import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt: # Ctrl+C가 입력되면 발생하는 오류
    print('사용자에 의해 프로그램이 종료되었습니다.')

#60 사용자 입력받기(input)
k = input('<값>을 입력하세요:')
print('당신이 입력한 값은 <' + k + '>입니다.')

#61 자료형 확인(type)
numdata = 57
strdata = '파이썬'
listdata = [1,2,3]
dictdata = {'a':1, 'b':2}

def func():
    print('안녕하세요.')

print(type(numdata))
print(type(strdata))
print(type(listdata))
print(type(dictdata))
print(type(func))

#62 나눗셈에서 나머지만 구하기(%)
a = 11113
b = 23
ret = a % b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.',%(a, b, ret))

#63