import bitvavoRest from '../bitvavo.js';
import { Int } from '../base/types.js';
export default class bitvavo extends bitvavoRest {
    describe(): any;
    watchPublic(name: any, symbol: any, params?: {}): Promise<any>;
    watchTicker(symbol: string, params?: {}): Promise<any>;
    handleTicker(client: any, message: any): any;
    watchTrades(symbol: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleTrade(client: any, message: any): void;
    watchOHLCV(symbol: string, timeframe?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleOHLCV(client: any, message: any): void;
    watchOrderBook(symbol: string, limit?: Int, params?: {}): Promise<any>;
    handleDelta(bookside: any, delta: any): void;
    handleDeltas(bookside: any, deltas: any): void;
    handleOrderBookMessage(client: any, message: any, orderbook: any): any;
    handleOrderBook(client: any, message: any): void;
    watchOrderBookSnapshot(client: any, message: any, subscription: any): Promise<any>;
    handleOrderBookSnapshot(client: any, message: any): any;
    handleOrderBookSubscription(client: any, message: any, subscription: any): void;
    handleOrderBookSubscriptions(client: any, message: any, marketIds: any): void;
    watchOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    watchMyTrades(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleOrder(client: any, message: any): void;
    handleMyTrade(client: any, message: any): void;
    handleSubscriptionStatus(client: any, message: any): any;
    authenticate(params?: {}): any;
    handleAuthenticationMessage(client: any, message: any): void;
    handleMessage(client: any, message: any): any;
}
