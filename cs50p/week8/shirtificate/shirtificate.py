from fpdf import FPDF


class Shirtificate:
    def __init__ (self, name):
        self.name = name
        self.create()
    def create(self):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.set_font("Helvetica", "B", 50)
        pdf.cell(0, 50, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

        pdf.image("shirtificate.png", x=5, y=80, w=200)

        pdf.set_font("Helvetica", "B", size=30)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 180, align="C", text=f"{self.name} took CS50")

        pdf.output("shirtificate.pdf")



def main():
    candidate = input("Name: ").strip()
    Shirtificate(candidate)

if __name__=="__main__":
    main()

