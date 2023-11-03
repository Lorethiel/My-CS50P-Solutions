from fpdf import FPDF


def main():
    user_input = input('Name: ')
    convert(user_input)



def convert(input):
    pdf = FPDF(format='A4')
    pdf.add_page()
    pdf.set_font('helvetica','B', 45)
    photo = 'shirtificate.png'
    result = 'shirtificate.pdf'
    pdf.image(photo,x=0,y=70)
    pdf.cell(0,60,'CS50 Shirtificate', align='C')
    pdf.set_font_size(50)
    pdf.set_text_color(255,255,255)
    pdf.text(x=39, y=150,text=f'{input} took CS50')
    pdf.output(result)

if __name__ == '__main__':
    main()

