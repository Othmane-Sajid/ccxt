# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange

# -----------------------------------------------------------------------------

try:
    basestring  # Python 3
except NameError:
    basestring = str  # Python 2
import json
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import InvalidNonce
from ccxt.base.precise import Precise


class btcbox(Exchange):

    def describe(self):
        return self.deep_extend(super(btcbox, self).describe(), {
            'id': 'btcbox',
            'name': 'BtcBox',
            'countries': ['JP'],
            'rateLimit': 1000,
            'version': 'v1',
            'has': {
                'cancelOrder': True,
                'CORS': False,
                'createOrder': True,
                'fetchBalance': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': True,
                'fetchTicker': True,
                'fetchTickers': False,
                'fetchTrades': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/51840849/87327317-98c55400-c53c-11ea-9a11-81f7d951cc74.jpg',
                'api': 'https://www.btcbox.co.jp/api',
                'www': 'https://www.btcbox.co.jp/',
                'doc': 'https://blog.btcbox.jp/en/archives/8762',
                'fees': 'https://support.btcbox.co.jp/hc/en-us/articles/360001235694-Fees-introduction',
            },
            'api': {
                'public': {
                    'get': [
                        'depth',
                        'orders',
                        'ticker',
                    ],
                },
                'private': {
                    'post': [
                        'balance',
                        'trade_add',
                        'trade_cancel',
                        'trade_list',
                        'trade_view',
                        'wallet',
                    ],
                },
            },
            'markets': {
                'BTC/JPY': {'id': 'btc', 'symbol': 'BTC/JPY', 'base': 'BTC', 'quote': 'JPY', 'baseId': 'btc', 'quoteId': 'jpy', 'taker': 0.05 / 100, 'maker': 0.05 / 100},
                'ETH/JPY': {'id': 'eth', 'symbol': 'ETH/JPY', 'base': 'ETH', 'quote': 'JPY', 'baseId': 'eth', 'quoteId': 'jpy', 'taker': 0.10 / 100, 'maker': 0.10 / 100},
                'LTC/JPY': {'id': 'ltc', 'symbol': 'LTC/JPY', 'base': 'LTC', 'quote': 'JPY', 'baseId': 'ltc', 'quoteId': 'jpy', 'taker': 0.10 / 100, 'maker': 0.10 / 100},
                'BCH/JPY': {'id': 'bch', 'symbol': 'BCH/JPY', 'base': 'BCH', 'quote': 'JPY', 'baseId': 'bch', 'quoteId': 'jpy', 'taker': 0.10 / 100, 'maker': 0.10 / 100},
            },
            'exceptions': {
                '104': AuthenticationError,
                '105': PermissionDenied,
                '106': InvalidNonce,
                '107': InvalidOrder,  # price should be an integer
                '200': InsufficientFunds,
                '201': InvalidOrder,  # amount too small
                '202': InvalidOrder,  # price should be [0 : 1000000]
                '203': OrderNotFound,
                '401': OrderNotFound,  # cancel canceled, closed or non-existent order
                '402': DDoSProtection,
            },
        })

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privatePostBalance(params)
        result = {'info': response}
        codes = list(self.currencies.keys())
        for i in range(0, len(codes)):
            code = codes[i]
            currency = self.currency(code)
            currencyId = currency['id']
            free = currencyId + '_balance'
            if free in response:
                account = self.account()
                used = currencyId + '_lock'
                account['free'] = self.safe_string(response, free)
                account['used'] = self.safe_string(response, used)
                result[code] = account
        return self.parse_balance(result, False)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {}
        numSymbols = len(self.symbols)
        if numSymbols > 1:
            request['coin'] = market['baseId']
        response = self.publicGetDepth(self.extend(request, params))
        return self.parse_order_book(response)

    def parse_ticker(self, ticker, market=None):
        timestamp = self.milliseconds()
        symbol = None
        if market is not None:
            symbol = market['symbol']
        last = self.safe_number(ticker, 'last')
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_number(ticker, 'high'),
            'low': self.safe_number(ticker, 'low'),
            'bid': self.safe_number(ticker, 'buy'),
            'bidVolume': None,
            'ask': self.safe_number(ticker, 'sell'),
            'askVolume': None,
            'vwap': None,
            'open': None,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': None,
            'percentage': None,
            'average': None,
            'baseVolume': self.safe_number(ticker, 'vol'),
            'quoteVolume': self.safe_number(ticker, 'volume'),
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {}
        numSymbols = len(self.symbols)
        if numSymbols > 1:
            request['coin'] = market['baseId']
        response = self.publicGetTicker(self.extend(request, params))
        return self.parse_ticker(response, market)

    def parse_trade(self, trade, market=None):
        timestamp = self.safe_timestamp(trade, 'date')
        symbol = None
        if market is not None:
            symbol = market['symbol']
        id = self.safe_string(trade, 'tid')
        priceString = self.safe_string(trade, 'price')
        amountString = self.safe_string(trade, 'amount')
        price = self.parse_number(priceString)
        amount = self.parse_number(amountString)
        cost = self.parse_number(Precise.string_mul(priceString, amountString))
        type = None
        side = self.safe_string(trade, 'type')
        return {
            'info': trade,
            'id': id,
            'order': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': type,
            'side': side,
            'takerOrMaker': None,
            'price': price,
            'amount': amount,
            'cost': cost,
            'fee': None,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {}
        numSymbols = len(self.symbols)
        if numSymbols > 1:
            request['coin'] = market['baseId']
        response = self.publicGetOrders(self.extend(request, params))
        return self.parse_trades(response, market, since, limit)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'amount': amount,
            'price': price,
            'type': side,
            'coin': market['baseId'],
        }
        response = self.privatePostTradeAdd(self.extend(request, params))
        #
        #     {
        #         "result":true,
        #         "id":"11"
        #     }
        #
        return self.parse_order(response, market)

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        # a special case for btcbox – default symbol is BTC/JPY
        if symbol is None:
            symbol = 'BTC/JPY'
        market = self.market(symbol)
        request = {
            'id': id,
            'coin': market['baseId'],
        }
        response = self.privatePostTradeCancel(self.extend(request, params))
        #
        #     {"result":true, "id":"11"}
        #
        return self.parse_order(response, market)

    def parse_order_status(self, status):
        statuses = {
            # TODO: complete list
            'part': 'open',  # partially or not at all executed
            'all': 'closed',  # fully executed
            'cancelled': 'canceled',
            'closed': 'closed',  # never encountered, seems to be bug in the doc
            'no': 'closed',  # not clarified in the docs...
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        #     {
        #         "id":11,
        #         "datetime":"2014-10-21 10:47:20",
        #         "type":"sell",
        #         "price":42000,
        #         "amount_original":1.2,
        #         "amount_outstanding":1.2,
        #         "status":"closed",
        #         "trades":[]
        #     }
        #
        id = self.safe_string(order, 'id')
        datetimeString = self.safe_string(order, 'datetime')
        timestamp = None
        if datetimeString is not None:
            timestamp = self.parse8601(order['datetime'] + '+09:00')  # Tokyo time
        amount = self.safe_number(order, 'amount_original')
        remaining = self.safe_number(order, 'amount_outstanding')
        price = self.safe_number(order, 'price')
        # status is set by fetchOrder method only
        status = self.parse_order_status(self.safe_string(order, 'status'))
        # fetchOrders do not return status, use heuristic
        if status is None:
            if remaining is not None and remaining == 0:
                status = 'closed'
        trades = None  # todo: self.parse_trades(order['trades'])
        symbol = None
        if market is not None:
            symbol = market['symbol']
        side = self.safe_string(order, 'type')
        return self.safe_order({
            'id': id,
            'clientOrderId': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'amount': amount,
            'remaining': remaining,
            'filled': None,
            'side': side,
            'type': None,
            'timeInForce': None,
            'postOnly': None,
            'status': status,
            'symbol': symbol,
            'price': price,
            'stopPrice': None,
            'cost': None,
            'trades': trades,
            'fee': None,
            'info': order,
            'average': None,
        })

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        # a special case for btcbox – default symbol is BTC/JPY
        if symbol is None:
            symbol = 'BTC/JPY'
        market = self.market(symbol)
        request = self.extend({
            'id': id,
            'coin': market['baseId'],
        }, params)
        response = self.privatePostTradeView(self.extend(request, params))
        return self.parse_order(response, market)

    def fetch_orders_by_type(self, type, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        # a special case for btcbox – default symbol is BTC/JPY
        if symbol is None:
            symbol = 'BTC/JPY'
        market = self.market(symbol)
        request = {
            'type': type,  # 'open' or 'all'
            'coin': market['baseId'],
        }
        response = self.privatePostTradeList(self.extend(request, params))
        orders = self.parse_orders(response, market, since, limit)
        # status(open/closed/canceled) is None
        # btcbox does not return status, but we know it's 'open' as we queried for open orders
        if type == 'open':
            for i in range(0, len(orders)):
                orders[i]['status'] = 'open'
        return orders

    def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_type('all', symbol, since, limit, params)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        return self.fetch_orders_by_type('open', symbol, since, limit, params)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        url = self.urls['api'] + '/' + self.version + '/' + path
        if api == 'public':
            if params:
                url += '?' + self.urlencode(params)
        else:
            self.check_required_credentials()
            nonce = str(self.nonce())
            query = self.extend({
                'key': self.apiKey,
                'nonce': nonce,
            }, params)
            request = self.urlencode(query)
            secret = self.hash(self.encode(self.secret))
            query['signature'] = self.hmac(self.encode(request), self.encode(secret))
            body = self.urlencode(query)
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # resort to defaultErrorHandler
        # typical error response: {"result":false,"code":"401"}
        if httpCode >= 400:
            return  # resort to defaultErrorHandler
        result = self.safe_value(response, 'result')
        if result is None or result is True:
            return  # either public API(no error codes expected) or success
        code = self.safe_value(response, 'code')
        feedback = self.id + ' ' + body
        self.throw_exactly_matched_exception(self.exceptions, code, feedback)
        raise ExchangeError(feedback)  # unknown message

    def request(self, path, api='public', method='GET', params={}, headers=None, body=None):
        response = self.fetch2(path, api, method, params, headers, body)
        if isinstance(response, basestring):
            # sometimes the exchange returns whitespace prepended to json
            response = self.strip(response)
            if not self.is_json_encoded_object(response):
                raise ExchangeError(self.id + ' ' + response)
            response = json.loads(response)
        return response
