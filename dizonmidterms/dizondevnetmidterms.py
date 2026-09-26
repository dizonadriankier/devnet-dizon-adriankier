movies = []


def add_movie(title, director, year, genre):
   
    movie = {
        "title": title,
        "director": director,
        "year": year,
        "genre": genre
    }
    movies.append(movie)  #
    print(f"Movie '{title}' added successfully.")


def edit_movie(movie_id, new_title=None, new_director=None, new_year=None, new_genre=None):
  
    for movie in movies:
        
            if new_title:
                movie["title"] = new_title
            if new_director:
                movie["director"] = new_director
            if new_year:
                movie["year"] = new_year
            if new_genre:
                movie["genre"] = new_genre
            print(f"Movie with ID {movie_id} updated successfully.")
            return
    print(f"Movie with ID {movie_id} not found.")

# Function to delete a movie
def delete_movie(movie_id):
    global movies
    # Create a new list without the movie to be deleted
    movies = [movie for movie in movies if movie["id"] != movie_id]
    print(f"Movie with ID {movie_id} deleted successfully.")

# Function to view all movies
def view_movies():
    if movies:
        for movie in movies:
            print(f"{movie['id']}. {movie['title']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print("No movies in the database.")

# Function to search for movies by title
def search_movie_by_title(title):
    found_movies = [movie for movie in movies if title.lower() in movie["title"].lower()]
    if found_movies:
        for movie in found_movies:
            print(f"{movie['id']}. {movie['title']}, directed by {movie['director']}, "
                  f"released in {movie['year']}, Genre: {movie['genre']}")
    else:
        print(f"No movies found with title '{title}'.")
