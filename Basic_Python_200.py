#001 인터프리터 언어 : 소스 코드를 한 줄씩 읽어서 바로 실행하는 언어
print("Hello World!")

#002 텍스트 에디터 : 라인 번호
print('안녕하세요')
a = 1
b = 1
print(a + b)

#003 변수명 만들기 : 변수명의 첫 문자는 _또는 영문자, 대소문자 구분, 숫자 사용 가능(단, 첫 문자 제외)
_myname = 'samsjang'
my_name = '홍길동'
MyName2 = 'Hong gil-dong'
counter = 1
Counter = 2

#004 변수에 값 대입하기 : 따로 자료형태 선언 없이 값 대입 시 자동으로 자료형 결정
number1 = 1
pi = 3.14
flag = True
char = 'x'
chars = 'I love Python'

#005 주석 # 
# 만든 날짜 : 2025.11.23
a = 1
b = 5
print(a+b)

#006 자료형
int_data = 1                            # 정수 선언
float_data = 3.14                       # 실수 선언
complex_data = 1 + 5j                   # 복소수 선언
str_data1 = 'I love Python'             # 문자열 선언(영문)
str_data2 = "반갑습니다."                  # 문자열 선언(한글)
list_data = [1, 2, 3]                   # 리스트 선언  
tuple_data = (1, 2, 3)                  # 튜플 선언 (요소 값 변경 불가)
dict_data = {0:'False', 1:'True'}       # 딕셔너리 선언

#007 자료형 출력(print)
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

#008 들여쓰기 : space bar 4칸, tab 1칸
listdata = ['a', 'b', 'c']
if 'a' in listdata:
    print('a가 listdata에 있습니다.')
    print(listdata)
else:
    print('a가 listdata에 존재하지 않습니다.')
    
#009 if-else문
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

#010 if-elif문
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

#011 for문(범위 설정 가능한 것 : 시퀀스 자료형, 반복 가능한 자료, 문자열, 리스트나 튜플, 사전, range(), 그 외에 반복 가능한 객체)
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
    
#012 for-continue-break문
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
    
#013 for-else문(break에 의해 중단됨이 없이 정상적으로 모두 실행되어야만 특정 코드를 실행하게 할 경우)
scope = [1,2,3]
for x in scope:
    print(x)
    #break
else:
    print('Perfect')
    
#014 while-continue-break문
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
    
#015 None(Types.NoneType) 자료형 : 값이 없음을 나타내는 자료형
val = None
condition = 1
if condition == 1:
    val = [1,2,3]
else:
    val = 'I love Python'
    
#016 정수형 자료
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

#017 실수형 자료 : 소수로 나타낼 . 수있는 유리수와 원주율이나 루트와 같은 소수로 표현할 수 없는 무리수로 구성된 수 집합
f1 = 1.0
f2 = 3.14
f3 = 1.56e3
f4 = -0.7e-4
print(f1)
print(f2)
print(f3)
print(f4)

#018 복소수형 자료 : 실수부 + 허수부j로 구성된 수
c1 = 1 + 7j
print(c1.real); print(c1.imag)
c2 = complex(2, 3)
print(c2)

#019 대입 연산자(=)
a = 1
b = 2
ret = a+b
print('a와 b를 더한 값은', end=' ')
print(ret,end=' ')
print('입니다.')

#020 사직 연산자(+,-,*,/,**)
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

#021 연산자 축약(+=,-=,*=,/=)
a = 0
a += 1       # a = a + 1, a의 값은 1
a -= 5       # a = a - 5, a의 값은 -4
a *= 2       # a = a * 2, a의 값은 -8
a /= 4       # a = a / 4, a의 값은 -2.0

#022 True/False 자료형 : True(참, 1)과 False(거짓, 0)을 나타내는 논리 자료형
a = True
b = False
print(a == 1) # True가 출력됨
print(b != 0) # False가 출력됨

#023 관계 연산자(==, !=, >, <, >=, <=)
x = 1; y = 2
str1 = 'abc'; str2 = 'python'
print(x == y)           # False가 출력됨
print(x != y)           # True가 출력됨
print(str1 == str2)     # False가 출력됨
print(str2 == 'python') # True가 출력됨
print(str1 < str2)      # True가 출력됨(문자열의 사전순서로 비교)

#024 논리 연산자(and, or, not)
bool1 = True; bool2 = False; bool3 = True; bool4 = False
print(bool1 and bool2)  # False가 출력됨
print(bool1 and bool3)  # True가 출력됨
print(bool2 or bool3)   # True가 출력됨
print(bool2 or bool4)   # False가 출력됨
print(not bool1)        # False가 출력됨
print(not bool2)        # True가 출력됨

#025 비트 연산자(&, |, ~, ^, <<, >>)
bit1 = 0x61
bit2 = 0x62
print(hex(bit1 & bit2))   # 0x60이 출력됨
print(hex(bit1 | bit2))   # 0x63이 출력됨
print(hex(bit1 ^ bit2))   # 0x3이 출력됨
print(hex(bit1 >> 1))     # 0x30이 출력됨
print(hex(bit2 << 2))     # 0x188이 출력됨

#026 시퀀스 자료형(어떤 객체가 순서를 가지고 나열되어 있는 것)
strdata = 'abcde'                # 문자열은 시퀀스 자료형
listdata = [1, [2, 3], '안녕']    # 리스트는 시퀀스 자료트
tupledata = (100, 200, 300)      # 튜플(값 변경 안됨)은 시퀀스 자료형

#027  파일 이름 바꾸기(os.rename)시퀀스 자료 인덱싱(인덱싱 : 시퀀스 자료형에서 인덱스를 통해 해당하는 값을 얻는 방법, 0부터 시작)
from os import rename

target_file = 'stockcode.txt'
newname =

strda 파일을 다른 디렉터리로 이동(os.rename) 파일 이름 바꾸기(os.rename)ta = 'Time is money!!'
from os import rename

target_file = 'stockcode.txt'
newname =

listd 파일을 다른 디렉터리로 이동 디렉터리에 있는 파일목록 얻기(os.listdir, glob.glob)(os.rename)ata = [1, 2,[1,2,3]]
print(strdata[5])     디렉터리에 있는 파일목록 얻기(os.listdir, glob.glob)    # 'i'가 출력됨
print(strdata[-2])       # '!'가 출력됨
print(listdata[0])       # 1이 출력됨
print(listdata[-1])      # [1,2,3]이 출력됨
print(listdata[2][-1])   # 3이 출력됨

#028 시퀀스 자료 슬라이싱(시퀀스 자료에서 일정 범위에 해당하는 부분을 취하는 방법, [시작 인덱스 : 끝 인덱스 : 스텝])
strdata = 'Time is money!!'
print(strdata[1:5])      # 'ime '가 출력됨
print(strdata[:7])       # 'Time is'가 출력됨
print(strdata[9:])       # 'oney!!'가 출력됨
print(strdata[:-3])      # 'Time is mone'가 출력됨
print(strdata[-3:])      # 'y!!'가 출력됨
print(strdata[:])        # 'Time is money!!'가 출력됨
print(strdata[::2])      # 'Tm smny!'가 출력됨

#029 시퀀스 자료 연결(+, 두 개의 시퀀스 자료형이 동일해야 함)
strdata1 = 'I love '; strdata = 'Python'; strdata3 = 'you'
listdata1 = [1,2,3]; listdata2 = [4,5,6]
print(strdata1 + strdata2)        # 'I love Python'이 출력됨
print(strdata1 + strdata3)        # 'I love you'가 출력됨
print(listdata1 + listdata2)      # [1,2,3,4,5,6]이 출력됨

#030 시퀀스 자료 반복(*)
artist = 'BTS!'
fan = 'ARMY'
dispdata = fan + '들이 외칩니다.' + artist * 3
print(dispdata)   # 'ARMY들이 외칩니다.BTS!BTS!BTS!'가 출력됨

#031 시퀀스 자료 크기(len())
strdata1 = 'I love Python'
strdata2 = '나는 파이썬을 사랑합니다'
listdata = ['a', 'b', 'c', strdata1, strdata2]
print(len(strdata1))      # 13이 출력됨
print(len(strdata2))      # 13가 출력됨
print(len(listdata))      # 5가 출력됨
print(len(listdata[3]))   # 13가 출력됨

#032 멤버체크(in, 자료에 어떤 값이 있는지 없는지 확인) : <값> in <자료>
listdata = [1, 2, 3, 4]
ret1 = 5 in listdata    # False
ret2 = 4 in listdata    # True
print(ret1); print(ret2)
strdata = 'abcde'
ret3 = 'c' in strdata   # True
ret4 = '1' in strdata   # False
print(ret3); print(ret4)

#033 문자열(문자나 기호가 순서로 나열되어 있는 시퀀스 자료)
strdata1 = '나는 파이썬 프로그래머다'
strdata2 = "You are a programmer"
strdata3 = """I love
    python. You love
python too!
"""
strdata4 = "My son's name is John"       # ""안에서 '사용하기
strdata5 = '문자열"abc"의 길이는 3입니다.'     # ''안에서 "사용하기

