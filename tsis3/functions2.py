#Ex1
def is_above_5_5(movie):
    return movie["imdb"] > 5.5
#Ex2
def movies_above_5_5(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
#Ex3
def movies_by_category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
#Ex4
def average_imdb_score(movies):
    if not movies:
        return 0.0
    total_score = sum(movie["imdb"] for movie in movies)
    return total_score / len(movies)
#Ex5
def average_imdb_score_by_category(movies, category):
    category_movies = movies_by_category(movies, category)
    return average_imdb_score(category_movies)