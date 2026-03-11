from imdb import IMDb

def get_movie_cast():

        try:
            movie_name =  input("Enter Your Favorite Movie Name: ")
            ia = IMDb()
            movie_cast = ia.search_movie(movie_name)


            if movie_cast:
                movie = movie_cast[0]
                ia.update_movie(movie)
                cast = movie.get("cast",[])
                if cast:
                        print(f"The main cast of movie '{movie['name']}' is:")
                        for actor in cast[:15]:
                            actor_name = actor["name"]
                            print(f"{actor_name}")
                        with open("movie_cast.txt","a") as file:
                            file.write(f"\nThe Movie '{movie['name']}' Is:\n")

                            file.write(f"All Actor name list{actor_name}\n")
                else:
                    print(f"No cast info found for {movie_name}")

            else:
                print(f"No Movie {movie_name} found")

        except ValueError:
            print("Invalid Movie Name entered")
        except IndexError:
            print("Index Error the program crash")
        else:
            print("Movie Casting Successful")
        finally:
            print("Program Ended")

if __name__ == '__main__':
    get_movie_cast()
