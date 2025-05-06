from flask import jsonify, url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class APIException(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)

def generate_sitemap(app):
    links = ['/admin/']
    for rule in app.url_map.iter_rules():
        # Filter out rules we can't navigate to in a browser
        # and rules that require parameters
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            if "/admin/" not in url:
                links.append(url)

    links_html = "".join(["<li><a href='" + y + "'>" + y + "</a></li>" for y in links])
    return """
        <div style="text-align: center;">
        <h1>Welcome to Star Wars Blog API</h1>
        <p>API HOST: <script>document.write('<input style="padding: 5px; width: 300px" type="text" value="'+window.location.href+'" />');</script></p>
        <p>Available endpoints:</p>
        <ul style="text-align: left;">"""+links_html+"</ul></div>"

def hash_password(password):
    """Generate a secure password hash."""
    return generate_password_hash(password)

def verify_password(hash, password):
    """Verify if the password matches the hash."""
    return check_password_hash(hash, password)

def format_datetime(dt):
    """Format a datetime in ISO format."""
    if isinstance(dt, datetime):
        return dt.isoformat()
    return dt

def validate_email(email):
    """Validate email format."""
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))
