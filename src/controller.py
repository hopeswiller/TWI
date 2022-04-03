from flask import Blueprint, render_template, request, send_file, flash
from werkzeug.security import check_password_hash, generate_password_hash
from .helpers import calculate_expiry_date, get_date_range
from .pdf_generator import PDF
from datetime import datetime
from enum import Enum

bp = Blueprint("app", __name__)


class RequestType(Enum):
    single = 1
    multi = 2


pdf = PDF()


@bp.route("/", methods=["GET", "POST"])
def index():
    showbtn = False
    if request.method == "POST":
        if request.form["type"] == RequestType.single.name:
            production_date_str = request.form["production_date"]

            production_date = datetime.strptime(production_date_str, "%m/%d/%Y").date()
            exp_date = calculate_expiry_date(production_date)

            context = {
                "prod_date": datetime.strftime(production_date, "%d %B, %Y"),
                "shortdate": datetime.strftime(exp_date, "%m/%d/%Y"),
                "longdate": datetime.strftime(exp_date, "%d %B, %Y"),
            }
            flash("Date Generated Successfully...")
            return render_template("content.html", context=context)

        else:
            # date strings
            start_date = request.form["start_date"]
            end_date = request.form["end_date"]

            start_date = datetime.strptime(start_date, "%m/%d/%Y").date()
            end_date = datetime.strptime(end_date, "%m/%d/%Y").date()

            in_range_days = get_date_range(start_date, end_date)

            result = {}  # production_date : expiry_date
            for i in in_range_days:
                exp_date = calculate_expiry_date(i)
                date_str = datetime.strftime(i, "%d %B, %Y - (%m/%d/%Y)")
                result[date_str] = datetime.strftime(exp_date, "%d %B, %Y - (%m/%d/%Y)")

            pdf.add_page()
            pdf.draw_border()
            pdf.set_font("Arial", size=8)
            pdf.cell(0, 5, txt=f"generated on {datetime.now().date()}", ln=2, align="R")
            pdf.set_font("Arial", size=14)
            pdf.cell(200, 10, txt="Dates Generated Over Period", ln=2, align="C")

            period_header = f"From {datetime.strftime(start_date, '%d %B, %Y')} to {datetime.strftime(end_date, '%d %B, %Y')}"
            pdf.cell(200, 7, txt=period_header, ln=2, align="C")
            pdf.set_line_width(0.0)
            pdf.line(10, 32, 200, 32)

            pdf.cell(100, 10, txt="Production Dates", ln=0, align="L")
            pdf.cell(78, 10, txt="Expiration Dates", ln=1, align="R")
            pdf.set_font("Arial", size=10)

            for key, value in result.items():
                pdf.cell(0, 7, txt=key, ln=0, align="L")
                pdf.cell(-190, 7, txt="=", ln=0, align="C")
                pdf.cell(0, 7, txt=value, ln=1, align="R")

            pdf.save_pdf("Expiry_Dates")
            showbtn = True
            context = {"showbtn": showbtn}

            flash("Dates Generated. PDF ready to download...")
            return render_template("content.html", context=context)

    context = {
        "showbtn": showbtn,
    }
    return render_template("content.html", context=context)


@bp.route("/download")
def download():
    path = "../Expiry_Dates.pdf"
    return send_file(path, as_attachment=True)