#034 문자열 포맷팅
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

#035 이스케이프 문자
print('나는 파이썬을 사랑합니다.\n파이썬은 자바보다 훨씬 쉽습니다.')
print('Name:John Smith\tSex:Male\tAge:22')
print('이 문장은 화면폭에 비해 너무 길어 보기가 힘듭니다. \
그래서 \\Enter키를 이용해 문장을 다음줄과 연속되도록 했습니다.')
print('작은따옴표(\')와 큰 따옴표(")는 문자열을 정의할 때 사용합니다.')

#036 리스트([])
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']
list3 = [1, 'a', 'abc', [1,2,3,4,5],['a','b','c']]
list1[0] = 6
print(list1)          # [6, 2, 3, 4, 5]로 출력됨
def myfunc():
    print('안녕하세요')
list4 = [1,2,myfunc]
list4[2]()            # '안녕하세요'가 출력됨, ()를 안쓰면 어떻게 되는가?

#037 튜플(()) : 요소의 값 변경 불가
tuple1 = (1, 2, 3, 4, 5)
tuple2 = ('a', 'b', 'c')
tuple3 = (1, 'a', 'abc', (1,2,3,4,5), ('a','b','c'))
tuple1[0] = 6    # 오류 발생(튜플은 값 변경 불가)
def myfunc():
    print('안녕하세요')
tuple4 = (1,2,myfunc)
tuple4[2]()      # '안녕하세요'가 출력됨

#038 사전({}) : 키와 값의 쌍으로 이루어진 자료형
dict1 = {'a':1, 'b':2, 'c':3}
print(dict1['a'])    # 1이 출력됨
dict1['d'] = 4
print(dict1)         # {'a':1, 'b':2, 'c':3, 'd':4}가 출력됨
dict1['b'] = 7
print(dict1)         # {'a':1, 'b':7, 'c':3, 'd':4}가 출력됨
print(len(dict1))    # 4가 출력됨

#039 함수(def)
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

#040 함수 인자
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

#041 지역변수와 전역변수(global) : 지역변수(함수 내에서만 유효한 변수), 전역변수(코드 전반에 걸쳐 유효한 변수)
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

#042 함수 리턴값(return) : 리턴값이 여러 개인 경우 튜플로 반환
def reverse(x, y, z):
    return z, y, x

ret = reverse(1, 2, 3)
print(ret)                        # (3, 2, 1)이 출력됨

r1, r2, r3 = reverse('a', 'b', 'c')
print(r1); print(r2); print(r3)   # 'c', 'b', 'a' 순으로 출력됨

#043 파이썬 모듈 : 다양한 기능을 미리 구현해 놓은 파이썬 파일(.py)
import time

print('5초간 프로그램을 정지합니다.')
time.sleep(5)
print('5초가 지났습니다.')

#044 파이썬 패키지(파이썬 모듈을 계층적인 디렉터리 형태로 구성한 것) : __init__.py 파일
import mypackage.mylib

ret1 = mypackage.mylib.add_txt('대한민국', '1등')
ret2 = mypackage.mylib.reverse(1, 2, 3)

#045 파이썬 모듈 임포트(import)
import time                        # 파이썬 내장 모듈인 time을 import
import mylib                       # 내가 만든 mylib을 module import
import mypackage.mylib             # mypackage에 있는 mylib module import(순서 : 패키지이름.모듈이름)

time.sleep(1)                      # time 모듈의 sleep 함수를 이용해 1초간 정지
mylib.add_txt('나는', '파이썬이다')    # mylib 모듈의 add_txt 함수 호출
mypackage.mylib.reverse(1, 2, 3)   # mypackage의 mylib 모듈의 reverse 함수 호출

#046 파이썬 모듈(from-import)
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

#047 파이썬 모듈(import~as) : import 이름이 긴 모듈명 as 별명
import mypackage as mp
import mypackage.mylib as ml

ret1 = mp.mylib.add_txt('대한민국', '1등')
ret2 = ml.reverse(1, 2, 3)

#048 파일 열고 닫기(open, close) : open(파일이름, 모드)
f1 = open('test.txt', 'r')
f2 = open('d:/myimages/mypictues1.jpg', 'rb')

#--------------------------------------------
# 오픈한 파일을 처리하는 코드를 작성함
#--------------------------------------------

f1.close()
f2.close()

#049 클래스(class)
class MyClass:
    var = '안녕하세요'
    def sayHello(self): # self : 인스턴스 객체 자기 자신을 의미
        print(self.var)
        
obj = MyClass()         # MyClass의 인스턴스 객체 생성
print(obj.var)          # '안녕하세요'가 출력됨
obj.sayHello()          # '안녕하세요'가 출력됨

#050 클래스 멤버(클래스 메소드 바깥에서 선언)와 인스턴스 멤버(클래스 메소드 안에서 self와 함께 선언되는 변수)
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

#051 클래스 메소드
class MyClass:
    def sayHello(self):
        print('안녕하세요')
    
    def sayBye(self, name):
        print('%s! 다음에 보자!' %name)

obj = MyClass()
obj.sayHello()            # '안녕하세요'가 출력됨
obj.sayBye('철수')         # '철수! 다음에 보자!'가 출력됨

#052 클래스 생성자(def __init__(self, *args), *args : 가변 인자)
class MyClass:
    def __init__(self):
        self.var = '안녕하세요!'
        print('MyClass 인스턴스 객체가 생성되었습니다')

obj = MyClass()          # 'MyClass 인스턴스 객체가 생성되었습니다'가 출력됨
print(obj.var)           # '안녕하세요!'가 출력됨

#053 클래스 소멸자
class MyClass:    
    def __del__(self):
        print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')

obj = MyClass()          # MyClass 인스턴스 객체가 생성됨
del obj                  # 'MyClass 인스턴스 객체가 메모리에서 제거됩니다'가 출력됨

#054 클래스 상속(class 자식클래스(부모클래스):)
class Add:
    def add(self, n1, n2):
        return n1 + n2

class Calculator(Add):
    def sub(self, n1, n2):
        return n1 - n2

obj = Calculator()
print(obj.add(1, 2))  # 3이 출력됨
print(obj.sub(1, 2))  # -1이 출력됨

#054-1 클래스 다중 상속
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

#055 예외처리(try~except)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')

#056 예외처리(try~except~else)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')
else: # 오류가 발생하지 않았을 때 실행
    print('예외가 발생하지 않았습니다.')

#057 예외처리(try~except~finally)
try:
    print('안녕하세요')
    print(param)
except:
    print('예외가 발생했습니다!')
finally: # 오류 발생 유무와 상관없이 어떤 코드를 무조건 실행
    print('무조건 실행하는 코드')

#058 예외처리(try~except Exception as e)
try:
    print(param)
except Exception as e:
    print(e)       # name 'param' is not defined가 출력됨

#059 예외처리(try~except 특정 예외)
import time
count = 1
try:
    while True:
        print(count)
        count += 1
        time.sleep(0.5)
except KeyboardInterrupt: # Ctrl+C가 입력되면 발생하는 오류
    print('사용자에 의해 프로그램이 종료되었습니다.')

#060 사용자 입력받기(input)
k = input('<값>을 입력하세요:')
print('당신이 입력한 값은 <' + k + '>입니다.')

#061 자료형 확인(type)
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

#062 나눗셈에서 나머지만 구하기(%)
a = 11113
b = 23
ret = a % b
print('<%d>를 <%d>로 나누면 <%d>가 나머지로 남습니다.',%(a, b, ret))

#063 몫과 나머지(divmod): 튜플로 리턴
a = 11113
b = 23
ret1, ret2 = divmod(a, b)
print('<%d/ %d>는 목이 <%d>, 나머지가 <%d>입니다.'%(a, b, ret1, ret2))

#064 10진수를 16진수로 변환(hex)
h1 = hex(97)       # h1은 문자열 '0x61'
h2 = hex(98)       # h2는 문자열 '0x62'
ret1 = h1 + h2
print(ret1)        # '0x610x62'가 출력됨
a = int(h1, 16)
b = int(h2, 16)
ret2 = a + b       # ret2는 10진수 195가 됨
print(hex(ret2))   # '0xc3'가 출력됨

#065 10진수를 2진수로 변환(bin) : bin의 결과도 문자열, int를 사용하여 10진수로 변환
b1 = bin(97)       # b1은 문자열 '0b11000001'
b2 = bin(98)       # b2는 문자열 '0b11000010'
ret1 = b1 + b2
print(ret1)        # '0b110000010b11000010'가 출력됨
a = int(b1, 2)
b = int(b2, 2)
ret2 = a + b
print(bin(ret2))   # '0b110000011'가 출력됨

