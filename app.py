from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_restful import Resource, Api
from flask_cors import CORS
import script
import os
from flask import session



# --------------------
# APP CONFIG
# --------------------
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
app.secret_key = "aura_check_secret"
CORS(app)
api = Api(app)

# --------------------
# WEBSITE ROUTES
# --------------------
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/tech")
def tech():
    return render_template("tech.html")

# --------------------
# AUTH ROUTES (TEMP / HACKATHON SAFE)
# --------------------
@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Temporary validation (can add DB later)
    if email and password:
        return redirect(url_for("quiz"))

    return redirect(url_for("home"))


@app.route("/signup", methods=["POST"])
def signup():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")

    if name and email and password:
        return redirect(url_for("quiz"))

    return redirect(url_for("home"))


@app.route("/predict")
def predict():
    if not session.get("form_done"):
        return render_template(
            "quiz.html",
            error="Please complete the questionnaire first."
        )

    anxiety = script.predict_anxiety()
    depression = script.predict_depression()
    stress = script.predict_stress()

    return render_template(
        "quiz.html",
        result={
            "anxiety": anxiety,
            "depression": depression,
            "stress": stress
        }
    )

@app.route("/form-submitted")
def form_submitted():
    session["form_done"] = True
    return redirect("https://forms.office.com/r/YyrrV7SUKs")

# --------------------
# API RESOURCES
# --------------------
class TestAPI(Resource):
    def get(self):
        return {"message": "Aura Check API is running"}

class DepressionPrediction(Resource):
    def get(self):
        try:
            pred = int(script.predict_depression())
            return {"prediction": pred}
        except Exception as e:
            return {"error": str(e)}, 500

class AnxietyPrediction(Resource):
    def get(self):
        try:
            pred = int(script.predict_anxiety())
            return {"prediction": pred}
        except Exception as e:
            return {"error": str(e)}, 500

class StressPrediction(Resource):
    def get(self):
        try:
            pred = int(script.predict_stress())
            return {"prediction": pred}
        except Exception as e:
            return {"error": str(e)}, 500

# --------------------
# REGISTER API ROUTES
# --------------------
api.add_resource(TestAPI, "/api")
api.add_resource(DepressionPrediction, "/api/depression")
api.add_resource(AnxietyPrediction, "/api/anxiety")
api.add_resource(StressPrediction, "/api/stress")

# --------------------
# RUN SERVER
# --------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port, debug=False)
