from flask import Flask, jsonify
import json
import os
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "http://localhost:5173"}})

# --- PATH CONFIGURATION ---
# Get the absolute path of the directory where app.py is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Join the base directory with the filename to create a reliable absolute path
DATA_FILE_PATH = os.path.join(BASE_DIR, 'get_table.json')

@app.route('/get_metadata', methods=['GET'])
def get_json_data():
    """Reads a JSON file using OS pathing and returns professional responses."""  
    
    # Check if file exists at the calculated path
    if not os.path.exists(DATA_FILE_PATH):
        return jsonify({
            "status": "error",
            "message": "Resource file not found on server.",
            "path_attempted": DATA_FILE_PATH  # Helpful for debugging
        }), 404

    try:
        with open(DATA_FILE_PATH, 'r') as file:
            data = json.load(file)

        return jsonify(data), 200

    except json.JSONDecodeError:
        return jsonify({
            "status": "error",
            "message": "The data file contains invalid JSON syntax."
        }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"An unexpected error occurred: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(debug=True)