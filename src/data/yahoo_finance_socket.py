from websocket import WebSocketApp
import websocket
import json
import symbols

class YahooFinanceWebSocket:
    def __init__(self, symbols):
        self.symbols = symbols
        self.ws = WebSocketApp("wss://streamer.finance.yahoo.com/",
                                        on_message=self.on_message,
                                        on_error=self.on_error,
                                        on_close=self.on_close)
        self.ws.on_open = self.on_open

    def on_message(self, ws, message):
        print(f"Message: {message}")

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws):
        print("### Connection Closed ###")

    def on_open(self, ws):
        def run(*args):
            # Subscribe to multiple symbols
            ws.send(json.dumps({"subscribe": self.symbols}))
        return run
        
    def start(self):
        # verbose WebSocket details for debugging
        websocket.enableTrace(True)
        self.ws.run_forever()

if __name__ == "__main__":
    yahoo_finance_ws = YahooFinanceWebSocket(symbols)
    yahoo_finance_ws.start()
