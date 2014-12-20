#!/usr/bin/env python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("output.pdf", pagesize=letter)
c.setFont("Times-Roman", 14)
width, height = letter
c.drawString(100, 100, "Page 1")
c.showPage() # next draws on new page
c.drawString(100, 100, "Page 2")
c.showPage()
c.save()
