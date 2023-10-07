import requests
from movie_api_key import api_key

# Class for Movie Data Base

class MovieDB:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = api_key
        self.lang_tr = "tr-TR"
        self.lang_en = "en-GB"
        self.page_num = 1

    # Function to get popular movies.

    def getPopular(self):
        if language == "tr":
            response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language={self.lang_tr}&page={self.page_num}")
        elif language == "en":
            response = requests.get(f"{self.api_url}movie/popular?api_key={self.api_key}&language={self.lang_en}&page={self.page_num}")
        return response.json()
    
    # Function to get top rated movies.

    def getTopRated(self):
        if language == "tr":
            response = requests.get(f"{self.api_url}movie/top_rated?api_key={self.api_key}&language={self.lang_tr}&page={self.page_num}")
        elif language == "en":
           response = requests.get(f"{self.api_url}movie/top_rated?api_key={self.api_key}&language={self.lang_en}&page={self.page_num}")
        return response.json()

    # Function to get movies with keywords.

    def getSearch(self, keyword):
        response = requests.get(f"{self.api_url}search/keyword?api_key={self.api_key}&query={keyword}&page={self.page_num}")
        return response.json()

    # Function to increase page number.

    def increasePageNum(self):
        self.page_num += 1


movieApi = MovieDB()


# Menu for both English and Turkish.



def menu():
        global language
        language = input("Choose your language: (TR/EN)\n").lower()
        if language == "tr":
            print("Film uygulamasına hoş geldin. Alttaki menüden dilediğini yapabilirsin. (Sayfa değiştirmek için N girin.. ) ")
        elif language == "en":
            print("Welcome to this film app. You can do anything from the menu. (Enter N to change pages.)")
        global choice
        if language == "tr":
            choice = input("1- Popüler Filmler\n2- En Sevilen Filmler\n3- Ara (Sadece İngilizce)\n4- Menu\n5- Çıkış\nSeçim: ")
        elif language == "en":
            choice = input("1- Popular Movies\n2- Top Rated Movies\n3- Search (English only)\n4- Menu\n5- Exit\nChoice: ")
        else:
            raise Exception("Enter valid language.")

menu()

# Creating a boolean variable to control a bug. 
#(If user chooses the Search function it tries to get an input everytime the user presses the new page button.. 
# And it won't show the new page because it will just reset the variable and show the first page.
# So we need to make sure that search mode is off.)
search_mode = True

while True:

    # If else statements to make sure everything goes according to menu.

    if choice == "4":
        menu()
    
    elif choice == "5":
        break

    elif choice == "1":   
        movies = movieApi.getPopular()
        for movie in movies["results"]:
            print(movie["title"])


    elif choice == "2":
        movies = movieApi.getTopRated()
        for movie in movies["results"]:
            print(movie["title"])

    elif choice == "3":
        if language == "tr":
            if search_mode == True:    
                search = input("Ara: ")
                movies = movieApi.getSearch(search)
                for movie in movies["results"]:
                    print(movie["name"])
                search_mode = False
            else:                            # We need to make sure that we print movies even if user didn't enter an input.
                movies = movieApi.getSearch(search)
                for movie in movies["results"]:
                    print(movie["name"])
                search_mode = False
        else:                                           
            if search_mode == True:
                search = input("Search: ")
                movies = movieApi.getSearch(search)
                for movie in movies["results"]:
                    print(movie["name"])
                search_mode = False
            else:
                movies = movieApi.getSearch(search)
                for movie in movies["results"]:
                    print(movie["name"])
                search_mode = False

    else:         # Rasing an exception so user does not mess up.
        raise Exception("Enter valid value.")

    page_input = input("")      # If user wants to go to the next page N should be entered.
                                # It will print menu otherwise.
    if page_input == "n":
        movieApi.increasePageNum()
    else:
        search_mode = True      # Don't forget to make search_mode True after user is done with search
                                # otherwise if they search first and then use the other features
                                # search will most likely reset and wont get a new input.
        menu()