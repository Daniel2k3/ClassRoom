from fpdf import FPDF

def convert_to_pdf(infile, outfile):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    with open(infile, "r") as f:
        for line in f:
            pdf.multi_cell(0, 10, line)

    pdf.output(outfile)