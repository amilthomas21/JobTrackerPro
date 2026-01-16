"""
JobTrackerPro - Main Application File
A web application to track and manage job applications
Author: Amil Thomas
"""

from flask import Flask, render_template

# Create Flask application
app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    """
    Homepage - Welcome screen
    """
    return """
    <html>
        <head>
            <title>JobTrackerPro</title>
            <style>
                body {
                    font-family: times new roman, sans-serif;
                    text-align: center;
                    padding: 50px;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                }
                h1 { font-size: 48px; margin-bottom: 20px; }
                p { font-size: 24px; }
            </style>
        </head>
        <body>
            <h1>🚀 Welcome to JobTrackerPro</h1>
            <p>Your AI-powered job search companion</p>
            <p>Built by Amil Thomas</p>
        </body>
    </html>
    """

# Jobs listing page
@app.route('/jobs')
def jobs():
    """
    Jobs listing page - will show all jobs
    """
    return "<h1>Jobs Page - Coming Soon!</h1>"

# Dashboard page
@app.route('/dashboard')
def dashboard():
    """
    Dashboard - statistics and insights
    """
    return "<h1>Dashboard - Coming Soon!</h1>"

# Run the application
if __name__ == '__main__':
    # debug=True shows detailed errors (helpful for learning!)
    app.run(debug=True, port=5000)