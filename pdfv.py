from fpdf import FPDF

class pdfcreator:
    def pdfgenerator(self):
        pdf =FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 10, 'Hello World!')
        pdf.output('test.pdf', 'F')