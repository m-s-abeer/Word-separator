from flask import Flask as flask, render_template, request, send_from_directory, jsonify
import json
import query
import signal

app = flask(__name__,static_url_path='', static_folder='templates/')


@app.route('/query', methods=['POST'])
def queryAnalyzer():
    nlq = str(request.form['query'])
    print("Query: "+nlq)
    results=query.query(nlq)
    print("query done")
    # print(results)
    return json.dumps({'query': nlq, 'data': results})

@app.route('/shutdown', methods=['POST'])
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    print('Quitting! Bye!')       
    func()
    return 'Shut Down'

@app.route('/')
def home():
    return app.send_static_file('index.html')


app.run(port=2222)