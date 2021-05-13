import os
from pathlib import Path

from flask import Flask, request, render_template
from main import compute


app = Flask(__name__, instance_relative_config=True)
workingDirectory = str(Path().absolute())

@app.route("/")
def home():
    return """<nav>
  <ul>
    <li><a href=http://127.0.0.1:5000/ class=”chapter”>Home</a></li>
    <li>REST APIs</li>
    <ul>
    <li><a href=/nlp/Romania class=”chapter”>Romania</a></li>
  </ul>  
  </ul>
</nav>"""

@app.route('/nlp/<topic>', methods=['GET'])
def nlp(topic):
    result = ''
    if topic:
        result = compute(topic)
    return result


def webServers_Starting():
    print("Initialising Ngork Tunneling...")
    os.system('start cmd /k "' + workingDirectory + '\\ngrok.exe http 5000')

if __name__ == '__main__':
    print("Loading...")
    webServers_Starting()
    print("Web Servers & Tunneling Started")
    app.run(host='0.0.0.0')