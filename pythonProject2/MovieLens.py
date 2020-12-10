import pandas as pd

pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']

users = pd.read_table('mytxt/users.dat', sep='::', header=None, names=unames)

print(users)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('mytxt/ratings.dat', sep='::', header=None, names=rnames)
print(ratings)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('mytxt/movies.dat', sep='::', header=None, names=mnames)
print(movies)

data = pd.merge(pd.merge(ratings, users), movies)
print(data)
print(data.iloc[0])

mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings)

ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])

active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)

mean_ratings = mean_ratings.loc[active_titles]
print(mean_ratings)

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings)

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=False)
print(sorted_by_diff)

rating_std_by_title = data.groupby('title')['rating'].std()
print(rating_std_by_title)
rating_std_by_title = rating_std_by_title.loc[active_titles]
print(rating_std_by_title)
rating_std_by_title.sort_values(ascending=False)
print(rating_std_by_title)
