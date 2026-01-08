from flask import Flask, render_template, request, jsonify
from color_sorter import ColorSorter
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sort', methods=['POST'])
def sort_api():
    try:
        data = request.get_json()
        
        # Extract inputs
        try:
            n = int(data.get('n'))
        except (ValueError, TypeError):
            return jsonify({'success': False, 'result': 'Invalid number of elements'})

        colors_input = data.get('colors', '')
        
        # Mimic the split() behavior from the original code
        # input(...).split() handles multiple spaces automatically
        inputs_list = colors_input.strip().split()

        # Call the class
        sorter = ColorSorter()
        result = sorter.sort(n, inputs_list)

        return jsonify({'success': True, 'result': result})

    except Exception as e:
        return jsonify({'success': False, 'result': f"Server Error: {str(e)}"})

if __name__ == '__main__':
    # Run the app
    # access at http://127.0.0.1:5000
    app.run(debug=True, port=5000)