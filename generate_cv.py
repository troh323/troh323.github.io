from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether
)

CRIMSON = HexColor("#A31F34")
DARK = HexColor("#222222")
GRAY = HexColor("#555555")
LIGHT_GRAY = HexColor("#999999")

doc = SimpleDocTemplate(
    "cv.pdf",
    pagesize=letter,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
    leftMargin=0.75*inch,
    rightMargin=0.75*inch,
)

# Styles
name_style = ParagraphStyle("Name", fontName="Helvetica-Bold", fontSize=18,
                            alignment=TA_CENTER, textColor=DARK, spaceAfter=2)
contact_style = ParagraphStyle("Contact", fontName="Helvetica", fontSize=9,
                               alignment=TA_CENTER, textColor=GRAY, spaceAfter=4)
section_style = ParagraphStyle("Section", fontName="Helvetica-Bold", fontSize=11,
                               textColor=CRIMSON, spaceBefore=14, spaceAfter=4)
institution_style = ParagraphStyle("Institution", fontName="Helvetica-Bold", fontSize=10,
                                   textColor=DARK, spaceBefore=4, spaceAfter=1)
body_style = ParagraphStyle("Body", fontName="Helvetica", fontSize=9.5,
                            textColor=DARK, leading=13, spaceAfter=1)
italic_style = ParagraphStyle("Italic", fontName="Helvetica-Oblique", fontSize=9.5,
                              textColor=DARK, leading=13, spaceAfter=1)
small_style = ParagraphStyle("Small", fontName="Helvetica", fontSize=9,
                             textColor=GRAY, leading=12, spaceAfter=1)

def section_header(text):
    return [
        Spacer(1, 4),
        Paragraph(text, section_style),
        HRFlowable(width="100%", thickness=0.8, color=CRIMSON, spaceAfter=4),
    ]

def entry_row(left_text, right_text, bold_left=False):
    font = "Helvetica-Bold" if bold_left else "Helvetica"
    left = Paragraph(f'<font name="{font}" size="9.5">{left_text}</font>', body_style)
    right = Paragraph(f'<font name="Helvetica" size="9" color="#777777">{right_text}</font>',
                      ParagraphStyle("R", alignment=2, fontName="Helvetica", fontSize=9))
    t = Table([[left, right]], colWidths=[5.0*inch, 2.0*inch])
    t.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 1),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    return t

story = []

# Name
story.append(Paragraph("TERRENCE ROH", name_style))
story.append(Spacer(1, 2))

# Contact row
story.append(Paragraph(
    'MIT Political Science (E53-406) &bull; 30 Wadsworth Street, Cambridge, MA 02142',
    contact_style
))
story.append(Paragraph(
    'troh@mit.edu &bull; (617) 852-6078 &bull; <link href="http://sites.google.com/view/troh">sites.google.com/view/troh</link>',
    contact_style
))

# Horizontal rule
story.append(Spacer(1, 4))
story.append(HRFlowable(width="100%", thickness=1.2, color=DARK, spaceAfter=2))

# ---- RESEARCH INTERESTS ----
story.extend(section_header("RESEARCH INTERESTS"))
story.append(Paragraph(
    "State Development, Urban Slums, Identity Politics, Conflict &amp; Violence, "
    "Causal Inference, Experiments, Measurement &amp; Scaling, Community Detection",
    body_style
))

# ---- EDUCATION ----
story.extend(section_header("EDUCATION"))

story.append(entry_row("<b>Massachusetts Institute of Technology (MIT)</b>, Cambridge, MA", ""))
story.append(Paragraph("Ph.D. Candidate, Political Science, 2023–present", body_style))
story.append(Paragraph("Fields: Comparative Politics, Political Methodology", small_style))
story.append(Paragraph("Committee: Noah Nathan, Volha Charnysh, Naoki Egami, F. Daniel Hidalgo (Chair)", small_style))

story.append(Spacer(1, 4))
story.append(entry_row("<b>Seoul National University (SNU)</b>, Seoul, Korea", ""))
story.append(Paragraph("M.A., Political Science, 2022", body_style))
story.append(Paragraph("B.A., Spanish (minor in Political Science), 2019 — <i>summa cum laude</i>, Highest Honors in Field", body_style))

story.append(Spacer(1, 4))
story.append(entry_row("<b>Universidad Nacional Autónoma de México (UNAM)</b>, México", ""))
story.append(Paragraph("Exchange Student, 2016", body_style))

# ---- WORKING PAPERS ----
story.extend(section_header("WORKING PAPERS"))
story.append(Paragraph(
    '“Spillover Effects of Ethnic Representation: Evidence from Peru”',
    body_style
))
story.append(Spacer(1, 4))
story.append(Paragraph(
    '“Life Dissatisfaction and Native-Immigrant Divides” with Syngjoo Choi and Yong Kyun Kim (<i>under review</i>)',
    body_style
))

# ---- WORKING PROJECTS ----
story.extend(section_header("WORKING PROJECTS"))
story.append(Paragraph(
    '“Governing the Periphery: Spatial Fragmentation and Collective Action”',
    body_style
))
story.append(Spacer(1, 4))
story.append(Paragraph(
    '“Targeting Hard-to-Reach Populations at Scale Using Automated Survey Bots via WhatsApp” with F. Daniel Hidalgo',
    body_style
))

