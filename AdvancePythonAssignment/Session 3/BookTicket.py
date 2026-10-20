def book_movie_ticket(tickets, wallet):
    try:
        price = wallet/tickets
        print("Price per ticket:", price)

    except ZeroDivisionError:
        print("Tickets cannot be zero!")

    except ValueError:
        print("Please enter valid values!")


book_movie_ticket(5, 1000)
book_movie_ticket(0, 1000)