#066 2진수, 16진수를 10진수로 변환(int)
bnum = 0b11110000; bstr = '0b11110000'
onum = 0o360; ostr = '0o360'
hnum = 0xf0; hstr = '0xf0'
b1 = int(bnum); b2 = int(bstr, 2)       # b2 = int(bstr, 0)으로도 가능
o1 = int(onum); o2 = int(ostr, 8)       # o2 = int(ostr, 0)으로도 가능
h1 = int(hnum); h2 = int(hstr, 16)      # h2 = int(hstr, 0)으로도 가능
print(b1); print(b2)
print(o1); print(o2)
print(h1); print(h2)                    # 모든 결과 240

#067 절대값(abs)
abs1 = abs(-3)      # 정수의 절대값
abs2 = abs(-5.72)   # 실수의 절대값
abs3 = abs(3+4j)    # 복소수의 절대값
print(abs1)         # 3이 출력됨
print(abs2)         # 5.72가 출력됨
print(abs3)         # 5.0이 출력됨

#068 반올림수(round)
ret1 = round(1118)        # 소수점 첫째자리에서 반올림해줌
ret2 = round(16.554)      # 소수점 첫째자리에서 반올림해줌
ret3 = round(1118, -1)    # 1자리에서 반올림해줌
ret4 = round(16.554, 2)   # 소수점 셋째자리에서 반올림해줌
print(ret1)               # 1118
print(ret2)               # 17
print(ret3)               # 1120
print(ret4)               # 16.55

#069 실수형 자료를 정수형 자료로 변환(int)
idata1 = int(-5.4)
idata2 = int(1.78e1)
idata3 = int(171.56)
print(idata1)       # -5가 출력됨
print(idata2)       # 17이 출력됨
print(idata3)       # 171이 출력됨

#070 정수형 자료를 실수형 자료로 변환(float)
fdata = float(10)
print(fdata)       # 10.0으로 출력됨

#071 정수 리스트에서 소수만 걸러내기(filter) : filter(함수, 자료)
def getPrime(x):
    if x%2 == 0:
        return
    
    for i in range(3, int(x/2), 2):
        if x%i == 0:
            break
    else:
        return x
    
listdata = [117, 119, 1113, 11113, 11119]
ret = filter(getPrime, listdata)
print(list(ret))            # [11113, 11119]가 출력됨

#072 최대값과 최소값(max, min)
listdata = [9.96, 1.27, 5.07, 6.45, 8.38, 9.29, 4.93, 7.73, 3.71, 0.93]
maxval = max(listdata)
minval = min(listdata)
print(maxval)      # 9.96이 출력됨
print(minval)      # 0.93이 출력됨

txt = 'Alotofthingsoccureachday'
maxval = max(txt)
minval = min(txt)
print(maxval)      # 'y'가 출력됨
print(minval)      # 'A'가 출력됨

maxval = max(2+3, 2*3, 2**3, 3**2)
minval = min('abz', 'a12')
print(maxval)      # 9가 출력됨
print(minval)      # 'a12'가 출력됨

#073 1바이트에서 하위 4비트 추출
a = 107        # 16진수로 0x6b
b = a & 0x0f
print(b)       # 11이 출력됨. 11은 16진수로 b임

#074 1바이트에서 상위 4비트 추출
a = 107              # 16진수로 0x6b
b = (a >> 4) & 0x0f
print(b)             # 6이 출력됨

#075 문자열에서 특정 위치의 문자 얻기
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[5])       # 'e'가 출력됨
print(txt2[-2])      # '라'가 출력됨

#076 문자열에서 지정한 구간의 문자열 얻기
txt1 = 'A tale that was not right'
txt2 = '이 또한 지나가리라.'
print(txt1[3:7])      # 'ale '가 출력됨
print(txt1[:6])       # 'A tale'가 출력됨
print(txt2[-4:])      # '가리라.'가 출력됨

txt = 'python'
for i in range(len(txt)):
    print(txt[:i+1])

#077 문자열에서 홀수 번째 문자만 추출
txt = 'aAbBcCdDeEfFgGhHiIjJkK'
ret = txt[::2]
print(ret)       # 'abcdefghijk'가 출력됨
ret = txt[1::2]  # 짝수 번째 문자만 추출
print(ret)       # 'ABCDEFGHIJK'가 출력됨

#078 문자열을 거꾸로 만들기
txt = 'abcdefghijk'
ret = txt[::-1]
print(ret)          # 'kjihgfedcba'가 출력됨
ret_1 = txt[::-2]   # 홀수 번째 문자만 거꾸로 추출
ret_2 = txt[2::-2]  # 짝수 번째 문자만 거꾸로 추출

#079 두 개의 문자열 합치기(+)
filename = input('저장할 파일이름을 입력하세요:')
filename = filename + '.jpg'
display_msg = '당신이 저장한 파일은<' + filename + '>입니다.'
print(display_msg)

#080 문자열을 반복해서 새로운 문자열로 만들기(*)
msg1 = '여러분'
msg2 = '파이팅!'
display_msg = msg1 + ', ' + msg2 * 3 + '~!'
print(display_msg)

#081 문자열에서 특정 문자가 있는지 확인(in)
msg = input('임의의 문장을 입력하세요:')
if 'a' in msg:
    print('당신이 입력한 문장에는 a문자가 있습니다.')
else:
    print('당신이 입력한 문장에는 a문자가 없습니다.')

#082 문자열에서 특정 문자열이 있는지 확인(in)
msg = input('임의의 문장을 입력하세요:')
if 'is' in msg:
    print('당신이 입력한 문장에는 is문자가 있습니다.')
else:
    print('당신이 입력한 문장에는 is문자가 없습니다.')

#083 문자열 길이(len)
msg = input('임의의 문장을 입력하세요:')
msglen = len(msg)
print('당신이 입력한 문장의 길이는 <%d>입니다.' %msglen)

#084 문자열이 알파벳인지 확인(isalpha) : 문자열의 모든 요소가 사람의 언어 문자로만 구성되어야 True
txt1 = 'A'
txt2 = '안녕'
txt3 = 'Warcraft Three'
txt4 = '3PO'
ret1 = txt1.isalpha()
ret2 = txt2.isalpha()
ret3 = txt3.isalpha()
ret4 = txt4.isalpha()
print(ret1)      # True가 출력됨
print(ret2)      # True가 출력됨
print(ret3)      # False가 출력됨
print(ret4)      # False가 출력됨

#085 문자열이 숫자인지 확인(isdigit) : 문자열을 구성하는 요소가 모두 숫자로 구성되어야 True
txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
print(ret1)      # False가 출력됨
print(ret2)      # False가 출력됨
print(ret3)      # True가 출력됨

#086 문자열이 알파벳 또는 숫자인지 확인(isalnum) : 문자열을 구성하는 요소가 모두 알파벳 또는 숫자로 구성되어야 True
txt1 = '안녕하세요?'
txt2 = '1.Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1)      # False가 출력됨
print(ret2)      # False가 출력됨
print(ret3)      # True가 출력됨

#087 문자열에서 대소문자 변환(upper, lower)
txt = 'A lot of Things occur each day.'
ret1 = txt.upper()
ret2 = txt.lower()
print(ret1)      # 'A LOT OF THINGS OCCUR EACH DAY.'가 출력됨
print(ret2)      # 'a lot of things occur each day.'가 출력됨

#088 문자열에서 좌우 공백 제거(lstrip, rstrip, strip)
txt = '   양쪽에 공백이 있는 문자열입니다.   '
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<' + txt + '>')    # '<   양쪽에 공백이 있는 문자열입니다.   >'
print('<' + ret1 + '>')   # '<양쪽에 공백이 있는 문자열입니다.   >'
print('<' + ret2 + '>')   # '<   양쪽에 공백이 있는 문자열입니다.>'
print('<' + ret3 + '>')   # '<양쪽에 공백이 있는 문자열입니다.>'

#089 문자열을 수치형 자료로 변환(int, float)
numstr = input('숫자를 입력하세요:')
try:
    num = int(numstr)
    print('당신이 입력한 숫자는 정수 <%d>입니다.' %num)
except:
    try:
        num = float(numstr)
        print('당신이 입력한 숫자는 실수 <%f>입니다.' %num)
    except:
        print('+++ 숫자를 입력하세요~ +++')

#090 수치형 자료를 문자열로 변환(str)
num1 = 1234
num2 = 3.14

numstr1 = str(num1)
numstr2 = str(num2)
print('num1을 문자열로 변환한 값은 "%s"입니다.' %numstr1)
print('num2을 문자열로 변환한 값은 "%s"입니다.' %numstr2)

#091 문자열에 있는 문자(열) 개수 구하기(count)
txt = 'A lot of things occur each day, every day.'
word_count1 = txt.count('o')
word_count2 = txt.count('day')
word_count3 = txt.count('')
print(word_count1)    # 3가 출력됨
print(word_count2)    # 2가 출력됨
print(word_count3)    # 8가 출력됨

