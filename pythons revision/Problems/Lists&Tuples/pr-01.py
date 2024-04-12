"""
1. Movie Recommendation System:
This program uses lists and user input to recommend movies.

i) Create a list of movie titles with different genres (e.g., ["Comedy" : ["The Hangover", "21 Jump Street"], "Action" : ["Mission: Impossible", "The Matrix"], "Drama" : ["Schindler's List", "The Shawshank Redemption"]]) - This is a dictionary where genres are keys and movie titles are lists as values.
ii) Ask the user for their preferred genre.
iii) Use a for loop to iterate through the movie titles in the chosen genre and display them as recommendations.
"""


def return_movies_name(movies: list):
    return "\n".join(movies)


list_of_movies = {
    "Comedy": ["The Hangover", "21 Jump Street"],
    "Action": ["Mission: Impossible", "The Matrix"],
    "Drama": ["Schindler's List", "The Shawshank Redemption"]
}

user_preferred_genre = input("Enter Your favourite genre: ")
capitalized_text = user_preferred_genre.capitalize()

if capitalized_text in list_of_movies:
    print(return_movies_name(list_of_movies[capitalized_text]))
else:
    print('This Genre is not in our database.')
