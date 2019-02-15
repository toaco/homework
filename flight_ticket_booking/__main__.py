import datetime

from flight_ticket_booking.flightsfinder import FlightsFinder

if __name__ == '__main__':
    flight_finder = FlightsFinder(
        customer_type='reward',
        departing_way='chengdu_to_xian',
        returning_way='xian_to_chengdu',
        departing_date=datetime.date(2016, 04, 10),
        returning_date=datetime.date(2016, 04, 20)
    )

    flights = flight_finder.run()

    if flights:
        departing_flight, returning_flight = flights
        print departing_flight['name']
        print returning_flight['name']
    else:
        print 'cannot find flights'
