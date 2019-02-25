from flight_ticket_booking.utlis.date_helper import DateHelper


class Flight(object):
    def __init__(self, name, from_, to, time, prices):
        self.name = name
        self.from_ = from_
        self.to = to
        self.time = time

        self.prices = prices

    def get_price(self, customer_type, date):
        if DateHelper.at_weekend(date):
            return self.prices[customer_type]['weekend']
        else:
            return self.prices[customer_type]['weekday']


class FlightDB(object):
    data = [
        Flight(name='GD2501', from_='xian', to='chengdu', time='08:00', prices={'reward': {'weekend': 500, 'weekday': 800}, 'regular': {'weekend': 900, 'weekday': 1100}}),
        Flight(name='GD2606', from_='xian', to='chengdu', time='12:25', prices={'reward': {'weekend': 500, 'weekday': 1100}, 'regular': {'weekend': 600, 'weekday': 1600}}),
        Flight(name='GD8732', from_='xian', to='chengdu', time='19:30', prices={'reward': {'weekend': 400, 'weekday': 1000}, 'regular': {'weekend': 1500, 'weekday': 2200}}),

        Flight(name='GD2502', from_='chengdu', to='xian', time='12:00', prices={'reward': {'weekend': 800, 'weekday': 800}, 'regular': {'weekend': 900, 'weekday': 1700}}),
        Flight(name='GD2607', from_='chengdu', to='xian', time='16:25', prices={'reward': {'weekend': 500, 'weekday': 1100}, 'regular': {'weekend': 600, 'weekday': 1600}}),
        Flight(name='GD8733', from_='chengdu', to='xian', time='23:30', prices={'reward': {'weekend': 400, 'weekday': 1500}, 'regular': {'weekend': 1000, 'weekday': 1600}}),
    ]

    @classmethod
    def get_flights(cls, from_, to):
        return filter(lambda flight: flight.from_ == from_ and flight.to == to, cls.data)
