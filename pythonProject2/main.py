from collections import Counter
from matplotlib import pyplot as plt
import math


def day12():
    # 데이터 시각화
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color='black', marker='x', linestyle='solid')
    plt.title("Nominal GDP")
    plt.ylabel("Billions of $")
    plt.show()

    # from matplotlib import pyplot as plt

    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp)
    plt.show()

    movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    num_oscars = [5, 11, 3, 8, 10]

    plt.bar(range(len(movies)), num_oscars)
    plt.xticks(range(len(movies)), movies)
    plt.show()

    # from collections import Counter
    grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
    print(grades[0] // 10)
    print(grades[0] // 10 * 10)
    print(grades[0] // (10 * 10))
    print((grades[0] // 10) * 10)  # Best
    for a in grades:
        print(min(a // 10 * 10, 90), end=' ')
    print()

    b = Counter([80, 90, 90, 80, 70, 0, 80, 80, 90, 60, 70, 70, 0])
    print(b)

    # 100점을 90대에 카운팅하기 위함
    histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)
    # print(histogram)
    # 점수에 해당되는것이 key
    for i in histogram.keys():
        print(i, end=' ')
    print()
    histogram = {80: 4, 90: 3, 70: 3, 0: 2, 60: 1}
    print(histogram.keys(), histogram.values())

    plt.bar([x + 5 for x in histogram.keys()], histogram.values(), 10, edgecolor=(0, 0, 0))
    # 각각 쌍을이루어 x []와 y[]의 값에 맞게 이루어졌다 [],[]가 의미하는
    plt.bar([85, 95, 75, 5, 65], [4, 3, 3, 2, 1], 10)
    # 15가 의미하는
    # bar 의 너비의 길이를 표시
    plt.bar([85, 95, 75, 5, 65], [4, 3, 3, 2, 1], 15)
    # 축의 시작점과 끝점을 설정하기 위해 막대바의 가운데 0 들어가는것을 방지
    plt.axis([-5, 105, 0, 5])
    plt.xticks([10 * i for i in range(11)])
    plt.show()

    variance = [1, 2, 4, 8, 16, 32, 64, 128, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]
    a = zip(variance, bias_squared)
    for i, v in a:
        print(i, v)
    total_error = [x + y for x, y in zip(variance, bias_squared)]
    print(total_error)
    print(variance)
    xs = [i for i, _ in enumerate(variance)]
    print(xs)

    plt.plot(xs, variance, 'g-', label='variance')
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')
    plt.plot(xs, total_error, 'b:', label='total error')
    plt.legend(loc=9)
    plt.show()

    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    plt.scatter(friends, minutes)

    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                     xy=(friend_count, minute_count),
                     xytext=(5, -5),
                     textcoords='offset points')

    plt.show()

    test_1_grades = [99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]

    plt.scatter(test_1_grades, test_2_grades)
    plt.axis("equal")
    plt.show()


def day13():
    # 벡터
    def f1(a, b):
        # c = [0, 0, 0]
        # c[0] = a[0] + b[0]
        # c[1] = a[1] + b[1]
        # c[2] = a[2] + b[2]
        c = []
        c.append(a[0] + b[0])
        c.append(a[1] + b[1])
        c.append(a[2] + b[2])
        return c

    print(f1([0, 1, 2], [3, 4, 5]))

    def f2(a, b):
        result = [i + j for i, j in zip(a, b)]
        return result

    print(f2([0, 1, 2], [3, 4, 5]))

    def f0(a, b):
        c = [i - j for i, j in zip(a, b)]
        return c

    print(f0([5, 7, 9], [4, 5, 6]))

    def f4(a):
        num = len(a[0])
        print(a)
        print(num)
        b = [sum(item[i]
                 for item in a)
             for i in range(num)]
        return b

    print(f4([[1, 2], [3, 4], [5, 6], [7, 8]]))

    def f1(c, v):
        a = [c * i for i in v]
        return a

    print(f1(2, [1, 2, 3]))
    print(f1(0.5, [1, 2, 3]))

    def f2(v):
        n = len(v)
        a = f1(1 / n, f4(v))
        return a

    print(f2([[1, 2], [3, 4], [5, 6]]))

    def f3(a, b):
        c = sum(i * j for i, j in zip(a, b))
        return c

    print(f3([1, 2, 3], [4, 5, 6]))

    def f4(a):
        return f3(a, a)

    print(f4([1, 2, 3]))

    # import math
    def f5(v):
        return math.sqrt(f4(v))

    print(f5([3, 4]))

    def f6(a, b):
        return f4(f0(a, b))

    print(f6([2, 1], [1, 2]))

    def f7(a, b):
        c = [0, 0]
        c[0] = a[0] - b[0]
        c[1] = a[1] - b[1]
        return f5(f0(a, b))

    print(f7([2, 1], [1, 2]))
    print(f7([4, 0], [0, 3]))

    # 행렬
    a = [[1, 2, 3],
         [4, 5, 6],
         [1, 2, 3],
         [7, 8, 9]]

    def f1(v):
        r = len(v)
        print(r)
        c = len(v[0])
        print(c)
        return r, c

    print(f1(a))

    def f2(a, b):
        return a[b]

    print(f2(a, 3))

    def f3(a, b):
        c = [i[b] for i in a]
        return c

    print(f3(a, 2))

    def f4(r, c, fn):
        a = [[fn(i, j)
              for j in range(c)]
             for i in range(r)]
        for i in a:
            print(i)
        print()
        return a

    print()

    def f5(n):
        return f4(n, n, lambda i, j: 1 if i == j else 0)

    def f6(i, j):
        if i == j:
            print(1)
        else:
            print(0)

    print(f6(1, 2))
    print(f5(5))

    for i in f5(5):
        print(i)

    print('-' * 10)
    # 행렬 곱 문제
    a = [[1, 2],
         [3, 4],
         [5, 6]]

    b = [[1, 2, 3],
         [4, 5, 6]]

    # a = [[1, 2, 3, 4],
    #      [2, 3, 1, 2],
    #      [1, 2, 1, 3]]
    # b = [[2, 1, 3],
    #      [1, 2, 2],
    #      [2, 3, 1],
    #      [3, 4, 1]]

    # *** 행렬의 곱셈 조건 ***
    # 행렬의 곱셈은 a*b 와 b*a 가 다른 결과가 나옴
    # 두 행렬 axb * cxd 는 b 와 c는 같은 수 이어야하고, 행렬의 곱셈 결과는 axd 행렬이 나옴
    # ex) 행렬 2 x 5 는
    # [1, 1, 1, 1, 1]
    # [1, 1, 1, 1, 1]

    # 행렬의 열을 구하는 함수
    def get_column(a, b):
        return [a_i[b] for a_i in a]

    def mul_matrix(a, b):
        result = []
        print(len(a[0]), len(b))
        # "행렬 a, b에 대한 곱을 위해서는 a의 열의 개수와 b의 행의 개수가 같아야 합니다."
        assert len(a[0]) == len(b)
        for a_row in a:
            result_row = []
            for j in range(len(b[0])):
                b_col = get_column(b, j)
                result_row.append(sum(a_row_v * b_col_v
                                      for a_row_v, b_col_v
                                      in zip(a_row, b_col)))
            result.append(result_row)
        return result

    result = mul_matrix(a, b)
    print('=======')
    for rows in result:
        print(rows)


def day14():
    # 통계
    # 데이터셋
    num_friends = [100.0, 49, 41, 40, 25, 21, 21, 19, 19, 18, 18, 16, 15, 15, 15, 15, 14, 14, 13, 13, 13, 13, 12, 12,
                   11, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                   9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
                   6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3,
                   3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    a = Counter(num_friends)
    b = range(101)
    c = [a[i] for i in b]
    # plt.bar(b, c)
    # plt.axis([0, 101, 0, 25])
    # plt.show()

    d = len(num_friends)
    print(d)
    e = max(num_friends)
    f = min(num_friends)
    print(e, f)
    g = sorted(num_friends)
    h = g[0]
    i = g[1]
    j = g[-2]
    print(h, i, j)

    # 평균
    def f1(a):
        b = sum(a) / len(a)
        return b

    print(f1(num_friends))

    # 중앙값
    def f2(a):
        b = sorted(a)[len(a) // 2]
        c = sorted(a)
        print(c)
        e = len(a) // 2
        print(e)
        d = c[len(a) // 2]
        print(d)
        return b

    def f3(a):
        b = sorted(a)
        c = len(a) // 2
        d = (b[c - 1] + b[c]) / 2
        return d

    def f4(a):
        b = f3(a) if len(a) % 2 == 0 else f2(a)
        return b

    print(f4([1, 10, 2, 9, 5]))
    print(f4([1, 9, 2, 10]))

    def func1():
        return 10

    def func2():
        return func1()

    def func3():
        return func2()

    print(func3())

    a = abs(-3)
    print(a)

    # 예약어 등 변수로 사용되면 함수의 기능을 잃어버림
    # abs = 10
    # a = abs(-3)
    # print(a)

    print(int(3.14))
    print(int(0.2 * 260))

    # 분위
    def f5(a, b):
        c = int(b * len(a))
        d = sorted(a)[c]
        e = sorted(a)[int(b * len(a))]
        print(e)
        return d

    print(f5(num_friends, 0.10))
    print(f5(num_friends, 0.25))
    print(f5(num_friends, 0.75))
    print(f5(num_friends, 0.90))

    # 최빈값
    def f6(a):
        b = Counter(a)
        c = max(b.values())
        d = [i for i, b in b.items()
             if b == c]
        return d

    print(set(f6(num_friends)))

    # 산포도
    # 변위
    a = [1, 2, 3, 4, 5]
    # 평균값
    b = sum(a) / len(a)
    print(b)
    # 편차
    c = [i - b for i in a]
    print(c)
    # 평균편차 - 편차 절대값에 합의 평균
    d = [abs(i) for i in c]
    e = sum(d) / len(d)
    print(e)
    # 분산 - 편차 제곱 합의 평균
    f = [i ** 2 for i in c]
    print(f)
    g = [abs(i) for i in f]
    h = sum(g) / len(g)
    print(h)
    # 표준편차 - 분산의 제곱근
    i = math.sqrt(h)
    print(i)

    print(0 < 3 < 7)

    # 확률
    # 조건부 확률
    # Enum 문법 - 내가 사용하려던 0값을 BOY라는 문자로 치환, 1값을 GIRL 문자로 치환해서 해석
    # import enum
    from enum import Enum

    class Kid(Enum):
        BOY = 0
        GIRL = 1

    print(Kid.BOY)
    print(Kid.BOY.value)
    print(Kid.BOY.name)

    import random
    print(random.choice([Kid.BOY, Kid.GIRL]))

    class Color(Enum):
        RED = 0
        GREEN = 1
        BLUE = 2

    print(random.choice([Color.RED, Color.GREEN, Color.BLUE]))

    ct0 = 0
    ct1 = 0
    ct2 = 0
    for _ in range(10000):
        a = random.choice([Kid.BOY, Kid.GIRL])
        b = random.choice([Kid.BOY, Kid.GIRL])
        if a == Kid.BOY:
            ct0 += 1
        if a == Kid.BOY and b == Kid.GIRL:
            ct1 += 1
        if a == Kid.BOY or b == Kid.GIRL:
            ct2 += 1
    print(ct0, ct1, ct2)
    print(ct1 / ct0)
    print(ct1 / ct2)

    # 확률 문제
    ct = 0
    for i in range(100000):
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        while a == b:
            b = random.randint(1, 10)

        a1 = random.randint(1, 10)
        b1 = random.randint(1, 10)
        while a1 == b1:
            b1 = random.randint(1, 10)

        if (a == a1 and b == b1) or (a == b1 and b == a1):
            ct += 1
    print(i / ct)

    # 정규분포
    a = math.sqrt(2 * math.pi)

    def ff(b, c=0, d=1):
        return (math.exp(-(b-c)**2/2/d**2)/(a*d))

    b = [i/10.0 for i in range(-50, 50)]
    plt.plot(b, [ff(i, d=1)for i in b], '-', label='mu=0,sigma=1')
    plt.plot(b, [ff(i, d=2)for i in b], '--', label='mu=0,sigma=2')
    plt.plot(b, [ff(i, d=0.5)for i in b], ':', label='mu=0,sigma=0.5')
    plt.plot(b, [ff(i, c=-1)for i in b], '-.', label='mu=1,sigma=1')
    plt.legend()
    plt.show()


def day15():
    # 경사 하강법 #
    # 예제 데이터 x = 학습 시간 / y = 점수
    x = [2, 4, 6, 8]
    y = [81, 93, 91, 97]

    # plt.scatter(x, y)

    # 최소제곱법 -> a = (x-x평균)*(y-y평균)의 합 / (x-x평균)^2의 합
    # a = ((2-5)*(81-90))+((4-5)*(93-90))... / ((2-5)^2)+((4-5)^2)...
    x1 = sum(x)/len(x)
    y1 = sum(y)/len(y)
    # a = []; b = []; c = []; d = []
    # a = [i-x1 for i in x]
    # b = [i-y1 for i in y]
    # c = [i*j for i, j in zip(a, b)]
    # d = [i**2 for i in a]

    ra = sum((i-x1)*(j-y1) for i, j in zip(x, y))/sum((i-x1)**2 for i in x)

    # c1 = sum(c)
    # d1 = sum(d)
    # print(a)
    # print(b)
    # print(c)
    # print(c1)
    # print(d)
    # print(d1)

    # 결과 = 2.3
    # r = c1/d1
    # print(r)
    print(ra)

    import numpy as np
    mx = np.mean(x)
    my = np.mean(y)
    print('x평균:', mx, 'y평균:', my)
    t1 = sum((i-mx)*(j-my) for i, j in zip(x, y))
    print('분자:', t1)
    t2 = sum((i-mx)**2 for i in x)
    print('분모:', t2)
    a = t1/t2
    print('a절편(기울기):', a)
    b = my-(mx*a)
    print('b절편:', b)

    # 예측값
    c = [(a*i)+b for i in x]
    # plt.plot(x, c)
    # plt.show()

    # 평균 제곱
    # y = [81, 93, 91, 97] - 실제값
    # [83.6, 88.2, 92.8, 97.4] 예측값
    # 평균 제곱 오차 = (예측값 - 실제값) ^2의 평균
    # ((83.6-81)**2+(88.2-93)**2+... / n
    # r = 8.29
    r = ((83.6-81)**2+(88.2-93)**2+(92.8-91)**2+(97.4-97)**2)/len(y)
    r = sum((i-j)**2 for i, j in zip(c, y))/len(y)
    print(r)

    # 이차방정식
    a = 0
    rv = []
    r1 = []
    for v in range(47):
        c1 = [(a*i)+b for i in x]
        a += 0.1
        r = sum((i - j) ** 2 for i, j in zip(c1, y)) / len(y)
        # plt.scatter(v, r)
        rv.append(v)
        r1.append(sum((i - j) ** 2 for i, j in zip(c1, y)) / len(y))
    # plt.plot(rv, r1)
    # plt.scatter(rv, r1)
    # plt.show()

    # 미분
    x = [2, 4, 6, 8]
    y = [81, 93, 91, 97]
    xdata = np.array(x)
    ydata = np.array(y)
    print(type(xdata), xdata)  # 배열이다.

    a = 0; b = 0
    lr = 0.05  # 확습률

    for i in range(1000):
        y = a * xdata + b

        # 미분 공식
        a_dif = -(1 / len(xdata)) * sum(xdata * (ydata - y))
        b_dif = -(1 / len(xdata)) * sum(ydata - y)

        a = a - lr * a_dif
        b = b - lr * b_dif

        print(i, round(a, 3), round(b, 3))


print('-' * 10)
# day12()
# day13()
# day14()
# day15()
