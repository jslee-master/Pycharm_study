import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from random import *
import pandas as pd
import numpy as np
from math import *

font_location = 'C:/Windows/Fonts/malgun.ttf'
font_family = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_family)


def day1():
    # ex 1
    # 시각화 설치
    # File - Settings - Project - Python Interpreter - '+'버튼 선택 - matplotlib 검색 - Install Package

    # ex 2
    # import 사용법 세 가지
    # import matplotlib.pyplot
    # matplotlib.pyplot.plot()
    # matplotlib.pyplot.show()

    # from matplotlib.pyplot import *
    # plot()
    # show()

    # 가장 일반적으로 사용되는 형태
    # import matplotlib.pyplot as plt

    # plt.plot()
    # plt.show()

    # ex 3
    # plot의 종류
    # 라인 플롯 - 점과 점 사이를 선으로 이어서 보여줌
    # 바 플롯 - 막대 그래프형태로 보여줌 / 바 차트
    # 히스토그램 - 분포도
    # 스캐터 플롯 - 점을 찍어서 보여줌
    # 컨투어 플롯 - 산의 높낮이 등고선 등을 표현함
    # 서피스 플롯
    # 박스 플롯 - 주식에서 사용됨
    # 파이 차트

    # ex 4
    # 그래프의 타이틀을 설정
    # plt.title('Tiger')
    # plt.show()

    # ex 5
    # 리스트 설정
    # 리스트가 하나만 입력되면 Y축 기준으로 출력됨
    # plt.plot([1, 4, 9, 16])
    # plt.show()

    # 두 개의 리스트 사용
    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    # plt.show()

    # 데이터의 길이가 다르면 오류 출력
    # plt.plot([1, 3, 5, 7], [10, 20, 30])
    # plt.show()

    # ex 6
    # 설정값은 show() 이전에 입력되어야함
    # .grid() 디폴트값은 False
    # plt.grid(True)
    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    # plt.show()

    # ex 7
    # x축 y축 이름 설정
    # plt.xlabel('Tiger')
    # plt.ylabel('Lion')
    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    # plt.show()

    # ex 8
    # 홀드 - 기존의 플롯을 그대로 유치한채 새로운 플롯을 추가하는 용어
    # plt.plot([10, 20, 30, 40], [1, 4, 9, 16])
    # plt.plot([10, 20, 30, 40], [3, 7, 11, 20])
    # plt.show()

    # ex 9
    # range를 사용하여 플롯을 그리는 방법
    # plt.plot([10, 20, 30, 40], range(4))
    # plt.plot([10, 20, 30, 40], range(2, 6))
    # plt.show()

    # ex 10
    # 예약어 설정된 색상
    # plt.plot(range(1, 5), 'r')
    # plt.plot(range(2, 6), 'g')
    # plt.plot(range(3, 7), 'b')
    # plt.plot(range(4, 8), 'c')
    # plt.plot(range(5, 9), 'm')
    # plt.plot(range(6, 10), 'y')
    # plt.plot(range(7, 11), 'k')
    # plt.plot(range(0, 4), 'w')
    # plt.plot(range(8, 12), range(9, 13), 'k')
    # plt.show()

    # ex 11
    # 마크 설정하는 방법
    # # 옵션으로 사용 가능한 20개의 문자들
    # a = '.,ov^<>w1234sp*hH+xDd'
    # # enumerate는 문자열로도 사용가능함
    # for k, v in enumerate(a):
    #     print(k, v)
    #     plt.plot(range(1 + k, 5 + k), v + '-')
    # plt.show()

    # ex 12
    # 선의 스타일을 설정하는 방법
    # # 디폴트 직선의 모양
    # plt.plot(range(1, 5), '-')
    # # 점선
    # plt.plot(range(2, 6), '--')
    # # 파선
    # plt.plot(range(3, 7), '-.')
    # # 세밀한 점선
    # plt.plot(range(4, 8), ':')
    # plt.show()

    # ex 13
    # 여러 옵션 설정 시 하나의 문자열 안에 색상 마크 스타일 순서로 설정
    # plt.plot(range(1, 5), 'r^:')
    # plt.plot(range(3, 7), [1, 6, 7, 12], 'k<-.')
    # plt.show()

    # ex 14
    # 선의 세부 설정하는 방법
    # plt.plot(
    #     [10, 20, 30, 40],   # x축
    #     [1, 4, 9, 16],      # y축
    #     c="b",              # 선 색깔
    #     lw=5,               # 선 굵기
    #     ls="--",            # 선 스타일
    #     marker="o",         # 마커 종류
    #     ms=15,              # 마커 크기
    #     mec="g",            # 마커 선 색깔
    #     mew=5,              # 마커 선 굵기
    #     mfc="r"             # 마커 내부 색깔
    # )
    # plt.show()

    # ex 15
    # x, y 유효 범위 설정
    plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    plt.xlim(-10, 30)
    plt.ylim(-20, 70)
    plt.grid(True)
    plt.show()


