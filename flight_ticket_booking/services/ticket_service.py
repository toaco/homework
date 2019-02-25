# -*- coding: utf-8 -*-

from flight_ticket_booking.entities.flight import FlightDB
from flight_ticket_booking.entities.ticket import Ticket


class TicketService(object):
    @classmethod
    def buy_ticket(cls, customer_type, from_, to, date, select_strategy):
        """ 购买单程票
        :param customer_type:  用户类型
        :param from_: 出发地
        :param to: 目的地
        :param date: 出发时间
        :param select_strategy: 多个航班可用时的选择策略
        :return: 票
        """
        ticket = Ticket()
        ticket.customer_type = customer_type
        ticket.date = date

        flights = FlightDB.get_flights(from_=from_, to=to)

        min_amount = float('+inf')
        available_flights = []
        for flight in flights:
            amount = flight.get_price(customer_type, date)
            if amount < min_amount:
                min_amount = amount
                available_flights = [flight]
                ticket.amount = min_amount
            elif amount == min_amount:
                available_flights.append(flight)

        ticket.flight = select_strategy.select(available_flights)
        return ticket

    @classmethod
    def buy_round_trip_tickets(cls, customer_type, from_, to, departing_date, returning_date, select_strategy):
        """ 购买往返票
        :param customer_type:  用户类型
        :param from_: 出发地
        :param to: 目的地
        :param departing_date: 出发时间
        :param returning_date: 返回时间
        :param select_strategy: 多个航班可用时的选择策略
        :return: 票
        """
        departing_ticket = cls.buy_ticket(customer_type=customer_type, from_=from_, to=to, date=departing_date, select_strategy=select_strategy)
        returning_ticket = cls.buy_ticket(customer_type=customer_type, from_=to, to=from_, date=returning_date, select_strategy=select_strategy)
        return departing_ticket, returning_ticket
