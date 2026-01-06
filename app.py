from flask import Flask, render_template, redirect, url_for, jsonify
from flask_cors import CORS
import os
import script

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

CORS(app)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/result")
def result():
    """
    Fetches latest Microsoft Form submission via script.py,
    runs ML models, and renders result page.
    """

    try:
        stress = script.predict_stress()
        anxiety = script.predict_anxiety()
        depression = script.predict_depression()

        # Map numeric outputs to labels
        def map_level(val):
            if val <= 1:
                return "Low"
            elif val == 2:
                return "Moderate"
            else:
                return "High"

        stress_label = map_level(stress)
        anxiety_label = map_level(anxiety)
        depression_label = map_level(depression)

        # Determine primary severity class for UI color
        severity_class = (
            "high" if stress_label == "High"
            else "moderate" if stress_label == "Moderate"
            else "low"
        )

        return render_template(
            "result.html",
            stress=stress_label,
            anxiety=anxiety_label,
            depression=depression_label,
            severity_class=severity_class
        )

    except Exception as e:
        return render_template(
            "result.html",
            error=str(e)
        )


@app.route("/api/stress")
def api_stress():
    return jsonify({"stress": script.predict_stress()})


@app.route("/api/anxiety")
def api_anxiety():
    return jsonify({"anxiety": script.predict_anxiety()})


@app.route("/api/depression")
def api_depression():
    return jsonify({"depression": script.predict_depression()})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5500))
    app.run(host="0.0.0.0", port=port, debug=False)
