from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    visitor_name = request.args.get('visitor_name', 'Visitor')
    client_ip = request.remote_addr

    # Here, we should use a real service to get the location and weather
    # For simplicity, let's hardcode these values
    location = "New York"
    temperature = 11

    response = {
        "client_ip": client_ip,
        "location": location,
        "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}"
    }

    return jsonify(response)

# Vercel requires the app to be a callable named "app"
app = app
