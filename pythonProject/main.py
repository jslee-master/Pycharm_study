from random import *


# Example


def day1():
    global str
    # ex1
    # 출력문 print
    print(10)
    # 실행 단축키 Shift + F10

    # ex2
    # 전체 주석
    # 원하는 범위만큼 블럭잡고 더블커텐션/커텐션 세번 입력 총 여섯개
    """
    print(10)
    print(20)
    """
    '''
    print(10)
    print(20)
    '''

    # ex3
    # 문자열 출력
    print('호랑이')

    # ex4
    # 숫자 문자 같이 출력 구분자 ','(콤마) 사용 / 콤마는 기본적으로 스페이스 입력함
    print(10, '호랑이', 20, '독수리', 3.14)

    # ex5
    # true/false 사용시 첫글자 대문자 꼭 사용
    print(True, False)

    # ex6
    # 코드 두줄을 한줄처리 할 경우 ";"세미콜론 사용
    print(10);
    print(20)

    # ex7
    # 기본적으로 문법에 "end='\n'"(줄바꿈/carriage return) 입력이 생략됨
    print(10, end='\n')
    print(20)

    # ex8
    # 구분선
    print('------------')
    # 구분선 여러개 출력
    print('-' * 50)

    # ex9
    # % 사용
    print('%d %d %s' % (10, 20, 'a'))
    print('코%d끼%d리%s' % (10, 20, 'a'))

    # ex10
    # 기본적으로 문법에 "sep=(' ')"(띄어쓰기) 입력이 생략됨
    print(10, 20, 30, 40)
    print(10, 20, 30, 40, sep=' ')

    # ex11
    # 기본적으로 문법에 입력이 생략된 두 코드
    print(10, 20, 30, 40, sep=' ', end='\n')

    # ex12
    # 타입 출력
    print(type(10), type('호랑이'), type(3.14), type(True))

    # ex13
    # 자료형
    # []-리스트, ()-튜플, {}-딕셔너리/사전 의미
    # <class 'list'> <class 'tuple'> <class 'dict'>
    print(type([]), type(()), type({}))

    # ex14
    # 정수형 문자열 변환
    print(10 + 20)
    # print(10+'호랑이') 문법이 성립하지 않음
    print('호랑이' + '독수리')
    print(10 + int('123'))
    print('호랑이' + str(10))

    # ex15
    # 변수 선언 4가지 유형
    # 파이썬은 변수를 선언하는 타입이 없음 - 새로 선언 하면 과거는 지워짐
    a = 10
    b = 20
    print(a, b)

    a = 30;
    b = 40
    print(a, b)
    # a = 10, b = 20 # ","를 사이에 넣어서 안되는 문법 ";"사용해야함

    a, b = 50, 60
    print(a, b)

    a = b = 70
    print(a, b)

    # ex16
    # 파이썬에서 스왑 프로그램
    a = 10
    b = 20
    b, a = a, b
    print(a, b)

    # ex17
    # 단항 연산 a++ 사용 안 됨
    a = 100
    # a++
    a = a + 1
    print(a)
    a += 1
    print(a)

    # ex18
    # 고유 식별 번호 검색 id 사용
    a = 10
    b = 20
    c = 10
    print(id(a), id(b), id(c))

    # 값의 메모리 번호를 가져서 같은 값은 변수명이 달라도 같은 id를 가짐
    a = '호랑이'
    b = '코끼리'
    c = '호랑이'
    print(id(a), id(b), id(c))

    # ex19
    # 16진수 표현
    a = 0x20
    print(a)

    # 8진수 표현
    b = 0o376
    print(b)

    # ex20
    # 복소수 사용 문법 a+bi
    j = 0
    a = 1 + j
    b = 3 + 4j
    print(a + b)

    # ex21
    # 나누기/, 몫%, 나머지//
    a = 10
    b = 3
    print(a / b, a % b, a // b)

    # ex22
    # 2의 8승
    print(2 ** 8)

    # ex23
    # round 함수 소수점 뒷자리 반올림
    print(round(3.145, 2))

    # ex24
    # 배열 문법으로 사용가능 실습
    str = 'apple'
    print(str[4])

    str = "무궁화꽃이피었습니다."
    print(str[4])

    str = "무궁화꽃이피었습니다."
    print(str[-2])

    # ex25
    # 많이 중요한 문법
    str = "무궁화꽃이피었습니다."
    #      [01 23 45 67 8 910]
    print(str[2:5])  # [시작인덱스:종료인덱스 앞까지 출력]
    # 해석 - 인덱스번호 2번부터 시작해서 5-2개 가져온다.

    str = "무궁화꽃이피었습니다."
    print(str[:5])  # 처음부터 5까지
    print(str[5:])  # 5번부터 끝까지

    # 동격 문법
    str = "무궁화꽃이피었습니다."
    print(str)
    print(str[:])

    # ex26
    str = 'apple'
    a = str[0]
    print(a)
    b = str[:2]
    print(b)

    # 문자열로 만들어진 변수는 만들어진 순간부터 상수화된다.
    # str[0] = 'B'
    print(a)

    c = 'B' + str[1:]
    print(c)


def day2():
    # ex27
    # 짝을 짓는 방법 실습
    print('호%d랑%s이' % (10, '코끼리'))
    # 하나만 사용할 때는 괄호 생략 가능
    print('호%d랑이' % 10)
    # .format 사용 방법
    print('무궁화{0}꽃이{1}피었습니다.'.format(10, '호랑이'))

    print("무궁화%d꽃이%s피었습니다." % (100, '호랑이'))
    print("무궁화{0}꽃이{1}피었습니다.".format('호랑이', 100))
    print('%s %s' % ("{0}무".format('무'), "{0}무".format('무', '마')))

    # 풀어서 해석
    # 1. 문자열 입력 사이에 {} 추가
    s = '무궁화{0}꽃이{1}피었습니다.'
    # 2. {}를 그대로 출력하는 것을 확인
    print(s)
    # 3. 출력문 변수 s에 format 사용되는 것을 확인
    print(s.format(10, '호랑이'))
    # 4. 변수 t에 s.format 대입되는 것을 확인
    t = s.format(10, '호랑이')
    print(t)
    # 5. sdp s.format 대입되는 것을 확인
    s = s.format(10, '호랑이')
    print(s)

    # ex28
    # 문자열의 개수를 얻을 때 'len' 사용
    s = '무궁화꽃이피었습니다'
    print(len(s))

    # ex29
    # 찾고자 하는 문자열의 개수를 얻을 때 문자열.count 사용
    s = '무궁화꽃이무궁화피었무궁화습니다무궁화'
    print(s.count('무궁화'))
    # 동격
    print('무궁화꽃이무궁화피었무궁화습니다무궁화'.count('무궁화'))

    # ex30
    # 배열의 인덱스 번호를 찾는 find
    # find 검색 실패가 일어나면 항상 '-1' 리턴함
    # 데이터 분석에서 '워드 카운트' 사용됨 / 예시) 대통령 신년사에서 코로나 단어 언급 횟수
    s = '무궁화꽃이꽃이피었습니다'
    print(s.find('호랑이'))

    # ex31
    # 문자열
    # 문자열을 관리하는 s 객체 생성
    s = 'Apple'
    t = s + 'Orange'
    print(t, s)
    s = s + 'Banana'
    print(s)
    # 문자열을 소문자 lower
    print(s.lower())
    print(s)
    # 원본 데이터는 변경하지 않는 것이 원칙
    t = s.lower()
    print(t)
    # 문자열을 대문자 upper
    print(s.upper())
    # 대치 replace
    print(s.replace('Banana', 'Orange'))
    print(s)
    # 대치 시 대소문자 구별함
    print(s.replace('banana', 'Orange'))

    s = '무궁화 꽃이 피었습니다.'
    # 스페이스를 기준으로 문자열을 분리함 split
    # 한 개 이상의 결괏값을 리턴할 땐 배열(list)로 리턴
    print(s.split())
    t = s.split()
    print(t)
    print(len(t))
    print(t[0], t[1] * 3, t[2])

    # 특정 문자 기준으로 분리할 때 split 안에 문자 입력함
    s = '무:궁화,꽃:이,피:었습니다.'
    print(s.split(':'))

    # ex32
    # 복합적으로 연산 사용시 1.산술 2.관계(대소) 3.논리 로 우선순위 진행
    # 산술연산 덧셈+ 뺄셈- 곱셈* 나누셈/ 나머지// 몫% 승수**
    print(16 + 3, 16 - 3, 16 * 3, 16 / 3, 16 // 3, 16 % 3, 16 ** 3)
    # 관계연산 대소관계를 구분
    print(3 > 2, 3 < 2, 3 >= 3, 3 <= 3, 3 == 3, 3 != 3)
    # 논리연산
    # AND &
    print(False & False)
    print(False & True)
    print(True & False)
    print(True & True)
    # OR |
    print(False | False)
    print(False | True)
    print(True | False)
    print(True | True)
    # 부정연산 not
    print(not (3 > 2))

    print('-' * 10)
    # 복합 연산 - 연산자 우선순위
    print(3 + 2 > 4 & 6 < 2 * 4)
    # 실행 순서 동격
    print(5 > 4 & 6 < 8)
    print(True & True)
    print(((3 + 2) > 4) & (6 < (2 * 4)))

    # ex33
    # 파이썬 내장함수 사용 -> 임포트
    # 시뮬레이션 데이터(모사데이터)로 작업시 사용
    # from random import *
    # 0.0~1.0 사이의 값 랜덤
    print(random())
    # 3 <= x <=5
    print(randint(3, 5))
    # 2부터 20까지 3씩 증가된 값을 랜덤하게
    # 2 5 8 11 14 17 20
    print(randrange(2, 20, 3))

    # ex34
    # 키보드로부터 입력받기 원할때 input
    a = input('입력하세요: ')
    print(a, type(a))

    # 문제 문자열 -> 숫자형
    print(int(a) * int(a), type(int(a)))
    print(int(a) ** 2)
    # 정석 코드
    a = int(input('입력: '))
    print(type(a), a ** 2)

    # ex35
    # 4대 제어문 if/while/for/switch
    # 1. 파이썬에서 조건문에 () 사용해도 되지만 정석은 사용 안 함
    # 2. 제어문의 끝에는 : 사용
    # 3. 조건이 만족될 때의 실행 문장은 반드시 TAP 처리함
    # if
    if 3 > 2:
        print(10)
    # if else
    a = int(input('숫자입력: '))
    if a > 2:
        print(1)
    else:
        print(2)

    print('-' * 10)
    # 주의점
    # TAP 처리 유무에 따라 else 판단
    # else 미포함
    if 3 > 2:
        print(1)
    else:
        print(2)
    print(3)
    # else 포함
    if 3 > 2:
        print(1)
    else:
        print(2)
        print(3)
    # else if
    i = int(input('점수: '))

    if i > 90:
        print('A')
    elif i > 80:
        print('B')
    elif i > 70:
        print('C')
    elif i > 60:
        print('D')
    else:
        print('F')

    # 중첩 제어문
    if 3 > 2:
        if i > 90:
            print('A')
        else:
            print('B')
    else:
        if i > 90:
            print('')
        else:
            print('F')

    # 문제
    r = int(random() * 100)
    print(r)
    a = r // 10
    b = r % 10
    if a % 2 == 0:
        if b % 2 == 0:
            print('우동')
        else:
            print('짜장')
    else:
        if b % 2 == 0:
            print('냉면')
        else:
            print('탕수육')
    # False, {}-빈배열, [], (), None, '', not()
    if not 1:
        print('호랑이')
    else:
        print('코끼리')
    # if(리스트찾을값) in[리스트목록]
    if 19 in [10, 20, 30, 40]:
        print(1)
    else:
        print(2)
    # 무궁화 문자열 판단 문제
    a = '무궁화 꽃이 피었습니다.'
    b = a.split()
    print(b)

    if '호랑이' in b:
        print('있다')
    else:
        print('없다')

    # while
    a = 0
    while a < 10:
        a += 1
        print(a)
    print('호랑이')

    # continue / break
    a = 0
    while a < 10:
        a += 1
        if a == 3:
            continue
        if a == 6:
            break
        print(a)
    print('호랑이')

    # 우박수 문제
    num = 23
    while True:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        if num == 1:
            print(int(num))
            break
        print(int(num))
    print("호랑이")


def day3():
    # ex36
    # 우박수 문제 삼항 연산
    num = 23
    while True:
        num = num / 2 if num % 2 == 0 else num * 3 + 1
        if num == 1:
            print(int(num))
            break
        print(int(num))
    print("호랑이")

    # ex37
    # range 함수
    print(range(0, 10)), print(type(range(0, 10)))

    # list(range())
    # 0 <= x < 10
    a = list(range(0, 10))
    print(a)
    print(list(range(5, 10)))
    print(list(range(3, 20, 2)))

    # ex38
    # for 문
    for i in [0, 1, 2, 3, 4]:
        print(i)
    # list 가 숫자를 관리함 으로 표현
    for i in [0, 1, 2, 3, 4]:
        print(i, end=' ')
    print()
    # list 가 문자열을 관리함 으로 표현
    for i in ['월', '화', '수', '목', '금', '토', '일']:
        print(i, end=' ')
    print()
    for i in ['호랑이', '고양이', '강아지']:
        print(i, end=' ')
    print()

    # ex39
    # for 문의 정석 코드 / 기본꼴
    for i in range(0, 10):
        print(i, end=' ')
    print()

    # ex40
    # 5단
    for i in range(0, 10):
        print('5 *', i, '=', i * 5)
    print()

    # ex41
    # 1 부터 10까지 더하는 합산 프로그램 - 결과 55
    add = 0
    for i in range(1, 11):
        add += i
    print(add)
    print()

    # ex42
    # 컨버팅 - 다른 랭귀지에서 만들어진 프로그램을 사용하는 랭귀지에 맞게 이식할때 사용하는 용어
    # 포팅 - os에 맞게끔 이식할때 사용하는 용어
    for i in range(0, 3):
        for j in range(0, 4):
            print('[', i, j, ']', end=' ')
        print()
    print()

    # ex43
    # 격자 컨버팅
    k = 0
    for i in range(3):
        for j in range(4):
            print('%02d' % k, end=' ')
            k += 1
        print()
    print()

    # ex44
    # 0~9 랜덤 숫자 4개 보이고 끝에 더해진 값 출력하기
    # 5 7 6 3 = 21
    for i in range(3):
        a = 0
        for j in range(4):
            r = int(random() * 10)
            print(r, end=" ")
            a += r
        print('=', a)
    print()

    # ex45
    # 랜덤하게 알파뱃(A~Z) 가로 네칸 세로 세칸 출력
    for i in range(3):
        for j in range(4):
            r = randint(0, 25)
            print(chr(65 + r), end=' ')
        print()
    print()


def day4():
    # ex46
    # 아스키 코드 변환
    print(chr(65))
    print(ord('A'))

    # ex47
    # 리스트를 사용하여 CRUD 하는 기본형
    # 리스트 생성 C
    a = [10, 20, 30, 40]
    print(a)
    b = ['호랑이', '독수리']
    print(b)
    # 서로 다른 타입을 멤버로 사용하는 리스트
    c = [10, '호', True]
    print(c)

    # ex48
    # R
    a = [10, 20, 30, 40]
    print(a)
    print(a[0], a[1], a[2], a[3])
    # a[4]를 출력하게 되면 에러 발생 - 아웃오브바운드 에러 / 경계를 넘어선 조심해야할 에러
    # print(a[4])
    for i in a:
        print(i, end=' ')
    print()
    for i in [1, 2, 3, 4]:
        print(i, end=' ')
    print()
    # 자주 사용되는 변수명 - value, item, data
    for data in a:
        print(data, end=' ')
    print()

    # ex49
    # U - 기존 데이터를 삭제하고 새로 데이터를 생성하여 업데이트됨
    a = [10, 20, 30, 40]
    a[0] = 50
    print(a)
    print(id(a[0]), id(a[1]))
    a[0] = 60
    print(id(a[0]), id(a[1]))

    # ex50
    # D - del
    del (a[0])
    print(a)

    # ex51
    # 길이 구하는 함수 - len
    print(len(a))

    # ex52
    # 중첩 리스트 - 이차원 배열 / 삼차원 배열
    a = [10, '호랑이', [20, '코끼리', [30, '독수리']]]
    print(a)
    print(a[2])
    print(a[2][0], a[2][1])
    print(a[2][2][0], a[2][2][1])

    # ex53
    # 배열 사용 주의점
    a = 'Apple'
    b = ['A', 'p', 'p', 'l', 'e']
    print(a[0])
    # A의 0번은 ''사이에 대문자 B라고 넣는 것은 안된다. 문자열은 직접적으로 업데이트할 수 없다.
    # a[0] = 'B'
    # B의 0번은 ''사이에 대문자 B를 넣으면 업데이트된다.
    b[0] = 'B'
    print(b[0])

    # ex54
    # 배열 갱신 방법 [:]개념 파이썬에서 자주 사용하는 문법
    a = ['a', 'b', 'c', 'd', 'e']
    # 인덱스 번호 1번 부터 3-1개 가져오기 / 직관적으로 해석함
    print(a[1:3])
    # 두개의 데이터를 삭제하고 그영역에 데이터를 추가함
    a[1:3] = ['F', 'G']
    a[1:3] = ['H', 'I', 'J', 'K', 'L']
    print(a)

    # ex55
    # 특정 부분의 영역을 삭제할때 사용하는 방법 / 삭제하고 추가할 데이터가 없음
    a = ['a', 'b', 'c', 'd', 'e']
    a[1:3] = []
    print(a)

    # 직접적으로 삭제
    a = ['a', 'b', 'c', 'd', 'e']
    del (a[1:3])
    print(a)

    # ex56
    # 리스트 맨 뒤에 추가 - .append
    a = ['o', 'r', 'a', 'n', 'g', 'e']
    print(a)
    a.append('f')
    print(a)
    a.append(10)
    print(a)

    # ex57
    # 특정 위치에 데이터를 추가하는 함수 - .insert
    a = ['o', 'r', 'a', 'n', 'g', 'e']
    a.insert(1, 10)
    print(a)

    # ex58
    # 맨 마지막에 있는 데이터를 지우는 함수 - .pop
    a = ['o', 'r', 'a', 'n', 'g', 'e']
    a.pop()
    print(a)
    # 특정 위치에 데이터를 지울 때 인덱스 번호 지정함
    a.pop(3)
    print(a)

    # ex59
    # 리스트 안에 요소를 검색해서 삭제 - .remove
    a = ['o', 'r', 'a', 'n', 'r', 'e']
    # 같은 데이터가 여러개 있어도 하나만 삭제함
    a.remove('r')
    print(a)

    # ex60
    # 검색해서 없으면 에러 출력됨
    # 검색 에러를 대비해 예외처리를 함 - try: except: pass
    try:
        a.remove('f')
    except ValueError:
        print('예외발생')
        pass
    print('호랑이')

    # ex61
    # 찾아서 인텍스 번호를 리턴함 - index
    try:
        b = a.index('f')
        print(b)
    except ValueError:
        print('예외발생')
        pass
    print('호랑이')

    # ex62
    # 정렬 - 비용이 많이 드는 함수
    # 비용 절감은 메모리 절약과 속도 증가 중에 메모리 절약을 선택하는 경향이 있음
    # 순차 정렬 함수 오름차순 = .sort
    a = ['o', 'r', 'a', 'n', 'r', 'e']
    a.sort()
    print(a)
    # 정렬이 되어있는 리스트의 역순 정렬 함수 내림차순 = .reverse
    a.reverse()
    print(a)

    a = ['a', 'c', 'e', 'f', 'd', 'b']
    a.sort()
    print(a)

    # 앞과 뒤에 순서를 바꾸는 함수
    a = ['a', 'c', 'e', 'f', 'd', 'b']
    a.reverse()
    print(a)

    # 역순 정렬 내림차순
    a = ['a', 'c', 'e', 'f', 'd', 'b']
    a.sort(reverse=True)
    print(a)

    # ex63
    # append()의 확장 형태
    a = [1, 2, 3]
    a.append(4)
    print(a)
    # 어펜드 개념 리스트가 한개 추가됨 = 값 4개
    a = [1, 2, 3]
    a.append([4, 5])
    print(a)

    a = [1, 2, 3]
    a.extend([4])
    print(a)
    # 익스텐드 개념 리스트가 한개 합성됨 = 값 6개
    a = [1, 2, 3]
    a.extend([4, 5, 6])
    print(a)
    # 익스텐드와 동일 결과 / 차이점?
    a = [1, 2, 3]
    a = a + [4, 5, 6]
    print(a)


def day5():
    # ex64
    # 튜플 - 이하는 일은 리스트와 거의 동격이다
    a = ()
    b = [10, 20, 30]
    print(a, b, type(a), type(b))

    a = (10,)
    print(a, type(a))
    b = 10,
    print(b, type(b))
    # 주의 - 숫자 한 개 사용 시 ","로 튜플 타입 구분됨 b나 c 형태로 () 생략하여 사용됨
    c = 10
    d = (10)
    print(type(c), type(d))
    e = (10, 20, 30,)
    print(e, type(e))
    # () 생략은 문법 해석하는 데만 사용, 작성 시 () 붙여서 습관
    f = 10, 20, 30
    print(type(f))

    # 튜플과 리스트 비슷한 문법구조를 가진다
    # 튜플 언패킹
    a = (10, 20, 30)
    b, c, d = a
    print(a, b, c, d)

    a = [10, 20, 30]
    b, c, d = a
    print(a, b, c, d)

    # 스왑
    a = 10
    b = 20
    a, b = b, a
    print(a, b)

    # 리스트 자료형을 튜플 자료형으로 리턴해주는 함수 - tuple()
    a = [10, 20, 30]
    b = tuple(a)
    print(type(a), type(b))

    a = (10,) + (20, 30)
    print(a)
    print((10,) + (20, 30))

    a = (1, 2)
    b = (1, 2, 3)
    # == 은 값 비교
    print(a == b)
    # 대소 비교는 - 개수 비교
    print(a <= b)
    # 순회비교?

    # 수정하기
    a = (10, 20, 30)
    b = [10, 20, 30]
    # 튜플 값 1개 확인 시 리스트 사용하듯이 [] 사용
    print(a[0])
    b[0] = 20
    print(b)
    # 튜플은 데이터 수정이 안됨 에러 출력
    # a[0] = 20

    # ex65
    # 리스트 - 중첩 사용 가능
    a = [10, '호랑이', [20, 30], (40, '코끼리', [50, 60], [70, 80])]
    print(a)

    a = []
    b = list()
    print(type(a), type(b))

    c = ()
    d = tuple()
    print(type(c), type(d))

    e = [10, 20]
    f = list('apple')
    print(e, f)

    a = []
    b = tuple(a)
    c = list(b)
    print(type(a), type(b), type(c))

    # 문자열을 분리하여 저장시키는 결과가 리스트인 것을 증명하는 함수 - .split
    a = '호 랑 이'
    b = a.split(' ')
    print(b)
    # offset 용어 정의 - 기준점으로부터 상대적으로 떨어진 거리
    a = [10, 20, 30]
    # -사용 시 뒤에서부터 출력 / 중요
    print(a[-1])

    # ex66
    # 딕셔너리 기본 문법 구조
    # a = {k:v, ... }
    # k = key (색인) : v = value (값)
    # 배열을 이용한 문법구조로 사용되지 않음
    a = {}
    print(type(a))
    a = {1: 10, 2: 20, 5: 40}
    print(a)
    a = {10: '호랑이', 20: "코끼리", 30: '독수리'}
    # 키가 같아서 제일 우측 가장 최근에 데이터로 갱신됨
    a = {1: 10, 2: 20, 2: 30, 5: 40}
    print(a)
    # 중첩
    a = {1: [10, 11], 2: [20, 21], 3: [30, 31]}
    print(a)
    a = {1: (10, 11), 2: (20, 21), 3: (30, 31)}
    print(a)
    a = {1: 10, 2: '호랑이', 3: [], 4: (), 5: {6: 60, 7: '호'}}
    print(a)
    a = {'호랑이': 10, '코끼리': 20, '독수리': 30}
    print(a)
    # 키값을 혼용해서 쓰는 건 가급적 피해서 사용
    a = {'호랑이': 10, 20: '코끼리', '독수리': 30}
    print(a)
    # 예시 json 문법 구조에 맞춰서 딕셔너리 사용하게 됨
    a = {'name': '홍길동', 'age': 20, 'salary': 300}
    print(a)
    # 데이터 갱신
    a['name'] = '이순신'
    print(a['name'])
    print(a['name'], a['age'], a['salary'])
    # 없는 데이터 추가
    a['hight'] = 180
    print(a)

    # ex67
    # 딕셔너리 CRUD
    a = {}
    # C
    a['name'] = '이순신'
    a['age'] = 20
    print(a)

    # R
    b = a['name']
    print(b, a['name'], a)

    # U
    a['name'] = '독수리'
    a['age'] = 100
    print(a)

    # D
    del (a['name'])
    # del a['name'] () 생략 가능 / 예약어로 삭제함 / 문법적 구조가 다름
    print(a)

    a = {'name': '홍길동', 'age': 20, 'salary': 300}
    # 동격 문법 - .get 을 조금 더 사용
    b = a['name']
    c = a.get('name')
    print(b, c)

    # 딕셔너리의 키를 전부 확인
    print(a.keys())

    # a = type(range(0, 10))
    # print(a)

    for i in a.keys():
        print(i)

    print('-' * 10)
    # ex68
    # 딕셔너리 사용 방법
    for item in a.items():
        # 전체 확인
        # print(item)
        # 타입 확인
        print(type(item))
        # 개별 값 확인
        print(item[0], item[1])
    # 실제 사용 많이 함 / 값을 확인하기 때문에
    for value in a.values():
        print(value)

    # ex69
    # 177 -188p 복습
    dic = {"day": "A", "pos": "M", "mis": "T"}
    print(dic)
    a = dict(first="W", middle="E", last="C")
    print(a)
    # 제약 사항 - 공백과 예약어가 없는 유효한 변수 이름 사용해야함
    # a = dict(name="E", def="h")
    print(a)
    lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
    print(dict(lol))
    lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
    print(dict(lot))
    tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
    print(dict(tol))
    los = ['ab', 'cd', 'ef']
    print(dict(los))
    tos = ('ab', 'cd', 'ef')
    print(dict(tos))
    py = {'c': 'g', 'i': 'e', 'j': 't'}
    print(py)
    py['g'] = 'g'
    print(py)
    py['g'] = 't'
    print(py)
    py = {'c': 'g', 't': 'e', 't': 'j'}
    print(py)
    print(py['c'])
    # print(py['a'])
    print('a' in py)
    print(py.get('c'))
    b = py.get('a', 'NO')
    print(b)
    print(py.get('a'))
    s = {'g': 'g', 'y': 'f', 'r': 's'}
    print(s.keys())
    print(list(s.keys()))
    print(list(s.values()))
    print(list(s.items()))
    print(len(s))

    f = {'a': 'a', 'b': 'b'}
    s = {'b': 'b', 'c': 'c'}
    t = {'d': 'd'}
    print({**f, **t, **s})

    py = {'c': 'g', 'i': 'e', 'j': 't'}
    o = {'m': 'g', 'h': 'm'}
    py.update(o)
    print(py)

    f = {'a': 'a', 'b': 'b'}
    s = {'b': 'c'}
    f.update(s)
    print(f)
    del py['m']
    print(py)
    del py['h']
    print(py)
    print('-' * 10)
    print(len(py))
    print(py.pop('j'))
    print(len(py))
    print('-' * 20)
    print(py.pop('f', 'no'))
    print(len(py))
    print('-' * 30)
    py = {'c': 'g', 'i': 'e', 'j': 't'}
    print(py.clear())
    py = {'c': 'g', 'i': 'e', 'j': 't'}
    py = {}
    print(py)
    py = {'c': 'g', 'i': 'e', 'j': 't'}
    print('c' in py)
    print('t' in py)
    s = {'g': 'g', 'y': 'f', 'r': 's'}
    s_s = s
    s['b'] = 'c'
    print(s_s)

    # ex70
    # 얕은 복사 - 메모리 공유
    a = [1, 2, 3]
    b = a
    print(id(a))
    print(id(b))
    a[0] = 4
    b[2] = 5
    print(a, b)
    a.append(99)
    print(a, b)
    # 깊은 복사
    a = [1, 2, 3]
    b = a[:]
    print(id(a))
    print(id(b))
    a[0] = 4
    b[2] = 5
    print(a, b)
    a.append(99)
    print(a, b)

    import copy
    a = [1, 2, 3]
    b = copy.deepcopy(a)
    print(id(a))
    print(id(b))
    a[0] = 4
    b[2] = 5
    print(a, b)
    a.append(99)
    print(a, b)


def day6():
    # ex71
    # 함수 사용 방법 네 가지
    # **********************************************************************************************
    # 함수
    # **********************************************************************************************
    # 모든 랭귀지의 함수는 반드시 4가지의 형태를 가진다.(리턴 값이 있다 없다, 인수 전달이 있다 없다.)
    # 함수
    # 자주 짜는 코드를 미리 데이터 백업 잡아놓는 목적.
    # 인수 전달이 없을 때
    print(99)

    def func01():
        print('1번 콜')
        print(2)
        print(3)

    func01()

    # 인수 전달이 있을 때
    # ( ) 안은 예약어만 아니면 뭐든 상관없음.
    def func02(num):
        print(num)
        a = num * num
        print(a)

    # func02('코코코콬코코콬코콬끼리') # 연산식이 있을 때 문자열을 넣으면 error 발생!
    func02(30)

    # 인수 전달이 없고 return 이 있을 때
    # return 을 처리하는 3가지의 방법
    # 1. return 을 하든지 말든지 무시
    # 2. return 을 하면 그걸 변수로 받아 사용
    # 3. 변수로도 받지 않고 직접적으로 사용
    # *** 주의 사항
    # print(func01()) # 이 형식은 return 이 있을 때만 사용할 수 있다.
    def func03():
        print('3번 콜')
        return 100

    func03()
    print('------------')
    a = func03()
    print(a)
    print(func03())
    print(func03() * 7)

    print('------------')

    # 인수 전달과 return 이 모두 있을 때
    def func04(num):
        print('4번 콜', num)
        return 777 + num

    func04(654)  # return 값은 출력이 안된다.
    a = func04(100)
    print(a)
    print(func04(654))

    # ex72 ?
    # 대소 비교
    a = [1, 2, 3]
    b = [1, 2, 3]
    print(a < b)
    print(a <= b)

    a = [1, 2, 3]
    b = [1, 2, 3, 4]
    print(a < b)
    print(a <= b)

    print('-' * 10)
    a = [1, 2, 3]
    b = [1, 2, 3, -4]
    print(a < b)
    print(a <= b)

    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 4]
    print(a < b)
    print(a <= b)

    a = [1, 2, 3, 4, 5]
    b = [1, 3, 4]
    print(a < b)
    print(a <= b)

    print('-' * 10)
    print('tiger' < 'tager')
    print('tiger' <= 'tzger')

    a = [1, 2, 3]
    b = [1, 2, 3, 4, 5]
    print(a < b)

    # ex73
    # 함수 사용
    def func05(a, b, c):
        sum = a + b + c
        print(sum)
        print(a * a + b * b + c * c)

    func05(2, 3, 4)
    func05(3, 4, 5)

    def func06():
        print(1)
        return
        print(2)

    func06()

    def func07(a, b):
        print(a, b)
        print(type(a), type(b))

    func07(10, '호랑이')

    # 함수의 인수 값을 초기화할 수 있음
    # 주의점 - 초기화는 맨 끝에서부터 해야 함
    def func08(a, b, c=10, d=20):
        print(a, b, c, d)

    func08(1, 2)
    func08(1, 2, 3)
    func08(1, 2, 3, 4)

    # 가변 인수 전달
    def func09(*args):
        print('-' * 10)
        for data in args:
            print(data)

    func09()
    func09(10, 20)
    func09(10, 20, '호랑이', 30)

    def func10(a, b, *args):
        print(a, b)
        for data in args:
            print(data)

    func10(10, 20)
    func10(10, 20, 30, 40)

    # bare 문법 - 가독성을 높일 때 사용함 / 코드 분석 용이함
    def func11(a, b, *, color, data):
        print(a, b, color, data)

    func11(1, 2, color=3, data=4)

    # 딕셔너리 출력됨 **
    def func12(**star):
        print(star)
        for item in star.items():
            print(item)
        for key in star.keys():
            print(key)
        for value in star.values():
            print(value)
        for k, v in star.items():
            print(k, v)

    func12(a=10, b=20)


def day7():
    # ex74
    # 클래스
    class Apple:
        # 생성자 함수 기본 꼴 - 인수 값에 self 들어가야 함
        def __init__(self):
            print("생성자 콜")

    a = Apple()
    print(a)

    class Apple:
        def __init__(self):
            pass

    a = Apple()
    print(a)

    # 기본 함수 정의 하는 네가지 방법
    class Apple:
        def __init__(self):
            pass

        def func01(self):
            print(1)

        # 함수 기본 꼴 - 인수 값에 self가 전부 들어가야 함 / 다른 인수를 받을 경우 self가 제일 앞에 있어야 함
        def func02(self, a):
            print(2)

        def func03(self):
            return 3

        def func04(self, a):
            return 4

    a = Apple()
    print(a.func01())
    print(a.func02(1))
    print(a.func03())
    print(a.func04(1))

    class Apple:
        # self는 생성된 객체 / 자바에서의 this
        def __init__(self):
            print(id(self))
            pass

    a = Apple()
    print(id(a))

    # ex75
    # 필드
    class Apple:
        num = 10

        def __init__(self):
            pass

    a = Apple()
    print(a.num)

    class Apple:
        # 생성자에서 self를 이용해서 필드 멤버로 선언하지 않아도 됨
        # num = 10

        def __init__(self, num):
            self.num = num
            pass

        def func(self):
            print(self.num)

    a = Apple(20)
    print(a.num)

    # ex76
    # 동적(dynamic)-필요할 때 만들어서 사용하고 사용이 끝나면 버리는 것 / 정적(static)-처음부터 만들어두고 끝까지 남아있는 것
    class Apple:
        def __init__(self, num):
            self.num = num
            pass

        def func(self):
            print(self.num)

    a = Apple(20)
    print(a.num)

    # a1정적 a2동적 a3지역변수
    class Apple:
        a1 = 10

        def __init__(self):
            self.a2 = 20
            pass

        def func(self):
            a3 = 30
            print(self.a1, self.a2, a3)

    a = Apple()
    print(a.func())


def day8():
    # ex77
    # 상속
    class Apple:
        def __init__(self):
            pass

        def func1(self):
            print(1)

        def func3(self):
            print('부모3')

    class Orange(Apple):
        def func2(self):
            print(2)

        def func3(self):
            print('자식3')

        def func4(self):
            self.func2()
            self.func3()
            super().func3()

    a = Orange()
    print(a.func1(), a.func2(), a.func3(), a.func4())
    print(Apple.mro())
    print(Orange.mro())
    print()

    # ex78
    # 다형성
    # 변수에 타입이 없어서 파이썬에서는 업캐스팅 논리가 없음
    # a1 = Apple()

    # class Dog:
    #     def __init__(self):
    #         pass
    #
    #     def cry(self):
    #         print('멍멍')
    #
    # class Cat:
    #     def __init__(self):
    #         pass
    #
    #     def cry(self):
    #         print('야옹')
    #
    # class Snake:
    #     def __init__(self):
    #         pass
    #
    #     def cry(self):
    #         print('없음')
    #
    # a1 = Dog()
    # a1.cry()
    # a2 = Cat()
    # a2.cry()
    # a3 = Snake()
    # a3.cry()
    #
    # a4 = [Dog(), Cat(), Snake()]
    # print(a4)
    # for animal in a4:
    #     print(animal.cry())

    # class Apple:
    #     def func01(self):
    #         print(1)
    #
    # def func02(a):
    #     print(2)
    #     a.func01()
    #
    # # 대입 연산 a = Apple()와 같은 의미
    # func02(Apple())
    # a1 = Apple()
    # print(a1.func01())

    # ex79
    # 다양한 형태의 모든 타입을 받는다 - 다형성
    class Zoo:
        def __init__(self, animal):
            self.animal = animal

        def cry(self):
            self.animal.cry()

    class Dog:
        def cry(self):
            print('멍멍')

    class Cat:
        def cry(self):
            print('야옹')

    t1 = Zoo(Dog())
    t1.cry()
    t2 = Zoo(Cat())
    t2.cry()

    # ex80
    # 예외처리
    try:
        print(0)
        a = 4 / 0
    except:
        print(1)
    print(2)

    # Exception as - 익센셥 내용 출력 시키는 코드
    try:
        print(0)
        a = 4 / 0
    except Exception as e:
        print(e)
    print(2)

    try:
        print(0)
        a = 4 / 0
    except Exception as e:
        print(e)
    finally:
        print(3)
    print(2)

    print()
    a = [10, 20, 30]
    b = a.index(30)
    print(b)

    try:
        c = a.index(100)
    except Exception as e:
        print(e)
    print("호랑이")

    # ex81
    # 파일 입출력
    # 쓰기 write
    file = open("sample.txt", 'w', encoding='UTF-8')
    file.write("호랑이")
    file.close()


def day9():
    # ex81 - 2
    # for i in range(5):
    #     print(i)
    # print()
    # for i in range(2, 7):
    #     print(i)
    # print()
    # for i in range(1, 10, 2):
    #     print(i)
    # print()
    #
    # file = open("sample.txt", 'w', encoding='UTF-8')
    # for i in range(5):
    #     file.write('호랑이')
    # file.close()
    #
    # file = open("sample.txt", 'w', encoding='UTF-8')
    # for i in range(5):
    #     file.write(str(i))
    # file.close()
    #
    # file = open("sample.txt", 'w', encoding='UTF-8')
    # for i in range(5):
    #     file.write('호랑이'+str(i)+'\n')
    # file.close()
    #
    # with open("sample.txt", 'w', encoding='UTF-8') as file:
    #     for i in range(5):
    #         file.write('호랑이'+str(i)+'\n')

    # ex82
    # 한 줄씩 읽기
    # file = open("sample.txt", 'r', encoding='UTF-8')
    # data = file.readline()
    # print(data)
    # if data:
    #     print(10)
    # # 한 줄 있는 데이터를 먼저 읽어서 읽을 데이터가 없는 상태라서 20이 출력 안됨
    # data = file.readline()
    # print(data)
    # if data:
    #     print(20)
    # file.close()
    #
    # if '호랑이':
    #     print(1)
    # if '':
    #     print(2)

    # readline 자동 줄바꿈됨
    file = open("sample.txt", 'r', encoding='UTF-8')
    while True:
        data = file.readline()
        print(data, end='')
        # 읽을 데이터가 없다면 break
        if not data:
            break
    file.close()
    print()
    print()

    # 리스트로 읽기
    file = open("sample.txt", 'r', encoding='UTF-8')
    data = file.readlines()
    print(data)
    file.close()

    for i in data:
        print(i, end='')
    print()

    a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
    a[0] = a[0].replace('\n', '')
    print(a[0], a[1])

    for i in range(len(a)):
        a[i] = a[i].replace("\n", "")
    print(a)

    print()
    a = ['호랑이0\n', '호랑이1\n', '호랑이2\n', '호랑이3\n', '호랑이4']
    print(a)
    for index, value in enumerate(a):
        print(index, value, end='')
        a[index] = value.replace('\n', '')
    print()
    print(a)
    print()

    # 정리 예시
    file = open("sample.txt", 'r', encoding='UTF-8')
    data = file.readlines()
    print(data)
    file.close()
    for index, value in enumerate(data):
        print(index, value, end='')
        data[index] = value.replace('\n', '')
    print()
    print(data)
    print()

    # 전체 내용 문자열 읽기
    file = open("sample.txt", 'r', encoding='UTF-8')
    data = file.read()
    file.close()
    print(data, type(data))
    print()

    # ex83
    # import - 외부의 파일을 읽음 / 파일 선두에 적음
    # import A as B - 이 문법이 가장 많이 사용됨
    # import Tiger
    # Tiger.func1()
    #
    # from Tiger import *
    # func1()
    #
    # import Tiger as t
    # t.func1()

    # ex84
    # 지금 실행되고 있는 파일명 출력
    # print(__name__)
    #
    # import Tiger as t
    # t.func1()
    # t.func2()

    # import Tiger as t
    # # 외부에서 파일 참조 할 때 특정 함수 내용만 실행 시키기 위해 main 비교함
    # if __name__=='__main__':
    #     print(1)
    #     t.func1()

    # 정석 코드 기본 꼴 - 메인 함수에 코드 작성
    def f1():
        print(2)

    # 프로그램 진입 점 / 엔트리 포인트
    def main():
        print(1)
        f1()

    if __name__ == '__main__':
        main()

    # ex85
    # 딕셔너리 사용 - k: v
    apple = {'n1': '호랑이', 'n2': '코끼리', 'n3': '독수리'}
    print(apple['n3'])

    orange = {10: 20, 20: '독수리', 30: True}
    print(orange[10], orange[20], orange[30])
    print()

    # 실습
    kiwi = {'이름': '홍길동',
            '나이': 20,
            '특기': ['독서', '무술', '프로그래밍'],
            '가족': {'아버지': '아빠', '어머니': '엄마'}}

    print(kiwi['이름'], kiwi['나이'])
    print(kiwi['특기'][0])
    print(kiwi['가족']['어머니'])
    print()
    print(kiwi['이름'], kiwi['특기'][2], kiwi['가족']['어머니'])
    print()

    data = {
        "response": {
            "body": {
                "items": [{
                    "addr": 1234,
                    "name": "홍길동"
                },
                    "득템"
                ]
            },
            "page": 100
        },
        "header": {
            "result": 200,
            "msg": "OK"
        }
    }

    print(data["response"]["body"]["items"][0]["addr"])
    print(data["response"]["body"]["items"][0]["name"])
    print(data["response"]["body"]["items"][1])
    print(data["response"]["page"])
    print(data["header"]["result"])
    print(data["header"]["msg"])

    print()
    # ex86
    apple = {'n1': '호랑이', 'n2': '코끼리', 'n3': '독수리'}
    orange = {10: 20, 20: '독수리', 30: True}
    print(apple['n1'])
    print(apple.get('n1'))
    print(orange[10])
    print(orange.get(10))

    # 범위 값을 넘어가는 둘의 차이점
    try:
        apple['n4']
    except:
        print("검색불가")
    num = apple.get('n4')
    print(num)
    if num is None:
        print("검색안됨")

    # ex87
    # filter
    # a = [10, 20, 30, 40]
    # print(sum(a))
    # print(sum([1, 2, 3, 4]))
    # a = sum([3, 4, 5, 6])
    # print(a)

    def f1(a):
        return a > 0

    print(filter(f1, [-2, -1, 0, 1, 2]))
    # b = [-2, -1, 0, 1, 2]
    # r = list(filter(f1, b))
    # print(r)
    print(list(filter(f1, [-2, -1, 0, 1, 2])))

    print()

    # ex88
    # 참조 / 다른 이름으로 메모리 공유
    # () 작성하면 호출
    def f1():
        print(1)

    f1()

    a = f1
    a()

    def f2():
        print(2)

    def f3(tt):
        tt()
        print(3)

    f3(f2)

    def f4():
        return 999

    def f5(tt):
        print(tt)

    f5(999)
    f5(f4())
    print()

    # ex89
    # swich 대안
    def f1(num):
        t = {10: '호랑이', 20: '독수리', 30: '앵무새'}
        return t[num]

    print(f1(10))

    # ex90
    # 리스트 반복
    # a = [10, 20, 30]
    # print(a*2)
    # 컴프리헨션
    # 반복 문과 조건문을 이용하여 리스트를 생성하는 것을 컴프리헨션 이라 함 기본형
    a = [i for i in range(5)]
    print(a)
    a = [i * 3 for i in range(5)]
    print(a)
    a = [10, 20, 30, 40]
    b = [i for i in a]
    print(b)
    b = [3 * i for i in a]
    print(b)

    # a에서 반복문으로 값을 찾으면서 조건문을 만나 25보다 큰 값을 찾고 30, 40을 i에 넣고 +2 해서 리스트를 생성한 결과를 출력함
    a = [10, 20, 30, 40]
    b = [i + 2 for i in a if i > 25]
    print(b)
    print()

    # ex91
    # dir함수를 이용하여 관련된 함수 목록 출력
    # 딕셔너리{} - 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
    # 리스트[] - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
    # 튜플() - 'count', 'index'
    print(dir(()))
    print()

    # ex92
    # 실습 예제 복습
    a = [10, 20, 30, 40]
    a.insert(3, 99)
    print(a)

    a = [10, 20, 30, 40]
    a.append(100)
    print(a)
    a.insert(len(a), 99)
    print(a)

    a = [10, 20, 30, 40]
    a += [50, 60]
    print(a)
    a.extend([50, 60])
    print(a)

    a = [10, 20, 30, 40]
    b = a
    c = a.copy()
    print(a, b, c)
    print(id(a), id(b), id(c))

    a[0] = 99
    print(a[0], b[0], c[0])

    a = [10, 20, 30, 40]
    a.clear()
    print(a)

    # 검색에 실패하면 익셉션 - try 문 사용해서 에러 방어
    # 중복된 데이터가 존재해도 첫 데이터만 삭제
    a = [10, 20, 30, 40, 10]
    try:
        a.remove(10)
    except:
        print("범위오류")
    print(a)

    a = [10, 20, 30, 40]
    del (a[2])
    print(a)

    # pop은 인덱스를 이용하여 값을 리턴 받고 리스트의 값은 삭제함
    a = [10, 20, 30, 40]
    b = a.pop(2)
    print(b, a)

    # 6을 제외한 나머지만 리스트로 출력
    a = [0, 3, 6, 9, 0, 3, 6, 9]

    def f1(a):
        return a != 6

    print(list(filter(f1, a)))


def day10():
    # ex93
    # 표준 함수 / 내장 함수 - 복습 정리
    a = 10
    print(id(a), type(a))
    print(abs(-10))
    a = [10, 20, 30]
    for i in a:
        print(i, end=' ')
    print()
    # key, value를 index, value로 사용하기도 함
    for key, value in enumerate(a):
        print(key, value)

    # evaluation 실행하다 - 예시 - 코딩 웹 사이트에서 사용
    a = 'print(10+20)'
    eval(a)

    print(min(3, 5, 7))
    print(max(3, 4, 5, 6))
    a = [1, 2, 3, 4]
    print(max(a))

    print(bin(200))
    print(oct(200))
    print(hex(200))

    a = int('123')
    print(type(a))
    a = str(123)
    print(type(a))

    a = list('apple')
    print(type(a), a)
    a = list(range(5))
    print(a)

    # divmod 몫, 나머지 출력
    a = divmod(7, 3)
    print(a, type(a))
    print(a[0], a[1])
    for i in a:
        print(i)
    print()

    # all / any
    print(True & True & True & False)
    print(all([True, True, True, False]))

    print(False | False | False | True)
    print(any([False, False, False, True]))

    # .sort() / sorted()
    a = [9, 6, 3, 7, 2]
    a.sort()
    print(a)

    a = [9, 6, 3, 7, 2]
    b = sorted(a)
    print(a)
    print(b)
    print()

    # ex94
    # 시간 time / datetime
    import time
    a = time.localtime(time.time())
    print(a)
    print(a.tm_year, '년', a.tm_mon, '월', a.tm_mday, '일', a.tm_hour, '시', a.tm_min, '분', a.tm_sec, '초')
    b = ['월', '화', '수', '목', '금', '토', '일']
    print(b[a.tm_wday], '요일', sep='')

    import datetime
    print(datetime.datetime.now())

    for i in range(5):
        print(i)
        time.sleep(0.5)

    # ex95
    # 람다
    def f1():
        print(1)

    f1()

    func02 = lambda: print(2)
    func02()

    print(type(func02))

    func03 = lambda x: print(x)
    func03(10)

    func04 = lambda x, y: print(x + y)
    func04(10, 20)

    func05 = lambda: 99
    print(func05())

    func06 = lambda x, y: x + y
    print(func06(3, 4))

    def f1(ff):
        ff()

    def f2():
        print('호랑이')

    f1(f2)

    f2 = lambda: print('코끼리')
    f1(f2)

    def f3(ff):
        ff(10, 20)

    f3(lambda x, y: print(x + y))

    # filter 사용 예
    def func04(a):
        return a > 0

    a = filter(func04, [-2, -1, 0, 1, 2])
    print(list(a))

    a = filter(lambda a: a > 0, [-2, -1, 0, 1, 2])
    print(list(a))


def day11():
    # ex96
    # Datum.py 확인
    # 쌍으로 된 두 개의 데이터는 ()튜플을 많이 사용

    # generator
    a = (i for i in range(5))
    print(type(a))

    # sum은 sum(리스트)와 sum(제너레이터) 타입을 사용 가능
    b = sum(a)
    print(b)

    # .sort(lambda)
    a = [
        ('호랑이0', 7, 9),
        ('호랑이1', 6, 6),
        ('호랑이2', 4, 3),
        ('호랑이3', 9, 7)
    ]

    # key= 예약어
    a.sort(key=lambda k: k[1])

    print(a)

    print()
    for i in range(3):
        for j in range(4):
            print((i, j), end=' ')
        print()
    print()

    # Counter() - 단어 카운팅 시 사용되는 함수
    from collections import Counter

    a = ['호랑이', '코끼리', '호랑이', '코끼리', '독수리', '호랑이']
    b = Counter(a)
    print(b)

    c = [10, 20, 30, 10, 20, 10]
    d = Counter(c)
    print(d)
    print()

    # 유저 0~ 끝까지 출력

    a = [(i, j)
         for i in range(3)
         for j in range(4)]
    print(a)

    a = [(i, j)
         for i in [0, 1, 2]
         for j in [0, 1, 2, 3]]
    print(a)

    a = [(i, j)
         for i in [7, 8, 9]
         for j in [4, 5, 6, 7]]
    print(a)

    a = [i
         for i in [0, 1, 2, 3, 4, 99, 100]
         if i % 2 == 0]
    print(a)

    print(15 in [10, 20, 30])
    print(10 not in [10, 20, 30])

    data = [
        (0, "호랑이"), (0, "코끼리"), (0, "독수리"),
        (1, "호랑이"), (1, "코끼리"),
        (2, "호랑이"), (3, "코끼리"), (3, "독수리")
    ]

    def f1(a):
        print(a)
        b = [i for i, j in data if j == a]
        print(b)

    f1("코끼리")

    def func(a):
        return [i for i, j in data if j == a]

    print(func("코끼리"))

    # defaultdict
    from collections import defaultdict
    wc = {}
    a = ["사과", "바나나", "사과", "바나나", "사과", "사과", "바나나"]
    wc = defaultdict(int)

    for i in a:
        wc[i] += 1
        print(wc)

    a = defaultdict(list)
    a["호랑이"].append(10)
    a["호랑이"].append(20)
    a["호랑이"].append(30)
    a["코끼리"].append(10)
    a["코끼리"].append(40)
    print(a)
    print(a["호랑이"])
    print()

    a = defaultdict(list)
    a[1].append(10)
    a[2].append(20)
    a[3].append(30)
    a[2].append(40)
    a[3].append(50)
    a[3].append(60)

    for i, j in a.items():
        print(i, j)

    b = {
        i: j
        for i, j in a.items()
    }
    print(b)

    b = {
        i: sum(j)
        for i, j in a.items()
    }
    print(b)

    b = {
        i: sum(j) / len(j)
        for i, j in a.items()
    }
    print(b)

    a = "Tiger Lion"
    b = a.lower().split()
    print(b)

    # ex97
    # 워드 카운터
    interests = [
        (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
        (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
        (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
        (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
        (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
        (3, "statistics"), (3, "regression"), (3, "probability"),
        (4, "machine learning"), (4, "regression"), (4, "decision trees"),
        (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
        (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
        (6, "probability"), (6, "mathematics"), (6, "theory"),
        (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
        (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
        (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
        (9, "Java"), (9, "MapReduce"), (9, "Big Data")
    ]

    words_and_counts = Counter(word
                               for user, interest in interests
                               for word in interest.lower().split())

    for word, count in words_and_counts.most_common():
        if count > 1:
            print(word, count)

    print('-' * 10)
    a = 2 + \
        3
    print(a)

    a = "무궁화 꽃이"
    b = "무궁화 \t꽃이"
    print(a)
    print(b)

    a = [0, 1, 2, 3, 4, 5, 6]
    print(a[::2])

    x, y = [1, 2]
    print(x, y)
    _, y = [1, 2]
    a = [3 for _ in range(5)]
    print(a)

    def f():
        return 1 + 2, 1 - 2, 1 * 2

    a = f()

    print(a)

    # {}에 키값이 없으면 set
    a = {10, 20, 30}
    print(type(a))
    print(a)
    a.add(40)
    print(a)
    # set은 중복된 데이터를 넣지 않음
    a.add(30)
    print(a)

    # assert
    assert 1 + 1 == 2
    assert 1 + 2 == 2

    def f(a):
        return min(a)

    assert f([1, 2, 3, 4]) == 1


def day12():
    # is not None 삼항연산
    safe_x = a if a is not None else 0
    print(safe_x)

    # 워드 카운트
    word_counts = Counter(interests)
    wc = sorted(word_counts.items(),
                key=lambda word_and_counts: word_and_counts[1],
                reverse=True)
    print(wc)

    # _ 빈 변수
    a = [10 for _ in [1, 1, 1, 1, 1]]
    print(a)

    j = 0
    a = [(i, j)
         for i in range(3)
         for j in range(4)]
    print(a)

    for i in range(3):
        for j in range(4):
            print(a[i * 4 + j], end=" ")
        print()

    class Apple:
        def __init__(self, count=0):
            self.count = count

        def click(self, num_times=1):
            self.count += num_times

        def read(self):
            return self.count

        def reset(self):
            self.count = 0

    a1 = Apple()
    a2 = Apple(10)
    a3 = Apple(count=20)

    clicker = Apple()
    clicker.click()
    clicker.click()
    clicker.reset()
    print(clicker.read())

    class Orange(Apple):
        def reset(self):
            pass

    clicker2 = Orange()
    clicker2.click()
    clicker2.reset()
    print(clicker2.read())

    # yield
    def f1():
        yield 10
        yield 20
        yield 30

    for i in f1():
        print(i, end=' ')
    print()

    def f2(n):
        i = 0
        while i < n:
            yield i
            i += 1

    for i in f2(10):
        print(i, end=' ')
    print()

    def f1():
        n = 1
        while True:
            yield n
            n += 1

    a = f1()
    print(a)

    # for i in a:
    #     print(a)

    # b = (i for i in a if i % 2 == 0)
    # for i in b:
    #     print(b)

    a = [1, 2, 3]
    for i, v in enumerate(a):
        print(i, v)

    b = {0: 10, 1: 20, 2: 30}
    for i, v in b.items():
        print(i, v)

    # from random import *

    print(random())
    print(randint(10, 20))
    print(randrange(0, 10, 3))

    # seed(0)
    for i in range(5):
        print(random())

    a = [1, 2, 3, 4, 5]
    shuffle(a)
    print(a)

    b = choice(a)
    print(b)

    c = sample(a, 3)
    print(c)

    # zip
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [i for i in zip(a, b)]
    print(c)
    # 인자 언패킹
    d, e = zip(*c)
    print(d)
    print(e)

    # 타입 어노테이션
    def f1(a: int, b: int) -> int:
        return a + b

    print(f1(3, 4))
    print(f1('호랑이', '호랑이'))

    # from typing import List

    # list() / List = []
    a: list()
    b: List = []

    print(type(a), type(b))

    c: List[int] = []
    print(type(c))

    # 3.9 이전 버전에서는 안됨
    d: list[int] = []
    print(type(d))
    # 데이터 시각화


def day13():
    # 벡터
    # 행렬
    # 행렬 곱 문제
    print(1)


def day14():
    # 통계
    # 데이터셋

    # 평균
    # 중앙값
    # 예약어 등 변수로 사용되면 함수의 기능을 잃어버림
    # 분위
    # 최빈값

    # 산포도
    # 변위
    # 평균값
    # 편차
    # 평균편차 - 편차 절대값에 합의 평균
    # 분산 - 편차 제곱 합의 평균
    # 표준편차 - 분산의 제곱근

    # 확률
    # 조건부 확률
    # Enum 문법 - 내가 사용하려던 0값을 BOY라는 문자로 치환, 1값을 GIRL 문자로 치환해서 해석

    # 확률 문제

    # 정규분포
    print(1)


def day15():
    # 경사 하강법 #
    # 최소제곱법 -> a = (x-x평균)*(y-y평균)의 합 / (x-x평균)^2의 합
    # 예측값
    # 평균 제곱 -> 평균 제곱 오차 = (예측값 - 실제값) ^2의 평균
    # 이차방정식
    # 미분
    # 학습률
    # 미분 공식
    print()


# day1()
# day2()
# day3()
# day4()
# day5()
# day6()
# day7()
# day8()
# day9()
# day10()
# day11()
# day12()
# day13()
# day14()
# day15()
print('\n', random())

# ex98

# 단축키 문법 오류 - Alt + Enter / 복사 Ctrl + D / 줄 이동 Ctrl + Shift + 방향키 / 줄 삭제 Ctrl + X

# 문제만 적고 직접 해보기

# 기본적으로 문법에 입력이 생략된 두 코드
# 타입 출력
# 자료형
# 정수형 문자열 변환
# 변수 선언 4가지 유형
# 파이썬에서 스왑 프로그램
# 값 증가 시 단항 연산 a++ 사용 안 되어서 다른 2가지 사용
# 고유 식별 번호 검색 id 사용 - 값의 메모리 번호를 가져서 같은 값은 변수명이 달라도 같은 id를 가짐
# 16진수 표현
# 8진수 표현
# 복소수 사용 문법 a+bi -> 듣기
# 나누기, 몫, 나머지
# 2의 8승
# round 함수 소수점 뒷자리 반올림 -> 듣기
# 배열 문법
# 많이 중요한 배열 문법
# 문자열로 만들어진 변수는 만들어진 순간부터 상수화된다.
# 상수화된 문자열 강제 변경 -> 듣기

# ---문자열---
# 문자열 짝을 짓는 방법 실습
# 하나만 사용할 때는 괄호 생략 가능
# format 사용 방법

# 풀어서 해석
# 1. 문자열 입력 사이에 {} 추가
# 2. {}를 그대로 출력하는 것을 확인
# 3. 출력문 변수 s에 format 사용되는 것을 확인
# 4. 변수 t에 s.format 대입되는 것을 확인
# 5. sdp s.format 대입되는 것을 확인

# 문자열의 개수를 얻을 때 'len' 사용
# 찾고자 하는 문자열의 개수를 얻을 때 문자열.count 사용 / 문자열.count(문자열)도 동격

# 배열의 인덱스 번호를 찾는 find
# find 검색 실패가 일어나면 항상 '-1' 리턴함
# 데이터 분석에서 '워드 카운트' 사용됨 / 예시) 대통령 신년사에서 코로나 단어 언급 횟수

# 표현 - 문자열을 관리하는 s 객체 생성
# 문자열을 소문자 lower
# 원본 데이터는 변경하지 않는 것이 원칙
# 문자열을 대문자 upper
# 대치 replace
# 대치 시 대소문자 구별함

# 스페이스를 기준으로 문자열을 분리함 split
# 한 개 이상의 결괏값을 리턴할 땐 배열(list)로 리턴

# 특정 문자 기준으로 분리할 때 split 안에 문자 입력함
# ------

# ---연산---
# 복합적으로 연산 사용시 1.산술 2.관계(대소) 3.논리 로 우선순위 진행
# 산술연산 덧셈+ 뺄셈- 곱셈* 나누셈/ 나머지// 몫% 승수**
# 관계연산 대소관계를 구분
# 논리연산
# -AND &
# -OR |
# -부정연산 not

# 복합 연산 - 연산자 우선순위
# 실행 순서 동격
# ------

# ---random---
# 파이썬 내장함수 사용 -> 임포트
# 시뮬레이션 데이터(모사데이터)로 작업시 사용
# 0.0~1.0 사이의 값 랜덤
# 3 <= x <=5
# 2부터 20까지 3씩 증가된 값을 랜덤하게
# 2 5 8 11 14 17 20

# ---입력---
# 키보드로부터 입력받기 원할때 input
# 문제 입력된 문자열 -> 숫자형
# 정석 코드

# ---제어문---
# 4대 제어문 if/while/for/switch
# 1. 파이썬에서 조건문에 () 사용해도 되지만 정석은 사용 안 함
# 2. 제어문의 끝에는 : 사용
# 3. 조건이 만족될 때의 실행 문장은 반드시 TAP 처리함

# ---if
# if else

# 주의점
# TAP 처리 유무에 따라 else 판단
# else 미포함
# else 포함

# else if

# 중첩 제어문

# 문제 - 100까지 랜덤값 입력받아서 일의 자리와 십의 자리의 홀짝에 따라 분기가 달라지는 홀짝프로그램

# if 안에서 false 로 사용되는 것들 - False/{} 빈배열/ []/ ()/ None/ ''/ not(True)

# if(리스트찾을값) in[리스트목록]
# 무궁화 문자열 판단 문제

# ---while
# continue / break
# 우박수 문제

# 우박수 문제 삼항 연산
# range 함수
# list(range())

# for 문
# list 가 숫자를 관리함 으로 표현
# list 가 문자열을 관리함 으로 표현
# for 문의 정석 코드 / 기본꼴
# 5단
# 1 부터 10까지 더하는 합산 프로그램 - 결과 55
# 컨버팅 - 다른 랭귀지에서 만들어진 프로그램을 사용하는 랭귀지에 맞게 이식할때 사용하는 용어
# 포팅 - os에 맞게끔 이식할때 사용하는 용어
# 격자 컨버팅
# 0~9 랜덤 숫자 4개 보이고 끝에 더해진 값 출력하기 5 7 6 3 = 21
# 랜덤하게 알파뱃(A~Z) 가로 네칸 세로 세칸 출력

# 아스키 코드 변환

# 리스트를 사용하여 CRUD 하는 기본형
# 리스트 생성 C
# 서로 다른 타입을 멤버로 사용하는 리스트

# R - 세가지 방법
# a[4]를 출력하게 되면 에러 발생 - 아웃오브바운드 에러 / 경계를 넘어선 조심해야할 에러
# print(a[4])
# 자주 사용되는 변수명 - value, item, data

# U - 기존 데이터를 삭제하고 새로 데이터를 생성하여 업데이트됨

# D - del

# 길이 구하는 함수 - len

# 중첩 리스트 - 이차원 배열 / 삼차원 배열

# 배열 사용 주의점
# A의 0번은 ''사이에 대문자 B라고 넣는 것은 안된다. 문자열은 직접적으로 업데이트할 수 없다.
# a[0] = 'B'
# B의 0번은 ''사이에 대문자 B를 넣으면 업데이트된다.

# 배열 갱신 방법 [:]개념 파이썬에서 자주 사용하는 문법
# 인덱스 번호 1번 부터 3-1개 가져오기 / 직관적으로 해석함
# 두개의 데이터를 삭제하고 그영역에 데이터를 추가함

# 특정 부분의 영역을 삭제할때 사용하는 방법 / 삭제하고 추가할 데이터가 없음

# 직접적으로 삭제

# 리스트 맨 뒤에 추가 - .append

# 특정 위치에 데이터를 추가하는 함수 - .insert

# 맨 마지막에 있는 데이터를 지우는 함수 - .pop
# 특정 위치에 데이터를 지울 때 인덱스 번호 지정함

# 리스트 안에 요소를 검색해서 삭제 - .remove
# 같은 데이터가 여러개 있어도 하나만 삭제함

# 검색해서 없으면 에러 출력됨
# 검색 에러를 대비해 예외처리를 함 - try: except: pass

# 찾아서 인텍스 번호를 리턴함 - index

# 정렬 - 비용이 많이 드는 함수
# 비용 절감은 메모리 절약과 속도 증가 중에 메모리 절약을 선택하는 경향이 있음
# 순차 정렬 함수 오름차순 = .sort
# 정렬이 되어있는 리스트의 역순 정렬 함수 내림차순 = .reverse
# 앞과 뒤에 순서를 바꾸는 함수 = .reverse
# 역순 정렬 내림차순

# append()의 확장 형태
# 어펜드 개념 리스트가 한개 추가됨 = 값 4개
# 익스텐드 개념 리스트가 한개 합성됨 = 값 6개
# 익스텐드와 동일 결과 / 차이점?

# 튜플 - 이하는 일은 리스트와 거의 동격이다?
# 주의 - 숫자 한 개 사용 시 ","로 튜플 타입 구분됨 b나 c 형태로 () 생략하여 사용됨
# () 생략은 문법 해석하는 데만 사용, 작성 시 () 붙여서 습관

# 튜플과 리스트 비슷한 문법구조를 가진다
# 튜플 언패킹
# 스왑

# 리스트 자료형을 튜플 자료형으로 리턴해주는 함수 - tuple()

# == 은 값 비교?
# 대소 비교는 - 개수 비교?
# 순회비교?

# 수정하기

# 튜플 값 1개 확인 시 리스트 사용하듯이 [] 사용
# 튜플은 데이터 수정이 안됨 에러 출력

# 리스트 - 중첩 사용 가능
# 문자열을 분리하여 저장시키는 결과가 리스트인 것을 증명하는 함수 - .split
# offset 용어 정의 - 기준점으로부터 상대적으로 떨어진 거리
# offset 에 -(음수)사용 시 뒤에서부터 출력 / 중요

# 딕셔너리 기본 문법 구조
# a = {k:v, ... }
# k = key (색인) : v = value (값)
# 배열을 이용한 문법구조로 사용되지 않음
# 키값이 같아서 제일 우측 가장 최근에 데이터로 갱신됨
# 중첩
# 키값을 혼용해서 쓰는 건 가급적 피해서 사용
# 예시 json 문법 구조에 맞춰서 딕셔너리 사용하게 됨
# 데이터 갱신
# 없는 데이터 추가

# 딕셔너리 CRUD
# C
# R
# U
# D
# del a['name'] () 생략 가능 / 예약어로 삭제함 / 문법적 구조가 다름

# 동격 문법 - .get 을 조금 더 사용

# 딕셔너리의 키를 전부 확인

# a = type(range(0, 10))
# print(a)

# 딕셔너리 사용 방법
# #전체 확인
# #print(item)
# #타입 확인
# #개별 값 확인
# #실제 사용 많이 함 / 값을 확인하기 때문에

# 얕은 복사 - 메모리 공유
# 깊은 복사

# 함수 사용 방법 네 가지
# 모든 랭귀지의 함수는 반드시 4가지의 형태를 가진다.(리턴 값이 있다 없다, 인수 전달이 있다 없다.)
# 자주 짜는 코드를 미리 데이터 백업 잡아놓는 목적.

# 인수 전달이 없을 때

# 인수 전달이 있을 때 - ( ) 안은 예약어만 아니면 뭐든 상관없음.
# func02('코코코콬코코콬코콬끼리') # 연산식이 있을 때 문자열을 넣으면 error 발생!

# 인수 전달이 없고 return 이 있을 때
# return 을 처리하는 3가지의 방법
# 1. return 을 하든지 말든지 무시
# 2. return 을 하면 그걸 변수로 받아 사용
# 3. 변수로도 받지 않고 직접적으로 사용
# *** 주의 사항
# print(func01()) # 이 형식은 return 이 있을 때만 사용할 수 있다.

# 인수 전달과 return 이 모두 있을 때
# return 값은 출력이 안된다.

# 대소비교

# 함수 사용
# 함수의 인수 값을 초기화할 수 있음 - 주의점 - 초기화는 맨 끝에서부터 해야 함
# 가변 인수 전달
# bare 문법 - 가독성을 높일 때 사용함 / 코드 분석 용이함
# 딕셔너리 출력됨 **

# 클래스
# 생성자 함수 기본 꼴 - 인수 값에 self 들어가야 함
# 기본 함수 정의 하는 네가지 방법
# 함수 기본 꼴 - 인수 값에 self가 전부 들어가야 함 / 다른 인수를 받을 경우 self가 제일 앞에 있어야 함
# self는 생성된 객체 / 자바에서의 this

# 필드
# 생성자에서 self를 이용해서 필드 멤버로 선언하지 않아도 됨
# 동적(dynamic)-필요할 때 만들어서 사용하고 사용이 끝나면 버리는 것 / 정적(static)-처음부터 만들어두고 끝까지 남아있는 것
# a1정적 a2동적 a3지역변수

# 상속
# 다형성
# 변수에 타입이 없어서 파이썬에서는 업캐스팅 논리가 없음

# 대입 연산 a = Apple()와 같은 의미

# 다양한 형태의 모든 타입을 받는다 - 다형성

# 예외처리
# Exception as - 익센셥 내용 출력 시키는 코드

# 파일 입출력
# 쓰기 write

# 한 줄씩 읽기
# 한 줄 있는 데이터를 먼저 읽어서 읽을 데이터가 없는 상태라서 20이 출력 안됨
# readline 자동 줄바꿈됨 - 읽을 데이터가 없다면 break 처리함
# 리스트로 읽기 - 정리 예시
# 전체 내용 문자열 읽기

# import - 외부의 파일을 읽음 / 파일 선두에 적음
# import A as B - 이 문법이 가장 많이 사용됨

# 지금 실행되고 있는 파일명 출력
# 외부에서 파일 참조 할 때 특정 함수 내용만 실행 시키기 위해 main 비교함
# 정석 코드 기본 꼴 - 메인 함수에 코드 작성
# 프로그램 진입 점 / 엔트리 포인트

# 딕셔너리 사용 - k: v
# 실습
# apple['n4'] / apple.get('n4') 범위 값을 넘어가는 둘의 차이점

# filter

# 참조 / 다른 이름으로 메모리 공유
# () 작성하면 호출

# swich 대안

# 리스트 반복

# 컴프리헨션
# 반복 문과 조건문을 이용하여 리스트를 생성하는 것을 컴프리헨션 이라 함 기본형
# a에서 반복문으로 값을 찾으면서 조건문을 만나 25보다 큰 값을 찾고 30, 40을 i에 넣고 +2 해서 리스트를 생성한 결과를 출력함

# dir함수를 이용하여 관련된 함수 목록 출력
# 딕셔너리{} - 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
# 리스트[] - 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
# 튜플() - 'count', 'index'

# 실습 예제 복습
# 검색에 실패하면 익셉션 - try 문 사용해서 에러 방어
# 중복된 데이터가 존재해도 첫 데이터만 삭제
# pop은 인덱스를 이용하여 값을 리턴 받고 리스트의 값은 삭제함
# 6을 제외한 나머지만 리스트로 출력

# 표준 함수 / 내장 함수 - 복습 정리
# key, value를 index, value로 사용하기도 함
# evaluation 실행하다 - 예시 - 코딩 웹 사이트에서 사용
# divmod 몫, 나머지 출력
# all / any
# .sort() / sorted()

# 시간 time / datetime

# 람다
# filter 사용 예

# 쌍으로 된 두 개의 데이터는 ()튜플을 많이 사용
# generator
# sum은 sum(리스트)와 sum(제너레이터) 타입을 사용 가능
# .sort(lambda)
# key= 예약어
# Counter() - 단어 카운팅 시 사용되는 함수
# 유저 0~ 끝까지 출력
# defaultdict

# 워드 카운터

# {}에 키값이 없으면 set
# set은 중복된 데이터를 넣지 않음
# assert

# is not None 삼항연산
# 워드 카운트
# _ 빈 변수
# yield
# enumerate
# random / randint / randrange
# seed(0)
# shuffle
# choice
# sample
# zip
# 인자 언패킹
# 타입 어노테이션
# list() / List = []
# 3.9 이전 버전에서는 안됨
# d: list[int] = []
# print(type(d))

# 데이터 시각화

# 벡터
# 행렬
# 행렬 곱 문제

# 통계
# 데이터셋

# 평균
# 중앙값
# 예약어 등 변수로 사용되면 함수의 기능을 잃어버림
# 분위
# 최빈값

# 산포도
# 변위
# 평균값
# 편차
# 평균편차 - 편차 절대값에 합의 평균
# 분산 - 편차 제곱 합의 평균
# 표준편차 - 분산의 제곱근

# 확률
# 조건부 확률
# Enum 문법 - 내가 사용하려던 0값을 BOY라는 문자로 치환, 1값을 GIRL 문자로 치환해서 해석

# 확률 문제

# 정규분포

# 경사 하강법 #
# 최소제곱법 -> a = (x-x평균)*(y-y평균)의 합 / (x-x평균)^2의 합
# 예측값
# 평균 제곱 -> 평균 제곱 오차 = (예측값 - 실제값) ^2의 평균
# 이차방정식
# 미분
# 학습률
# 미분 공식
