from flight_ticket_booking.strategies.filght_select_strategies.base import FlightSelectStrategy


class Nearly12pmStrategy(FlightSelectStrategy):
    SECONDS_OF_12PM = 12 * 3600

    def select(self, flights):
        flights = sorted(flights, key=self.__compare_key)
        return flights[0]

    def __compare_key(self, flight):
        seconds = self.__time_to_seconds(flight.time)
        return abs(seconds - self.SECONDS_OF_12PM)

    @staticmethod
    def __time_to_seconds(time):
        hour, minute = time.split(':')
        minutes = int(hour) * 60 + int(minute)
        seconds = minutes * 60
        return seconds
