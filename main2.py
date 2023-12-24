from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')
#line_number = 27

for i, row in df.iterrows():
    pdf.add_page()
# Sets header
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=f"{row['Topic']}", align='L', ln=1)
    for line in range(20, 290, 10):
        pdf.line(x1=10, y1=line, x2=200, y2=line)

# Sets footer
    pdf.ln(258)
    pdf.set_font(family='Times', style='I', size=9)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for page in range(row['Pages']-1):
        pdf.add_page()
        pdf.ln(268)
        pdf.set_font(family='Times', style='I', size=9)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')
        #line_y = 20
        #for lines in range(line_number):
            #pdf.line(x1=10, y1=line_y, x2=200, y2=line_y)
            #line_y = line_y + 10
        for y in range(20, 290, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)


pdf.output('output2.pdf')
