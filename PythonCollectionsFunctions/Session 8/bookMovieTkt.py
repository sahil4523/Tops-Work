def book_movie_ticket(movie_name, seat_type="Regular", snacks=None):
    print("Movie:", movie_name)
    print("Seat:", seat_type)
    print("Snacks:", snacks)


book_movie_ticket("Jawan")
book_movie_ticket("Jawan", "VIP")
book_movie_ticket("Jawan", snacks="Popcorn", seat_type="VIP")