def day2():
    # ex 16
    # 눈금자
    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    # plt.xticks(range(0, 10))
    # plt.yticks(range(0, 100, 10))
    # plt.show()
    # print(1)

    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40])
    # plt.xticks([1, 2, 3, 4], ['1day', '2day', '3day', '4day'], rotation='70')
    # plt.yticks([1, 2, 3, 4], ['Tige', 'LIon', 'Dog', 'Cat'])
    # plt.show()

    # ex 17
    # 범례
    # plt.plot([1, 4, 9, 16], [10, 20, 30, 40], label='Tiger')
    # plt.plot([2, 5, 10, 17], [10, 20, 30, 40], label='Lion')
    # plt.legend(loc=6)

    # ex 18
    # 배경색
    # 255 / 0xMAX / 0.0 ~ 1.0f
    # plt.gca().set_facecolor((0.7, 0.8, 0.2))

    # ex 19
    # 윈도우창 크기 조절
    # plt.figure(figsize=(6.4, 4.8))
    # plt.figure(figsize=(6.4*2, 4.8*2))
    # plt.show()

    # ex 20
    # 영상 처리

    # ex 21
    # 한글 설정 방법
    # import matplotlib.font_manager as fm
    # font_location = 'C:/Windows/Fonts/malgun.ttf'  # 오른쪽 마우스 정보 얻음
    # font_family = fm.FontProperties(fname=font_location).get_name()
    # plt.rc('font', family=font_family)

    # plt.plot(['호랑이', '코끼리', '독수리'])

    # ex 22
    # 플롯 그래프를 하나의 창에 여러 개 그리기
    # plt.subplot(2, 2, 2)
    # plt.plot([[1, 2, 3, 4], [10, 20, 30, 40]])
    # plt.subplot(2, 2, 3)
    # plt.plot([[1, 2, 3, 4], [10, 20, 30, 40]])
    # plt.subplot(4, 3, 1)
    # plt.plot([[1, 2, 3, 4], [10, 20, 30, 40]])

    # ex 23
    # y 축 두 개 사용하기
    # age = [10, 20, 30, 40, 50, 60]
    # weight = [20, 40, 55, 50, 70, 63]
    # height = [100, 120, 140, 150, 170, 165]
    # plt.plot(age, weight, 'r')
    # plt.twinx()
    # plt.plot(age, height, 'g')

    # ex 24
    # 데이터 저장
    # plt.plot([10, 20, 30, 40, 50, 60])
    # fig = plt.gcf()
    # plt.show()
    # fig.savefig('test.png')

    # ex 25
    # 바 차트
    # plt.bar([1, 2, 3], [2, 3, 1])
    # plt.barh([1, 2, 3], [2, 3, 1])
    # a = ['python', 'c++', 'java', 'scala', 'lisp', 'perl', 'javascript']
    # b = [12, 10, 8, 6, 5, 4, 3]
    # plt.subplot(1, 2, 1)
    # plt.bar(a, b, align='center')
    # plt.subplot(1, 2, 2)
    # plt.bar(a, b, align='edge')

    # ex 26
    # Ctrl + B - 함수 보기
    # 함수 우클릭 - Go To - Dclaration or Usages
    # a = ['python', 'c++', 'java', 'scala', 'lisp', 'perl', 'javascript']
    # b = [12, 10, 8, 6, 5, 4, 3]
    # plt.bar(a, b, width=0.2, bottom=10, align='edge', alpha=0.6)
    # plt.show()

    # ex 27
    # 배열
    import numpy as np
    a = [1, 2, 3, 4]
    # a = a + 3
    a = range(4)
    # a = a + 3
    a = np.arange(4)
    a = a + 3
    print(type(a))

    a = a + 0.35
    print(a)

    # a = plt.bar(np.arange(4) + 0.0, [90, 55, 40, 65], 0.4, color='red', label='a')
    # b = plt.bar(np.arange(4) + 0.2, [65, 40, 55, 95], 0.4, color='green', label='b')
    # plt.legend()

    # ex 28
    # a = plt.bar(np.arange(4), [90, 55, 40, 65], 0.4)
    # b = plt.bar(np.arange(4), [65, 40, 55, 95], 0.4, bottom=[90, 55, 40, 65])

    # ex 29
    # 연도별 우리나라 석탄 채굴량
    # 나이대별 급여 / 직업별 월급 차이 / 성별 급여 차이 / 학과별 경쟁률 / 월별 수익률 / 팀별 성적 / 종교 유무별 이혼율 / 동물원별 사자와 호랑이에 대한 개체 수 / 나라별 인구수
    # 나라별 남자 여자에 대한 인구수 / 연령대별 성별에 대한 월급 차이 / 성별 직업에 대한 빈도수 / 지역별 연령대 비율 /
    # 연령대별 정당에 대한 지지율 / 지역별 정당에 대한 지지율 / 나라별 금은동에 대한 메달 수 / 도시별 성별에 대한 범죄율 / 기타 등등
    # 경제성장률/자살률/합격률/취업률/백분율(프로야구 타율)/판매량/재고량/성장률/생산량/분포량/빈도/유입량/이자율
    a = []
    b = []
    for i in range(41):
        a.append(random() * 100000)
        i += 1980
        b.append(i)
    #
    # plt.bar(b, a)
    # plt.xticks(rotation='35')
    # plt.title('연도별 우리나라 석탄 채굴량')
    # plt.show()

    # ex 30
    # pandas - 데이터 분석을 위한 라이브러리
    # series - 일차원적인 자료 / 일차원배열
    # dataframe - 이차원 자료구조 / 테이블
    # import pandas as pd

    # dataframe 생성
    data = {'이름': ['호랑이', '코끼리', '독수리'],
            '나이': [10, 20, 30],
            '고향': ['한국', '미국', '영국']}
    df = pd.DataFrame(data)
    print(df)
    print(data.keys())

    # ex 31
    # dataframe 사용
    a = [10, 20, 30, 40]  # 많은 부분에서 필드의 성격을 짓는다
    b = [50, 60, 70, 80]
    c = [a, b]
    df = pd.DataFrame(c)
    # df = pd.DataFrame(c).T
    df.columns = ['나이', '급여', 'a', 'b']
    print(df)

    # ex 32
    # 데이터가 비어있는 columns 생성 - 테이블 생성
    df = pd.DataFrame(columns=['이름', '나이', '고향'])
    print(df)
    print(len(df))

    # ex 33
    # CRUD - insert 생성
    df.loc[20] = ['호랑이', 20, '서울']
    df.loc[30] = ['이순신', 10, '여수']
    print(df)
    print(len(df))

    # ex 34
    # CRUD - update 갱신
    df.loc[30] = ['홍길동', 100, '한국']
    print(df)
    print(len(df))

    # ex 35
    # CRUD - delete 삭제
    for i in range(10):
        df.loc[len(df)] = ['이순신' + str(i), '나이' + str(i), '서울' + str(i)]
    print(df)
    print(len(df))
    # df = df.drop([10])
    df = df.drop([20, 3, 4, 5])
    print(df)

    # ex 36
    # CRUD - read 읽기
    print(df.loc[6])
    print(df[2:4])
    print(df.head())
    print(df.head(3))
    print(df.tail());
    print('' * 30)


