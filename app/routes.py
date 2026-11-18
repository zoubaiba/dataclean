from flask import Blueprint, jsonify, session, redirect, url_for, render_template
from app.scanner import simulate_metadata_scan

main_bp = Blueprint('main', __name__)

SCOPES = ['https://www.googleapis.com/auth/gmail.metadata']

@main_bp.route('/')
def index():
    is_auth = "credentials" in session
    stats = simulate_metadata_scan() if is_auth else None
    return render_template('index.html', authenticated=is_auth, stats=stats)

@main_bp.route('/login')
def login():
    # Simulation de connexion pour valider l'UI en attendant le client OAuth complet
    session["credentials"] = "active_mock_token"
    return redirect(url_for('main.index'))

@main_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

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
    return jsonify(simulate_metadata_scan())