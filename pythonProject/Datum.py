from collections import Counter
from collections import defaultdict
from random import *
from typing import List

users = [
    {"id": 0, "name": "호랑이0"},
    {"id": 1, "name": "호랑이1"},
    {"id": 2, "name": "호랑이2"},
    {"id": 3, "name": "호랑이3"},
    {"id": 4, "name": "호랑이4"},
    {"id": 5, "name": "호랑이5"},
    {"id": 6, "name": "호랑이6"},
    {"id": 7, "name": "호랑이7"},
    {"id": 8, "name": "호랑이8"},
    {"id": 9, "name": "호랑이9"}
]

print(len(users))

# 쌍으로 된 두 개의 데이터는 ()튜플을 많이 사용
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

friendships = {user["id"]: [] for user in users}
print(friendships)

for i, j in friendship_pairs:
    print(i, j)
    friendships[i].append(j)
    friendships[j].append(i)

print(friendships)

for k, v in friendships.items():
    print(k, v)

a = sum([10, 20, 30])
print(a)


def numer_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


total_connections = sum(numer_of_friends(user) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users

# generator
a = (i for i in range(5))
print(type(a))

# sum은 sum(리스트)와 sum(제너레이터) 타입을 사용 가능
b = sum(a)
print(b)

num_friends_by_id = [(user["id"], numer_of_friends(user)) for user in users]

num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

print(num_friends_by_id)

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
a = ['호랑이', '코끼리', '호랑이', '코끼리', '독수리', '호랑이']
b = Counter(a)
print(b)

c = [10, 20, 30, 10, 20, 10]
d = Counter(c)
print(d)
print()


# 유저 0~ 끝까지 출력
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user["id"]]
            for foaf_id in friendships[friend_id]]


def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )


for i in range(10):
    print(i, friends_of_friends(users[i]))
print()

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


def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


print(data_scientists_who_like("Java"))

# defaultdict
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

user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
for k, v in user_ids_by_interest.items():
    print(k, v)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
for i, v in interests_by_user_id.items():
    print(i, v)


def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for interest in interests_by_user_id["id"]
        for interested_user_id in user_ids_by_interest[interest]
        if interested_user_id != user["id"]
    )


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

print('-' * 10)
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


a = "Tiger Lion"
b = a.lower().split()
print(b)

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

word_and_counts = Counter(word
                          for user, interest in interests
                          for word in interest.lower().split())

for word, count in word_and_counts.most_common():
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


# assert 1 + 2 == 2


def f(a):
    return min(a)


assert f([1, 2, 3, 4]) == 1

# 11월 9일 학습
print('-' * 10)
# 삼항연산
a = 10
# a = None
safe_x = a if a is not None else 0
print(safe_x)

word_counts = Counter(interests)
wc = sorted(word_counts.items(),
            key=lambda word_and_counts: word_and_counts[1],
            reverse=True)
print(wc)

a = [10 for _ in [1, 1, 1, 1, 1]]
print(a)

j = 0
a = [(i, j)
     for i in range(3)
     for j in range(4)]
print(a)

for i in range(3):
    for j in range(4):
        print(a[i*4+j], end=" ")
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

a = [1, 2, 3]
b = [4, 5, 6]
c = [i for i in zip(a, b)]
print(c)
d, e = zip(*c)
print(d)
print(e)


def f1(a: int, b: int) -> int:
    return a+b


print(f1(3, 4))
print(f1('호랑이', '호랑이'))

# from typing import List

a: list()
b: List = []

print(type(a), type(b))

c: List[int] = []
print(type(c))

# 3.9 이전 버전에서는 안됨
d: list[int] = []
print(type(d))
