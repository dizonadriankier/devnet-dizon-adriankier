"""
Midterm Practical Exam — Movie Collection Manager
Student: Dizon, Adrian Kier T.
"""

movies = []


def display_menu():
    print("\n===Movie Collection Manager===")
    print("1. Add a movie")
    print("2. View all movies")
    print("3. Count watched vs unwatched")
    print("4. Find a movie")
    print("5. Exit")

    choice = input("Choose an option: ")
    return choice

def add_movie(movie_list):
    

    title = input("Enter movie title: ")
    director = input("Enter director: ")
    status = input("Enter status: ")

    movietitle = title.split()
    moviedirector = director.split()
    moviestatus = status.split()

    print("Movie added succesfully.")
    # ask for title, director, and status
    # build the movie string
    # add it to the list
    pass


def view_movies(movie_list):

    # loop through and print every movie
    # handle empty list
    pass


def count_watched_unwatched(movie_list):
    # loop through the list
    # count Watched vs Unwatched
    # return both counts
    pass


def find_movie(movie_list):

    input = ("Movie title: ")

    print("No movies in the collection.")

    # ask for a movie title
    # search the list
    # search should be case-insensitive
    # print the result or "Movie not found."
    pass


def main():

    

    # create the main menu loop
    # call the appropriate function based on the user's choice
    pass


main()
