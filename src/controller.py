from flask import (
    Blueprint, render_template, request, send_file
)
from werkzeug.security import check_password_hash, generate_password_hash
from .helpers import calculate_expiry_date, get_date_range
from .pdf_generator import PDF
from datetime import datetime
from enum import Enum

# bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('app', __name__)

class RequestType(Enum):
    single = 1
    multi = 2

pdf = PDF()

@bp.route('/', methods=['GET','POST'])
def index():
    showbtn = False
    if request.method == 'POST':
        if request.form['type'] == RequestType.single.name:
            production_date_str = request.form['production_date'] 

            production_date = datetime.strptime(production_date_str, '%m/%d/%Y').date()
            exp_date = calculate_expiry_date(production_date)

            context = {
                "prod_date":  datetime.strftime(production_date, '%d %B, %Y'),
                "shortdate" : datetime.strftime(exp_date, '%m/%d/%Y'),
                "longdate": datetime.strftime(exp_date, '%d %B, %Y')
            }

            return render_template('index.html',context=context)
        
        else:
            start_date = request.form['start_date'] 
            end_date = request.form['end_date']

            in_range_days = get_date_range(
                datetime.strptime(start_date, '%m/%d/%Y').date(),
                datetime.strptime(end_date, '%m/%d/%Y').date()
            )
            result = {} # production_date : expiry_date
            for i in in_range_days:
                exp_date = calculate_expiry_date(i)
                date_str = datetime.strftime(i, '%d %B, %Y - (%m/%d/%Y)')
                result[date_str] = datetime.strftime(exp_date, '%d %B, %Y - (%m/%d/%Y)')

            pdf.add_page()
            pdf.set_font("Arial",size = 14)
            pdf.draw_border()
            pdf.cell(200, 10, txt = "Dates Genera....blah blah", ln = 2, align = 'C')
            pdf.cell(100, 10, txt = "Production Dates", ln = 0, align = 'L')
            pdf.cell(78, 10, txt = "Expiration Dates", ln = 1, align = 'R')
            pdf.set_font("Arial",size = 10)
            
            for key,value in result.items():
                pdf.cell(100, 10, txt = key, ln = 0, align = 'L')
                pdf.cell(0, 10, txt = value, ln = 1, align = 'R')

            pdf.save_pdf('Expiry_Dates')
            showbtn = True
            context = {
                "showbtn": showbtn
            }

            return render_template('index.html', context=context)

    context = {
        "showbtn": showbtn,
    }
    return render_template('index.html',context=context)



@bp.route('/download')
def download():
    path = "../Expiry_Dates.pdf"
    return send_file(path, as_attachment=True)