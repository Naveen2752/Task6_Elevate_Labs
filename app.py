from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("\n--- New Contact Form Submission ---")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)
        print("----------------------------------\n")

        return render_template("contact.html", success=True)

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
