# -*- coding: utf-8 -*-
import datetime
from collections import defaultdict

from flight_ticket_booking import config
from flight_ticket_booking.utlis.date_helper import DateHelper


class FlightsFinder(object):
    def __init__(self, customer_type, departing_way, returning_way, departing_date, returning_date):
        self.customer_type = customer_type
        self.departing_way = departing_way
        self.returning_way = returning_way
        self.departing_date = departing_date
        self.returning_date = returning_date

    def run(self):
        departing_flights = config.FLIGHTS[self.departing_way][self.customer_type]
        returning_flights = config.FLIGHTS[self.returning_way][self.customer_type]
        return self.__find_way(departing_flights, returning_flights)

    def __find_way(self, departing_flights, returning_flights):
        min_amount = float('+inf')
        amount_map = defaultdict(list)

        for df in departing_flights:
            for rf in returning_flights:
                if self.__is_available_way(df, rf):
                    amount = self.__get_amount(df, rf)
                    if amount <= min_amount:
                        min_amount = amount
                        amount_map[min_amount].append((df, rf))

        flights = amount_map.get(min_amount)
        if flights:
            return flights[-1]  # FLIGHTS有序，返回最后一个

    def __is_available_way(self, departing_flight, returning_flight):
        start_time = self.__earliest_time(departing_flight)
        return_time = self.__latest_time(returning_flight)
        if start_time and return_time and start_time < return_time:
            return True

    def __earliest_time(self, flight):
        if flight['at_weekends']:
            date = DateHelper.next_weekend(self.departing_date)
        else:
            date = DateHelper.next_weekday(self.departing_date)
        if date <= self.returning_date:
            hour, minute = map(lambda x: int(x), flight['time'].split(':'))
            return datetime.datetime.combine(date, datetime.time(hour, minute))

    def __latest_time(self, flight):
        if flight['at_weekends']:
            date = DateHelper.prev_weekend(self.returning_date)
        else:
            date = DateHelper.prev_weekday(self.returning_date)
        if date >= self.departing_date:
            hour, minute = map(lambda x: int(x), flight['time'].split(':'))
            return datetime.datetime.combine(date, datetime.time(hour, minute))

    @staticmethod
    def __get_amount(departing_flight, returning_flight):
        return departing_flight['price'] + returning_flight['price']
