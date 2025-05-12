from flask import Flask

app = Flask(__name__)  # ← Esta línea es indispensable

@app.route("/")
def home():
    return "¡La app de Madres está funcionando en Render Clarines que si!"

if __name__ == "__main__":
    from os import environ
    app.run(host='0.0.0.0', port=int(environ.get("PORT", 5000)))
