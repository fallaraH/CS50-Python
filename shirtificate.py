from fpdf import FPDF

pdf = FPDF(orientation="P", format="A4")

pdf.add_page()
pdf.set_font("helvetica", style="BU", size=36)
pdf.image("shirtificate.png", x="C", y=40)
pdf.cell(text="CS50 Shirtificate", center=True, border=0, new_y="TMARGIN", new_x="CENTER")

name = input("What's your name?: ")

pdf.set_font("Times", size=24)
pdf.set_text_color(255, 255, 255)
pdf.text(text=f"{name} took CS50", x=77, y=100)


pdf.output("shirtificate.pdf")

