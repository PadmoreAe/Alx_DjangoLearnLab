# Project Instructions

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/yourrepository.git


# Permissions and Groups Setup

### Custom Permissions
Custom permissions defined in the `Book` model:
- `can_view`: Allows users to view the book list and details.
- `can_create`: Allows users to add new books.
- `can_edit`: Allows users to modify existing books.
- `can_delete`: Allows users to remove books from the database.

### Groups
- **Viewers**: Can only view books.
- **Editors**: Can view, create, and edit books.
- **Admins**: Full permissions (view, create, edit, delete).



CSRF Protection: All POST forms include {% csrf_token %} to prevent unauthorized command execution.

SQL Injection: All data access is handled via Django’s ORM to ensure parameterization.

Secure Headers: Configured X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, and SECURE_BROWSER_XSS_FILTER to protect against clickjacking and MIME sniffing.

Cookie Security: SECURE flags are set to True to ensure session data is only sent over HTTPS.






## Deployment Configuration for HTTPS (Nginx)

To support the Django HTTPS settings, the edge server (Nginx) must be configured with SSL certificates (e.g., from Let's Encrypt).

Example Nginx Config:
```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri; # Redirect HTTP to HTTPS
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/[yourdomain.com/fullchain.pem](https://yourdomain.com/fullchain.pem);
    ssl_certificate_key /etc/letsencrypt/live/[yourdomain.com/privkey.pem](https://yourdomain.com/privkey.pem);

    location / {
        proxy_pass [http://127.0.0.1:8000](http://127.0.0.1:8000);
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme; # Crucial for SECURE_PROXY_SSL_HEADER
    }
}




Security Review: HTTPS & Headers Implementation

HTTPS Enforcement: By setting SECURE_SSL_REDIRECT and SECURE_HSTS_SECONDS, we ensure that data in transit is encrypted, protecting against Man-in-the-Middle (MITM) attacks.

Cookie Hardening: SESSION_COOKIE_SECURE prevents session hijacking over unencrypted connections.

Protocol Downgrade Protection: HSTS Preloading prevents users from ever connecting via HTTP, even on their first visit.

Improvement Areas: Future steps could include implementing a stricter Content Security Policy (CSP) to further mitigate XSS.