def day3():
    # ex 37
    # 파이썬에는 스위치문이 없어서 딕셔너리를 이용함
    a = {10: '호랑이', 20: '독수리'}

    def f1():
        print('구구단')

    def f2():
        print('합산')

    def f3(n):
        b = {10: f1, 20: f2}
        b[n]()

    print('숫자 10 또는 20을 입력하세요: ')
    c = int(input())
    f3(c)

    def func1(n):
        a = {10: '호랑이', 20: '독수리'}
        print(a[n])

    func1(10)

    def func2():
        print('구구단')

    def func3():
        print('합산')

    def func4(n):
        b = {10: func1, 20: func2, 30: func3}
        b[n]()

    func4(30)

    # ex 38
    # XOR - Exclusive OR
    # 두 개가 같으면 False 한 개가 다르 면 True
    print(False ^ False)
    print(True ^ False)
    print(False ^ True)
    print(True ^ True)

    # ex 39
    # NumPy
    # import numpy as np
    a = np.arange(10)  # [0 1 2 3]
    b = list(range(10))
    print(a)
    print(b)
    for _ in range(10):
        c = a - 2
    print(c)
    # for _ in range(10):
    #     d = b - 2  # 에러 출력됨
    # print(d)

    # ex 40
    # N차원 배열 객체
    a = np.random.randn(3, 4)
    print(a);
    print('' * 50)

    b = a + a
    print(b)

    c = a + b
    print(c)

    print(a.shape, a.dtype, type(a.shape))

    # ndarray 생성하기
    a = [1, 2, 3, 4]
    b = np.array(a)
    print(b)

    # 코드 작성 정석
    a = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    b = np.array(a)
    print(b)

    print(b.ndim, b.shape)

    print(np.zeros(5))

    print(np.zeros((3, 4, 2)))

    # ex 41
    # ndarray의 dtype
    a = np.arange(10)
    print(a)

    # ex 42
    # NumPy 배열의 산술 연산
    a = np.array(
        [[1, 2, 3],
         [4, 5, 6]])
    b = np.array(
        [[2, 3, 4],
         [5, 6, 7]])
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a % b)
    print(1 / a)

    # 루트 값
    print(4 ** 0.5)

    # ex 43
    # 색인과 슬라이싱 기초
    a = np.arange(10)
    print(a)
    print(a[5])
    # 5부터 8-5의 개수만큼 출력
    print(a[5:8])
    a[5:8] = 12
    print(a)
    b = a[5:8]
    print(b)
    b[0] = 123
    print(b)
    print(a)
    a[:] = 7
    print(a)

    a = np.array(
        [[1, 2, 3],
         [4, 5, 6]])
    print(a)
    print(a[1])
    # 동일 결과 출력
    print(a[1][2])
    print(a[1, 2])
    a[1][2] = 100
    print(a)
    a[1, 2] = 200
    print(a)

    a = np.array(
        [[1, 2, 3],
         [4, 5, 6]])
    b = a[:2, 1:]
    print(b)

    # 슬라이스로 선택하기 - 3x4 12
    a = np.array(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
    b = a[:2, 2:]
    print(b)
    b = a[1:, 1:3]
    print(b)
    b = a[:, 1:3]
    print(b)

    # ex 44
    # 불리언값으로 선택하기
    a = np.array(['호랑이', '코끼리', '독수리', '호랑이'])
    print(a == '호랑이')
    # ~ 틸 부정연산
    print(~(a == '호랑이'))

    # ex 45
    # 팬시 색인
    a = np.empty((4, 3))
    a[2] = 5
    print(a)

    a = np.arange(32)
    print(a)

    # .reshape - 일차원 배열을 이차원 배열로 변경하여 사용
    b = a.reshape(8, 4)
    print(b)

    # ex 46
    # 배열의 전치(대각)와 축 바꾸기
    # 전치 - x축과 y축 바꿈
    a = np.array(
        [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]])
    print(a.T)

    # 행렬 곱
    # 3 x 4 -> 4 x 3 = 3 x 3
    print(np.dot(a, a.T))

    # ex 47
    # 유니버설 함수 - 범용 함수
    a = np.array([1, 2, 3, 4, 5])
    # print(np.sqrt(a, a))

    a = np.array([-10, 0, 10])
    print(np.sign(a))

    # Nan - Not a Number

    # 동일 결과 출력됨
    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])
    print(a + b)
    print(np.add(a, b))

    # ex 48
    # imshow 함수
    points = np.arange(-5, 5, 0.01)
    xs, ys = np.meshgrid(points, points)
    print(ys)

    z = np.sqrt(xs ** 2 + ys ** 2)
    print(z)

    plt.imshow(z, cmap=plt.cm.gray)
    plt.colorbar()
    plt.show()

    # ex 49
    # 책 예제 실습
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])

    result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
    print(result)
    result = np.where(cond, xarr, yarr)
    print(result)

    arr = np.random.randn(4, 4)
    print(arr)
    print(arr > 0)
    print(np.where(arr > 0, 2, -2))
    print(np.where(arr > 0, 2, arr))

    arr = np.random.randn(5, 4)
    print(arr)
    print(arr.mean())
    print(np.mean(arr))
    print(arr.sum())
    print(arr.mean(axis=1))
    print(arr.sum(axis=0))
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
    print(arr.cumsum())
    arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    print(arr)
    print(arr.cumsum(axis=0))
    print(arr.cumprod(axis=1))

    arr = np.random.randn(100)
    print((arr > 0).sum())
    bools = np.array([False, False, True, False])
    print(bools.any())
    print(bools.all())

    arr = np.random.randn(6)
    print(arr)
    arr.sort()
    print(arr)
    arr = np.random.randn(5, 3)
    print(arr)
    arr.sort(1)
    print(arr)
    large_arr = np.random.randn(1000)
    large_arr.sort()
    print(large_arr[int(0.05 * len(large_arr))])

    names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
    print(np.unique(names))
    ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
    print(np.unique(ints))
    print(sorted(set(names)))
    values = np.array([6, 0, 0, 3, 2, 5, 6])
    print(np.in1d(values, [2, 3, 6]))

    # ex 50
    # 배열 데이터의 파일 입출력
    a = np.arange(10)
    np.save('some_array', a)
    print(np.load('some_array.npy'))
    b = np.load('some_array.npy')
    print(b)


