# DataClean – Automated GDPR Compliance Tool

Open-source web application designed to automate digital footprint discovery and **GDPR Article 17 (Right to Erasure)** requests while enforcing strict privacy-by-design principles.

## Key Security & Architecture Features
- **Principle of Least Privilege:** Uses the restricted `https://www.googleapis.com/auth/gmail.metadata` OAuth2 scope. The backend strictly inspects email headers (`From`, `Date`, `List-Unsubscribe`) and is technically prevented from reading email bodies or attachments.
- **Zero Persistent Plaintext Storage:** Session tokens are kept in encrypted client-side cookies or ephemeral memory during scanning.
- **Containerized Hardening:** Packaged with Docker (`python:3.11-slim`) and executed under an unprivileged non-root user (`appuser`) via Gunicorn.

## Tech Stack
- **Backend:** Python 3.11, Flask, Gunicorn
- **Security & Auth:** Google OAuth 2.0 (`google-auth-oauthlib`), REST API
- **Infrastructure:** Docker, Docker Compose

## Quick Start (Docker)

```bash
# 1. Clone the repository
git clone https://github.com/zoubaiba/dataclean.git
cd dataclean

# 2. Build and start the container
docker compose up --build
```

The application will be available at `http://localhost:5000` (UI) and `http://localhost:5000/api/scan` (JSON API).
