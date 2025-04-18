from fpdf import FPDF
import pandas as pd
from key_ratios import get_financial_summary

# Set up PDF
pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font('Arial', 'B', 16)

# Title
pdf.cell(200, 10, 'Group 63: Perpetual Ltd', ln=True, align='C')

# Chart
pdf.set_font('Arial', size=12)
image_y = 30
image_height = 120  # adjust if your image is taller
pdf.image("ppt_vs_asx200.png", x=10, y=image_y, w=190)
pdf.set_y(image_y + image_height + 10)

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

# Save the PDF
pdf.output('Perpetual Equity Research Report.pdf')
