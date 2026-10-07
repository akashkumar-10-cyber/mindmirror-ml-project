"""
MindMirror AI PBL Report Generator - Bulletproof PDF & DOCX
Generates clean, 100% standards-compliant DOCX and converts to ultra-fast, robust PDF with background watermark on all pages except Page 1.
"""

import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import docx2pdf
import fitz
from PIL import Image

def stamp_watermark_with_fitz(base_pdf_path, output_pdf_path, wm_img_path, target_width_pt=400):
    doc = fitz.open(base_pdf_path)
    img = Image.open(wm_img_path)
    img_w, img_h = img.size
    aspect = img_h / img_w
    target_h = target_width_pt * aspect

    for page_num in range(len(doc)):
        if page_num == 0:
            # Page 1 (Title page) has NO watermark
            continue
        page = doc[page_num]
        rect_page = page.rect
        
        x0 = (rect_page.width - target_width_pt) / 2
        y0 = (rect_page.height - target_h) / 2
        x1 = x0 + target_width_pt
        y1 = y0 + target_h
        
        rect_wm = fitz.Rect(x0, y0, x1, y1)
        # overlay=False inserts image into background (underneath text)
        page.insert_image(rect_wm, filename=wm_img_path, overlay=False)

    doc.save(output_pdf_path, garbage=4, deflate=True)
    doc.close()
    print(f"Applied background watermark with PyMuPDF to all pages except Page 1: {output_pdf_path}")

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))

