from flask import Flask, render_template,request, url_for
import os
import platform
import socket

app = Flask(__name__)


@app.route("/")
def index_page():
    global startTime
    return "<html>" + \
           "<head><title>Docker + Flask Demo</title></head>" + \
           "<body>" + \
           "<table>" + \
           "<tr><td> Start Time </td> <td>" +  startTime + "</td> </tr>" \
           "<tr><td> Hostname </td> <td>" + utils.gethostname() + "</td> </tr>" \
           "<tr><td> Local Address </td> <td>" + utils.getlocaladdress() + "</td> </tr>" \
           "<tr><td> Remote Address </td> <td>" + request.remote_addr + "</td> </tr>" \
           "<tr><td> Server Hit </td> <td>" + str(hit.getServerHitCount()) + "</td> </tr>" \
           "</table>" + \
           "</body>" + \
           "</html>"

@app.route("/api/status")
def api_status():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    return {
       "host": hostname,
       "version": os.getenv("APISERVER_VERSION", "1.0"),
       "remote": request.remote_addr,
       "local": hostip
    }


if __name__ == "__main__":
        app.run(debug = True, host = '0.0.0.0')
