from  flask import Flask, request, jsonify
import requests
from flask_cors import CORS
import math
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/', methods=['GET'])
def home():
    return( "home")

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number."""

    num_str = str(n)
    if num_str.startswith('-'):
        num_str = num_str[1:]

    digits = list(map(int, num_str))
    power = len(digits)

    
    return ""if sum(d ** power for d in digits) == abs(n) else "-"



def get_fun_fact(n):
    """Fetch a fun fact about the number from Numbers API."""
    url = f"http://numbersapi.com/{n}/math?json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get("text", "No fun fact found.")
    except requests.RequestException:
        return "Fun fact not available."
    return "Fun fact not available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """API endpoint to classify a number based on its mathematical properties."""
    num = request.args.get('number')

    if not num :
        return jsonify({
    "number": "alphabet",
    "error": True
}), 400

    num = int(num)

    properties = []
    if is_armstrong(num):
        properties.append("armstrong")

    properties.append("even" if num % 2 == 0 else "odd")

    response_data = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum":sum(map(int, str(abs(num)))),
        "fun_fact": get_fun_fact(num)
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=False)