def day4():
    # # ex 51
    # # 선형대수 책 예제
    # x = np.array([[1, 2, 3], [4, 5, 6]])
    # y = np.array([[1, 2], [3, 4], [5, 6]])
    # print(x)
    # print(y)
    #
    # print(x.dot(y))
    # print(np.dot(x, y))
    #
    # print(np.ones(3))
    #
    # print(np.dot(x, np.ones(3)))
    # print(x@np.ones(3))
    #
    # # ex 52
    # # .linalg - 행렬에서 자주 사용되는 공식 라이브러리
    # from numpy.linalg import inv, qr
    #
    # x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    #
    # print(x)
    # print(x.T)
    # print(x.T.dot(x))
    # mat = x.T.dot(x)
    # print(inv(mat))
    # print(mat.dot(inv(mat)))
    # q, r = qr(mat)
    # print(r)

    # a = np.array([1, 2, 3, 4])
    # print(np.diag(a))
    # b = np.diag(a)
    # print(np.trace(b))
    # c = np.linalg.inv(x)
    # print(c)
    # # a * x = b 에서 a b를 알때 x 구하는 함수
    # a = np.array([[1, 2, 1], [0, 1, 1], [1, 0, 1]])
    # b = np.array([4, 3, 5])
    # c = np.linalg.solve(a, b)
    # print(c)

    # ex 53
    # 2x + 3y = 5 / 3x + y = 2 문제
    # a = np.array([[2, 3],
    #               [3, 1]])
    # b = np.array([[5],
    #               [2]])
    # # c = np.linalg.inv(a)
    # # cc = c.dot(b)
    # # print(cc)
    # d = np.linalg.solve(a, b)
    # print(d)

    # ex 54
    # transform 만들기 문제
    # # translate - 이동
    # a = np.array([10, 20, 20, 10, 10])
    # b = np.array([10, 10, 20, 20, 10])
    # plt.plot(a, b)
    #
    # x = []
    # y = []
    # for i in range(len(a)):
    #     a1 = np.array([[1, 0, 50], [0, 1, 30], [0, 0, 1]])
    #     b1 = np.array([[a[i]], [b[i]], [1]])
    #     c = a1.dot(b1)
    #     x.append(c[0][0])
    #     y.append(c[1][0])
    # print(x, y)
    # plt.plot(x, y)
    #
    # # rotate - 30도 회전 시키기
    # print(sin(radians(30)))
    #
    # r = radians(30)
    #
    # a0 = np.array([-5, 5, 5, -5, -5])
    # b0 = np.array([-5, -5, 5, 5, -5])
    # plt.plot(a0, b0)
    #
    # x0 = []
    # y0 = []
    # for i in range(len(a)):
    #     a1 = np.array([[cos(r), -sin(r), 0],
    #                    [sin(r), cos(r), 0],
    #                    [0, 0, 1]])
    #     b1 = np.array([[a0[i]], [b0[i]], [1]])
    #     c = a1.dot(b1)
    #     x0.append(c[0][0])
    #     y0.append(c[1][0])
    # print(x0, y0)
    # plt.plot(x0, y0)
    #
    # xr = []
    # yr = []
    # for i in range(len(a)):
    #     a1 = np.array([[1, 0, 15], [0, 1, 15], [0, 0, 1]])
    #     b1 = np.array([[x0[i]], [y0[i]], [1]])
    #     c = a1.dot(b1)
    #     xr.append(c[0][0])
    #     yr.append(c[1][0])
    # print(xr, yr)
    # plt.plot(xr, yr)
    #
    # # scale - 확대 / 축소
    # sx = []
    # sy = []
    # for i in range(len(a)):
    #     a1 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
    #     b1 = np.array([[a0[i]], [b0[i]], [1]])
    #     c = a1.dot(b1)
    #     sx.append(c[0][0])
    #     sy.append(c[1][0])
    # print(sx, sy)
    # plt.plot(sx, sy)

    # rx = []
    # ry = []
    #
    # def trans(sx, sy, ro, tx, ty):
    #     a0 = np.array([-5, 5, 5, -5, -5])
    #     b0 = np.array([-5, -5, 5, 5, -5])
    #
    #     x = []
    #     y = []
    #     for i in range(len(a0)):
    #         a1 = np.array([[sx, 0, 0],
    #                        [0, sy, 0],
    #                        [0, 0, 1]])
    #         b1 = np.array([[a0[i]], [b0[i]], [1]])
    #         c = a1.dot(b1)
    #         x.append(c[0][0])
    #         y.append(c[1][0])
    #     r = radians(ro)
    #     x0 = []
    #     y0 = []
    #     for i in range(len(a0)):
    #         a1 = np.array([[cos(r), -sin(r), 0],
    #                        [sin(r), cos(r), 0],
    #                        [0, 0, 1]])
    #         b1 = np.array([[x[i]], [y[i]], [1]])
    #         c = a1.dot(b1)
    #         x0.append(c[0][0])
    #         y0.append(c[1][0])
    #     for i in range(len(a0)):
    #         a1 = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    #         b1 = np.array([[x0[i]], [y0[i]], [1]])
    #         c = a1.dot(b1)
    #         rx.append(c[0][0])
    #         ry.append(c[1][0])
    #     print(rx, ry)
    #     return rx, ry
    #
    # trans(0.5, 3, 30, 30, 27)
    # plt.plot(rx, ry)
    # plt.xlim(-30, 100)
    # plt.ylim(-30, 100)
    # plt.show()

    # ex 55
    # 별 그리기
    # stx = []
    # sty = []
    #
    # def star(x, y, n, tx, ty):
    #     seta = 360/n
    #     for i in range(n+1):
    #         r = radians((seta*2)*i)
    #         a1 = np.array([[cos(r), -sin(r), tx],
    #                        [sin(r), cos(r), ty],
    #                        [0, 0, 1]])
    #         b1 = np.array([[x],
    #                        [y],
    #                        [1]])
    #         c = a1.dot(b1)
    #         stx.append(c[0][0])
    #         sty.append(c[1][0])
    #
    # star(0, 20, 5, 30, 40)
    # plt.plot(stx, sty)

    # plt.xlim(0, 100)
    # plt.ylim(0, 100)
    # plt.show()

    # ex 56
    # 책 계단 오르내리기 예제 실습
    position = 0
    walk = [position]
    steps = 1000
    for i in range(steps):
        step = 1 if randint(0, 1) else -1
        position += step
        walk.append(position)
    # plt.plot(walk[:100])

    nsteps = 1000
    draws = np.random.randint(0, 2, size=nsteps)
    steps = np.where(draws > 0, 1, -1)
    walk = steps.cumsum()
    print(walk.min())
    print(walk.max())
    print((np.abs(walk) >= 10).argmax())

    nwalks = 5000
    nsteps = 1000
    draws = np.random.randint(0, 2, size=(nwalks, nsteps))
    steps = np.where(draws > 0, 1, -1)
    walks = steps.cumsum(1)
    print(walks)
    print(walks.max())
    print(walks.min())

    hits30 = (np.abs(walks) >= 30).any(1)
    print(hits30)
    print(hits30.sum())
    steps = np.random.normal(loc=0, scale=0.25, size=(nwalks, nsteps))
    print(steps)

    plt.show()


