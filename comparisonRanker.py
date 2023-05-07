movies = input("Enter a list of movies, separated by commas: ").split(", ")

movie_pairs = []
for i in range(len(movies)):
    for j in range(i+1, len(movies)):
        movie_pairs.append((movies[i], movies[j]))

rankings = {}
for pair in movie_pairs:
    print("Which movie do you prefer?")
    print("1. " + pair[0])
    print("2. " + pair[1])
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        if pair[0] in rankings:
            rankings[pair[0]] += 1
        else:
            rankings[pair[0]] = 1
    else:
        if pair[1] in rankings:
            rankings[pair[1]] += 1
        else:
            rankings[pair[1]] = 1

for movie in movies:
    if movie not in rankings:
        rankings[movie] = 0

ranked_movies = sorted(rankings.items(), key=lambda x: x[1], reverse=True)
print("Final ranking:")
for i, movie in enumerate(ranked_movies):
    print(str(i+1) + ". " + movie[0])