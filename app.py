from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure key

# Store points in memory (temporary)
points = 0

@app.route('/')
def index():
    return render_template('index.html', points=points)

@app.route('/tap')
def tap():
    global points
    points += 10  # Earn 10 points for tapping
    return jsonify(points=points)

if __name__ == '__main__':
    app.run(debug=True)
  