# ---- CONFERENCE & TALK ----
story.extend(section_header("CONFERENCE PRESENTATIONS &amp; TALKS"))
for conf, year in [
    ("Midwest Political Science Association (MPSA)", "2022, 2026"),
    ("International Political Science Association (IPSA)", "2025"),
    ("MIT Political Experimental Research Lab (PERL)", "2024"),
    ("SNU Experimental Political Science Working Group", "2024"),
    ("PUC-Chile Centro de Estudios Asiáticos", "2019"),
]:
    story.append(entry_row(conf, year))

# ---- RESEARCH AFFILIATIONS ----
story.extend(section_header("RESEARCH AFFILIATIONS"))
for inst, role, year in [
    ("Pontificia Universidad Católica de Peru (PUCP), Lima, Peru", "Visiting Researcher", "Summer 2026"),
    ("MIT Global Diversity Lab (GDL), Cambridge, MA", "Graduate Affiliate", "2024–present"),
    ("Universidad de Ingeniería y Tecnología (UTEC), Lima, Peru", "Visiting Researcher", "Summer 2024"),
    ("SNU Experimental Political Science Lab, Seoul, Korea", "Research Associate", "2023–2024"),
]:
    story.append(entry_row(f"<b>{inst}</b>", year))
    story.append(Paragraph(role, small_style))

# ---- RESEARCH EXPERIENCE ----
story.extend(section_header("RESEARCH EXPERIENCE"))
for desc, year in [
    ("Research Assistance to Naoki Egami", "Summer 2026"),
    ("Research Assistance to F. Daniel Hidalgo", "Fall 2025"),
    ("Research Assistance to Noah Nathan", "Summer 2024"),
]:
    story.append(entry_row(desc, year))

# ---- TEACHING EXPERIENCE ----
story.extend(section_header("TEACHING EXPERIENCE"))
story.append(entry_row("<b>17.802 Quantitative Methods II: Causal Inference</b>", "Spring 2026"))
story.append(Paragraph("Teaching Assistance to Naoki Egami", small_style))

# ---- PROFESSIONAL EXPERIENCE ----
story.extend(section_header("PROFESSIONAL EXPERIENCE"))
story.append(entry_row("<b>Sustainable IF (SUSIF)</b>, Seoul, Korea", "2022–2023"))
story.append(Paragraph("Data Analyst (non-resident), development consultancy", small_style))
story.append(Spacer(1, 3))
story.append(entry_row("<b>United Nations ECLAC</b>, Santiago, Chile", "2019–2020"))
story.append(Paragraph("Research Intern, Program Planning &amp; Operations Division (DPPO)", small_style))

# ---- GRANTS & AWARDS ----
story.extend(section_header("GRANTS &amp; AWARDS"))

story.append(Paragraph("<b><i>Massachusetts Institute of Technology</i></b>", body_style))
for desc, year in [
    ("Political Methodology Lab (PML) Research Grant", "2025"),
    ("Departmental Graduate Research Grant", "2024, 2025, 2026"),
    ("Kenan Sahin Presidential Fellowship", "2023–2024"),
]:
    story.append(entry_row(desc, year))

story.append(Spacer(1, 3))
story.append(Paragraph("<b><i>Seoul National University</i></b>", body_style))
for desc, year in [
    ("Graduate Field Research Grant", "2021, 2022, 2023"),
    ("Next Generation Fellowship in Fundamental Sciences", "2021–2022"),
]:
    story.append(entry_row(desc, year))

story.append(Spacer(1, 3))
story.append(Paragraph("<b><i>External</i></b>", body_style))
for desc, year in [
    ("Institute for Humane Studies Fellowship", "2026"),
    ("Fulbright Graduate Study Grant (<i>declined</i>)", "2022"),
    ("Scholarship for Korea’s Future Leaders", "2019"),
    ("Ministerial Award for Best Research Paper on Latin America", "2018"),
]:
    story.append(entry_row(desc, year))

# ---- SERVICE ----
story.extend(section_header("SERVICE"))
for desc, year in [
    ("Organizer, MIT Latin America Working Group (LAWG)", "2025–present"),
    ("Graduate Assistant, MIT GDL Pathways Program", "2025"),
    ("Social Chair, Graduate Student Council", "2024–2025"),
]:
    story.append(entry_row(desc, year))

# ---- ADDITIONAL TRAINING ----
story.extend(section_header("ADDITIONAL TRAINING"))
story.append(entry_row("Quantitative Methods Program, <b>ICPSR</b> — <i>EITM Certificate</i>", "Summer 2022"))
story.append(entry_row("Data Science Bootcamp, <b>SNU Graduate School of Data Science</b>", "Winter 2020"))

# ---- SKILLS ----
story.extend(section_header("SKILLS"))
story.append(Paragraph("<b>Programming:</b> R, Python, LaTeX, QGIS, Qualtrics", body_style))
story.append(Paragraph("<b>Languages:</b> Korean (native), Spanish (fluent), Portuguese (intermediate)", body_style))

# ---- FIELDWORK ----
story.extend(section_header("FIELDWORK"))
story.append(Paragraph("Lima, Peru (2024) &bull; Mexico City, Mexico (2026) &bull; São Paulo, Brazil (2024)", body_style))

# Page number
def add_page_number(canvas_obj, doc_obj):
    canvas_obj.saveState()
    canvas_obj.setFont("Helvetica", 8)
    canvas_obj.setFillColor(LIGHT_GRAY)
    canvas_obj.drawCentredString(letter[0]/2.0, 0.4*inch, f"– {doc_obj.page} –")
    canvas_obj.restoreState()

doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
print("CV PDF generated successfully")
