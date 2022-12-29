# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import BadRequest
from ccxt.base.errors import BadSymbol
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import NotSupported
from ccxt.base.decimal_to_precision import TICK_SIZE


class alpaca(Exchange):

    def describe(self):
        return self.deep_extend(super(alpaca, self).describe(), {
            'id': 'alpaca',
            'name': 'Alpaca',
            'countries': ['US'],
            'rateLimit': 333,  # 3 req per second
            'hostname': 'alpaca.markets',
            'pro': True,
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/187234005-b864db3d-f1e3-447a-aaf9-a9fc7b955d07.jpg',
                'www': 'https://alpaca.markets',
                'api': {
                    'public': 'https://api.{hostname}/{version}',
                    'private': 'https://api.{hostname}/{version}',
                    'cryptoPublic': 'https://data.{hostname}/{version}',
                    'markets': 'https://api.{hostname}/{version}',
                },
                'test': {
                    'public': 'https://paper-api.{hostname}/{version}',
                    'private': 'https://paper-api.{hostname}/{version}',
                    'cryptoPublic': 'https://data.{hostname}/{version}',
                    'markets': 'https://api.{hostname}/{version}',
                },
                'doc': 'https://alpaca.markets/docs/',
                'fees': 'https://alpaca.markets/support/what-are-the-fees-associated-with-crypto-trading/',
            },
            'has': {
                'CORS': False,
                'spot': True,
                'margin': False,
                'swap': False,
                'future': False,
                'option': False,
                'cancelAllOrders': True,
                'cancelOrder': True,
                'createOrder': True,
                'fetchBalance': True,
                'fetchBidsAsks': False,
                'fetchClosedOrders': False,
                'fetchCurrencies': False,
                'fetchDepositAddress': False,
                'fetchDepositAddressesByNetwork': False,
                'fetchDeposits': False,
                'fetchFundingHistory': False,
                'fetchFundingRate': False,
                'fetchFundingRates': False,
                'fetchL1OrderBook': True,
                'fetchL2OrderBook': False,
                'fetchMarkets': True,
                'fetchMyTrades': False,
                'fetchOHLCV': True,
                'fetchOpenOrder': False,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrders': False,
                'fetchPositions': False,
                'fetchStatus': False,
                'fetchTicker': False,
                'fetchTickers': False,
                'fetchTime': False,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'fetchTransactionFees': False,
                'fetchTransactions': False,
                'fetchTransfers': False,
                'fetchWithdrawals': False,
                'setLeverage': False,
                'setMarginMode': False,
                'transfer': False,
                'withdraw': False,
            },
            'api': {
                'markets': {
                    'get': [
                        'assets/public/beta',
                    ],
                },
                'private': {
                    'get': [
                        'account',
                        'orders',
                        'orders/{order_id}',
                        'positions',
                        'positions/{symbol}',
                        'account/activities/{activity_type}',
                    ],
                    'post': [
                        'orders',
                    ],
                    'delete': [
                        'orders',
                        'orders/{order_id}',
                    ],
                },
                'cryptoPublic': {
                    'get': [
                        'crypto/latest/orderbooks',
                        'crypto/trades',
                        'crypto/quotes',
                        'crypto/latest/quotes',
                        'crypto/bars',
                        'crypto/snapshots',
                    ],
                },
            },
            'timeframes': {
                '1m': '1min',
                '3m': '3min',
                '5m': '5min',
                '15m': '15min',
                '30m': '30min',
                '1h': '1H',
                '2h': '2H',
                '4h': '4H',
                '6h': '6H',
                '8h': '8H',
                '12h': '12H',
                '1d': '1D',
                '3d': '3D',
                '1w': '1W',
                '1M': '1M',
            },
            'precisionMode': TICK_SIZE,
            'requiredCredentials': {
                'apiKey': True,
                'secret': True,
            },
            'fees': {
                'trading': {
                    'tierBased': True,
                    'percentage': True,
                    'maker': self.parse_number('0.003'),
                    'taker': self.parse_number('0.003'),
                    'tiers': {
                        'taker': [
                            [self.parse_number('0'), self.parse_number('0.003')],
                            [self.parse_number('500000'), self.parse_number('0.0028')],
                            [self.parse_number('1000000'), self.parse_number('0.0025')],
                            [self.parse_number('5000000'), self.parse_number('0.002')],
                            [self.parse_number('10000000'), self.parse_number('0.0018')],
                            [self.parse_number('25000000'), self.parse_number('0.0015')],
                            [self.parse_number('50000000'), self.parse_number('0.00125')],
                            [self.parse_number('100000000'), self.parse_number('0.001')],
                        ],
                        'maker': [
                            [self.parse_number('0'), self.parse_number('0.003')],
                            [self.parse_number('500000'), self.parse_number('0.0028')],
                            [self.parse_number('1000000'), self.parse_number('0.0025')],
                            [self.parse_number('5000000'), self.parse_number('0.002')],
                            [self.parse_number('10000000'), self.parse_number('0.0018')],
                            [self.parse_number('25000000'), self.parse_number('0.0015')],
                            [self.parse_number('50000000'), self.parse_number('0.00125')],
                            [self.parse_number('100000000'), self.parse_number('0.001')],
                        ],
                    },
                },
            },
            'headers': {
                'APCA-PARTNER-ID': 'ccxt',
            },
            'options': {
                'fetchTradesMethod': 'cryptoPublicGetCryptoTrades',  # or cryptoPublicGetCryptoLatestTrades
                'fetchOHLCVMethod': 'cryptoPublicGetCryptoBars',  # or cryptoPublicGetCryptoLatestBars
                'versions': {
                    'public': 'v2',
                    'private': 'v2',
                    'cryptoPublic': 'v1beta2',  # crypto beta
                    'markets': 'v2',  # crypto beta
                },
                'defaultExchange': 'CBSE',
                'exchanges': [
                    'CBSE',  # Coinbase
                    'FTX',  # FTXUS
                    'GNSS',  # Genesis
                    'ERSX',  # ErisX
                ],
                'defaultTimeInForce': 'gtc',  # fok, gtc, ioc
                'clientOrderId': 'ccxt_{id}',
            },
            'exceptions': {
                'exact': {
                    'forbidden.': PermissionDenied,  # {"message": "forbidden."}
                    '40410000': InvalidOrder,  # {"code": 40410000, "message": "order is not found."}
                    '40010001': BadRequest,  # {"code":40010001,"message":"invalid order type for crypto order"}
                    '40110000': PermissionDenied,  # {"code": 40110000, "message": "request is not authorized"}
                    '40310000': InsufficientFunds,  # {"available":"0","balance":"0","code":40310000,"message":"insufficient balance for USDT(requested: 221.63, available: 0)","symbol":"USDT"}
                },
                'broad': {
                    'Invalid format for parameter': BadRequest,  # {"message":"Invalid format for parameter start: error parsing '0' as RFC3339 or 2006-01-02 time: parsing time \"0\" as \"2006-01-02\": cannot parse \"0\" as \"2006\""}
                    'Invalid symbol': BadSymbol,  # {"message":"Invalid symbol(s): BTC/USDdsda does not match ^[A-Z]+/[A-Z]+$"}
                },
            },
        })

    def fetch_markets(self, params={}):
        """
        retrieves data on all markets for alpaca
        :param dict params: extra parameters specific to the exchange api endpoint
        :returns [dict]: an array of objects representing market data
        """
        request = {
            'asset_class': 'crypto',
            'tradeable': True,
        }
        assets = self.marketsGetAssetsPublicBeta(self.extend(request, params))
        #
        #    [
        #        {
        #           "id":"a3ba8ac0-166d-460b-b17a-1f035622dd47",
        #           "class":"crypto",
        #           "exchange":"FTXU",
        #           "symbol":"DOGEUSD",
        #           "name":"Dogecoin",
        #           "status":"active",
        #           "tradable":true,
        #           "marginable":false,
        #           "shortable":false,
        #           "easy_to_borrow":false,
        #           "fractionable":true,
        #           "min_order_size":"1",
        #           "min_trade_increment":"1",
        #           "price_increment":"0.0000005"
        #        }
        #    ]
        #
        markets = []
        for i in range(0, len(assets)):
            asset = assets[i]
            marketId = self.safe_string(asset, 'symbol')
            parts = marketId.split('/')
            baseId = self.safe_string(parts, 0)
            quoteId = self.safe_string(parts, 1)
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            status = self.safe_string(asset, 'status')
            active = (status == 'active')
            minAmount = self.safe_number(asset, 'min_order_size')
            amount = self.safe_number(asset, 'min_trade_increment')
            price = self.safe_number(asset, 'price_increment')
            markets.append({
                'id': marketId,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'settle': None,
                'baseId': baseId,
                'quoteId': quoteId,
                'settleId': None,
                'type': 'spot',
                'spot': True,
                'margin': None,
                'swap': False,
                'future': False,
                'option': False,
                'active': active,
                'contract': False,
                'linear': None,
                'inverse': None,
                'contractSize': None,
                'expiry': None,
                'expiryDatetime': None,
                'strike': None,
                'optionType': None,
                'precision': {
                    'amount': amount,
                    'price': price,
                },
                'limits': {
                    'leverage': {
                        'min': None,
                        'max': None,
                    },
                    'amount': {
                        'min': minAmount,
                        'max': None,
                    },
                    'price': {
                        'min': None,
                        'max': None,
                    },
                    'cost': {
                        'min': None,
                        'max': None,
                    },
                },
                'info': asset,
            })
        return markets

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        """
        get the list of most recent trades for a particular symbol
        :param str symbol: unified symbol of the market to fetch trades for
        :param int|None since: timestamp in ms of the earliest trade to fetch
        :param int|None limit: the maximum amount of trades to fetch
        :param dict params: extra parameters specific to the alpaca api endpoint
        :returns [dict]: a list of `trade structures <https://docs.ccxt.com/en/latest/manual.html?#public-trades>`
        """
        self.load_markets()
        market = self.market(symbol)
        id = market['id']
        request = {
            'symbols': id,
        }
        if since is not None:
            request['start'] = self.iso8601(since)
        if limit is not None:
            request['limit'] = int(limit)
        method = self.safe_string(self.options, 'fetchTradesMethod', 'cryptoPublicGetCryptoTrades')
        response = getattr(self, method)(self.extend(request, params))
        #
        # {
        #     "next_page_token":null,
        #     "trades":{
        #        "BTC/USD":[
        #           {
        #              "i":36440704,
        #              "p":22625,
        #              "s":0.0001,
        #              "t":"2022-07-21T11:47:31.073391Z",
        #              "tks":"B"
        #           }
        #        ]
        #     }
        # }
        #
        trades = self.safe_value(response, 'trades', {})
        symbolTrades = self.safe_value(trades, market['id'], {})
        return self.parse_trades(symbolTrades, market, since, limit)

    def fetch_order_book(self, symbol, limit=None, params={}):
        """
        fetches information on open orders with bid(buy) and ask(sell) prices, volumes and other data
        :param str symbol: unified symbol of the market to fetch the order book for
        :param int|None limit: the maximum amount of order book entries to return
        :param dict params: extra parameters specific to the alpaca api endpoint
        :returns dict: A dictionary of `order book structures <https://docs.ccxt.com/en/latest/manual.html#order-book-structure>` indexed by market symbols
        """
        self.load_markets()
        market = self.market(symbol)
        id = market['id']
        request = {
            'symbols': id,
        }
        response = self.cryptoPublicGetCryptoLatestOrderbooks(self.extend(request, params))
        #
        #   {
        #       "orderbooks":{
        #          "BTC/USD":{
        #             "a":[
        #                {
        #                   "p":22208,
        #                   "s":0.0051
        #                },
        #                {
        #                   "p":22209,
        #                   "s":0.1123
        #                },
        #                {
        #                   "p":22210,
        #                   "s":0.2465
        #                }
        #             ],
        #             "b":[
        #                {
        #                   "p":22203,
        #                   "s":0.395
        #                },
        #                {
        #                   "p":22202,
        #                   "s":0.2465
        #                },
        #                {
        #                   "p":22201,
        #                   "s":0.6455
        #                }
        #             ],
        #             "t":"2022-07-19T13:41:55.13210112Z"
        #          }
        #       }
        #   }
        #
        orderbooks = self.safe_value(response, 'orderbooks', {})
        rawOrderbook = self.safe_value(orderbooks, id, {})
        timestamp = self.parse8601(self.safe_string(rawOrderbook, 't'))
        return self.parse_order_book(rawOrderbook, market['symbol'], timestamp, 'b', 'a', 'p', 's')

    def fetch_ohlcv(self, symbol, timeframe='1m', since=None, limit=None, params={}):
        """
        fetches historical candlestick data containing the open, high, low, and close price, and the volume of a market
        :param str symbol: unified symbol of the market to fetch OHLCV data for
        :param str timeframe: the length of time each candle represents
        :param int|None since: timestamp in ms of the earliest candle to fetch
        :param int|None limit: the maximum amount of candles to fetch
        :param dict params: extra parameters specific to the alpha api endpoint
        :returns [[int]]: A list of candles ordered as timestamp, open, high, low, close, volume
        """
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbols': market['id'],
            'timeframe': self.timeframes[timeframe],
        }
        if limit is not None:
            request['limit'] = limit
        if since is not None:
            request['start'] = self.yyyymmdd(since)
        method = self.safe_string(self.options, 'fetchOHLCVMethod', 'cryptoPublicGetCryptoBars')
        response = getattr(self, method)(self.extend(request, params))
        #
        #    {
        #        "bars":{
        #           "BTC/USD":[
        #              {
        #                 "c":22887,
        #                 "h":22888,
        #                 "l":22873,
        #                 "n":11,
        #                 "o":22883,
        #                 "t":"2022-07-21T05:00:00Z",
        #                 "v":1.1138,
        #                 "vw":22883.0155324116
        #              },
        #              {
        #                 "c":22895,
        #                 "h":22895,
        #                 "l":22884,
        #                 "n":6,
        #                 "o":22884,
        #                 "t":"2022-07-21T05:01:00Z",
        #                 "v":0.001,
        #                 "vw":22889.5
        #              }
        #           ]
        #        },
        #        "next_page_token":"QlRDL1VTRHxNfDIwMjItMDctMjFUMDU6MDE6MDAuMDAwMDAwMDAwWg=="
        #     }
        #
        bars = self.safe_value(response, 'bars', {})
        ohlcvs = self.safe_value(bars, market['id'], {})
        return self.parse_ohlcvs(ohlcvs, market, timeframe, since, limit)

    def parse_ohlcv(self, ohlcv, market=None):
        #
        #     {
        #        "c":22895,
        #        "h":22895,
        #        "l":22884,
        #        "n":6,
        #        "o":22884,
        #        "t":"2022-07-21T05:01:00Z",
        #        "v":0.001,
        #        "vw":22889.5
        #     }
        #
        datetime = self.safe_string(ohlcv, 't')
        timestamp = self.parse8601(datetime)
        return [
            timestamp,  # timestamp
            self.safe_number(ohlcv, 'o'),  # open
            self.safe_number(ohlcv, 'h'),  # high
            self.safe_number(ohlcv, 'l'),  # low
            self.safe_number(ohlcv, 'c'),  # close
            self.safe_number(ohlcv, 'v'),  # volume
        ]

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        """
        create a trade order
        :param str symbol: unified symbol of the market to create an order in
        :param str type: 'market', 'limit' or 'stop_limit'
        :param str side: 'buy' or 'sell'
        :param float amount: how much of currency you want to trade in units of base currency
        :param float price: the price at which the order is to be fullfilled, in units of the quote currency, ignored in market orders
        :param dict params: extra parameters specific to the alpaca api endpoint
        :param float params['triggerPrice']: The price at which a trigger order is triggered at
        :returns dict: an `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        self.load_markets()
        market = self.market(symbol)
        id = market['id']
        request = {
            'symbol': id,
            'qty': self.amount_to_precision(symbol, amount),
            'side': side,
            'type': type,  # market, limit, stop_limit
        }
        triggerPrice = self.safe_string_n(params, ['triggerPrice', 'stop_price'])
        if triggerPrice is not None:
            newType = None
            if type.find('limit') >= 0:
                newType = 'stop_limit'
            else:
                raise NotSupported(self.id + ' createOrder() does not support stop orders for ' + type + ' orders, only stop_limit orders are supported')
            request['stop_price'] = self.price_to_precision(symbol, triggerPrice)
            request['type'] = newType
        if type.find('limit') >= 0:
            request['limit_price'] = self.price_to_precision(symbol, price)
        defaultTIF = self.safe_string(self.options, 'defaultTimeInForce')
        request['time_in_force'] = self.safe_string(params, 'timeInForce', defaultTIF)
        params = self.omit(params, ['timeInForce', 'triggerPrice'])
        clientOrderIdprefix = self.safe_string(self.options, 'clientOrderId')
        uuid = self.uuid()
        parts = uuid.split('-')
        random_id = ''.join(parts)
        defaultClientId = self.implode_params(clientOrderIdprefix, {'id': random_id})
        clientOrderId = self.safe_string(params, 'clientOrderId', defaultClientId)
        request['client_order_id'] = clientOrderId
        params = self.omit(params, ['clientOrderId'])
        order = self.privatePostOrders(self.extend(request, params))
        #
        #   {
        #      "id": "61e69015-8549-4bfd-b9c3-01e75843f47d",
        #      "client_order_id": "eb9e2aaa-f71a-4f51-b5b4-52a6c565dad4",
        #      "created_at": "2021-03-16T18:38:01.942282Z",
        #      "updated_at": "2021-03-16T18:38:01.942282Z",
        #      "submitted_at": "2021-03-16T18:38:01.937734Z",
        #      "filled_at": null,
        #      "expired_at": null,
        #      "canceled_at": null,
        #      "failed_at": null,
        #      "replaced_at": null,
        #      "replaced_by": null,
        #      "replaces": null,
        #      "asset_id": "b0b6dd9d-8b9b-48a9-ba46-b9d54906e415",
        #      "symbol": "AAPL",
        #      "asset_class": "us_equity",
        #      "notional": "500",
        #      "qty": null,
        #      "filled_qty": "0",
        #      "filled_avg_price": null,
        #      "order_class": "",
        #      "order_type": "market",
        #      "type": "market",
        #      "side": "buy",
        #      "time_in_force": "day",
        #      "limit_price": null,
        #      "stop_price": null,
        #      "status": "accepted",
        #      "extended_hours": False,
        #      "legs": null,
        #      "trail_percent": null,
        #      "trail_price": null,
        #      "hwm": null
        #   }
        #
        return self.parse_order(order, market)

    def cancel_order(self, id, symbol=None, params={}):
        """
        cancels an open order
        :param str id: order id
        :param str|None symbol: unified symbol of the market the order was made in
        :param dict params: extra parameters specific to the alpaca api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        request = {
            'order_id': id,
        }
        response = self.privateDeleteOrdersOrderId(self.extend(request, params))
        #
        #   {
        #       "code": 40410000,
        #       "message": "order is not found."
        #   }
        #
        return self.safe_value(response, 'message', {})

    def fetch_order(self, id, symbol=None, params={}):
        """
        fetches information on an order made by the user
        :param str|None symbol: unified symbol of the market the order was made in
        :param dict params: extra parameters specific to the alpaca api endpoint
        :returns dict: An `order structure <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        self.load_markets()
        request = {
            'order_id': id,
        }
        order = self.privateGetOrdersOrderId(self.extend(request, params))
        marketId = self.safe_string(order, 'symbol')
        market = self.safe_market(marketId)
        return self.parse_order(order, market)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        """
        fetch all unfilled currently open orders
        :param str|None symbol: unified market symbol
        :param int|None since: the earliest time in ms to fetch open orders for
        :param int|None limit: the maximum number of  open orders structures to retrieve
        :param dict params: extra parameters specific to the alpaca api endpoint
        :returns [dict]: a list of `order structures <https://docs.ccxt.com/en/latest/manual.html#order-structure>`
        """
        self.load_markets()
        market = None
        if symbol is not None:
            market = self.market(symbol)
        orders = self.privateGetOrders(params)
        return self.parse_orders(orders, market, since, limit)

    def parse_order(self, order, market=None):
        #
        #    {
        #        "id":"6ecfcc34-4bed-4b53-83ba-c564aa832a81",
        #        "client_order_id":"ccxt_1c6ceab0b5e84727b2f1c0394ba17560",
        #        "created_at":"2022-06-14T13:59:30.224037068Z",
        #        "updated_at":"2022-06-14T13:59:30.224037068Z",
        #        "submitted_at":"2022-06-14T13:59:30.221856828Z",
        #        "filled_at":null,
        #        "expired_at":null,
        #        "canceled_at":null,
        #        "failed_at":null,
        #        "replaced_at":null,
        #        "replaced_by":null,
        #        "replaces":null,
        #        "asset_id":"64bbff51-59d6-4b3c-9351-13ad85e3c752",
        #        "symbol":"BTCUSD",
        #        "asset_class":"crypto",
        #        "notional":null,
        #        "qty":"0.01",
        #        "filled_qty":"0",
        #        "filled_avg_price":null,
        #        "order_class":"",
        #        "order_type":"limit",
        #        "type":"limit",
        #        "side":"buy",
        #        "time_in_force":"day",
        #        "limit_price":"14000",
        #        "stop_price":null,
        #        "status":"accepted",
        #        "extended_hours":false,
        #        "legs":null,
        #        "trail_percent":null,
        #        "trail_price":null,
        #        "hwm":null,
        #        "commission":"0.42",
        #        "source":null
        #    }
        #
        marketId = self.safe_string(order, 'symbol')
        market = self.safe_market(marketId, market)
        symbol = market['symbol']
        alpacaStatus = self.safe_string(order, 'status')
        status = self.parse_order_status(alpacaStatus)
        feeValue = self.safe_string(order, 'commission')
        fee = None
        if feeValue is not None:
            fee = {
                'cost': feeValue,
                'currency': 'USD',
            }
        orderType = self.safe_string(order, 'order_type')
        if orderType.find('limit') >= 0:
            # might be limit or stop-limit
            orderType = 'limit'
        datetime = self.safe_string(order, 'submitted_at')
        timestamp = self.parse8601(datetime)
        return self.safe_order({
            'id': self.safe_string(order, 'id'),
            'clientOrderId': self.safe_string(order, 'client_order_id'),
            'timestamp': timestamp,
            'datetime': datetime,
            'lastTradeTimeStamp': None,
            'status': status,
            'symbol': symbol,
            'type': orderType,
            'timeInForce': self.parse_time_in_force(self.safe_string(order, 'time_in_force')),
            'postOnly': None,
            'side': self.safe_string(order, 'side'),
            'price': self.safe_number(order, 'limit_price'),
            'stopPrice': self.safe_number(order, 'stop_price'),
            'cost': None,
            'average': self.safe_number(order, 'filled_avg_price'),
            'amount': self.safe_number(order, 'qty'),
            'filled': self.safe_number(order, 'filled_qty'),
            'remaining': None,
            'trades': None,
            'fee': fee,
            'info': order,
        }, market)

    def parse_order_status(self, status):
        statuses = {
            'pending_new': 'open',
            'accepted': 'open',
            'new': 'open',
            'partially_filled': 'open',
            'activated': 'open',
            'filled': 'closed',
        }
        return self.safe_string(statuses, status, status)

    def parse_time_in_force(self, timeInForce):
        timeInForces = {
            'day': 'Day',
        }
        return self.safe_string(timeInForces, timeInForce, timeInForce)

    def parse_trade(self, trade, market=None):
        #
        #   {
        #       "t":"2022-06-14T05:00:00.027869Z",
        #       "x":"CBSE",
        #       "p":"21942.15",
        #       "s":"0.0001",
        #       "tks":"S",
        #       "i":"355681339"
        #   }
        #
        marketId = self.safe_string(trade, 'S')
        symbol = self.safe_symbol(marketId, market)
        datetime = self.safe_string(trade, 't')
        timestamp = self.parse8601(datetime)
        alpacaSide = self.safe_string(trade, 'tks')
        side = None
        if alpacaSide == 'B':
            side = 'buy'
        elif alpacaSide == 'S':
            side = 'sell'
        priceString = self.safe_string(trade, 'p')
        amountString = self.safe_string(trade, 's')
        return self.safe_trade({
            'info': trade,
            'id': self.safe_string(trade, 'i'),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'order': None,
            'type': None,
            'side': side,
            'takerOrMaker': 'taker',
            'price': priceString,
            'amount': amountString,
            'cost': None,
            'fee': None,
        }, market)

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        versions = self.safe_value(self.options, 'versions')
        version = self.safe_string(versions, api)
        endpoint = '/' + self.implode_params(path, params)
        url = self.implode_params(self.urls['api'][api], {'version': version})
        url = self.implode_hostname(url)
        headers = headers if (headers is not None) else {}
        if api == 'private':
            headers['APCA-API-KEY-ID'] = self.apiKey
            headers['APCA-API-SECRET-KEY'] = self.secret
        query = self.omit(params, self.extract_params(path))
        if query:
            if (method == 'GET') or (method == 'DELETE'):
                endpoint += '?' + self.urlencode(query)
            else:
                body = self.json(query)
                headers['Content-Type'] = 'application/json'
        url = url + endpoint
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return  # default error handler
        # {
        #     "code": 40110000,
        #     "message": "request is not authorized"
        # }
        feedback = self.id + ' ' + body
        errorCode = self.safe_string(response, 'code')
        if code is not None:
            self.throw_exactly_matched_exception(self.exceptions['exact'], errorCode, feedback)
        message = self.safe_value(response, 'message', None)
        if message is not None:
            self.throw_exactly_matched_exception(self.exceptions['exact'], message, feedback)
            self.throw_broadly_matched_exception(self.exceptions['broad'], message, feedback)
            raise ExchangeError(feedback)
