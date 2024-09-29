from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


class PDFReport:
    def __init__(self):
        pass

    def generateReportFromInstagramData(self,instagramData,fileName="report.pdf"):
        document = SimpleDocTemplate(fileName,pagesize=letter)
        styles = getSampleStyleSheet()
        story = []

        title = f"Instagram Report for {instagramData['username']}"
        story.append(Paragraph(title,styles['Title']))
        story.append(Spacer(1,12))

        intro = Paragraph("This report contains the information of the Instagram profile of "+instagramData['username'],styles['Normal'])
        story.append(intro)
        story.append(Spacer(1, 12))

        story.append(Paragraph("Profile Information",styles['Heading1']))
        story.append(Spacer(1, 12))

        data = [
            ["username",instagramData['username']],
            ["full name",instagramData['full_name']],
            ["biography",instagramData['biography']],
            ["external url",instagramData['external_url']],
            ["category",instagramData['category']],
            ["is business",instagramData['is_business']],
            ["followers",instagramData['follower_count']],
            ["following",instagramData['following_count']],
        ]

        t = Table(data)

        t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.grey),
                                 ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                                 ('ALIGN',(0,0),(-1,-1),'CENTER'),
                                 ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
                                 ('BOTTOMPADDING',(0,0),(-1,0),12),
                                 ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                                 ]))
        
        story.append(t)

        document.build(story)
