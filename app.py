from flask import Flask, render_template, request
from project1 import calculate_available_time, generate_schedule  # <- use your file

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    schedule = []

    if request.method == "POST":
        routine = {
            "wake": request.form["wake"],
            "sleep": request.form["sleep"],
            "school_start": request.form["school_start"],
            "school_end": request.form["school_end"],
            "tuition_start": request.form["tuition_start"],
            "tuition_end": request.form["tuition_end"],
            "meals": int(request.form["meals"]),
            "travel": int(request.form["travel"]),
            "breaks": int(request.form["breaks"])
        }

        subjects = request.form["subjects"].split(",")  # comma separated list

        available = calculate_available_time(routine)
        schedule = generate_schedule(subjects, available)

    return render_template("index.html", schedule=schedule)

if __name__ == "__main__":
    app.run(debug=True)
