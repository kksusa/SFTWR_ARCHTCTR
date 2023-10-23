from user import User, UserProvider
from ticket import Ticket, TicketProvider
from carrier import CarrierProvider
from cash import CashProvider
from datetime import datetime


class Customer:
    def __init__(self, user: User):
        self.user_provider = UserProvider()
        self.user = user
        self.cash_provider = CashProvider()
        self.ticket_provider = TicketProvider()
        self.carrier_provider = CarrierProvider()
        self.tickets = []

    def search_tickets(self, date_time: datetime, city: str) -> [Ticket]:
        return self.ticket_provider.find_tickets(date_time, city)

    def buy_ticket(self, ticket: Ticket, count: int) -> bool:
        self.tickets.extend(self.ticket_provider.get_tickets(ticket, count))
        value = ticket.price * count
        if self.cash_provider.check_balance(self.user, value)\
                and self.cash_provider.decrease_money(self.user, value)\
                and self.cash_provider.increase_money(ticket.carrier, value):
            return self.carrier_provider.booking_ticket(ticket.carrier, count)
        return True

    def return_ticket(self, ticket: Ticket) -> bool:
        for item in self.tickets:
            if item == ticket:
                self.tickets.remove(item)
                self.cash_provider.decrease_money(self.user, ticket.price)
                self.cash_provider.decrease_money(ticket.carrier, ticket.price)
                self.carrier_provider.return_ticket(ticket.carrier, 1)
                return True
        return False
