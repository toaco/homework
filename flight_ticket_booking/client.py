# -*- coding: utf-8 -*-

import datetime

from flight_ticket_booking.services.ticket_service import TicketService
from flight_ticket_booking.strategies.filght_select_strategies.nearly_12pm_strategy import Nearly12pmStrategy


class Client(object):
    def __init__(self, from_, to, select_strategy):
        """
        :param from_: 出发地
        :param to: 目的地
        :param select_strategy: 多个航班可选择时的航班选择策略
        """
        self.from_ = from_
        self.to = to
        self.select_strategy = select_strategy

    def by_round_trip_ticket(self):
        # 处理输入
        print 'input:'
        try:
            customer_type, departing_date, returning_date = map(lambda x: x.strip(), raw_input().split(','))
        except ValueError:
            print('input format error!')
            return

        customer_type = customer_type.lower()
        departing_date = datetime.datetime.strptime(departing_date[:8], '%Y%m%d')
        returning_date = datetime.datetime.strptime(returning_date[:8], '%Y%m%d')

        # 调用服务
        ticket_service = TicketService()
        departing_ticket, returning_ticket = ticket_service.buy_round_trip_tickets(
            customer_type=customer_type,
            from_=self.from_,
            to=self.to,
            departing_date=departing_date,
            returning_date=returning_date,
            select_strategy=self.select_strategy,
        )

        # 输出
        print 'output:'
        print departing_ticket.flight.name
        print returning_ticket.flight.name


if __name__ == '__main__':
    client = Client(from_='chengdu', to='xian', select_strategy=Nearly12pmStrategy())
    client.by_round_trip_ticket()
    """
    input:
    REGULAR, 20190213WED, 20190220WED
    output:
    GD2607
    GD2501
    
    input:
    REWARD, 20190213WED, 20190220WED
    output:
    GD2502
    GD2501
    """
