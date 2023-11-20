import json

import quart
import quart_cors
from quart import request

import requests

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

@app.post("/run/<string:user>/<string:repo>")
async def run(user, repo):
    request = await quart.request.get_json(force=True)
    data = {}
    for k in request.keys():
        data[k] = request[k]
    for k in ['main', 'pre', 'post']:
        if k not in data:
            data[k] = ''
    r = requests.post(f"https://io.livecode.ch/api/run/{user}/{repo}", data = data)
    text = r.text
    if text.startswith('installation error'):
        text = "The repository is not a valid io.livecode.ch repository. Ask the user for one."
    text = json.dumps({'result': text})
    return quart.Response(response=text, mimetype="text/json", status=200)
    
@app.get("/logo.png")
async def plugin_logo():
    filename = 'logo.png'
    return await quart.send_file(filename, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    s = '' if host == 'localhost' else 's'
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        text = text.replace("PLUGIN_HOSTNAME", f"http{s}://{host}")
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    s = '' if host == 'localhost' else 's'
    with open("openapi.yaml") as f:
        text = f.read()
        text = text.replace("PLUGIN_HOSTNAME", f"http{s}://{host}")
        return quart.Response(text, mimetype="text/yaml")

@app.get("/")
async def index():
    with open("index.html") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/html")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
