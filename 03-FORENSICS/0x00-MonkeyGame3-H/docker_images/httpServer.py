from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import threading
import binascii

hostName = "0.0.0.0"
serverPort = 8000
with open("_key.jpg", "rb") as f:
    content = f.read()
fileRead = binascii.hexlify(content)

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.headers.get('User-Agent'))
        if self.headers.get('User-Agent') == "c2V0X2NvdmVydE1zZ19tb2Rl":
            sample_dataset = {"id":"023", "properties":{"updates":"There are no updates for you at this time, agent. Use the secret to unlock 'it'.","currentLocation":"Monkey Island","currentConfirms":"12","burnerPhone":"(2133)-505-1000","secret":f"{fileRead}"}}
            self.wfile.write(json.dumps({"kind":"bigquery#datasetList","datasets":[sample_dataset]}).encode("utf-8"))
            print("Agent Found.")
        elif self.headers.get('User-Agent') == "c2V0X25ld3BsYXllcl9tb2Rl":
            self.wfile.write("Player registered.".encode("utf-8"))
            print("Player Registered.")
        elif self.headers.get('User-Agent') == "c2V0X2RlY2xpbmVkX21vZGU=":
            self.wfile.write("Player declined".encode("utf-8"))
            print("Player Declined.")
        else:
            self.wfile.write("Unexpected result logged.".encode("utf-8"))
            print("Unexpected Outcome.")
        
if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
        
    webServer.server_close()
    print("Goodbye!")