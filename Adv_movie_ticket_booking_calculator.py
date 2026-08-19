#Movie Ticket booking calculator.

import random

class Movie:
    ticket_price = {"silver": 250, "gold": 500, "premium": 750, "vip": 1000}

    # Seating layout: rows A-E, seats 1-10 => 50 total seats
    rows = ["A", "B", "C", "D", "E"]
    seats_per_row = 10
    all_seats = [f"{row}{num}" for row in rows for num in range(1, 11)]

    # Tracks which seats are already booked (shared across all Movie objects in this run)
    booked_seats = set()

    def __init__(self):
        # Age input with validation
        while True:
            try:
                self.age = int(input("Enter your age: "))
                break
            except ValueError:
                print("Invalid input! Age must be a number. Try again.")

        # Membership input
        self.is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"

        # Number of tickets input with validation
        available_count = len(self.all_seats) - len(self.booked_seats)
        while True:
            try:
                self.no_of_tickets = int(input("Enter number of tickets: "))
                if self.no_of_tickets <= 0:
                    print("Number of tickets must be at least 1. Try again.")
                elif self.no_of_tickets > available_count:
                    print(f"Only {available_count} seat(s) left. Enter a smaller number.")
                else:
                    break
            except ValueError:
                print("Invalid input! Number of tickets must be a number. Try again.")

        # Ticket category input with validation
        while True:
            self.category = input("Enter ticket category (Silver/Gold/Premium/VIP): ").strip().lower()
            if self.category in self.ticket_price:
                break
            else:
                print("Invalid category! Please choose Silver, Gold, Premium, or VIP.")

        # Weekend input
        self.is_weekend = input("Is it a weekend? (yes/no): ").strip().lower() == "yes"

        # Randomly assign seats from whatever is still available
        available_seats = [seat for seat in self.all_seats if seat not in self.booked_seats]
        self.seat_numbers = random.sample(available_seats, self.no_of_tickets)

        # Mark these seats as booked so future bookings in this run won't reuse them
        self.booked_seats.update(self.seat_numbers)

    def details(self):
        if self.age < 7:
            print("Your age is not eligible for booking.")
            return False

        print("Your Movie Ticket is Booked")

        self.discount = 0
        if self.age >= 18 and self.is_member:
            self.discount = 20
            print(f"You have got a discount of {self.discount}%")
        else:
            print("You do not qualify for any discount")

        self.extra_charges = 0
        if self.is_weekend:
            if self.age > 18:
                self.extra_charges = 7
            elif self.age >= 7:
                self.extra_charges = 5
            print(f"You have to pay extra charges of {self.extra_charges}%")
        else:
            print("You do not pay any extra charges")

        return True

    def show(self):
        base_price = self.ticket_price[self.category]
        price_per_ticket = base_price + (base_price * self.extra_charges / 100) - (base_price * self.discount / 100)
        total_amount = price_per_ticket * self.no_of_tickets

        print("Your Tickets are booked")
        print(f"Category: {self.category.upper() if self.category == 'vip' else self.category.title()}")
        print(f"Seats: {', '.join(sorted(self.seat_numbers))}")
        print(f"Total amount: Rs.{total_amount:.2f}")


booking = Movie()
if booking.details():
    booking.show()