def day5():
    # ex 57
    # Series 책 예제 실습
    obj = pd.Series([4, 7, -5, 3])
    print(obj)
    print(obj.values)
    print(obj.index)

    obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
    print(obj2)
    print(obj2.index)
    print(obj2['a'])
    obj2['d'] = 6
    print(obj2[['c', 'a', 'd']])
    print(obj2[obj2 > 0])
    print(obj2 * 2)
    print(np.exp(obj2))
    print('b' in obj2)
    print('e' in obj2)

    sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
    obj3 = pd.Series(sdata)
    print(obj3)

    states = ['California', 'Ohio', 'Oregon', 'Texas']
    obj4 = pd.Series(sdata, index=states)
    print(obj4)
    print(pd.isnull(obj4))
    print(pd.notnull(obj4))
    print(obj4.isnull())
    print(obj3)
    print(obj4)
    print(obj3 + obj4)
    obj4.name = 'population'
    obj4.index.name = 'state'
    print(obj4)
    print(obj)
    obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
    print(obj)

    # ex 58
    # DataFrame 책 예제 실습
    # 229페이지 까지
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
            'year': [2000, 2001, 2002, 2001, 2002, 2003],
            'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
    frame = pd.DataFrame(data)
    print(frame)
    print(frame.head())

    frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                         index=['a', 'c', 'd'],
                         columns=['Ohio', 'Texas', 'California'])
    states = ['Texas', 'Utah', 'California']
    frame = frame.reindex(columns=states)
    print(frame.loc[['a', 'c', 'd'], states])

    obj = pd.Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
    obj.drop('c', inplace=True)
    print(obj)

    print('-' * 10)
    ser = pd.Series(np.arange(3.))
    print(ser)
    ser = pd.Series(np.arange(3.), index=['a', 'b', 'c'])
    print(ser[-1])

    print('-' * 10)
    # ex 59
    # 상관관계 예제
    df = pd.DataFrame({'t1': [2, 4, 6, 8],
                       't2': [81, 93, 91, 97]})
    print(df.dtypes)
    print(df)
    print(df.corr(method='pearson'))
    print(df['t1'].corr(df['t2']))
    print(df.t1.corr(df.t2))

    df = pd.DataFrame(columns=['t1', 't2'], dtype='int64')
    print(df.columns)
    df.loc['0'] = [2, 81]
    df.loc['1'] = [4, 93]
    df.loc['2'] = [6, 91]
    df.loc['3'] = [8, 97]
    print(df.dtypes)
    print(df)
    print(df.corr(method='pearson'))
    print(df['t1'].corr(df['t2']))

    # ex 60
    # 책 예제 실습
    # 235페이지 까지

    # ex 61
    # 데이터 로딩과 저장, 파일 형식
    # 텍스트 파일
    df = pd.read_csv('mytxt/ex1.csv')
    print(df)

    print(pd.read_csv('mytxt/ex1.csv', sep='.'))
    df = pd.read_csv('mytxt/ex1.csv', sep='.', header=None)
    print(pd.read_csv('mytxt/ex1.csv', sep='.', names=['이름', '나이', '급여', 'A', '메시지']))

    # ex 62
    # cx_oracle
    # 오라클 테이블을 판다스로 읽어오기
    import cx_Oracle as cO
    from datetime import datetime

    start_tm = datetime.now()
    dsn_tns = cO.makedsn('localhost', '1521', service_name="orcl")
    con = cO.connect(user="ljs", password="1234", dsn=dsn_tns)
    cur = con.cursor()
    qr = 'select * from EMP'
    cur.execute(qr)
    dept = dict()
    deft = pd.DataFrame([{'NAME': a, 'AGE': b, 'SALARY': c} for a, b, c in cur.execute(qr)])
    print(deft)


