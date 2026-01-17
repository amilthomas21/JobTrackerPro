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
    # These are temporary placeholder values
    # We'll replace them with real database data later
    stats = {
        'total_jobs': 1250,
        'new_jobs': 47,
        'applications': 0,
        'interviews': 0
    }
    return render_template('home.html', **stats)

# Jobs listing page
@app.route('/jobs')
def jobs():
    """
    Jobs listing page - will show all jobs from database
    """
    return render_template('jobs.html')

# Dashboard page
@app.route('/dashboard')
def dashboard():
    """
    Dashboard - statistics and insights
    """
    return render_template('dashboard.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5000)