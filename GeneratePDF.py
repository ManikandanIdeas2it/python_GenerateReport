import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

data = pd.read_csv('propertyData.csv')
locationAvg = data.groupby('location')[['price', 'sqft']].mean()
propertyTypeAvg = data.groupby('propertyType')[['bedrooms', 'bathrooms']].mean()
def generate_report(locationAvg, propertyTypeAvg):
    pdf_file  = canvas.Canvas("Generatereport.pdf", pagesize=letter)
    pdf_file .setFont("Helvetica-Bold", 16)
    pdf_file.drawString(3 * inch, 9.5 * inch, "-----------------")
    pdf_file .drawString(1 * inch, 9.5 * inch, "Average Values")
    pdf_file.drawString(3 * inch, 9.5 * inch,"-----------------")
    pdf_file .setFont("Helvetica", 12)
    y_offset = 9 * inch
    for location, avg_data in locationAvg.iterrows():
        pdf_file .drawString(1 * inch, y_offset, location)
        pdf_file.drawString(2 * inch, y_offset, "Price: {:,.2f}".format(avg_data['price']))
        pdf_file .drawString(3.5 * inch, y_offset, "Sqft: {:.2f}".format(avg_data['sqft']))
        y_offset -= 0.25 * inch
    pdf_file .setFont("Helvetica-Bold", 16)
    pdf_file.drawString(3 * inch, 9.5 * inch, "-----------------")
    pdf_file .drawString(1 * inch, y_offset - 0.5 * inch, "Average Values")
    pdf_file .setFont("Helvetica", 12)
    y_offset -= 0.75 * inch
    for prop_type, avg_data in propertyTypeAvg.iterrows():
        pdf_file .drawString(1 * inch, y_offset, prop_type)
        pdf_file .drawString(2 * inch, y_offset, "Bedrooms: {:.2f}".format(avg_data['bedrooms']))
        pdf_file .drawString(3.5 * inch, y_offset, "Bathrooms: {:.2f}".format(avg_data['bathrooms']))
        y_offset -= 0.25 * inch
    pdf_file .showPage()
    pdf_file .save()

if __name__ == "__main__":
    generate_report(locationAvg, propertyTypeAvg)