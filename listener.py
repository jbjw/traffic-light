import websocket
import time
import json

def on_message(ws, message):
    print( 'tst' )
    print( message )
    # print( json.loads( message ) )

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    message = "i am a client"
    ws.send( json.dumps( message ) )
    # ws.close()

if __name__ == "__main__":
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
