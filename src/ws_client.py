import websocket
import json
from message_processor import process_message

class WebSocketClient:
    def on_message(self, ws, message):
        parsed_message = json.loads(message)
        process_message(parsed_message)

    def run(self):
        ws = websocket.WebSocketApp('ws://65.2.167.52:8080',
                                    on_message=self.on_message)
        ws.run_forever()