from fpdf import FPDF

def main():
    name = input('Your Name: ')
    shirtificate(name)

def shirtificate(name):
    pdf= FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font('Times', size=40)
    pdf.cell(w=40, h=10, text='CS50 Shirtificate',align='C', center=True)
    pdf.image('shirtificate.png', x=15, y=70, w=180, h=181)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Times', size=24)
    pdf.cell(w=15, h=240, text=f'{name} took cs50',align='C', center=True)
    pdf.output('shirtificate.pdf')

if __name__ == "__main__":
    main()