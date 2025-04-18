from fpdf import FPDF
import pandas as pd
from key_ratios import get_financial_summary

# Set up PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Title
pdf.cell(200, 10, 'Group 63: Perpetual Ltd', ln=True, align='C')

# Company Overview
pdf.set_font("Arial", size=12)
with open("C:/Users/Lucy/OneDrive/BAFE YR3/FINM3422/Perpetual Research Report/analyst_report-1/Overview", "r", encoding="utf-8") as file:
    text = file.read()

pdf.multi_cell(0, 10, text)

# Insert space for chart to avoid overlap with commentary
pdf.ln(10)  # Adds a line break, providing space before the chart

# Chart
pdf.set_font('Arial', size=12)

image_y = pdf.get_y()  # Position for the image (just after the commentary)
image_height = 120  # adjust if your image is taller

pdf.image("ppt_vs_asx200.png", x=10, y=image_y, w=190)
pdf.set_y(image_y + image_height + 10)  # Set y position after the image

# Add a new page for financial summary
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Input values
TICKER = "PPT.AX"
last_price = 15.53
pe_ratio = -3.7694
dividend_yield = 3.93
eps = -4.12
roa = -12.86

# Get summary
summary = get_financial_summary(TICKER, last_price, pe_ratio, dividend_yield, eps, roa)
df = pd.DataFrame(summary.items(), columns=["Metric", "Value"])

# Financial summary header
pdf.set_font("Arial", style='B', size=14)
pdf.cell(200, 10, f"Financial Summary for {TICKER}", ln=True, align='C')

# Add a line break
pdf.ln(5)

# Table headers
pdf.set_font("Arial", size=12)
pdf.set_fill_color(200, 220, 255)
col_widths = [80, 40]
pdf.cell(col_widths[0], 10, "Metric", border=1, fill=True)
pdf.cell(col_widths[1], 10, "Value", border=1, ln=True, fill=True)

# Table rows with zebra striping
pdf.set_fill_color(245, 245, 245)
for i, row in df.iterrows():
    fill = i % 2 == 0
    pdf.cell(col_widths[0], 10, str(row["Metric"]), border=1, fill=fill)
    pdf.cell(col_widths[1], 10, str(row["Value"]), border=1, ln=True, fill=fill)

pdf.ln(5)
# Ratio Analysis 
pdf.set_font("Arial", size=12)
with open("C:/Users/Lucy/OneDrive/BAFE YR3/FINM3422/Perpetual Research Report/analyst_report-1/Ratio Analysis", "r", encoding="utf-8") as file:
    text = file.read()

pdf.multi_cell(0, 10, text)

# Add a new page for the image
pdf.add_page()

# Heading for the image
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, "AUM and Flows by Boutique (A$Bn)", ln=True, align = 'C')

# Small spacing below image heading
pdf.ln(5)

image_y = pdf.get_y()   # Position for image
image_height = 80       # Adjust as needed to fit the image cleanly

# Insert the image - adjust witdth (w=190) to match page width
pdf.image("ppt_boutique_flows.png", x=10, y=image_y, w=190)

# Move cursor below image so next section doesn't overlap
pdf.set_y(image_y + image_height + 10)

# Insert space for chart to avoid overlap with commentary
pdf.ln(10)  #
# Save the PDF
pdf.output('Perpetual Equity Research Report.pdf')
