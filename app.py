"""
Flask Application - Backend API Server

OOP Principles Applied:
1. DEPENDENCY INJECTION - Chatbot instance is injected into routes
2. SEPARATION OF CONCERNS - Web layer separated from business logic
3. SINGLE RESPONSIBILITY - Each route handles one specific task

This file demonstrates how OOP classes are used in a web application context.
"""

import os
import threading
import time
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from chatbot import RegistrarChatbot

app = Flask(__name__, static_folder='.', static_url_path='')

CORS(app)

chatbot_instance = RegistrarChatbot()
chatbot_instance.load_faq_data()

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat requests from frontend

    OOP PRINCIPLE: DEPENDENCY INJECTION
    - Uses the chatbot_instance to process requests
    - Business logic is separated from web handling

    Returns:
        JSON response with chatbot answer
    """
    try:
        data = request.get_json()
        user_message = data.get('message', '')

        if not user_message:
            return jsonify({
                'response': 'Please provide a message.'
            }), 400

        response = chatbot_instance.get_response(user_message)

        return jsonify({
            'response': response
        }), 200

    except Exception as e:
        return jsonify({
            'response': 'An error occurred. Please try again.',
            'error': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint

    Returns:
        JSON response indicating server status
    """
    return jsonify({
        'status': 'healthy',
        'faq_count': chatbot_instance.get_faq_count()
    }), 200

@app.route('/', methods=['GET'])
def home():
    """
    Serve the chatbot interface (index.html)

    Returns:
        HTML response with the chatbot interface
    """
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>', methods=['GET'])
def serve_static(filename):
    """
    Serve static files (CSS, JS, etc.)

    Returns:
        Static file from current directory
    """
    return send_from_directory('.', filename)

def run_app():
    """Run the Flask app"""
    app.run(debug=False, port=5000, use_reloader=False, threaded=True)

if __name__ == '__main__':
    print("=" * 50)
    print("Registrar AI Chatbot Backend Server")
    print("=" * 50)
    print(f"FAQ Database loaded: {chatbot_instance.get_faq_count()} items")
    print("Server starting on http://localhost:5000")
    print("=" * 50)
    
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_app, daemon=True)
    flask_thread.start()
    
    # Wait for server to start
    time.sleep(2)
    
    # Open in pywebview desktop window
    try:
        import webview
        webview.create_window('Registrar AI Chatbot', 'http://localhost:5000')
        webview.start()
    except ImportError:
        print("pywebview not installed. Install with: pip install pywebview")
        print("Opening in browser instead...")
        import webbrowser
        webbrowser.open('http://localhost:5000')
        # Keep the server running
        flask_thread.join()