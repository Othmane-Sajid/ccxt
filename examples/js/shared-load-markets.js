const ccxt = require ('../../ccxt')

// ----------------------------------------------------------------------------
// an example of how to load markets for each exchange just once
// in order to save memory and time for initializing multiple exchange instances
// see https://github.com/ccxt/ccxt/issues/7312 for details
// ----------------------------------------------------------------------------

const globalIds = [ 'binance', 'poloniex', 'bittrex', 'bitstamp' ]
const globalExchanges = {}

async function loadExchange (id) {
    try {
        const exchange = new ccxt[id] ({
            'enableRateLimit': true,
        })
        await exchange.loadMarkets ()
        globalExchanges[id] = exchange
    } catch (e) {
        // throw e // uncomment to break the entire program on any error
        // console.log (e) // print the exception and ignore this exchange
    }
}

async function main () {

    // initialize unique global exchange instances first
    await Promise.all (globalIds.map (async (id) => loadExchange (id)))
    console.log ('Loaded global exchanges:', Object.keys (globalExchanges))

    // load user exchanges and keys from a database or configure these via json
    const users = {
        'user1': {
            'binance': { 'apiKey': 'USER1_BINANCE_API_KEY', 'secret': 'USER1_BINANCE_SECRET' },
            'poloniex': { 'apiKey': 'USER1_POLONIEX_API_KEY', 'secret': 'USER1_POLONIEX_SECRET' }
        },
        'user2': {
            'poloniex': { 'apiKey': 'USER2_POLONIEX_API_KEY', 'secret': 'USER2_POLONIEX_SECRET' },
            'bittrex': { 'apiKey': 'USER2_BITTREX_API_KEY', 'secret': 'USER2_BITTREX_SECRET' }
        },
        'user3': {
            'bittrex': { 'apiKey': 'USER2_BITTREX_API_KEY', 'secret': 'USER2_BITTREX_SECRET' },
            'bitstamp': { 'apiKey': 'USER2_BITSTAMP_API_KEY', 'secret': 'USER2_BITSTAMP_SECRET' }
        }
    }

    // initialize local exchanges per user
    const localExchanges = {}
    for (const userId in users) {
        const userExchanges = {}
        for (const exchangeId in users[userId]) {
            if (exchangeId in globalExchanges) {
                const globalExchange = globalExchanges[exchangeId]
                const exchange = new ccxt[exchangeId] ({
                    'enableRateLimit': true,
                    'verbose': true,
                    ... users[userId][exchangeId],
                });
                [
                    'ids',
                    'markets',
                    'markets_by_id',
                    'marketsById',
                    'currencies',
                    'currencies_by_id',
                    'baseCurrencies',
                    'quoteCurrencies',
                    'symbols',
                ].forEach ((propertyName) => {
                    exchange[propertyName] = globalExchange[propertyName]
                })
                userExchanges[exchangeId] = exchange
            }
        }
        localExchanges[userId] = userExchanges
    }

    // print the loaded exchanges per user
    for (const userId in localExchanges) {
        console.log ('Loaded', userId, Object.keys (localExchanges[userId]))
    }
}

main ()
