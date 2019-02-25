# -*- coding: utf-8 -*-


class FlightSelectStrategy(object):
    """航班选择策略
    表示当有多个可选择的航班时，具体选择哪一个所用的策略
    """

    def select(self, flights):
        """选择一个航班"""
        raise NotImplementedError
