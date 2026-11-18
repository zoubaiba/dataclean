def extract_domain_from_header(from_header: str) -> str:
    """Extracts the clean sender domain from an RFC 2822 From header."""
    if "<" in from_header and ">" in from_header:
        email_part = from_header.split("<")[1].split(">")[0]
    else:
        email_part = from_header.strip()
    return email_part.split("@")[-1].lower() if "@" in email_part else email_part.lower()

def simulate_metadata_scan():
    """
    Placeholder for Gmail API users().messages().list() & get(format='metadata').
    Only processes 'From', 'Date', and 'List-Unsubscribe' headers without body access.
    """
    sample_headers = [
        {"From": "newsletter@ecommerce-shop.fr", "Date": "2026-10-12"},
        {"From": "no-reply@old-forum.com", "Date": "2025-04-03"},
        {"From": "promo@fastfashion-brand.com", "Date": "2026-11-01"},
    ]
    domains = sorted(list({extract_domain_from_header(h["From"]) for h in sample_headers}))
    return {
        "scanned_headers_count": len(sample_headers),
        "identified_data_controllers": domains,
        "gdpr_action": "Ready to generate Art. 17 GDPR right-to-erasure requests"
    }
