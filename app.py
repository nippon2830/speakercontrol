from flask import Flask, request, jsonify, render_template
import os

# Mock GPIO class for development on non-Raspberry devices
class MockGPIO:
    OUT = 'OUT'
    IN = 'IN'
    HIGH = 1
    LOW = 0

    def __init__(self):
        self.pins = {}

    def setup(self, pin, mode):
        self.pins[pin] = {'mode': mode, 'state': MockGPIO.LOW}

    def output(self, pin, state):
        if pin in self.pins and self.pins[pin]['mode'] == MockGPIO.OUT:
            self.pins[pin]['state'] = state
        else:
            raise RuntimeError("Pin not set as output")

    def input(self, pin):
        if pin in self.pins:
            return self.pins[pin]['state']
        else:
            raise RuntimeError("Pin not configured")

    def cleanup(self):
        self.pins = {}

# Use MockGPIO for development
GPIO = MockGPIO()

# Initialize Flask application
app = Flask(__name__)
app.template_folder = os.path.join(os.path.dirname(__file__), 'templates')

# Configure GPIO pins (example setup)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gpio/<string:action>', methods=['GET', 'POST'])
def gpio_control(action):
    if request.method == 'GET':
        # Get the state of the pin
        try:
            state = GPIO.input(17)
            return jsonify({"action": action, "state": state})
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 400

    elif request.method == 'POST':
        # Set the state of the pin
        data = request.json
        state = data.get('state')
        if state not in [GPIO.HIGH, GPIO.LOW]:
            return jsonify({"error": "Invalid state"}), 400
        try:
            GPIO.output(pin, state)
            return jsonify({"pin": pin, "state": state})
        except RuntimeError as e:
            return jsonify({"error": str(e)}), 400

@app.route('/gpio/cleanup', methods=['POST'])
def gpio_cleanup():
    GPIO.cleanup()
    return jsonify({"message": "GPIO cleanup done"})

if __name__ == '__main__':
    app.run(debug=True)
