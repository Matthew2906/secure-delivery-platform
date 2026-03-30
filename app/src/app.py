from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Secure Delivery Platform</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #0f172a, #1e293b);
                color: white;
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .card {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 20px;
                padding: 40px;
                width: 90%;
                max-width: 700px;
                box-shadow: 0 20px 50px rgba(0, 0, 0, 0.35);
                backdrop-filter: blur(10px);
            }

            h1 {
                margin-top: 0;
                font-size: 2.5rem;
                margin-bottom: 10px;
            }

            p {
                font-size: 1.1rem;
                line-height: 1.6;
                color: #dbeafe;
            }

            .badge {
                display: inline-block;
                margin-top: 15px;
                padding: 10px 16px;
                border-radius: 999px;
                background: #22c55e;
                color: #052e16;
                font-weight: bold;
            }

            .section {
                margin-top: 30px;
                padding-top: 20px;
                border-top: 1px solid rgba(255, 255, 255, 0.15);
            }

            .endpoint {
                background: rgba(255, 255, 255, 0.08);
                padding: 12px 16px;
                border-radius: 12px;
                margin-top: 10px;
                font-family: Consolas, monospace;
                color: #93c5fd;
            }

            a.button {
                display: inline-block;
                margin-top: 25px;
                text-decoration: none;
                background: #3b82f6;
                color: white;
                padding: 12px 20px;
                border-radius: 12px;
                font-weight: bold;
                transition: 0.2s ease;
            }

            a.button:hover {
                background: #2563eb;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Secure Delivery Platform</h1>
            <p>
                enterprise style DevOps project focused on
                secure CI/CD, least privilege access, environment separation,
                and controlled production delivery.
            </p>

            <div class="badge">System Status: Running</div>

            <div class="section">
                <h2>Project Focus</h2>
                <p>
                    This application is a sample workload for a secure azure
                    DevOps pipeline that i Matthew Raphael which im typing manually 
                    errorre see chatgpt cant do that. Even look at the check
                    Health endpoint button theres a 3 there. Anyways i will  
                    include Docker, Key Vault, environment approvals
                    and Kubernetes deployment patterns.
                </p>
            </div>

            <div class="section">
                <h2>Available Endpoint</h2>
                <div class="endpoint">GET /health</div>
                <a class="button" href="/health">Check H3alth Endpoint</a>
            </div>
        </div>
    </body>
    </html>
    """)

@app.route("/health")
def health():
    return jsonify({
        "status": "This is a pretty healthy page"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)