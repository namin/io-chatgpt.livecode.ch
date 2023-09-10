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
    if 'main' not in data:
        data['main'] = ''
    if 'pre' not in data:
        data['pre'] = ''
    if 'post' not in data:
        data['post'] = ''
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
    with open("./.well-known/ai-plugin.json") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    with open("openapi.yaml") as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

@app.get("/")
async def index():
    return quart.Response("""
<html>
<head>
<title>Exec io.livecode.ch</title>
</head>
<body>
<h1>Exec <a href="https://io.livecode.ch">io.livecode.ch</a></h1>

<blockquote>
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</blockquote>

</body>
</html>

""", mimetype="text/html")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
