# -*- coding: utf-8 -*-

import datetime

from flight_ticket_booking.services.ticket_service import TicketService


class Client(object):
    def __init__(self, from_, to):
        self.from_ = from_
        self.to = to

    def by_round_trip_ticket(self, input):
        # 处理输入
        customer_type, departing_date, returning_date = input.split(',')
        customer_type = customer_type.lower()
        departing_date = datetime.datetime.strptime(departing_date[:8], '%Y%m%d')
        returning_date = datetime.datetime.strptime(returning_date[:8], '%Y%m%d')

        # 调用服务
        ticket_service = TicketService()
        departing_ticket, returning_ticket = ticket_service.by_round_trip_ticket(
            customer_type=customer_type,
            from_=self.from_,
            to=self.to,
            departing_date=departing_date,
            returning_date=returning_date,
        )

        # 输出
        print departing_ticket.flight.name
        print returning_ticket.flight.name


if __name__ == '__main__':
    client = Client(from_='chengdu', to='xian')
    client.by_round_trip_ticket('REGULAR,20190213WED,20190220WED')
    client.by_round_trip_ticket('REWARD,20190213WED,20190220WED')