def day6():
    # ex 63
    # 데이터 쓰기
    df = pd.DataFrame(['호랑이', '코끼리'], [10, 20])
    fn = 'mytxt/out.csv'
    df.to_csv(fn)

    pd.DataFrame(['호랑이', '코끼리'], [10, 20]).to_csv('mytxt/ex2.csv', index_label=['age', 'name'])

    data = pd.read_csv('mytxt/ex2.csv', index_col='name')
    print(data)

    # ex 64
    # 데이터 분리 예제
    print(fn)

    for i in range(3):
        # fn = 'mytxt/Tiger%04d.csv' % (i+1)
        filename = df.to_csv('mytxt/Tiger%04d.csv' % (i), sep='|')
        # print(fn)

    print('-' * 10)
    # ex 65
    # sys.stdout
    import sys
    data.to_csv(sys.stdout, na_rep='NULL')

    pd.DataFrame(['호랑이', '', '코끼리'], [10, '', 20])
    data.to_csv(sys.stdout, na_rep='호랑이')

    # ex 66
    # 결측 데이터
    data = pd.read_csv('mytxt/out1.csv')
    print(data)
    print(data.isnull())
    print(data.fillna(0))

    print('-' * 10)
    # ex 67
    #
    # pd.DataFrame([''a'', ''b'', ''c''], [''1'', ''2'', ''3''], [''4'', ''5'', ''6'']).to_csv('mytxt/ex3.csv')
    data = pd.read_csv('mytxt/ex3.csv')
    print(data)

    import csv
    f = open('mytxt/ex3.csv')
    reader = csv.reader(f)

    for line in reader:
        print(line)

    with open('mytxt/ex3.csv') as f:
        lines = list(csv.reader(f))
    header, values = lines[0], lines[1:]
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    print(data_dict)

    a = [1, 2, 3]
    b = [[4, 5, 6]]
    print(a)
    print(b)

    # for i in zip(a, b):
    for i in zip(a, *b):  # *은 전치를 뜻함
        print(i)

    # ex 68
    # JSON 데이터 책 예제 실습
    obj = """
    {"name": "Wes",
     "places_lived": ["United States", "Spain", "Germany"],
     "pet": null,
     "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                  {"name": "Katie", "age": 38,
                   "pets": ["Sixes", "Stache", "Cisco"]}]
     }
    """

    import json
    result = json.loads(obj)
    print(result)

    asjson = json.dumps(result)
    print(asjson)

    siblings = pd.DataFrame(result['siblings'], columns=['name', 'age'])
    print(siblings)

    data = pd.read_json('mytxt/example.json')
    print(data)
    print(data.to_json())
    print(data.to_json(orient='records'))

    # ex 69
    # 엑셀 파일에서 데이터 읽어오기
    xlsx = pd.ExcelFile('mytxt/ex1.xlsx')
    xls = pd.read_excel(xlsx, 'Sheet1')
    print(xls)
    frame = pd.read_excel('mytxt/ex1.xlsx', 'Sheet1')
    print(frame)

    writer = pd.ExcelWriter('mytxt/ex2.xlsx')
    frame.to_excel(writer, 'Sheet1')
    writer.save()
    xlsx2 = pd.ExcelFile('mytxt/ex2.xlsx')
    xls2 = pd.read_excel(xlsx2, 'Sheet1')
    print(xls2)

    frame.to_excel('mytxt/ex3.xlsx')
    xlsx3 = pd.read_excel('mytxt/ex3.xlsx', 'Sheet1')
    print(xlsx3)

    # ex 70
    # 웹 API 사용하기
    import requests
    url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
    resp = requests.get(url)
    print(resp)
    data = resp.json()
    print(data[0]['title'])
    issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
    print(issues)

    # ex 71
    # 데이터 정제 및 준비 - 결측 데이터 처리 책 예제 실습
    # 306페이지 까지 - 298 페이지 정규 표현식은 제외
    import re
    text = "foo    bar\t baz  \tqux"
    re.split('\s+', text)
    regex = re.compile('\s+')
    regex.split(text)
    regex.findall(text)
    text = """Dave dave@google.com
    Steve steve@gmail.com
    Rob rob@gmail.com
    Ryan ryan@yahoo.com
    """
    pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

    # re.IGNORECASE makes the regex case-insensitive
    regex = re.compile(pattern, flags=re.IGNORECASE)
    regex.findall(text)
    m = regex.search(text)
    text[m.start():m.end()]
    print(regex.match(text))
    print(regex.sub('REDACTED', text))
    pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    m = regex.match('wesm@bright.net')
    m.groups()
    regex.findall(text)
    print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text))
    data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
            'Rob': 'rob@gmail.com', 'Wes': np.nan}
    data = pd.Series(data)
    data.isnull()
    data.str.contains('gmail')
    data.str.findall(pattern, flags=re.IGNORECASE)
    matches = data.str.match(pattern, flags=re.IGNORECASE)
    print(matches)
    print('-' * 10)
    matches = matches.astype(str)
    print(matches.str.get(1))
    print(matches.str[0])
    print(data.str[:5])

    # # ex 72
    # # 데이터 분석 예제 529페이지
    path = 'mytxt/example.txt'
    print(open(path).readline())

    import json
    path = 'mytxt/example.txt'
    records = [json.loads(line) for line in open(path)]
    print(records[0])
    # time_zones = [rec['tz'] for rec in records]
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    print(time_zones[:10])

    def get_counts(sequence):
        counts = {}
        for x in sequence:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        return counts

    counts = get_counts(time_zones)
    print(counts['America/New_York'])
    print(len(time_zones))

    def top_counts(count_dict, n=10):
        value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
        value_key_pairs.sort()
        return value_key_pairs[-n:]

    print(top_counts(counts))

    from collections import Counter
    counts = Counter(time_zones)
    print(counts.most_common(10))

    frame = pd.DataFrame(records)
    print(frame.info())
    print(frame['tz'][:10])

    tz_counts = frame['tz'].value_counts()
    print(tz_counts[:10])

    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()
    print(tz_counts[:10])

    import seaborn as sns
    subset = tz_counts[:10]
    # sns.barplot(y=subset.index, x=subset.values)
    # plt.show()

    print(frame['a'][1])
    print(frame['a'][50])
    print(frame['a'][51][:50])

    results = pd.Series([x.split()[0] for x in frame.a.dropna()])
    print(results[:5])
    print(results.value_counts()[:8])

    cframe = frame[frame.a.notnull()].copy()
    print(cframe)
    cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
    print(cframe['os'][:5])

    by_tz_os = cframe.groupby(['tz', 'os'])
    agg_counts = by_tz_os.size().unstack().fillna(0)
    print(agg_counts[:10])

    indexer = agg_counts.sum(1).argsort()
    print(indexer[:10])

    count_subset = agg_counts.take(indexer[-10:])
    print(count_subset)
    print(agg_counts.sum(1).nlargest(10))

    count_subset = count_subset.stack()
    count_subset.name = 'total'
    count_subset = count_subset.reset_index()
    print(count_subset[:10])

    # sns.barplot(x='total', y='tz', hue='os', data=count_subset)
    # plt.show()

    def norm_total(group):
        group['normed_total'] = group.total / group.total.sum()
        return group

    results = count_subset.groupby('tz').apply(norm_total)
    sns.barplot(x='normed_total', y='tz', hue='os', data=results)
    plt.show()

    g = count_subset.groupby('tz')
    results2 = count_subset.total / g.total.transform('sum')
    print(results2)


