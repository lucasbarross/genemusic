from .models.history import History
from http.server import BaseHTTPRequestHandler, HTTPServer
from .config import SCALES

import json
import time

hostName = "localhost"
hostPort = 3000

class MyServer(BaseHTTPRequestHandler):
    def parse_qs(self, qs):
        args = qs[1:]
        args = args.split("&")

        qs = {}

        for key_value in args:
            print(key_value)
            key, value = key_value.split("=")
            
            if value:
                qs[key] = value
            else:
                qs[key] = ""

        return qs
    
    def set_headers(self):
        self.send_header("Content-type", "application/json")
        self.end_headers()

    def do_GET(self):
        res = { "success": "true" }

        try: 
            read = self.path.split("/")
            
            if read[1] == "run":
                params = self.parse_qs(read[len(read)-1])
                
                pop = int(params["pop"])
                max_gen = int(params["max_gen"])
                scale = params["scale"]

                if pop and max_gen and scale:

                    if pop > 300 or max_gen > 300 or scale not in SCALES:
                        raise ValueError("Numbers too high or invalid scale")
                    else:
                        history = History(pop, max_gen, scale)
                        bestOfEachGen = history.run()
                        res["result"] = bestOfEachGen
                else:
                    raise ValueError("Population or Max generations or Scale params are missing")

            self.send_response(200)
            self.set_headers()
            json_string = json.dumps(res)
            self.wfile.write(json_string.encode(encoding='utf_8'))
        except ValueError as e:
            print(e)
            self.send_error(400, str(e))
        except Exception as e:
            print(e)
            self.send_error(500, str(e))

if __name__ == "__main__":
    # import sys
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass
    # run(sys.argv[1])

    