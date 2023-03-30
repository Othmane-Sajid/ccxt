import krakenRest from '../kraken.js';
import { Int } from '../base/types.js';
export default class kraken extends krakenRest {
    describe(): any;
    handleTicker(client: any, message: any, subscription: any): void;
    handleTrades(client: any, message: any, subscription: any): void;
    handleOHLCV(client: any, message: any, subscription: any): void;
    requestId(): any;
    watchPublic(name: any, symbol: any, params?: {}): Promise<any>;
    watchTicker(symbol: string, params?: {}): Promise<any>;
    watchTrades(symbol: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    watchOrderBook(symbol: string, limit?: Int, params?: {}): Promise<any>;
    watchOHLCV(symbol: string, timeframe?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    loadMarkets(reload?: boolean, params?: {}): Promise<import("../base/types.js").Dictionary<import("../base/types.js").Market>>;
    watchHeartbeat(params?: {}): Promise<any>;
    handleHeartbeat(client: any, message: any): void;
    handleOrderBook(client: any, message: any, subscription: any): void;
    formatNumber(n: any, length: any): string;
    handleDeltas(bookside: any, deltas: any, timestamp?: any): any;
    handleSystemStatus(client: any, message: any): any;
    authenticate(params?: {}): Promise<string>;
    watchPrivate(name: any, symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    watchMyTrades(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleMyTrades(client: any, message: any, subscription?: any): void;
    parseWsTrade(trade: any, market?: any): {
        id: string;
        order: string;
        info: any;
        timestamp: number;
        datetime: string;
        symbol: any;
        type: string;
        side: string;
        takerOrMaker: any;
        price: number;
        amount: number;
        cost: any;
        fee: any;
    };
    watchOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleOrders(client: any, message: any, subscription?: any): void;
    parseWsOrder(order: any, market?: any): any;
    handleSubscriptionStatus(client: any, message: any): void;
    handleErrorMessage(client: any, message: any): boolean;
    handleMessage(client: any, message: any): any;
}
