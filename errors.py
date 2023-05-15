from flask import render_template
from app import app

# Handle 404 errors
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, error_message="The requested page was not found."), 404

# Handle 500 errors
@app.errorhandler(500)
def internal_error(error):
    return render_template('error.html', error_code=500, error_message="An internal server error occurred."), 500

# Handle other HTTP errors
@app.errorhandler(Exception)
def unhandled_exception(e):
    return render_template('error.html', error_code=500, error_message=str(e)), 500
