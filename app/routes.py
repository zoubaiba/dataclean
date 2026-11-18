from flask import Blueprint, jsonify, session, redirect, url_for, request, render_template
from app.scanner import simulate_metadata_scan

main_bp = Blueprint('main', __name__)

# Scope strictly limited to metadata (Principle of Least Privilege)
SCOPES = ['https://www.googleapis.com/auth/gmail.metadata']

@main_bp.route('/')
def index():
    return render_template('index.html', authenticated=("credentials" in session))

@main_bp.route('/api/status')
def status():
    return jsonify({
        "project": "DataClean - GDPR Compliance Tool",
        "status": "Running in Docker",
        "scope_enforced": SCOPES[0],
        "authenticated": "credentials" in session
    })

@main_bp.route('/api/scan')
def scan_preview():
    results = simulate_metadata_scan()
    return jsonify(results)
