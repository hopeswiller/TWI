from fpdf import FPDF

class PDF(FPDF):

    def draw_border(self):
        self.set_line_width(0.0)
        # self.set_fill_color(0.0, 0.0, 0.0) # color for outer rectangle
        self.rect(5.0, 5.0, 200.0, 287.0) 
        self.set_fill_color(255, 255, 255) # color for inner rectangle
        self.rect(8.0, 8.0, 194.0,282.0)

    def save_pdf(self, filename):
        self.set_author('hopeswiller_<davidba941@gmail.com>')
        self.output(f'{filename}.pdf','F')
        print('File saved')



# defualt size of A4 (w:210 mm and h:297 mm)
pdf_w=210
pdf_h=297
