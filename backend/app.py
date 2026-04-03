from flask import Flask, request, jsonify
from flask_cors import CORS

from resume_optimizer import optimize_resume
from ats_score import calculate_ats_score
from database import get_connection

app = Flask(__name__)
CORS(app)

@app.route("/optimize", methods=["POST"])
def optimize():
    data = request.get_json()
    resume_text = data.get("resume", "")

    if not resume_text:
        return jsonify({"error": "Resume text is required"}), 400

    optimized = optimize_resume(resume_text)
    ats_score = calculate_ats_score(optimized)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO resumes (original_resume, optimized_resume, ats_score)
        VALUES (%s, %s, %s)
        """,
        (resume_text, optimized, ats_score)
    )
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({
        "optimized_resume": optimized,
        "ats_score": ats_score
    })

if __name__ == "__main__":
    app.run(debug=True)
