# ---------- app.py (FINAL) ----------
from flask import Flask, render_template, request
import os, time, csv

app = Flask(__name__)

# ---------- File‑save paths ----------
BASE_UPLOADS   = "uploads"
IDCARD_FOLDER  = os.path.join(BASE_UPLOADS, "idcards")
OFFER_FOLDER   = os.path.join(BASE_UPLOADS, "offers")

for p in (IDCARD_FOLDER, OFFER_FOLDER):
    os.makedirs(p, exist_ok=True)              # auto‑create folders

# ---------- ROUTES ----------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/student-progress")
def student_progress():
    return render_template("student_progress.html")


@app.route("/placement-details")
def placement_details():
    return render_template("placement_details.html")


# ---------- Student‑progress POST (ID‑card) ----------
@app.route("/submit", methods=["POST"])
def submit_progress():
    name    = request.form["name"]
    dno     = request.form["dno"]
    college = request.form["college"]
    place   = request.form["place"]
    degree = request.form.get("degree", "")
    id_card = request.files["id_card"]

    if not id_card or not id_card.filename.lower().endswith(".pdf"):
        return "❌ Only PDF files allowed for ID card!"

    pdf_name = f"{dno}_{int(time.time())}.pdf"
    id_card.save(os.path.join(IDCARD_FOLDER, pdf_name))

    # CSV row
    with open("student_data.csv", "a", newline="") as f:
        csv.writer(f).writerow([name, dno, college, place, degree, pdf_name])

    # show branded success page
    return render_template(
        "success.html",
        title="Progress Saved",
        msg=f"✔ Progression saved for {name}",
        sub=f"Degree : {degree}"
    )


# ---------- Placement POST (Offer‑letter) ----------
@app.route("/submit-placement", methods=["POST"])
def submit_placement():
    name         = request.form["name"]
    dno          = request.form["dno"]
    company      = request.form["company"]
    place        = request.form["place"]
    offer_letter = request.files["offer_letter"]

    if not offer_letter or not offer_letter.filename.lower().endswith(".pdf"):
        return "❌ Only PDF files allowed for Offer Letter!"

    pdf_name = f"{dno}_{int(time.time())}.pdf"
    offer_letter.save(os.path.join(OFFER_FOLDER, pdf_name))

    # CSV row
    with open("placement_data.csv", "a", newline="") as f:
        csv.writer(f).writerow([name, dno, company, place, pdf_name])

    return render_template(
        "success.html",
        title="Placement Saved",
        msg=f"✔ Placement saved for {name}",
        sub=f"{company} – {place}"
    )


# ---------- main ----------
if __name__ == "__main__":
    app.run(debug=True)        # auto‑reload while coding