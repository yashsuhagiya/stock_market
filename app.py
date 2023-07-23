from flask import Flask, render_template, jsonify
import time

# Your existing code to fetch real-time stock data goes here
# (using the get_stock_data() function from previous versions)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_stock_data')
def fetch_stock_data():  # Renamed the route function to fetch_stock_data
    stock_data = get_stock_data()  # Your function to fetch real-time data
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(debug=True)