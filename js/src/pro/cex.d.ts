import cexRest from '../cex.js';
import { Int } from '../base/types.js';
export default class cex extends cexRest {
    describe(): any;
    requestId(): any;
    watchBalance(params?: {}): Promise<any>;
    handleBalance(client: any, message: any): void;
    watchTrades(symbol: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleTradesSnapshot(client: any, message: any): void;
    parseWsOldTrade(trade: any, market?: any): import("../base/types.js").Trade;
    handleTrade(client: any, message: any): void;
    watchTicker(symbol: string, params?: {}): Promise<any>;
    watchTickers(symbols?: any, params?: {}): any;
    handleTicker(client: any, message: any): void;
    parseWsTicker(ticker: any, market?: any): import("../base/types.js").Ticker;
    watchOrders(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    watchMyTrades(symbol?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleTransaction(client: any, message: any): void;
    handleMyTrades(client: any, message: any): void;
    parseWsTrade(trade: any, market?: any): import("../base/types.js").Trade;
    handleOrderUpdate(client: any, message: any): void;
    parseWsOrderUpdate(order: any, market?: any): any;
    fromPrecision(amount: any, scale: any): string;
    currencyFromPrecision(currency: any, amount: any): string;
    handleOrdersSnapshot(client: any, message: any): void;
    watchOrderBook(symbol: string, limit?: Int, params?: {}): Promise<any>;
    handleOrderBookSnapshot(client: any, message: any): void;
    pairToSymbol(pair: any): string;
    handleOrderBookUpdate(client: any, message: any): void;
    handleDelta(bookside: any, delta: any): void;
    handleDeltas(bookside: any, deltas: any): void;
    watchOHLCV(symbol: string, timeframe?: string, since?: Int, limit?: Int, params?: {}): Promise<any>;
    handleInitOHLCV(client: any, message: any): void;
    handleOHLCV24(client: any, message: any): any;
    handleOHLCV1m(client: any, message: any): void;
    handleOHLCV(client: any, message: any): void;
    handleConnected(client: any, message: any): any;
    handleErrorMessage(client: any, message: any): void;
    handleMessage(client: any, message: any): any;
    handleAuthenticationMessage(client: any, message: any): void;
    authenticate(params?: {}): Promise<any>;
}
