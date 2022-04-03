from fpdf import FPDF


class PDF(FPDF):

    # default size of A4 (w:210 mm and h:297 mm)
    pdf_w = 210
    pdf_h = 297

    def draw_border(self):
        self.set_line_width(1.0)
        self.rect(5.0, 5.0, 200.0, 287.0)

    def save_pdf(self, filename):
        self.set_author("hopeswiller_<davidba941@gmail.com>")
        self.output(f"{filename}.pdf", "F")
        print("File saved")
