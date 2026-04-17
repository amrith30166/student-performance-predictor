from flask import Flask, render_template, request
from model import predict_score
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # ✅ FIXED INPUT HANDLING (prevents crash if empty)
        hours = float(request.form.get("hours", 0))
        attendance = float(request.form.get("attendance", 0))
        previous = float(request.form.get("previous", 0))

        result = predict_score(hours, attendance, previous)

        if result >= 80:
            level = "Excellent 🎉"
            suggestion = "Keep up the great work!"
        elif result >= 60:
            level = "Good 👍"
            suggestion = "Try to study 1–2 hours more daily."
        else:
            level = "Needs Improvement ⚠️"
            suggestion = "Focus on consistency and improve attendance."

        return render_template(
            "index.html",
            prediction_text=f"Predicted Score: {result:.2f}",
            level=level,
            suggestion=suggestion,
            score=round(result, 2)
        )

    except Exception as e:
        print("Error:", e)  # ✅ helps debugging in console
        return render_template(
            "index.html",
            prediction_text="Error occurred. Please enter valid values."
        )

# ✅ RUN CONFIG (already correct)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))