#092 문자열에서 특정 문자(열) 위치 찾기(find) : 해당 문자나 문자열을 찾을 수 없으면 -1 리턴
txt = 'A lot of things occur each day, every day.'
offset1 = txt.find('e')
offset2 = txt.find('day')
offset3 = txt.find('day', 30)
print(offset1)    # 22이 출력됨
print(offset2)    # 27이 출력됨
print(offset3)    # 38가 출력됨

#093 문자열을 특정 문자(열)로 분리(split)
url = 'http://www.naver.com/news/today=20160831'
log = 'name:홍길동 age:17 sex:남자 nation:조선'

ret1 = url.split('/')
print(ret1)   # ['http:', '', 'www.naver.com', 'news', 'today=20160831']가 출력됨

ret2 = log.split()   # 공백문자로 분리
for data in ret2:
    d1, d2 = data.split(':')
    print('%s -> %s' %(d1, d2))

#094 문자열을 특정 문자(열)로 결합(join)
# join()의 인자는 문자열이 아니라 문자열을 요소로 가지는 리스트
loglist = ['2016/08.26 10:12:11', '200', 'OK', '이 또한 지나가리라']
bond = ';'
log = bond.join(loglist)
print(log)   # '2016/08.26 10:12:11;200;OK;이 또한 지나가리라' 출력

#095 문자열에서 특정 문자(열)를 다른 문자(열)로 변경(replace)
txt = 'My password is 1234'
ret1 = txt.replace('1', '0')
ret2 = txt.replace('1', 'python')
print(ret1)   # 'My password is 0234'가 출력됨
print(ret2)   # 'My password is python234'가 출력됨

txt = '매일 많은 일들일 일어납니다.'
ret3 = txt.replace('매일', '항상')
ret4 = ret3.replace('일', '사건')
print(ret3)   # '항상 많은 일들일 일어납니다.'가 출력됨
print(ret4)   # '항상 많은 사건들 사건어납니다.'가 출력됨

#096 문자열을 바이트 객체로 바꾸기(encode)
u_txt = 'I love python'
b_txt = u_txt.encode()
print(u_txt)        # 'I love python'이 출력됨
print(b_txt)        # b'I love python'이 출력됨

ret1 = 'I' == u_txt[0]
ret2 = 'I' == b_txt[0]
print(ret1)         # True가 출력됨
print(ret2)         # False가 출력됨

#097 바이트 객체를 문자열로 바꾸기(decode)
b_txt = b'A lot of things occur each day.'
u_txt = b_txt.decode()
print(u_txt)

#098 문자열을 정렬(sorted, join)
strdata = input('정렬할 문자열을 입력하세요:')
ret1 = sorted(strdata)
ret2 = sorted(strdata, reverse=True)
print(ret1)
print(ret2)
ret1 = ''.join(ret1)
ret2 = ''.join(ret2)
ret3 = ''.join(sorted(strdata))
ret4 = ''.join(sorted(strdata, reverse=True))
print('오름차순으로 정렬된 문자열을 <' + ret1 + '>입니다.')
print('내림차순으로 정렬된 문자열을 <' + ret2 + '>입니다.')
print('오름차순으로 정렬된 문자열을 <' + ret3 + '>입니다.')
print('내림차순으로 정렬된 문자열을 <' + ret4 + '>입니다.')

#099 순차적인 정수 리스트 만들기(range)
range1 = range(10)
range2 = range(10, 20)
print(list(range1))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]가 출력됨
print(list(range2))    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]가 출력됨

ret = 0
for i in range(10):
    ret += (i+1)

#100 리스트에서 특정 위치의 요소 얻기
listdata = [1, 2, 'a', 'b', 'c', [4, 5, 6]]
val1 = listdata[1]
val2 = listdata[3]
val3 = listdata[5][1]
print(val1)      # 2가 출력됨
print(val2)      # 'b'가 출력됨
print(val3)      # 5가 출력됨

#101 리스트에서 특정 요소의 위치 구하기(index)
slolarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성', '지구']
planet = '지구'
pos = solarsys.index(planet)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))
pos = solarsys.index(planet, 5)
print('%s은(는) 태양계에서 %d번째에 위치하고 있습니다.' %(planet, pos))

#102 리스트에서 특정 위치의 요소를 변경
soloarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
planet = '화성'
pos = soloarsys.index(planet)
soloarsys[pos] = 'Mars'
print(solarsys)

#103 리스트에서 특정 구간에 있는 요소 추출
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
rock_planets = solarsys[1:4]
gas_planets = solarsys[4:]
print('태양계의 암석형 행성:',end='');print(rock_planets)
print('태양계의 가스형 행성:',end='');print(gas_planets)

#104 리스트에서 짝수 번째 요소만 추출
listdata = list(range(1, 21))
evenlist = listdata[1::2]
print(evenlist)
# 홀수 번째
oddlist = listdata[::2]
print(oddlist)

#105 리스트 요소 순서를 역순으로 만들기(reverse)
listdata = list(range(5))
listdata.reverse()
print(listdata)   # [4, 3, 2, 1, 0]이 출력됨

#106 리스트 요소 순서를 역순으로 만들기(reversed)
listdata = list(range(5))
ret1 = reversed(listdata)
print('원본 리스트', end='');print(listdata)
print('역순 리스트', end='');print(list(ret1))

ret2 = listdata[::-1]
print('슬라이싱 이용', end='');print(ret2)

#107 리스트 합치기(+)
listdata1 = ['a', 'b', 'c', 'd', 'e']
listdata2 = ['f', 'g', 'h', 'i', 'j']
listdata3 = listdata1 + listdata2
listdata4 = listdata2 + listdata1
print(listdata3)   # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']가 출력됨
print(listdata4)   # ['f', 'g', 'h', 'i', 'j', 'a', 'b', 'c', 'd', 'e']가 출력됨

#108 리스트 반복하기(*)
listdata = list(range(3))
ret = listdata * 3
print(ret)   # [0, 1, 2, 0, 1, 2, 0, 1, 2]가 출력됨

#109 리스트에 요소 추가(append)
listdata = []
for i in range(3):
    txt = input('리스트에 추가할 값을 입력하세요[%d/3]:' %(i+1))
    listdata.append(txt)
    print(listdata)

#110 리스트의 특정 위치에 요소 삽입(insert)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print(solarsys)

#111 리스트의 특정 위치의 요소 제거(del)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
del solarsys[0]
print(solarsys)
del solarsys[-2]
print(solarsys)

#112 리스트에서 특정 요소 제거(remove)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solarsys.remove('태양')
print(solarsys)

#113 리스트에서 특정 구간에 있는 모든 요소 제거
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
del solarsys[1:3]
print(solarsys)

#114 리스트에 있는 요소 개수 구하기(len)
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
listsize = len(listdata)
print(listsize)   # 15가 출력됨

#115 리스트에서 특정 요소 개수 구하기(count)
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
c1 = listdata.count(2)
c2 = listdata.count(7)
print(c1)   # 3이 출력됨
print(c2)   # 1이 출력됨

#116 리스트 제거하기(del)
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
del listdata
print(listdata)