def day7():
    # ex 73
    # 재현성과 피벗
    print(np.arange(6).reshape(2, 3))
    data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                        index=pd.Index(['Ohio', 'Colorado'], name='state'),
                        columns=pd.Index(['one', 'twe', 'three'], name='number'))
    print(data)
    result = data.stack()
    print(result)
    print(result.unstack())
    print(result.unstack(0))
    print(result.unstack('state'))

    # ex 74
    # 그래프와 시각화
    # 379페이지 까지
    import seaborn as sns
    tips = pd.read_csv('mytxt/tips.csv')
    tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
    print(tips.head())

    # sns.barplot(x='tip_pct', y='day', data=tips, orient='h')

    # sns.barplot(x='tip_pct', y='day', hue='time', data=tips, orient='h')

    sns.set(style='whitegrid')
    # tips['tip_pct'].plot.hist(bins=50)
    # tips['tip_pct'].plot.density()

    # comp1 = np.random.normal(0, 1, size=200)
    # comp2 = np.random.normal(10, 2, size=200)
    # values = pd.Series(np.concatenate([comp1, comp2]))
    # sns.distplot(values, bins=100, color='k')

    macro = pd.read_csv('mytxt/macrodata.csv')
    data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
    trans_data = np.log(data).diff().dropna()
    print(trans_data[-5:])
    sns.regplot('m1', 'unemp', data=trans_data)
    plt.title('Changes in log %s versus log %s' % ('m1', 'unemp'))
    sns.pairplot(trans_data, diag_kind='kde', plot_kws={'alpha': 0.2})

    plt.show()
    # ex 75
    # 책 550 페이지 예제 실습


def day8():
    # ex 76
    # 책 567 페이지 예제 실습

    # ex 77
    # 554 페이지 함수 문법 설명
    class Apple:
        def f1(self):
            print(1)
            return self

        def f2(self, func):
            print(2)
            num = func(100)  # f3(group)인수
            return num * 3

    def f3(group):
        print(group)  # 100 출력
        return group * 2

    a = Apple()

    b = a.f1().f2(f3)  # 함수 번호 1번에 return이 반드시 있어야한다
    print(b)

    class Apple:
        def groupby(self):
            print(1)
            return self

        def apply(self, func):
            print(2)
            num = func(100)
            return num * 3

    def add_prop(group):
        print(group)
        return group * 2

    names = Apple()

    b = names.groupby().apply(add_prop)
    print(b)

    # ex 78
    # 책 574 페이지 예제 실습


# print(1)
# day1()
# day2()
# day3()
# day4()
# day5()
# day6()
# day7()
day8()

# ex 76
