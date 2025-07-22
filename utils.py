from functools import wraps
from flask import session, redirect, url_for, flash

def login_required(f):
    """Decorator to require login for accessing routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Please log in to access this page.', 'error')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user_id():
    """Get the current user's ID from session."""
    return session.get('user_id')

def is_user_authenticated():
    """Check if user is authenticated."""
    return 'user_id' in session
