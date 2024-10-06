import abc

class Ticket(abc.ABC):
    def __init__(self, passenger, number):
        self._passenger = passenger
        self._number = number

    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    def passenger(self, value):
        self._passenger = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @abc.abstractmethod
    def print_details(self):
        pass

    @staticmethod
    def validate_ticket_number(ticket_number):
        return len(ticket_number) == 6 and ticket_number.isalnum()


class EconomyTicket(Ticket):
    def print_details(self):
        print(f"Economy ticket: Passenger - {self.passenger}, Number - {self.number}")


class Loyalty:
    def __init__(self, points=0):
        self.points = points

    def earn_points(self, amount):
        self.points += amount
        print(f"Earned {amount} points. Total: {self.points}")


class BusinessTicket(Ticket, Loyalty):
    def __init__(self, passenger, number, points=0):
        Ticket.__init__(self, passenger, number)
        Loyalty.__init__(self, points)

    def print_details(self):
        print(f"Business ticket: Passenger - {self.passenger}, Number - {self.number}, Loyalty points: {self.points}")


bookings = []

def book_ticket():
    passenger = input("Enter passenger name: ")
    number = input("Enter ticket number (6 characters): ")

    while not Ticket.validate_ticket_number(number):
        print("Invalid ticket number! Please enter a valid 6-character ticket number.")
        number = input("Enter ticket number (6 characters): ")

    ticket_type = input("Enter ticket type (economy or business): ").lower()

    if ticket_type == "economy":
        ticket = EconomyTicket(passenger, number)
    elif ticket_type == "business":
        points = int(input("Enter initial loyalty points: "))
        ticket = BusinessTicket(passenger, number, points)
    else:
        print("Invalid ticket type!")
        return

    bookings.append(ticket)
    print("Ticket successfully booked!")


def view_bookings():
    if not bookings:
        print("No bookings found!")
    else:
        print("\nBooked Tickets:")
        for index, ticket in enumerate(bookings, 1):
            print(f"Ticket {index}:")
            ticket.print_details()


def edit_ticket():
    if not bookings:
        print("No bookings to edit!")
        return

    view_bookings()

    ticket_index = int(input("\nEnter the ticket number to edit: ")) - 1

    if ticket_index < 0 or ticket_index >= len(bookings):
        print("Invalid ticket number!")
        return

    ticket = bookings[ticket_index]

    print("\nEditing ticket details:")
    new_passenger = input(f"Enter new passenger name (current: {ticket.passenger}): ")
    new_number = input(f"Enter new ticket number (current: {ticket.number}, 6 characters): ")

    while not Ticket.validate_ticket_number(new_number):
        print("Invalid ticket number! Please enter a valid 6-character ticket number.")
        new_number = input(f"Enter new ticket number (current: {ticket.number}, 6 characters): ")

    ticket.passenger = new_passenger
    ticket.number = new_number

    print("Ticket updated successfully!")


def menu():
    while True:
        print("\n1. Book a ticket")
        print("2. View all bookings")
        print("3. Edit a booking")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            view_bookings()
        elif choice == "3":
            edit_ticket()
        elif choice == "4":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    menu()