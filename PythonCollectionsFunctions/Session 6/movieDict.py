titles=["3 Idiots", "Dangal", "KGF"]
genres=["Comedy", "Drama", "Action"]
ratings=[4.8, 4.5, 4.3]

movies = [
    {"title": title, "genre": genre, "rating": rating}
    for title, genre, rating in zip(titles, genres, ratings)
]

print(movies)