import markdown
import pdfkit

with open("input.md", "r", encoding="utf-8") as f:
    md_text = f.read()

html = markdown.markdown(md_text)

path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_string(html, "output.pdf", configuration=config)