#117 리스트 요소 정렬(sort)
namelist = ['Marry', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
namelist.sort()
print(namelist)   # ['Aimy', 'Bob', 'Kelly', 'Marry', 'Michale', 'Sams', 'Tom']가 출력됨
namelist.sort(reverse=True)
print(namelist)   # ['Tom', 'Sams', 'Michale', 'Marry', 'Kelly', 'Bob', 'Aimy']가 출력됨

#118 리스트 요소 정렬(sorted)
namelist = ['Marry', 'Sams', 'Aimy', 'Tom', 'Michale', 'Bob', 'Kelly']
ret1 = sorted(namelist)
ret2 = sorted(namelist, reverse=True)
print(namelist)
print(ret1)
print(ret2)

"""
sort()   : 원본 리스트를 정렬한 형태로 변경
sorted() : 원본 리스트는 그대로 두고 정렬한 결과 리스트 리턴
"""

#119 리스트 요소 무작위로 섞기(shuffle)
from random import shuffle

listdata = list(range(1, 11))
for i in range(3):
    shuffle(listdata)
    print(listdata)      # 출력 결과는 실행할 때마다 달라짐

#120 리스트의 모든 요소를 인덱스와 쌍으로 추출(enumerate)
solarsys = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
ret = list(enumerate(solarsys))
print(ret)

for i, body in enumerate(solarsys):
    print('태양계의 %d번째 천체 : %s' %(i, body))

#121 리스트의 모든 요소의 합 구하기(sum)
listdata = [2, 2, 1, 3, 8, 5, 7, 6, 3, 6, 2, 3, 9, 4, 4]
ret = sum(listdata)
print(ret)  # 65가 출력됨

#122 리스트 요소가 모두 참인지 확인(all, any)
# 거짓 : 0(숫자), ''(빈 문자열), ""(빈 문자열), [](빈 리스트), ()(빈 튜플), {}(빈 사전), None
listdata1 = [0, 1, 2, 3, 4]
listdata2 = [True, True, True]
listdata3 = ['', [], (), {}, None, False]
print(all(listdata1))   # False가 출력됨
print(any(listdata1))   # True가 출력됨
print(all(listdata2))   # True가 출력됨
print(any(listdata2))   # True가 출력됨
print(all(listdata3))   # False가 출력됨
print(any(listdata3))   # False가 출력됨

#123 사전에 요소 추가
solar1 = ['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
solar2 = ['Sun', 'Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solardict = {} # 순서가 없는 사전 자료
for i, k in enumerate(solar1):
    val = solar2[i]
    solardict[k] = val
    
print(solardict)

#124 사전의 특정 요소값 변경
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
names['Aimy'] = 10000
print(names)

#125 사전의 특정 요소 제거(del)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
del names['Sams']
print(names)

#126 사전의 모든 요소 제거(clear)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
names.clear()
print(names)

#127 사전에서 키만 추출(keys)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
ks = names.keys()
print(ks)

for k in ks:
    print('Key:%s \tValue:%d' %(k, names[k]))

#128 사전에서 값만 추출(values)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
vals = names.values()
print(vals)

vals_list = list(vals)
ret = sum(vals_list)
print('출생아 수 총계: %d' %ret)

#129 사전 요소를 모두 추출(items)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
items = names.items()
print(items)

for item in items:
    print(item)

#130 사전에 특정 키가 존재하는지 확인(in)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
k = input('이름을 입력하세요:')
if k in names:
    print('이름이 <%s>인 출생아 수는 <%d>명입니다.' %(k, names[k]))
else:
    print('자료에 <%s>인 이름이 존재하지 않습니다.' %k)

#131 사전 정렬(sorted)
names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245,
         'Michale':27115, 'Bob':5887, 'Kelly'7855}
ret1 = sorted(names)
print(ret1)

def f1(x):
    return x[0]

def f2(x):
    return x[1]

ret2 = sorted(names.items(), key=f1)
print(ret2)

ret3 = sorted(names.items(), key=f2)
print(ret3)

ret4 = sorted(names.items(), key=f2, reverse=True)
print(ret4)

#132 문자 코드값 구하기(ord)
ch = input('문자를 1개 입력하세요:')
if len(ch) != 0:
    ch = ch[0]
    chv = ord(ch)
    print('문자: %s \t코드값: %d[%s]' %(ch, chv, hex(chv)))

#133 코드값에 대응하는 문자 얻기(chr)
val = input('문자 코드값을 입력하세요:')
val = int(val)
try:
    ch = chr(val)
    print('코드값: %d[%s], 문자: %s' %(val, hex(val), ch))
except ValueError:
    print('입력한 <%d>에 대한 문자가 조냊하지 않습니다!' %val)

#134 문자열도 된 식을 실행(eval)
expr1 = '2+3'
expr2 = 'round(3.7)'
ret1 = eval(expr1)
ret2 = eval(expr2)
print('<%s>를 eval()로 실행한 결과:' %expr1, end='');print(ret1)
print('<%s>를 eval()로 실행한 결과:' %expr2, end='');print(ret2)

#135 이름없는 한줄짜리 함수 만들기(lambda)
add = lambda x, y: x + y
ret = add(1, 3)
print(ret)   # 4가 출력됨

funcs = [lambda x: x + '.pptx', lambda x: x + '.docx']
ret1 = funcs[0]('intro')
ret2 = funcs[1]('Report')
print(ret1)   # 'intro.pptx'가 출력됨
print(ret2)   # 'Report.docx'가 출력됨

names = {'Mary':10999, 'Sams':2111, 'Aimy':9778, 'Tom':20245, 'Michale':27115, 
         'Bob':5887, 'Kelly'7855}
ret3 = sorted(names.items(), key=lambda x: x[0]) # names의 키를 기준으로 오름차순으로 정렬한 결과를 리턴
print(ret3)

"""
def 함수이름(인자,...):
    실행코드
   
lambda 인자, 인자...: 실행코드
"""

#136 인자를 바꾸어 함수를 반복 호출하여 결과값 얻기(map)
f = lambda x: x * x
args = [1, 2, 3, 4, 5]
ret = map(f, args)
print(list(ret))

#137 텍스트 파일을 읽고 출력(read)
f = open('stockcode.txt', 'r')
data = f.read()
print(data)
f.close()

#138 텍스트 파일을 한줄씩 읽고 출력(readline)
f = open('stockcode.txt', 'r')
line_num = 1
line = f.readline()
while line:
    print('%d: %s' %(line_num, line), end='')
    line = f.readline()
    line_num += 1
f.close()

#139 텍스트 파일을 한줄씩 읽고 출력(readlines)
f = open('stockcode.txt', 'r')
lines = f.readlines()
for line_num, line in enumerate(lines):
    print('%d %s' %(line_num+1, line), end='')
f.close()

#140 화면에서 사용자 입력을 받고 파일로 쓰기(write)
text = input('파일에 저장할 내용을 입력하세요:')
f = open('mydata.txt', 'w')
f.write(text)
f.close()

#141 텍스트 파일에 한줄씩 쓰기(writelines)
count = 1
data = []
print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요')
while True:
    text = input('[%d]파일에 저장할 내용을 입력하세요: ' %count)
    if text == '':
        break
    data.append(text + '\n')
    count += 1

f = open('mydata.txt', 'w')
f.writelines(data)
f.close()

#142 텍스트 파일 복사(read, write)
f = open('stockcode.txt', 'r')
h = open('stockcode_copy.txt', 'w')

data = f.read()
h.write(data)

f.close()
h.close()

#143 바이너리 파일 복사(read, write)
bufsize = 1024 # 1024 = 1KB
f = open('img_sample.jpg', 'wb')
h = open('img_sample_copy.jpg', 'rb')

data = f.read(bufsize)
while data:
    h.write(data)
    data = f.read(bufsize)
    
f.close()
h.close()

#144 파일을 열고 자동으로 닫기(with ~ as)
with open('stockcode.txt', 'r') as f:
    for line_num, line in enumerate(f.readlines()):
        print('%d %s' %(line_num+1, line), end='')

#145 파일의 특정 부분만 복사(seek, read, write)
spos = 105     # 파일을 읽는 위치 저장
size = 500     # 읽을 크기를 지정

f = open('stockcode.txt', 'r')
h = open('stockcode_part.txt', 'w')

f.seek(spos)
data = f.read(size)
h.write(data)

h.close()
f.close()

#146 파일의 크기 구하기(os.path.getsize)
from os.path import getsize

file1 = 'stockcode.txt'
file2 = 'd:/devlab/py200/img_sample.jpg'
file_size1 = getsize(file1)
file_size2 = getsize(file2)

print('File Name: %s \tSize: %d bytes' %(file1, file_size1))
print('File Name: %s \tSize: %d bytes' %(file2, file_size2))

#147 파일 삭제(os.remove)
from os import remove

target_file = 'stockcode_copy.txt'
k = input('[%s] 파일을 삭제하겠습니까? (y/n): ' %target_file)
if k == 'y':
    remove(target_file)
    print('[%s] 파일을 삭제했습니다.' %target_file)

#148 파일 이름 바꾸기(os.rename)
from os import rename

target_file = 'stockcode.txt'
newname = input('[%s]에 대한 새로운 파일이름을 입력하세요:' %target_file)
rename(target_file, newname)
print('[%s] -> [%s]로 파일이름이 변경되었습니다.' %(target_file, newname))

#149 파일을 다른 디렉터리로 이동(os.rename)
from os import rename

target_file = 'stockcode.txt'
newpath = input('[%s]를 이동할 디렉터리의 절대경로를 입력하세요:' %target_file)

if newpath[-1] == '/':
    newname = newpath + target_file
else:
    newname = newpath + '/' + target_file
    
try:
    rename(target_file, newname)
    print('[%s] -> [%s]로 이동되었습니다.' %(target_file, newname))
except FileNotFoundError as e:
    print(e)

#150 디렉터리에 있는 파일목록 얻기(os.listdir, glob.glob)
import os, glob

folder = 'd:/devlab/py200'
file_list = os.listdir(folder)
print(file_list)

files = '*.txt'
file_list = glob.glob(files)
print(file_list)

"""
listdir() : 인자로 입력된 조건이나 경로에 해당하는 파일들을 리스트로 리턴
glob()    : 인자는 윈도우 명령 프롬프트나 유닉스 쉘 프로그램에서 사용하는 와일드카드(*)를 사용 가능
"""

#151 현재 디렉터리 확인하고 바꾸기(os.getcwd, os.chdir)
import os

pdir = os.getcwd(); print(pdir)
os.chdir('..'); print(os.getcwd())
os.chdir(pdir); print(os.getcwd())

#152 디렉터리 생성(os.mkdir)
import os

newfolder = input('새로 생성할 디렉터리 이름을 입력하세요:')
try:
    os.mkdir(newfolder)
    print('[%s] 디렉터리가 생성되었습니다.' %newfolder)
except Exception as e:
    print(e)

#153 디렉터리 제거(os.rmdir)
import os

target_folder = 'tmp'
k = input('[%s] 디렉터리를 삭제하겠습니까? (y/n): ' %target_folder)
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('[%s] 디렉터리를 삭제되었습니다.' %target_folder)
    except Exception as e:
        print(e)

#154 하위 디렉터리 및 파일 전체 삭제(shutil.rmtree)
import shutil
import os

target_folder = 'd:/devlab/py200/tmp'
print('[%s] 하위 모든 디렉터리 및 파일들을 삭제합니다.' %target_folder)
for file in os.listdir(target_folder):
    print(file)
k = input('[%s]를 삭제하겠습니까? (y/n): ' %target_folder)
if k == 'y':
    try:
        shutil.rmtree(target_folder)
        print('[%s] 모든 하위 디렉터리와 파일들을 삭제했습니다.' %target_folder)
    except Exception as e:
        print(e)

#155 파일이 존재하는지 체크(os.path.exists)
import os
from os.path import exists

dir_name = input('새로 생성할 디렉터리 이름을 입력하세요:')
if not exists(dir_name):
    os.mkdir(dir_name)
    print('[%s] 디렉터리를 생성되었습니다.' %dir_name)
else:
    print('[%s](는) 이미 존재합니다.' %dir_name)

#156 파일인지 디렉터리인지 확인(os.path.isfile, os.path.isdir)
import os
from os.path import exists, isdir, isfile

files = os.listdir()
for file in files:
    if isdir(file):
        print('DIR: %s' %file)

for file in files:
    if isfile(file):
        print('FILE: %s' %file)

#157 현재 시간을 년-월-일 시:분:초로 출력(localtime, strftime)
from time import localtime, strftime

logfile = 'test.log'
def writelog(logfile, log):
    time_stamp = strftime('%Y-%m-%d %X\t', localtime())
    log = time_stamp + log + '\n'
    
    with open(logfile, 'a') as f:
        f.writelines(log)
        
writelog(logfile, '첫 번째 로깅 문장입니다.')

#158 올해 경과된 날짜수 계산(localtime)
from time import localtime

t = localtime()
start_day = '%d-01-01' %t.tm_year
elapsed_day = t.tm_yday

print('오늘은 [%s]이후 [%d]일째 되는 날입니다.' %(start_day, elapsed_day))

#159 오늘의 요일 계산(localtime)
from time import localtime

weekdays = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']

t = localtime()
today = '%d-%d-%d' %(t.tm_year, t.tm_mon, t.tm_mday)
week = weekdays[t.tm_wday]

print('[%s] 오늘은 [%s]입니다.' %(today, week))

#160 프로그램 실행 시간 계산(datetime.now)
from datetime import datetime

start = datetime.now()
print('1에서 백만까지 더합니다.')
ret = 0
for i in range(1000001):
    ret += i
print('1에서 백만까지 더한 결과: %d' %ret)
end = datetime.now()
elapsed = end - start
print('총 계산 시간: ', end='');print(elapsed)
elapsed_ms = int(elapsed.total_seconds()*1000)
print('총 계산 시간: %dms' %elapsed_ms)

#161 주어진 숫자를 천 단위로 구분
num = input('아무 숫자를 입력하세요: ')

if num.isdigit():
    num = num[::-1]
    ret = ''
    for i, c in enumerate(num):
        if i != len(num) and i%3 == 0:
            ret += (c + ',')
        else:
            ret += c
    ret = ret[::-1]
    print(ret)
else:
    print('입력한 내용 [%s]: 숫자가 아닙니다.' %num)

#162 문자열의 각 문자를 그 다음 문자로 변경 
text = input('문자열을 입력하세요:')

ret = ''
for i in range(len(text)):
    if i != len(text) - 1:
        ret += text[i+1]
    else:
        ret += text[0]

print(ret)

#163 URL에서 호스트 도메인 추출
url = 'http://news.naver.com/main.read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('/')
domain = tmp[2]
print(domain)

#164 URL에서 쿼리 문자열 추출
url = 'http://news.naver.com/main.read.nhn?mode=LSD&mid=shm&sid1=105&oid=028&aid=0002334601'

tmp = url.split('?')
queries = tmp[1].split('&')
for query in queries:
    print(query)

#165 스택 구현(append, pop)
mystack = []

def putdata(data):
    global mystack
    mystack.append(data)
    
def popdata():
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()

putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

print('<스택상태>: ', end='');print(mystack)

ret = popdata()
while ret != None:
    print('스택에서 데이터 추출:', end='');print(ret)
    print('<스택상태>: ', end='');print(mystack)
    ret = popdata()

#166 문장에 나타나는 문자 빈도수 계산
def getTextFreq(filename):
    with open(filename, 'r') as f:
        text = f.read()
        fa = {}
        for c in text:
            if c in fa:
                fa[c] += 1
            else:
                fa[c] = 1
    return fa

ret = getTextFreq('mydata.txt')
ret = sorted(ret.items(), key=lambda x:x[1], reverse=True)
for c, freq in ret:
    if c == '\n':
        continue
    print('[%c] -> [%d]회 나타남' %(c, freq))

#167 텍스트 파일에 있는 단어 개수 계산
with open('mydata.txt', 'r') as f:
    data = f.read()
    tmp = data.split()
    print('단어수 : [%d]' %len(tmp))

#168 파일에서 특정 단어 개수 계산
def countWord(filename, word):
    with open(filename, 'r') as f:
        text = f.read()
        text = text.lower()
        pos = text.find(word)
        count = 0
        while pos != -1:
            count += 1
            pos = text.find(word, pos + 1)
    return count

word = input('mydata.txt에서 개수를 구할 단어를 입력하세요: ')
word = word.lower()
ret = countWord('mydata.txt', word)
print('[%s]의 개수: %d' %(word, ret))

#169 파일에서 특정 문자열 교체
t1 = input('찾을 단어를 입력하세요: ')
t2 = input('변경할 단어를 입력하세요: ')

with open('mydata.txt', 'r') as f:
    with open('mydata2.txt, 'w) as h
        text = f.read()
        text = text.replace(t1, t2)
        h.write(text)
        
print('[%s]를 [%s]로 변경하였습니다.' %(t1, t2))
        
#170 URL에 접속하여 HTML 페이지 화면에 출력
from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    print(doc)

#171 URL에 접속하여 HTML 페이지를 파일로 저장
from urllib.request import urlopen

url = 'https://www.python.org'
with urlopen(url) as f:
    doc = f.read().decode()
    with open('pyhonhome.html', 'w') as h:
        h.writelines(doc)

#172 인터넷에 있는 이미지를 내 PC로 저장
from urllib.request import urlopen

imgurl = 'http://www.iaidol.com/img_sample.jpg'
imgname = imgurl.split('/')[-1]
try:
    with urlopen(imgurl) as f:
        with open(imgname, 'wb') as h:
            imgdata = f.read()
            h.write(img)
except Exception as e:
    print(e)

#173 인터넷에 있는 대용량 파일을 내 PC로 저장(용량을 BUFSIZE로 쪼개서 다운로드)
from urllib.request import urlopen

BUFSIZE = 256*1024

fileurl = 'https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe'
filename = fileurl.split('/')[-1]
try:
    with urlopen(fileurl) as f:
        with open(filename. 'wb') as h:
            buf = f.read(BUFSIZE)
            while buf:
                h.write(buf)
                buf = f.read(BUFSIZE)
except Exception as e:
    print(e)

#174 10MB 파일을 1MB 파일 10개로 분리
filename = 'python-3.8.2.exe'
subsize = 1024*1024*3  # 3MB
suffix = 0

with open(filename, 'rb') as f:
    buf = f.read(subsize)
    while buf:
        subfilename = filename + '_' + str(suffix)
        with open(subfilename, 'wb') as h:
            h.write(buf)
            print('[%s] 완료' %subfilename)
            
        buf = f.read(subsize)
        suffix += 1

#175 1MB 파일 10개를 합쳐서 10MB 파일로 만들기
BUFSIZE = 256*1024
merge_filename = 'ret.exe'
filelist = ['python=3.5.2.exe+' + str(x) for x in range(10)]

with open(merge_filename, 'wb') as f:
    for filename in filelist:
        print('[%s] 합치는 중..' %filename)
        with open(filename, 'rb') as h:
            buf = h.read(BUFSIZE)
            while buf:
                f.write(buf)
                buf = h.read(BUFSIZE)

print('파일 합치기가 완료되었습니다.')

#176 파일을 ZIP 압축 파일로 만들기
from zipfile import *

def compressZip(zipname, filename):
    print('[%s] -> [%s] 압축...' %(filename, zipname))
    with ZipFile(zipname, 'w') as ziph:
        ziph.write(filename)
        
    print('압축이 끝났습니다.')

filename = 'mydata.txt'
zipname = filename + '.zip'
compressZip(zipname, filename)

#177 디렉터리를 하나의 ZIP 압축 파일로 만들기
from zipfile import *
import os

def compressAll(zipname, folder):
    print('[%s] -> [%s] 압축...' %(folder, zipname))
    with ZipFile(zipname, 'w') as ziph:
        for dirname, subdirs, files in os.walk(folder):
            for file in files:
                ziph.write(os.path.join(dirname, file))
    
folder = 'tmp'
zipname = folder + '.zip'
compressAll(zipname, folder)

#178 ZIP 파일 압축 풀기
from zipfile import *

def extractZip(zipname):
    with ZipFile(zipname, 'r') as ziph:
        ziph.extractall()
        print('[%s]가 성공적으로 추출되었습니다.' %zipname)
        
extractZip('files.zip')

#179 로또 번호 추출기 만들기
from random import shuffle
from time import sleep

gamenum = input('로또 게임 회수를 입력하세요: ')

for i in range(int(gamenum)):
    balls = [x+1 for x in range(45)]
    ret = []
    for j in range(6):
        shuffle(balls)
        number = balls.pop()
        ret.append(number)
    ret.sort()
    print('로또 번호[%d]: ' %(i+1), end='')
    print(ret)
    sleep(1)

#180 남녀 파트너 정해주기 프로그램 만들기(zip) : 동일한 요소 개수를 가진 두 개 이상의 리스트를 인자로 받고, 각 리스트의 같은 인덱스의 요소들끼리 묶은 튜플을 요소로 하는 리스트로 만들어 리턴
from random import shuffle

male = ['슈퍼맨', '심봉사', '로미오', '이몽룡', '마루치']
female = ['원더우먼', '뺑덕', '줄리엣', '성춘향', '아라치']
shuffle(male)
shuffle(female)
couples = zip(male, female)

for i, couple in enumerate(couples):
    print('커플[%d]: [%s] - [%s]' %(i+1, couple[0], couple[1]))

#181 데이터 처리하기_1 연도별 출생아 수 계산
def countBirths():
    ret = []
    for y in range(1880, 2016):
        count = 0
        filename = 'names/yob%d.txt' %y
        with open(filename, 'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':
                    d d[:-1]
            
                birth = d.split(',')[2]
                count += int(birth)
        ret.append((y, count))
    return ret

result = countBirths()
with open('birth_by_year.csv', 'w') as f:
    for year, birth in result:
        data = '%s, %s\n' %(year, birth)
        print(data)
        f.writhe(data)

#182 데이터 처리하기_2 연도별 성별 출생아 수 계산
def countBirthsBySex():
    ret = []
    for y in range(1880, 2016):
        count_f = 0                # 여자아기 출생아 수
        conut_m = 0                # 남자아기 출생아 수
        filename = 'names/yob%d.txt' %y
        with open(filename, 'r') as f:
            data = f.readlines()
            for d in data:
                if d[-1] == '\n':
                    d = d[:-1]
                    
                tmp = d.split(',')
                sex = tmp[1]
                birth = tmp[2]
                
                if sex == 'F':
                    count_f += int(birth)
                else:
                    count_m += int(birth)
        ret.append((y, count_f, count_m))
    return ret

result = countBirthsBySex()
with open('birth_by_sex.csv', 'w') as f:
    for y, bf, bm in result:
        data = '%s, %s, %s\n' %(y, bf, bm)
        print(data)
        f.write(data)    

#183 데이터 처리하기_3 연도별 인기있는 상위 10개 성별 출생아 이름 구하기
from os.path import exists

def getTop10BabyName(year):
    nameF = { }
    nameM = { }
    
    filename = 'names/yob%d.txt' %year
    if not exists(filename):
        print('[%s] 파일이 존재하지 않습니다.' %filename)
        return None
        
    with open(filename, 'r') as f:
        data = f.readlines()
        for d in data:
            if d[-1] == '\n':
                d = d[:-1]
            
            tmp = d.split(',')
            name = tmp[0]
            sex = tmp[1]
            birth = tmp[2]
            
            if sex == 'F':
                ret = nameF
            else:
                ret = nameM
            
            if name in ret:
                ret[name] += int(birth)
            else:
                ret[name] = int(birth)
    
    retF = sorted(nameF.items(), key=lambda x:x[1], reverse=True)
    retM = sorted(nameM.items(), key=lambda x:x[1], reverse=True)
    
    for i, name in enumerate(retF):
        if i > 9:
            break
        print('TOP_%d 여자아기이름: %s' %(i+1, name))
    
    for i, name in enumerate(retM):
        if i > 9:
            break
        print('TOP_%d 남자아기이름: %s' %(i+1, name))
    
y = input('인기순 상위10개 이름을 알고 싶은 출생년도를 입력하세요(예:2001): ')
getTop10BabyName(y)

#184 웹서버 로그 처리하기_1 총 페이지뷰 수 계산
pageviews = 0

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        status = log[8]
        if status == '200':
            pageviews += 1
    
print('총 페이지뷰: [%d]' %pageviews)

#185 웹서버 로그 처리하기_2 고유 방문자 수 계산
visit_ip = [ ]

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        if ip not in visit_ip:
            visit_ip.append(ip)
            
print('고유 방문자 수: [%d]' %len(visit_ip))

#186 웹서버 로그 처리하기_3 총 서비스 용량 계산
KB = 1024
total_service = 0

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        servicebyte = log[9]
        if servicebyte.isdigit():
            total_service += int(servicebyte)
        
total_service /= KB
print('총 서비스 용량: %dKB' %total_service)

#187 웹서버 로그 처리하기_4 사용자별 서비스 용량 계산
services = [ ]

with open('access_log', 'r') as f:
    logs = f.readlines()
    for log in logs:
        log = log.split()
        ip = log[0]
        servicebyte = log[9]
        if servicebyte.isdigit():
            servicebyte = int(servicebyte)
        else:
            servicebyte = 0
            
        if ip not in services:
            services[ip] = servicebyte
        else:
            services[ip] += servicebyte
            
ret = sorted(services.items(), key=lambda x:x[1], reverse=True)

print('사용자IP - 서비스용량')
for ip, b in ret:
    print('[%s] - [%d]' %(ip, b))

#188 간단한 슈팅게임 만들기_1 게임화면 구성
import pygame

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640

# 게임 실행 메인 함수
def runGame():
    global gamepad, clock
    
    on game = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                doneFlag = True
        
        # 게임 화면을 검은색으로 채우고 화면을 업데이트 함
        gamepad.fill(BLACK)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    
# 게임 초기화 함수
def initGame():
    global gamepad, clock
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    clock = pygame.time.Clock()
    
initGame()
runGame()

#189 간단한 슈팅게임 만들기_2 전투기 배치
import pygame

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 48

# 게임에 등장하는 객체를 드로잉
def drawObjecgt(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
# 게임 실행 메인 함수
def runGame():
    global gamepad, clock,flighter
    
    # 전투기 초기 위치 (x, y) 설정
    x = int(pad_width * 0.45)
    y = int(pad_height * 0.9)
    x_change = 0
    
    on game = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        # 게임 화면을 검은색으로 채우기
        gamepad.fill(BLACK)
        
        # 전투기 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width
            
        drawObject(fighter, x, y)
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()
    
# 게임 초기화 함수
def initGame():
    global gamepad, clock, fighter
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    clock = pygame.time.Clock()
    
initGame()
runGame()

#190 간단한 슈팅게임 만들기_2 전투기 배치
import pygame
import random

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 48
enemy_width = 26
enemy_height = 20

# 게임에 등장하는 객체를 드로잉
def drawObjecgt(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
# 게임 실행 메인 함수
def runGame():
    global gamepad, clock, flighter, enemy
    
    # 전투기 초기 위치 (x, y) 설정
    x = int(pad_width * 0.45)
    y = int(pad_height * 0.9)
    x_change = 0
    
    # 적 초기 위치 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3
    
    on game = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        # 게임 화면을 검은색으로 채우기
        gamepad.fill(BLACK)
        
        # 전투기 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width
            
        drawObject(fighter, x, y)
        
        # 적을 아래로 움직임
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            
        drawObject(enemy, enemy_x, enemy_y)
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit() 
    
# 게임 초기화 함수
def initGame():
    global gamepad, clock, fighter, enemy
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    clock = pygame.time.Clock()
    
initGame()
runGame()

#191 간단한 슈팅게임 만들기_4 무기 발사
import pygame
import random

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 48
enemy_width = 26
enemy_height = 20

# 게임에 등장하는 객체를 드로잉
def drawObjecgt(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
# 게임 실행 메인 함수
def runGame():
    global gamepad, clock, flighter, enemy, bullet
    
    # 무기 좌표를 위한 리스트 자료
    bullet_xy = [ ]
    
    # 전투기 초기 위치 (x, y) 설정
    x = int(pad_width * 0.45)
    y = int(pad_height * 0.9)
    x_change = 0
    
    # 적 초기 위치 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3
    
    on game = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
                    
            # 왼쪽 컨트롤 키를 누르면 무기 발사. 무기는 한 번에 2발만 발사됨
            elif event.key == pygame.K_LCTRL:
                if len(bullet_xy) < 2:
                    bullet_x = x + int(fighter_width/2)
                    bullet_y = y - fighter_height
                    bullet_xy.append([bullet_x, bullet_y])
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        # 게임 화면을 검은색으로 채우기
        gamepad.fill(BLACK)
        
        # 전투기 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width
            
        drawObject(fighter, x, y)
        
        # 전투기 무기 발사 화면에 그리기
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
                    
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)
        
        # 적을 아래로 움직임
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            
        drawObject(enemy, enemy_x, enemy_y)
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit() 
    
# 게임 초기화 함수
def initGame():
    global gamepad, clock, fighter, enemy, bullet
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock()
    
initGame()
runGame()

#192 간단한 슈팅게임 만들기_5 게임규칙 적용
import pygame
import random
from time import sleep

# 게임에 사용되는 전역변수 정의
BLACK = (0, 0, 0)
RED = (255, 0, 0)
pad_width = 480
pad_height = 640
fighter_width = 36
fighter_height = 48
enemy_width = 26
enemy_height = 20

# 적을 맞춘 개수 계산
def drawScore(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemy Kills: ' + str(count), True, (255, 255, 255))
    gamepad.blit(text, (0, 0)) 

# 적이 화면 아래로 통과한 개수
def drawPassed(count):
    global gamepad
    font = pygame.font.SysFont(None, 20)
    text = font.render('Enemies Passed: ' + str(count), True, RED)
    gamepad.blit(text, (360, 0))

# 화면에 글씨 보이게 하기
def dispMessage(text):
    global gamepad
    textfont = pygame.font.Font('freesansbold.ttf', 80)
    text = textfont.render(text, True, RED)
    textpos = text.get_rect()
    textpos.cnter = (int(pad_width/2), int(pad_height/2))
    gamepad.blit(text, textpos)
    pygame.display.update()
    sleep(2)
    runGame()
    
# 전투기가 적과 충돌했을 때 메시지 출력
def crash():
    global gamepad
    dispMessage('CRASHED!')

# 게임오버 메시지 보이기
def gameover():
    global gamepad
    dispMessage('GAME OVER')

# 게임에 등장하는 객체를 드로잉
def drawObjecgt(obj, x, y):
    global gamepad
    gamepad.blit(obj, (x, y))
    
# 게임 실행 메인 함수
def runGame():
    global gamepad, clock, flighter, enemy, bullet
    
    # 전투기 무기에 적이 맞았을 경우 True로 설정되는 플래그
    isShot = False
    shotcount = 0
    enemypassed = 0
    
    # 무기 좌표를 위한 리스트 자료
    bullet_xy = [ ]
    
    # 전투기 초기 위치 (x, y) 설정
    x = int(pad_width * 0.45)
    y = int(pad_height * 0.9)
    x_change = 0
    
    # 적 초기 위치 설정
    enemy_x = random.randrange(0, pad_width - enemy_width)
    enemy_y = 0
    enemy_speed = 3
    
    on game = False
    while not ongame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ongame = True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change -= 5
                
                elif event.key == pygame.K_RIGHT:
                    x_change += 5
                    
            # 왼쪽 컨트롤 키를 누르면 무기 발사. 무기는 한 번에 2발만 발사됨
           됨elif event.key == pygame.K_LCTRL:
                if len(bullet_xy) < 2:
                    bullet_x = x + int(fighter_width/2)
                    bullet_y = y - fighter_height
                    bullet_xy.append([bullet_x, bullet_y])
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        
        # 게임 화면을 검은색으로 채우기
        gamepad.fill(BLACK)
        
        # 전투기 위치를 재조정
        x += x_change
        if x < 0:
            x = 0
        elif x > pad_width - fighter_width:
            x = pad_width - fighter_width
            
        # 게이머 전투기가 적과 충돌했는지 체크
        if y < enemy_y + enemy_height:
            if (enemy_x > x and enemy_x < x + fighter_width) or \
                (enemy_x + enemy_width > x and enemy_x + enemy_width < x + fighter_width):
                crash()
            
        drawObject(fighter, x, y)
        
        # 전투기 무기 발사 화면에 그리기
        if len(bullet_xy) != 0:
            for i, bxy in enumerate(bullet_xy):
                bxy[1] -= 10
                bullet_xy[i][1] = bxy[1]
                
                # 전투기 무기가 적을 격추했을 경우
                if bxy[1] < enemy_y:
                    if bxy[0] > enemy_x and bxy[0] < enemy_x + enemy_width:
                        bullet_xy.remove(bxy)
                        isShot = True
                        shotcount += 1
                  
                if bxy[1] <= 0:
                    try:
                        bullet_xy.remove(bxy)
                    except:
                        pass
                    
        if len(bullet_xy) != 0:
            for bx, by in bullet_xy:
                drawObject(bullet, bx, by)
        
        drawScore(shotcount)
        
        # 적을 아래로 움직임
        enemy_y += enemy_speed
        if enemy_y > pad_height:
            enemy_y = 0
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemypassed += 1
        
        if enemypassed == 3:
            gameover()
        
        drawPassed(enemypassed)
        
        # 적이 무기에 맞았는지 체크하고 맞았으면 스피드업
        if isShot:
            enemy_speed += 1
            if enemy_speed >= 10:
                enemy_speed = 10
            
            enemy_x = random.randrange(0, pad_width - enemy_width)
            enemy_y = 0
            isShot = False
            
        drawObject(enemy, enemy_x, enemy_y)
        
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit() 
    
# 게임 초기화 함수
def initGame():
    global gamepad, clock, fighter, enemy, bullet
    
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_height))
    pygame.display.set_caption('MyGalaga')
    fighter = pygame.image.load('fighter.png')
    enemy = pygame.image.load('enemy.png')
    bullet = pygame.image.load('bullet.png')
    clock = pygame.time.Clock()
    
initGame()
runGame()

#193 에코 서버 만들기_1
import socket

HOST = ''
PORT = 9009

def runServer():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((HOST, PORT))
        sock.listen(1)
        print('클라이언트 연결을 기다리는 중..')
        conn. addr = sock.accept()
        with conn:
            print('[%s]와 연결됨' %addr[0])
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('메시지 수신[%s]' %data.decode())
                conn.sendall(data)

runServer()

#194 에코 클라이언트 만들기_1
import socket

HOST = 'localhost'
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    msg = input('메시지 입력: ')
    sock.sendall(msg.encode())
    data = sock.recv(1024)

print('에코 서버로부터 받은 데이터 [%s]' %data.decode())

#195 에코 서버 만들기_1
import socket

HOST = ''
PORT = 9009

class MyTcpHandler(socketserver.BaseRequestHandler):
    # 이 클래스는 서버 하나당 단 한 번 초기화됩니다.
    # handle() 메소드에 클라이언트 연결 처리를 위한 로직을 구현합니다.
    def handle(self):
        print('[%s] 연결됨' %self.client_address[0])
        
        try:
            while True:
                self.data = self.request.recv(1024)
                if self.data.decode() == '/quit':
                    print('[%s] 사용자에 의해 중단' %self.client_address[0])
                    return
                
                print('[%s] %self.data.decode()')
                self.request.sendall(self.data)
        except Exception as e:
            print(e)
            
def runServer():
    print('+++ 에코 서버를 시작합니다.')
    print('+++ 에코 서버를 끝내려면 Ctrl+C를 누르세요.')
    
    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 에코 서버를 종료합니다.')

runServer()

#196 에코 클라이언트 만들기_2
import socket

HOST = 'localhost'
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    
    while True:
        msg = input('메시지 입력: ')
        if msg == '/quit':
            sock.sendall(msg.encode())
            break
        
        sock.sendall(msg.encode())
        data = sock.recv(1024)
        print('에코 서버로부터 받은 데이터 [%s]' %data.decode())
        
print('클라이언트 종료')

#197 파일 송신 프로그램 만들기
import socket
from os.path import exists

HOST = ''
PORT = 9009

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] 연결됨' %self.client_address[0])
        filename = self.request.recv(1024)
        filename = filename.decode()
        
        if not exists(filename):
            return
        
        print('파일 [%s] 전송 시작...' %filename)
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024)
                while data:
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
        
        print('전송완료 [%s], 전송량 [%d]' %(filename, data_transferred))
        
def runServer():
    print('+++ 파일 서버를 시작합니다.')
    print('+++ 파일 서버를 끝내려면 Ctrl+C를 누르세요.')
    
    try:
        server = socketserver.TCPServer((HOST, PORT), MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('--- 파일 서버를 종료합니다.')
        
runServer()

#198 파일 수신 프로그램 만들기


#199 채팅 서버 만들기


#200 채팅 클라이언트 만들기