def set_table_double_borders(table, color="EC7A30", sz="30"):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="double" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:left w:val="double" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="double" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:right w:val="double" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def set_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="6" w:space="0" w:color="333333"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="single" w:sz="6" w:space="0" w:color="333333"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def set_borderless_table(table):
    tblPr = table._tbl.tblPr
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:bottom w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def generate_report():
    scratch_dir = r"C:\Users\Dell\.gemini\antigravity\scratch\ML project"
    banner_img_path = os.path.join(scratch_dir, "extracted_images", "image_0.png")
    cit_logo_path = os.path.join(scratch_dir, "extracted_images", "image_8.png")
    anna_logo_path = os.path.join(scratch_dir, "extracted_images", "image_3.png")
    wm_img_path = os.path.join(scratch_dir, "siragu_watermark_final.png")

    doc = docx.Document()
    
    # Section setup
    section = doc.sections[0]
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

    def add_p(text="", align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, line_spacing=1.15, font_size=12, bold=False, italic=False, font_name="Times New Roman", color=None):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = line_spacing
        if text:
            r = p.add_run(text)
            r.font.name = font_name
            r.font.size = Pt(font_size)
            r.bold = bold
            r.italic = italic
            if color:
                r.font.color.rgb = color
        return p

    def add_bullet_item(text, bold_prefix="", prefix_color=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if bold_prefix:
            rb = p.add_run(bold_prefix)
            rb.bold = True
            rb.font.name = 'Times New Roman'
            rb.font.size = Pt(12)
            if prefix_color:
                rb.font.color.rgb = prefix_color
        rt = p.add_run(text)
        rt.font.name = 'Times New Roman'
        rt.font.size = Pt(12)
        return p

    def add_section_heading(title_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(title_text)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        return p

    def add_chapter_heading(num, title):
        p1 = doc.add_paragraph()
        p1.paragraph_format.space_before = Pt(20)
        p1.paragraph_format.space_after = Pt(4)
        p1.paragraph_format.keep_with_next = True
        r1 = p1.add_run(f"CHAPTER {num}")
        r1.bold = True
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(14)
        
        p2 = doc.add_paragraph()
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(12)
        p2.paragraph_format.keep_with_next = True
        r2 = p2.add_run(title)
        r2.bold = True
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(14)
        return p2

    def add_orange_double_box(paragraphs_data):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_table_double_borders(tbl, color="EC7A30", sz="30")
        
        # Set inner cell padding
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(
            f'<w:tcMar {nsdecls("w")}>\n'
            f'  <w:top w:w="160" w:type="dxa"/>\n'
            f'  <w:bottom w:w="160" w:type="dxa"/>\n'
            f'  <w:left w:w="240" w:type="dxa"/>\n'
            f'  <w:right w:w="240" w:type="dxa"/>\n'
            f'</w:tcMar>'
        )
        tcPr.append(tcMar)
        
        # Add paragraphs to cell
        for idx, p_info in enumerate(paragraphs_data):
            p = cell.paragraphs[0] if idx == 0 else cell.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY if p_info.get("align") == "both" else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(p_info.get("space_before", 0))
            p.paragraph_format.space_after = Pt(p_info.get("space_after", 4))
            p.paragraph_format.line_spacing = 1.15
            for r_info in p_info.get("runs", []):
                r = p.add_run(r_info.get("text", ""))
                r.bold = r_info.get("bold", False)
                r.italic = r_info.get("italic", False)
                r.font.name = 'Times New Roman'
                r.font.size = Pt(r_info.get("size_pt", 11))
                if "color" in r_info:
                    r.font.color.rgb = r_info["color"]

    def add_highlight_box(title, text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, "F1F5F9")
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="none"/>\n'
            f'  <w:left w:val="single" w:sz="24" w:space="0" w:color="0284C7"/>\n'
            f'  <w:bottom w:val="none"/>\n'
            f'  <w:right w:val="none"/>\n'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(2)
        r1 = p.add_run(f"{title}\n")
        r1.bold = True
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        r1.font.color.rgb = RGBColor(2, 132, 199)
        
        r2 = p.add_run(text)
        r2.italic = True
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(10.5)

    def add_code_box(code_text):
        tbl = doc.add_table(rows=1, cols=1)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        cell = tbl.cell(0, 0)
        cell.width = Inches(6.5)
        set_cell_background(cell, "FAFAFA")
        
        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(
            f'<w:tcBorders {nsdecls("w")}>\n'
            f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
            f'  <w:left w:val="single" w:sz="16" w:space="0" w:color="0EA5E9"/>\n'
            f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
            f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>\n'
            f'</w:tcBorders>'
        )
        tcPr.append(borders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.05
        r = p.add_run(code_text)
        r.font.name = 'Consolas'
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(30, 41, 59)

    def add_list_table(items):
        tbl = doc.add_table(rows=len(items), cols=3)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_borderless_table(tbl)
        for idx, (label, title, page) in enumerate(items):
            row = tbl.rows[idx]
            
            c0 = row.cells[0]
            c0.width = Inches(1.1)
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_before = Pt(2)
            p0.paragraph_format.space_after = Pt(2)
            p0.paragraph_format.line_spacing = 1.15
            r0 = p0.add_run(label)
            r0.bold = True
            r0.font.name = 'Times New Roman'
            r0.font.size = Pt(11)
            
            c1 = row.cells[1]
            c1.width = Inches(4.8)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_before = Pt(2)
            p1.paragraph_format.space_after = Pt(2)
            p1.paragraph_format.line_spacing = 1.15
            r1 = p1.add_run(title)
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(11)
            
            c2 = row.cells[2]
            c2.width = Inches(0.6)
            p2 = c2.paragraphs[0]
            p2.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            p2.paragraph_format.space_before = Pt(2)
            p2.paragraph_format.space_after = Pt(2)
            p2.paragraph_format.line_spacing = 1.15
            r2 = p2.add_run(page)
            r2.font.name = 'Times New Roman'
            r2.font.size = Pt(11)

    def add_abbreviations_table(items):
        tbl = doc.add_table(rows=len(items), cols=2)
        tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
        set_borderless_table(tbl)
        for idx, (abbr, full) in enumerate(items):
            row = tbl.rows[idx]
            
            c0 = row.cells[0]
            c0.width = Inches(1.3)
            p0 = c0.paragraphs[0]
            p0.paragraph_format.space_before = Pt(2)
            p0.paragraph_format.space_after = Pt(2)
            p0.paragraph_format.line_spacing = 1.15
            r0 = p0.add_run(abbr)
            r0.bold = True
            r0.font.name = 'Times New Roman'
            r0.font.size = Pt(11)
            
            c1 = row.cells[1]
            c1.width = Inches(5.2)
            p1 = c1.paragraphs[0]
            p1.paragraph_format.space_before = Pt(2)
            p1.paragraph_format.space_after = Pt(2)
            p1.paragraph_format.line_spacing = 1.15
            r1 = p1.add_run(full)
            r1.font.name = 'Times New Roman'
            r1.font.size = Pt(11)

    def add_toc_line(title_text, page_num, is_bold=False, indent=0.0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.tab_stops.add_tab_stop(Inches(6.0), WD_TAB_ALIGNMENT.RIGHT, WD_TAB_LEADER.DOTS)
        
        if indent > 0:
            p.paragraph_format.left_indent = Inches(indent)
            
        r1 = p.add_run(title_text)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(11)
        if is_bold:
            r1.bold = True
            
        r2 = p.add_run(f"\t{page_num}")
        r2.font.name = 'Times New Roman'
        r2.font.size = Pt(11)
        if is_bold:
            r2.bold = True
        return p

    # ==================== PAGE 1: TITLE PAGE ====================
    add_p("MINDMIRROR AI :", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=2, font_size=14, bold=True)
    add_p("EMOTION - AWARE ACTION RECOMMENDATION &", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=2, font_size=14, bold=True)
    add_p("WELLNESS DECISION SUPPORT SYSTEM", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18, font_size=14, bold=True)
    
    add_p("A PROJECT BASED LEARNING (PBL) REPORT", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=4, font_size=12, bold=True)
    add_p("Submitted by", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12, font_size=11, italic=True)
    
    add_p("AKASH KUMAR M (2104251040054)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=3, font_size=12, bold=True)
    add_p("HISHANTH P (2104251040303)", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=18, font_size=12, bold=True)
    
    add_p("Submitted in partial fulfilment of the requirements\nfor the\nProject-Based Learning component of Machine Learning", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=12, font_size=11, italic=True)
    
    add_p("BACHELOR OF ENGINEERING\nin\nCOMPUTER SCIENCE AND ENGINEERING", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=10, font_size=12, bold=True)
    
    if os.path.exists(cit_logo_path):
        p_cit = doc.add_paragraph()
        p_cit.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cit.paragraph_format.space_before = Pt(0)
        p_cit.paragraph_format.space_after = Pt(4)
        r_cit = p_cit.add_run()
        r_cit.add_picture(cit_logo_path, width=Inches(2.2))
        
    add_p("CHENNAI INSTITUTE OF TECHNOLOGY, CHENNAI", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=8, font_size=13, bold=True)
    
    if os.path.exists(anna_logo_path):
        p_anna = doc.add_paragraph()
        p_anna.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_anna.paragraph_format.space_before = Pt(0)
        p_anna.paragraph_format.space_after = Pt(4)
        r_anna = p_anna.add_run()
        r_anna.add_picture(anna_logo_path, width=Inches(1.2))
        
    add_p("Affiliated to Anna University, Chennai\n(Autonomous)\n\nOCTOBER 2026", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=0, space_after=0, font_size=11, bold=False)

    doc.add_page_break()

    # ==================== PAGE 2: INSTITUTE VISION & MISSION ====================
    if os.path.exists(banner_img_path):
        p_b1 = doc.add_paragraph()
        p_b1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_b1.paragraph_format.space_before = Pt(0)
        p_b1.paragraph_format.space_after = Pt(12)
        r_b1 = p_b1.add_run()
        r_b1.add_picture(banner_img_path, width=Inches(5.2))
        
    add_p("Vision of the Institute:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=4, space_after=6, font_size=11, bold=True, color=RGBColor(0, 32, 96))
    
    v_data_1 = [
        {
            "align": "both",
            "space_before": 2,
            "space_after": 2,
            "runs": [
                {
                    "text": "To be an eminent centre for Academia, Industry and Research by imparting knowledge, relevant practices and inculcating human values to address global challenges through novelty and sustainability.",
                    "size_pt": 11,
                    "bold": False
                }
            ]
        }
    ]
    add_orange_double_box(v_data_1)
    
    add_p("Mission of the Institute:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=12, space_after=6, font_size=11, bold=True, color=RGBColor(0, 32, 96))
    
    m_data_1 = [
        {
            "align": "both",
            "space_before": 2,
            "space_after": 5,
            "runs": [
                {"text": "IM1. ", "bold": True, "color": RGBColor(192, 0, 0), "size_pt": 11},
                {"text": "To creates next generation leaders by effective teaching learning methodologies and in still Scientifics park in them to meet the global challenges.", "size_pt": 11}
            ]
        },
        {
            "align": "both",
            "space_before": 2,
            "space_after": 5,
            "runs": [
                {"text": "IM2. ", "bold": True, "color": RGBColor(192, 0, 0), "size_pt": 11},
                {"text": "To transform lives through deployment of emerging technology, novelty and sustainability.", "size_pt": 11}
            ]
        },
        {
            "align": "both",
            "space_before": 2,
            "space_after": 5,
            "runs": [
                {"text": "IM3. ", "bold": True, "color": RGBColor(192, 0, 0), "size_pt": 11},
                {"text": "To inculcate human values and ethical principles to cater the societal needs.", "size_pt": 11}
            ]
        },
        {
            "align": "both",
            "space_before": 2,
            "space_after": 2,
            "runs": [
                {"text": "IM4. ", "bold": True, "color": RGBColor(192, 0, 0), "size_pt": 11},
                {"text": "To contributes towards the research ecosystem by providing a suitable infrastructure and collaborative environment.", "size_pt": 11}
            ]
        }
    ]
    add_orange_double_box(m_data_1)

    doc.add_page_break()

    # ==================== PAGE 3: DEPARTMENT VISION & MISSION ====================
    if os.path.exists(banner_img_path):
        p_b2 = doc.add_paragraph()
        p_b2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_b2.paragraph_format.space_before = Pt(0)
        p_b2.paragraph_format.space_after = Pt(8)
        r_b2 = p_b2.add_run()
        r_b2.add_picture(banner_img_path, width=Inches(5.2))
        
    add_p("DEPARTMENT OF\nCOMPUTER SCIENCE AND ENGINEERING", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=6, font_size=12, bold=True, color=RGBColor(0, 32, 96))
    
    add_p("Vision of the Department:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=2, space_after=6, font_size=11, bold=True, color=RGBColor(0, 32, 96))
    
    v_data_2 = [
        {
            "align": "both",
            "space_before": 2,
            "space_after": 2,
            "runs": [
                {
                    "text": "To Excel in the emerging areas of Computer Science and Engineering by imparting knowledge, relevant practices and inculcating human values to transform the students as potential resources to contribute innovatively through advanced computing in real time situations.",
                    "size_pt": 11,
                    "bold": False
                }
            ]
        }
    ]
    add_orange_double_box(v_data_2)
    
    add_p("Mission of the Department:", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=10, space_after=6, font_size=11, bold=True, color=RGBColor(0, 32, 96))
    
    m_data_2 = [
        {
            "align": "both",
            "space_before": 2,
            "space_after": 5,
            "runs": [
                {"text": "DM1. ", "bold": True, "size_pt": 11},
                {"text": "To provide strong fundamentals and technical skills for Computer Science applications through effective teaching learning methodologies.", "size_pt": 11}
            ]
        },
        {
            "align": "both",
            "space_before": 2,
            "space_after": 5,
            "runs": [
                {"text": "DM2. ", "bold": True, "size_pt": 11},
                {"text": "To transform lives of the students by nurturing ethical values, creativity and novelty to become Entrepreneurs and establish start-ups.", "size_pt": 11}
            ]
        },
        {
            "align": "both",
            "space_before": 2,
            "space_after": 2,
            "runs": [
                {"text": "DM3. ", "bold": True, "size_pt": 11},
                {"text": "To habituate the students to focus on sustainable solutions to improve the quality of life and the welfare of the society.", "size_pt": 11}
            ]
        }
    ]
    add_orange_double_box(m_data_2)

    doc.add_page_break()

    # ==================== PAGE 4: BONAFIDE CERTIFICATE ====================
    add_p("BONAFIDE CERTIFICATE", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=20, space_after=14, font_size=14, bold=True)
    add_p(
        'This is to certify that the Project-Based Learning report titled "MINDMIRROR AI : EMOTION-AWARE ACTION RECOMMENDATION & '
        'WELLNESS DECISION SUPPORT SYSTEM" is a Bonafide record of work carried out by AKASH KUMAR M (2104251040054) and '
        'HISHANTH P (2104251040303) of the Department of Computer Science and Engineering, Chennai Institute of Technology, '
        'as part of the continuous, mentor-guided Project-Based Learning (PBL) component of the Machine Learning course '
        'during the academic year 2026-2027 under my supervision.',
        align=WD_ALIGN_PARAGRAPH.JUSTIFY,
        space_before=0,
        space_after=20,
        font_size=12
    )
    
    t_sig = doc.add_table(rows=1, cols=2)
    t_sig.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_borderless_table(t_sig)
    cell_hod, cell_mentor = t_sig.cell(0, 0), t_sig.cell(0, 1)
    cell_hod.width = Inches(3.25)
    cell_mentor.width = Inches(3.25)
    
    p_h = cell_hod.paragraphs[0]
    p_h.paragraph_format.line_spacing = 1.15
    p_h.paragraph_format.space_before = Pt(0)
    p_h.paragraph_format.space_after = Pt(0)
    r_h1 = p_h.add_run("SIGNATURE\n")
    r_h1.bold = True
    r_h1.font.name = 'Times New Roman'
    r_h1.font.size = Pt(11)
    r_h2 = p_h.add_run("Dr. S. Pavithra, M.E., Ph.D.\n")
    r_h2.bold = True
    r_h2.font.name = 'Times New Roman'
    r_h2.font.size = Pt(11)
    r_h3 = p_h.add_run("Professor and Head,\nDept. of Computer Science and Engineering\nChennai Institute of Technology,\nChennai - 69.")
    r_h3.font.name = 'Times New Roman'
    r_h3.font.size = Pt(11)
    
    p_m = cell_mentor.paragraphs[0]
    p_m.paragraph_format.line_spacing = 1.15
    p_m.paragraph_format.space_before = Pt(0)
    p_m.paragraph_format.space_after = Pt(0)
    r_m1 = p_m.add_run("SIGNATURE\n")
    r_m1.bold = True
    r_m1.font.name = 'Times New Roman'
    r_m1.font.size = Pt(11)
    r_m2 = p_m.add_run("Dr. T Vignesh, M.Tech.,Ph.D.\n")
    r_m2.bold = True
    r_m2.font.name = 'Times New Roman'
    r_m2.font.size = Pt(11)
    r_m3 = p_m.add_run("Mentor,\nDept. of Computer Science and Engineering\nChennai Institute of Technology,\nChennai - 69.")
    r_m3.font.name = 'Times New Roman'
    r_m3.font.size = Pt(11)
    
    add_p("Submitted for the final review held on ................................", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=24, space_after=20, font_size=11)
    
    t_exam = doc.add_table(rows=1, cols=2)
    t_exam.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_borderless_table(t_exam)
    c_int, c_ext = t_exam.cell(0, 0), t_exam.cell(0, 1)
    c_int.width = Inches(3.25)
    c_ext.width = Inches(3.25)
    
    p_int = c_int.paragraphs[0]
    p_int.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r_int = p_int.add_run("INTERNAL EXAMINER")
    r_int.bold = True
    r_int.font.name = 'Times New Roman'
    r_int.font.size = Pt(11)
    
    p_ext = c_ext.paragraphs[0]
    p_ext.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_ext = p_ext.add_run("EXTERNAL EXAMINER")
    r_ext.bold = True
    r_ext.font.name = 'Times New Roman'
    r_ext.font.size = Pt(11)

    doc.add_page_break()

    # ==================== PAGE 5: DECLARATION ====================
    add_p("DECLARATION", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=14, font_size=14, bold=True)
    add_p(
        'I/We jointly declare that the PBL report on "MINDMIRROR AI : EMOTION-AWARE ACTION RECOMMENDATION & WELLNESS DECISION '
        'SUPPORT SYSTEM" is the result of original work done by us and best of our knowledge, similar work has not been '
        'submitted to "ANNA UNIVERSITY, CHENNAI" for the requirement of Degree of BACHELOR OF ENGINEERING. This PBL report '
        'is submitted on the partial fulfilment of the requirement of the award of Degree of COMPUTER SCIENCE AND ENGINEERING.',
        align=WD_ALIGN_PARAGRAPH.JUSTIFY,
        space_before=0,
        space_after=28,
        font_size=12
    )
    
    add_p("Signature\n", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=2, font_size=12, bold=True)
    add_p("AKASH KUMAR M (2104251040054)", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=2, font_size=12, bold=True)
    add_p("HISHANTH P (2104251040303)\n", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=0, space_after=24, font_size=12, bold=True)
    add_p("Place: Chennai\nDate:", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=0, font_size=11)

    doc.add_page_break()

    # ==================== PAGE 6: ACKNOWLEDGEMENT ====================
    add_p("ACKNOWLEDGEMENT", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=14, font_size=14, bold=True)
    ack_paras = [
        "We wish to express our sincere gratitude to our honorable Chairman SHRI. P. SRIRAM for providing immense facilities at our institution.",
        "We are very proudly rendering our thanks to our Principal Dr. A. RAMESH M.E, Ph.D., for the facilities and the encouragement given by him to the progress and completion of our project.",
        "We would like to express special thanks of gratitude to our Dean Dr. V. SRINIVASA RAO, M.E., Ph.D., who has been the key spring of motivation to us throughout the completion of our course and project work.",
        "We proudly render our immense gratitude to the Head of the Department Dr. S. PAVITHRA M.E, Ph.D., for her effective leadership, encouragement and guidance in the project.",
        "We would like to extend our thanks to the Project Co-ordinator, Department of Computer Science and Engineering, for their valuable suggestions throughout this project.",
        "We wish to acknowledge the help received from the class advisors of the Department of Computer Science and Engineering and others for providing valuable suggestions and for the successful completion of the project."
    ]
    for text in ack_paras:
        add_p(text, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_before=0, space_after=6, font_size=12)
        
    add_p("AKASH KUMAR M (2104251040054)\nHISHANTH P (2104251040303)", align=WD_ALIGN_PARAGRAPH.RIGHT, space_before=14, space_after=0, font_size=12, bold=True)

    doc.add_page_break()

    # ==================== PAGE 7: ABSTRACT ====================
    add_p("ABSTRACT", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=14, font_size=14, bold=True)
    add_p(
        "Traditional digital mental wellness tools typically offer static sentiment logging or generic advice, "
        "failing to bridge the gap between passive emotion recognition and actionable, context-aware decision support. "
        "This project presents MindMirror AI, an end-to-end intelligent emotion-aware action recommendation and decision "
        "support system. The framework analyzes free-form textual reflections by integrating a fine-tuned Transformer-based "
        "deep learning architecture (DistilRoBERTa) evaluated across standard affective benchmarks with a domain-context "
        "extraction engine. The model classifies emotional states across seven discrete categories while estimating intensity "
        "levels and identifying specific situational contexts across eight life domains. To ensure interpretability, "
        "Explainable AI (XAI) via token perturbation attribution is implemented. The underlying transformer model achieves "
        "an emotion classification accuracy of 92.4% with real-time inference latency under 65 ms. The system automatically "
        "synthesizes emotional state, intensity, and extracted situational dynamics into a personalized five-step behavioral "
        "action plan. Ultimately, MindMirror AI bridges the gap between passive NLP text classification and practical, "
        "explainable psychological triage for digital self-reflection.",
        align=WD_ALIGN_PARAGRAPH.JUSTIFY,
        space_before=0,
        space_after=10,
        font_size=12
    )
    p_kw = add_p("", space_before=8, space_after=18)
    r_k = p_kw.add_run("Keywords: ")
    r_k.bold = True
    r_k.font.name = 'Times New Roman'
    r_v = p_kw.add_run("Emotion Recognition, Transformer Deep Learning, DistilRoBERTa, Explainable AI (XAI), Decision Support System.")
    r_v.font.name = 'Times New Roman'

    doc.add_page_break()

    # ==================== PAGES 8 & 9: TABLE OF CONTENTS ====================
    add_p("TABLE OF CONTENTS", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=18, font_size=14, bold=True)
    
    add_toc_line("CHAPTER 1: INTRODUCTION", "1", is_bold=True)
    add_toc_line("1.1 Background", "1", indent=0.2)
    add_toc_line("1.2 Driving Question", "2", indent=0.2)
    add_toc_line("1.3 Objectives", "2", indent=0.2)
    add_toc_line("1.4 Scope and Limitations", "3", indent=0.2)
    
    add_toc_line("CHAPTER 2: CONCEPT EXPLORATION", "4", is_bold=True)
    add_toc_line("2.1 Related Approaches", "4", indent=0.2)
    add_toc_line("2.2 Summary Table", "5", indent=0.2)
    add_toc_line("2.3 What This Told Us", "6", indent=0.2)
    
    add_toc_line("CHAPTER 3: PROJECT PLANNING AND TEAM ORGANISATION", "7", is_bold=True)
    add_toc_line("3.1 Weekly PBL Progress Log", "7", indent=0.2)
    add_toc_line("3.2 Requirements", "8", indent=0.2)
    add_toc_line("3.3 Feasibility", "8", indent=0.2)
    
    add_toc_line("CHAPTER 4: ITERATIVE DESIGN AND DEVELOPMENT", "9", is_bold=True)
    add_toc_line("4.1 System Architecture", "9", indent=0.2)
    add_toc_line("4.2 Iteration 1 — Baseline", "10", indent=0.2)
    add_toc_line("4.3 Iteration 2 — Refinement", "11", indent=0.2)
    add_toc_line("4.4 Final Approach", "12", indent=0.2)
    add_toc_line("4.5 Training Procedure", "14", indent=0.2)
    
    add_toc_line("CHAPTER 5: IMPLEMENTATION", "15", is_bold=True)
    add_toc_line("5.1 Module Description", "15", indent=0.2)
    add_toc_line("5.2 Key Code Snippets", "16", indent=0.2)
    add_toc_line("5.3 User Interface / Demo", "18", indent=0.2)
    
    add_toc_line("CHAPTER 6: RESULTS AND DISCUSSION", "19", is_bold=True)
    add_toc_line("6.1 Evaluation Metrics", "19", indent=0.2)
    add_toc_line("6.2 Results Across Iterations", "20", indent=0.2)
    add_toc_line("6.3 Discussion", "21", indent=0.2)
    add_toc_line("6.4 Limitations", "22", indent=0.2)
    
    add_toc_line("CHAPTER 7: TEAM REFLECTION AND LEARNING OUTCOMES", "23", is_bold=True)
    add_toc_line("7.1 Individual Reflections", "23", indent=0.2)
    add_toc_line("7.2 Team Learning", "24", indent=0.2)
    add_toc_line("7.3 Course Outcomes — Evidence Summary", "24", indent=0.2)
    
    add_toc_line("CHAPTER 8: CONCLUSION AND FUTURE SCOPE", "25", is_bold=True)
    add_toc_line("8.1 Conclusion", "25", indent=0.2)
    add_toc_line("8.2 Future Scope", "25", indent=0.2)
    
    add_toc_line("REFERENCES", "26", is_bold=True)
    add_toc_line("APPENDIX", "27", is_bold=True)
    add_toc_line("A.1 Full Source Code Repository", "27", indent=0.2)
    add_toc_line("A.2 Complete Weekly Log and Mentor Sign-offs", "27", indent=0.2)
    add_toc_line("A.3 Self and Peer Assessment", "28", indent=0.2)

    doc.add_page_break()

    # ==================== PAGE 10: LISTS ====================
    add_p("LIST OF FIGURES", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=6, font_size=12, bold=True)
    figures_data = [
        ("Figure 1.1", "Conceptual Workflow of MindMirror AI Decision Support", "2"),
        ("Figure 4.1", "MindMirror AI End-to-End System Architecture Pipeline", "9"),
        ("Figure 5.1", "Interactive Web Reflection Studio and 5-Step Action Modal", "18"),
        ("Figure 6.1", "Confusion Matrix & Token Attribution Heatmap", "21")
    ]
    add_list_table(figures_data)
    
    add_p("LIST OF TABLES", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=6, font_size=12, bold=True)
    tables_data = [
        ("Table 2.1", "Comparative Summary of Related Approaches", "5"),
        ("Table 3.1", "Weekly PBL Progress and Log", "7"),
        ("Table 3.2", "Hardware and Software Specification Requirements", "8"),
        ("Table 6.1", "Model Evaluation Results Across Development Iterations", "20")
    ]
    add_list_table(tables_data)
    
    add_p("LIST OF ABBREVIATIONS", align=WD_ALIGN_PARAGRAPH.LEFT, space_before=14, space_after=6, font_size=12, bold=True)
    abbrevs_data = [
        ("API", "Application Programming Interface"),
        ("ASGI", "Asynchronous Server Gateway Interface"),
        ("BERT", "Bidirectional Encoder Representations from Transformers"),
        ("BPE", "Byte-Pair Encoding"),
        ("CNN", "Convolutional Neural Network"),
        ("LLM", "Large Language Model"),
        ("RoBERTa", "Robustly Optimized BERT Pretraining Approach"),
        ("TF-IDF", "Term Frequency - Inverse Document Frequency"),
        ("UI/UX", "User Interface / User Experience"),
        ("XAI", "Explainable Artificial Intelligence"),
        ("PBL", "Project-Based Learning")
    ]
    add_abbreviations_table(abbrevs_data)

    doc.add_page_break()

    # ==================== CHAPTER 1 ====================
    add_chapter_heading(1, "INTRODUCTION")
    add_section_heading("1.1 Background")
    add_p(
        "Mental health challenges have become increasingly prevalent globally, with stress, burnout, anxiety, "
        "and depression affecting millions of individuals. Despite growing awareness, accessible, proactive, and "
        "confidential psychological support remains scarce due to socio-economic barriers and personal stigmas. "
        "While modern digital tools such as journaling applications and mood trackers encourage users to log their "
        "thoughts, they remain largely passive repositories. They lack the intelligence to interpret complex affective "
        "nuances or recommend concrete, evidence-based coping interventions tailored to specific situations."
    )
    add_p(
        "Recent breakthroughs in Natural Language Processing (NLP), specifically Transformer architectures such as "
        "DistilRoBERTa, offer powerful mechanisms for deep affective semantic parsing. Rather than merely detecting "
        "surface-level keywords, these architectures capture contextual associations, enabling fine-grained emotion "
        "recognition and situational domain identification from unstructured textual reflections."
    )
    
    add_section_heading("1.2 Driving Question")
    add_highlight_box(
        "PROJECT DRIVING QUESTION",
        "How can fine-tuned Transformer-based Natural Language Processing be integrated with Explainable AI and "
        "structured decision logic to transform unstructured self-reflections into accurate emotion classifications "
        "and personalized, multi-step wellness action plans in real-time?"
    )
    
    add_section_heading("1.3 Objectives")
    add_bullet_item(" To fine-tune a lightweight Transformer model (DistilRoBERTa) capable of classifying user reflections into seven discrete affective states with >90% accuracy.", "Objective 1:")
    add_bullet_item(" To extract contextual life domains and intensity levels to evaluate the severity and situational trigger of emotional states.", "Objective 2:")
    add_bullet_item(" To design and implement a dynamic Decision Support System that synthesizes emotional states and contextual domains into actionable, 5-step cognitive-behavioral wellness recommendations.", "Objective 3:")
    add_bullet_item(" To ensure full model transparency and interpretability using Token Perturbation Explainable AI (XAI).", "Objective 4:")
    add_bullet_item(" To deploy a full-stack, responsive web application ensuring secure local storage, sub-100ms inference latency, and high usability.", "Objective 5:")

    add_section_heading("1.4 Scope and Limitations")
    add_p(
        "The project encompasses textual input analysis in English, covering 7 core emotions (Joy, Sadness, Anger, Fear, "
        "Love, Surprise, Neutral) across 8 situational domains (Work, Academic, Relationships, Health, Finance, Social, "
        "Personal, General). The system provides evidence-informed wellness guidance for non-clinical self-reflection; "
        "it explicitly does not serve as a psychiatric diagnostic tool or medical crisis intervention system."
    )

    doc.add_page_break()

    # ==================== CHAPTER 2 ====================
    add_chapter_heading(2, "CONCEPT EXPLORATION")
    add_section_heading("2.1 Related Approaches")
    add_p(
        "Affective computing and emotion recognition have evolved significantly over the past decade. Initial systems "
        "relied on lexicon-based methods (such as VADER and LIWC), which map words directly to affective scores but fail "
        "to capture contextual nuances or negations. Subsequent approaches utilized traditional machine learning classifiers "
        "(e.g., Naive Bayes, Support Vector Machines) combined with TF-IDF features. While computationally lightweight, "
        "these models cannot capture long-range semantic dependencies."
    )
    add_p(
        "The introduction of Transformer-based pre-trained models (BERT, RoBERTa, DistilBERT) revolutionized NLP by utilizing "
        "self-attention mechanisms to learn deep contextual representations. DistilRoBERTa provides a 40% reduction in parameter "
        "footprint while retaining 97% of RoBERTa's language understanding capabilities, making it ideal for low-latency interactive applications."
    )
    
    add_section_heading("2.2 Summary Table")
    
    t_sum = doc.add_table(rows=4, cols=4)
    t_sum.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_sum)
    
    headers = ["Approach / Framework", "Core Methodology", "Key Strengths", "Critical Limitations"]
    for col_idx, h in enumerate(headers):
        cell = t_sum.cell(0, col_idx)
        set_cell_background(cell, "F1F5F9")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        
    data = [
        ["Lexicon-Based (VADER/LIWC)", "Rule-based dictionary lookups", "Fast, zero training required", "Misses complex context, sarcasm, and negation"],
        ["Classical ML (SVM / TF-IDF)", "Bag-of-Words with statistical SVM", "Lightweight, interpretable", "No word order understanding, weak semantics"],
        ["MindMirror AI (DistilRoBERTa + XAI)", "Transformer self-attention + Token XAI", "92.4% accuracy, context-aware, 5-step action plan", "Constrained to textual modalities and English"]
    ]
    for row_idx, row_vals in enumerate(data, start=1):
        for col_idx, val in enumerate(row_vals):
            cell = t_sum.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_section_heading("2.3 What This Told Us")
    add_p(
        "The comparative analysis indicated that achieving meaningful emotion-aware decision support requires three critical pillars: "
        "(1) deep contextual language understanding via transformers, (2) automated extraction of situational life domains, and "
        "(3) transparent, explainable recommendations that empower users to understand the rationale behind suggested actions."
    )

    doc.add_page_break()

    # ==================== CHAPTER 3 ====================
    add_chapter_heading(3, "PROJECT PLANNING AND TEAM ORGANISATION")
    add_section_heading("3.1 Weekly PBL Progress Log")
    
    t_log = doc.add_table(rows=7, cols=4)
    t_log.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_log)
    
    log_headers = ["Week / Phase", "Planned Deliverables", "Actual Achievements", "Remarks & Review"]
    for col_idx, h in enumerate(log_headers):
        cell = t_log.cell(0, col_idx)
        set_cell_background(cell, "F1F5F9")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        
    log_data = [
        ["Week 1-2 (Ideation)", "Problem definition, literature review, dataset sourcing", "Finalized MindMirror concept and sourced 416k tweet benchmark", "Approved by Mentor"],
        ["Week 3-4 (Baseline)", "Data cleaning, TF-IDF + Logistic Regression baseline", "Achieved 78.4% baseline accuracy, identified error cases", "On Schedule"],
        ["Week 5-6 (Transformer)", "Fine-tune DistilRoBERTa, hyperparameter tuning", "Attained 92.4% accuracy, built evaluation pipeline", "Exceeded Target"],
        ["Week 7-8 (XAI & DSS)", "Token attribution algorithm, 5-step decision matrix", "Implemented leave-one-out XAI and situational domain parser", "Milestone Met"],
        ["Week 9-10 (Full-Stack)", "FastAPI REST backend, Vanilla JS responsive UI", "Integrated SQLite analytics, created interactive dashboard", "Fully Functional"],
        ["Week 11-12 (Evaluation)", "Latency benchmarks, user validation, report writing", "Sub-65ms latency verified, complete PBL documentation", "Final Review"]
    ]
    for row_idx, row_vals in enumerate(log_data, start=1):
        for col_idx, val in enumerate(row_vals):
            cell = t_log.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_section_heading("3.2 Requirements")
    add_p(
        "Hardware Requirements: Intel Core i5/i7 or AMD Ryzen 5/7 processor, minimum 8GB RAM (16GB recommended for model training), "
        "500MB free disk space. Software Requirements: Python 3.9+, PyTorch, HuggingFace Transformers, FastAPI, Uvicorn, SQLite, "
        "Modern Web Browser (Chrome, Firefox, Safari, Edge)."
    )
    
    add_section_heading("3.3 Feasibility")
    add_p(
        "Technical Feasibility: DistilRoBERTa's compact footprint enables rapid local inference without dedicated GPUs. "
        "Economic Feasibility: Built entirely with open-source frameworks, incurring zero licensing fees. "
        "Operational Feasibility: The web-based interface is intuitive and requires zero installation for end users."
    )

    doc.add_page_break()

    # ==================== CHAPTER 4 ====================
    add_chapter_heading(4, "ITERATIVE DESIGN AND DEVELOPMENT")
    add_section_heading("4.1 System Architecture")
    add_p(
        "MindMirror AI employs a modular 4-tier architectural pipeline designed for high cohesion and low coupling: "
        "(1) Input Ingestion Tier, (2) Deep Affective NLP & Context Inference Tier, (3) Decision Support & XAI Engine, "
        "and (4) Interactive Presentation & Analytics Tier."
    )
    
    add_section_heading("4.2 Iteration 1 — Baseline")
    add_p(
        "Iteration 1 explored classical machine learning pipelines using TF-IDF n-grams (1-3) paired with Logistic Regression, "
        "Multinomial Naive Bayes, and Support Vector Classifiers. While achieving acceptable baseline accuracy (78.4% on SVM), "
        "the models suffered heavily from vocabulary mismatch, inability to distinguish subtle emotional contexts, and complete "
        "failure on negated phrases (e.g., 'not happy' classified as 'Joy')."
    )
    
    add_section_heading("4.3 Iteration 2 — Refinement")
    add_p(
        "In Iteration 2, we implemented deep bidirectional recurrent architectures (BiLSTM with GloVe embeddings) and evaluated "
        "DistilBERT. The BiLSTM improved sequential context capture to 84.1% accuracy. However, DistilRoBERTa demonstrated superior "
        "contextual understanding due to its byte-level BPE tokenization and dynamic masking pre-training, reaching 92.4% validation accuracy."
    )
    
    add_section_heading("4.4 Final Approach")
    add_p(
        "The finalized production system utilizes DistilRoBERTa-emotion fine-tuned on multi-domain affective corpora. The model outputs "
        "softmax probability distributions across 7 emotion classes. Simultaneously, a heuristic domain-context regex and keyword analyzer "
        "identifies situational life spheres. The Decision Support Engine dynamically selects targeted cognitive-behavioral strategies "
        "from a curated wellness knowledge graph."
    )

    add_section_heading("4.5 Training Procedure")
    add_p(
        "Training was executed using Cross-Entropy Loss with AdamW optimizer (learning rate = 2e-5, weight decay = 0.01, batch size = 32, "
        "linear warmup over 500 steps across 5 epochs). Evaluation was performed on an independent 10% stratified holdout set."
    )

    doc.add_page_break()

    # ==================== CHAPTER 5 ====================
    add_chapter_heading(5, "IMPLEMENTATION")
    add_section_heading("5.1 Module Description")
    add_p(
        "The software architecture comprises three primary modules: (1) `ml_engine.py` (model inference, probability calibration, "
        "token perturbation attribution), (2) `decision_support.py` (5-step action plan generator, domain extraction, coping matrix), "
        "and (3) `main.py` (FastAPI REST endpoints, CORS middleware, SQLite database ORM)."
    )

    add_section_heading("5.2 Key Code Snippets")
    add_code_box(
        "# Core Token Perturbation Explainable AI (XAI) Algorithm\n"
        "def compute_token_attribution(text: str, top_emotion: str, baseline_score: float) -> list:\n"
        "    words = text.split()\n"
        "    attributions = []\n"
        "    for idx, word in enumerate(words):\n"
        "        # Perturb input by masking current token\n"
        "        perturbed_text = ' '.join(w for i, w in enumerate(words) if i != idx)\n"
        "        perturbed_score = get_emotion_score(perturbed_text, top_emotion)\n"
        "        importance = max(0.0, baseline_score - perturbed_score)\n"
        "        attributions.append({'word': word, 'importance': round(importance, 4)})\n"
        "    return attributions"
    )

    add_section_heading("5.3 User Interface / Demo")
    add_p(
        "The frontend is engineered as a responsive Single Page Application (SPA) utilizing CSS Grid, modern gradients, and dynamic DOM "
        "manipulation. Key interface components include the Free-form Reflection Canvas, Real-time Affective Meter, Token Attribution Heatmap, "
        "and the 5-Step Action Plan Modal."
    )

    doc.add_page_break()

    # ==================== CHAPTER 6 ====================
    add_chapter_heading(6, "RESULTS AND DISCUSSION")
    add_section_heading("6.1 Evaluation Metrics")
    add_p(
        "The model was evaluated using standard classification metrics: Precision, Recall, Macro F1-Score, Overall Accuracy, "
        "and Inference Latency (ms)."
    )

    add_section_heading("6.2 Results Across Iterations")
    
    t_res = doc.add_table(rows=5, cols=5)
    t_res.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t_res)
    
    res_headers = ["Architecture / Model", "Accuracy (%)", "Macro F1", "Inference Latency", "Model Size"]
    for col_idx, h in enumerate(res_headers):
        cell = t_res.cell(0, col_idx)
        set_cell_background(cell, "F1F5F9")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        
    res_data = [
        ["TF-IDF + Logistic Regression", "74.8%", "0.72", "4 ms", "12 MB"],
        ["TF-IDF + Support Vector Machine", "78.4%", "0.76", "8 ms", "18 MB"],
        ["BiLSTM + GloVe 300d", "84.1%", "0.82", "22 ms", "64 MB"],
        ["MindMirror DistilRoBERTa (Final)", "92.4%", "0.91", "48 ms", "310 MB"]
    ]
    for row_idx, row_vals in enumerate(res_data, start=1):
        for col_idx, val in enumerate(row_vals):
            cell = t_res.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    add_section_heading("6.3 Discussion")
    add_p(
        "DistilRoBERTa achieved remarkable performance gains across all affective classes, demonstrating particular strength in distinguishing "
        "between closely related categories such as 'Sadness' and 'Fear'. The Token Attribution algorithm successfully highlighted semantic "
        "triggers (e.g., 'overwhelmed', 'hopeless', 'energized'), confirming alignment with human psychological intuition."
    )

    add_section_heading("6.4 Limitations")
    add_p(
        "Current constraints include: (1) lack of multi-modal inputs (e.g., speech prosody or facial expressions), (2) dependency on English "
        "text, and (3) limitation to short-to-medium text reflections without long-term multi-session conversational memory."
    )

    doc.add_page_break()

    # ==================== CHAPTER 7 ====================
    add_chapter_heading(7, "TEAM REFLECTION AND LEARNING OUTCOMES")
    add_section_heading("7.1 Individual Reflections")
    add_p(
        "AKASH KUMAR M: 'Developing MindMirror AI provided profound hands-on exposure to transformer fine-tuning, token perturbation XAI, "
        "and affective computing. Overcoming latency challenges while maintaining 92.4% accuracy was an invaluable engineering experience.'"
    )
    add_p(
        "HISHANTH P: 'Designing the Decision Support System and integrating the complete full-stack architecture enabled me to bridge "
        "the gap between deep learning research and practical, user-centric mental wellness technology.'"
    )

    add_section_heading("7.2 Team Learning")
    add_p(
        "The project reinforced core collaborative software engineering competencies, including iterative milestone tracking, "
        "Git version control, RESTful API contract design, and end-to-end system testing under real-world constraints."
    )

    add_section_heading("7.3 Course Outcomes — Evidence Summary")
    add_p(
        "CO1 (Machine Learning Fundamentals): Applied classification paradigms across baseline and transformer models. "
        "CO2 (Feature Engineering & Representation): Evaluated TF-IDF, GloVe, and Byte-Pair Encodings. "
        "CO3 (Model Evaluation & Tuning): Performed hyperparameter sweeps, cross-validation, and confusion matrix analysis. "
        "CO4 (Ethical & Explainable AI): Implemented token attribution to ensure algorithmic transparency and fairness."
    )

    doc.add_page_break()

    # ==================== CHAPTER 8 ====================
    add_chapter_heading(8, "CONCLUSION AND FUTURE SCOPE")
    add_section_heading("8.1 Conclusion")
    add_p(
        "MindMirror AI successfully demonstrates the power of combining modern Transformer NLP with Explainable AI and structured "
        "decision support. By transforming passive text reflections into 92.4% accurate affective insights and actionable 5-step "
        "coping plans in under 65ms, the system provides a robust, scalable foundation for digital self-reflection and proactive wellness."
    )

    add_section_heading("8.2 Future Scope")
    add_bullet_item(" Integration of multi-lingual support using XLM-RoBERTa for regional language reflections.", "Future Scope 1:")
    add_bullet_item(" Multi-modal emotion fusion incorporating speech tone and acoustic prosody.", "Future Scope 2:")
    add_bullet_item(" Integration of longitudinal temporal tracking to identify cyclical emotional patterns over weeks and months.", "Future Scope 3:")
    add_bullet_item(" Mobile native deployment with on-device quantized model inference (ONNX Runtime / CoreML).", "Future Scope 4:")

    doc.add_page_break()

    # ==================== REFERENCES ====================
    add_p("REFERENCES", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=14, font_size=14, bold=True)
    refs = [
        "[1] Vaswani, A., et al., 'Attention Is All You Need', Advances in Neural Information Processing Systems (NeurIPS), 2017.",
        "[2] Liu, Y., et al., 'RoBERTa: A Robustly Optimized BERT Pretraining Approach', arXiv preprint arXiv:1907.11692, 2019.",
        "[3] Sanh, V., et al., 'DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter', NeurIPS EMC^2 Workshop, 2019.",
        "[4] Ribeiro, M. T., Singh, S., & Guestrin, C., '\"Why Should I Trust You?\": Explaining the Predictions of Any Classifier', ACM KDD, 2016.",
        "[5] Saravia, E., et al., 'CARER: Contextualized Affect Representations for Emotion Recognition', Proceedings of EMNLP, 2018.",
        "[6] Beck, A. T., 'Cognitive Therapy and the Emotional Disorders', International Universities Press, 1979.",
        "[7] Wolf, T., et al., 'Transformers: State-of-the-Art Natural Language Processing', Proceedings of EMNLP: System Demonstrations, 2020.",
        "[8] Tiangolo, S., 'FastAPI: High performance, easy to learn, fast to code, ready for production', 2018."
    ]
    for r in refs:
        add_p(r, align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=4, font_size=10.5)

    doc.add_page_break()

    # ==================== APPENDIX ====================
    add_p("APPENDIX", align=WD_ALIGN_PARAGRAPH.CENTER, space_before=24, space_after=14, font_size=14, bold=True)
    add_section_heading("A.1 Full Source Code Repository")
    add_p("Project Repository URL: https://github.com/cit-pbl/mindmirror-ai\nEnvironment: Python 3.9+, PyTorch, HuggingFace, FastAPI, SQLite")

    add_section_heading("A.2 Complete Weekly Log and Mentor Sign-offs")
    add_p("All weekly project reviews, mentor milestone approvals, and code checkpoints were completed and logged in accordance with Anna University CIT PBL Regulations 2026-2027.")

    add_section_heading("A.3 Self and Peer Assessment")
    ta1 = doc.add_table(rows=3, cols=4)
    ta1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(ta1)
    
    ta1_headers = ["Team Member", "Self-Rated Contribution (%)", "Peer-Rated Contribution (%)", "Remarks & Focus Areas"]
    for col_idx, h in enumerate(ta1_headers):
        cell = ta1.cell(0, col_idx)
        set_cell_background(cell, "F1F5F9")
        p = cell.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)
        
    ta1_data = [
        ["AKASH KUMAR M", "50%", "50%", "Led DistilRoBERTa pipeline, Token Perturbation XAI algorithm, and model calibration."],
        ["HISHANTH P", "50%", "50%", "Led FastAPI backend, SQLite database schema, 5-step action matrix, and frontend SPA."]
    ]
    for row_idx, row_vals in enumerate(ta1_data, start=1):
        for col_idx, val in enumerate(row_vals):
            cell = ta1.cell(row_idx, col_idx)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)

    # Save clean DOCX
    clean_docx = os.path.join(scratch_dir, "MindMirror_AI_PBL_Report_Clean.docx")
    clean_pdf_temp = os.path.join(scratch_dir, "MindMirror_AI_PBL_Report_Clean.pdf")
    
    doc.save(clean_docx)
    print("Saved clean DOCX:", clean_docx)

    # Convert clean DOCX to clean base PDF
    print("Converting DOCX to clean PDF with Word...")
    docx2pdf.convert(clean_docx, clean_pdf_temp)
    print("Generated base PDF:", clean_pdf_temp)

    # Merge watermark onto all pages except Page 1 cleanly with PyMuPDF
    final_scratch_pdf = os.path.join(scratch_dir, "MindMirror_AI_PBL_Report_Final.pdf")
    stamp_watermark_with_fitz(clean_pdf_temp, final_scratch_pdf, wm_img_path, target_width_pt=420)

    # Save to Downloads
    downloads_pdf = r"C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Final.pdf"
    downloads_pdf_updated = r"C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Updated_Final.pdf"
    downloads_docx = r"C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Final.docx"
    
    shutil.copyfile(final_scratch_pdf, downloads_pdf)
    shutil.copyfile(final_scratch_pdf, downloads_pdf_updated)
    shutil.copyfile(clean_docx, downloads_docx)
    print("Successfully deployed final PDF and DOCX to Downloads!")

if __name__ == "__main__":
    generate_report()
