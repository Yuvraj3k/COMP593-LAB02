"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        "full_name": "Yuvrajsinh Khengar",
        # TODO: Put student ID into data structure
        "student_id": "10319213",
        # TODO: Put list of 3 pizza toppings into data structure
        "pizza_toppings": ["Chicken", "Onion", "Tomato"],
        # TODO: Add movies to data structure
        "movies": [
            {
                "title": "Dune",
                "genre": "sci-fi"
            },
            {
                "title": "Dune 2",
                "genre": "Adventure"
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ["Peppers", "Pineapple"])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, "The Lord of the Rings", "fantasy")

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me["movies"])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # Print sentence containing name
    full_name = my_info["full_name"]
    first_name = full_name.split()[0]
    # Print sentence containing student ID
    student_id = my_info["student_id"]
    print(f"My name is {full_name}, but you can call me Legend {first_name}.")
    print(f"My student ID is {student_id}.")
    print()

def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    print("My favourite pizza toppings are:")
    for topping in my_info["pizza_toppings"]:
        print(f"- {topping}")

def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    # Append new pizza toppings to end of list 
    my_info["pizza_toppings"].extend(toppings)
    # Convert all pizza toppings to lowercase and sort the list alphabetically
    my_info["pizza_toppings"] = [topping.lower() for topping in my_info["pizza_toppings"]]
    my_info["pizza_toppings"].sort()

def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    new_movie = {
        "title": title,
        "genre": genre
    }
    my_info["movies"].append(new_movie)

def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    genres = [movie["genre"] for movie in my_info["movies"]]
    print("I like to watch", end=" ")
    for i, genre in enumerate(genres):
        if i == len(genres) - 1:
            print(f"and {genre}", end=" ")
        else:
            print(f"{genre},", end=" ")
    print("movies.")

def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    titles = [movie["title"].title() for movie in movie_list]
    print("Some of my favorite movies are", end=" ")
    for i, title in enumerate(titles):
        if i == len(titles) - 1:
            print(f"and {title}!")
        else:
            print(f"{title},", end=" ")

if __name__ == "__main__":
    main()
