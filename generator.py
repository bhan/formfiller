#!/usr/bin/env python
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Image, SimpleDocTemplate

c = canvas.Canvas("output.pdf", pagesize=letter)
c.setFont("Times-Roman", 14)
width, height = letter

Image("page1.png", width=width, height=height).drawOn(c,0,0)
#c.drawString(100, 600, "Page 1")
c.showPage() # next draws on new page

#c.drawString(100, 100, "Page 2")
Image("page2.png", width=width, height=height).drawOn(c,0,0)
c.showPage()

c.save()

#TODO save pdf origin as image and overlay
#things = []
#things.append(Image("seal.png"))
#doc = SimpleDocTemplate("output.pdf", pagesize=letter)
#doc.build(things)
