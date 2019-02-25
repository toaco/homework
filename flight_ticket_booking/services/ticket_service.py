# -*- coding: utf-8 -*-

from flight_ticket_booking.entities.flight import FlightDB
from flight_ticket_booking.entities.ticket import Ticket


class TicketService(object):
    @classmethod
    def buy_ticket(cls, customer_type, from_, to, date):
        ticket = Ticket()
        ticket.customer_type = customer_type
        ticket.date = date

        flights = FlightDB.get_flights(from_=from_, to=to)

        min_amount = float('+inf')
        for flight in flights:
            amount = flight.get_price(customer_type, date)
            if amount < min_amount:
                min_amount = amount
                ticket.flight = flight
                ticket.amount = min_amount

        return ticket

    @classmethod
    def buy_round_trip_ticket(cls, customer_type, from_, to, departing_date, returning_date):
        departing_ticket = cls.buy_ticket(customer_type=customer_type, from_=from_, to=to, date=departing_date)
        returning_ticket = cls.buy_ticket(customer_type=customer_type, from_=to, to=from_, date=returning_date)
        return departing_ticket, returning_ticket
