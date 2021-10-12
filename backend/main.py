from flask import Flask, request, jsonify, g, send_file, Response, make_response

app = Flask(name)

# rotas and shiieeeet

if name == "main":
    app.debug = os.getenv("DEBUG", False)
    app.run(host='0.0.0.0')
