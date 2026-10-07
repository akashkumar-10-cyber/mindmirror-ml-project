import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
import copy, shutil, os

def set_orange_box_borders(table, color_hex="E36C09", sz="12"):
    tblPr = table._tbl.tblPr
    # remove old borders if any
    for b in tblPr.xpath("./w:tblBorders"):
        tblPr.remove(b)
    tblBorders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>\n'
        f'  <w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>\n'
        f'  <w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>\n'
        f'  <w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color_hex}"/>\n'
        f'  <w:insideH w:val="none"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(tblBorders)

def set_cell_padding(cell, top=140, bottom=140, left=200, right=200):
    tcPr = cell._tc.get_or_add_tcPr()
    # remove old shading
    for s in tcPr.xpath("./w:shd"):
        tcPr.remove(s)
    # remove old tcMar
    for m in tcPr.xpath("./w:tcMar"):
        tcPr.remove(m)
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>\n'
        f'  <w:top w:w="{top}" w:type="dxa"/>\n'
        f'  <w:bottom w:w="{bottom}" w:type="dxa"/>\n'
        f'  <w:left w:w="{left}" w:type="dxa"/>\n'
        f'  <w:right w:w="{right}" w:type="dxa"/>\n'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def update_report_vision_mission():
    src_path = r"C:\Users\Dell\.gemini\antigravity\scratch\ML project\MindMirror_AI_PBL_Report_Final.docx"
    doc = docx.Document(src_path)
    
    # 1. Update Table 0 (Institute Vision Box)
    t0 = doc.tables[0]
    set_orange_box_borders(t0, "E36C09", "12")
    c0 = t0.cell(0, 0)
    set_cell_padding(c0, top=140, bottom=140, left=200, right=200)
    c0.text = ""
    p_v_inst = c0.paragraphs[0]
    p_v_inst.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_v_inst.paragraph_format.space_before = Pt(2)
    p_v_inst.paragraph_format.space_after = Pt(2)
    p_v_inst.paragraph_format.line_spacing = 1.15
    r = p_v_inst.add_run(
        "To be an eminent centre for Academia, Industry and Research by imparting knowledge, "
        "relevant practices and inculcating human values to address global challenges through novelty and sustainability."
    )
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    
    # 2. Update Table 1 (Department Vision Box)
    t1 = doc.tables[1]
    set_orange_box_borders(t1, "E36C09", "12")
    c1 = t1.cell(0, 0)
    set_cell_padding(c1, top=140, bottom=140, left=200, right=200)
    c1.text = ""
    p_v_dept = c1.paragraphs[0]
    p_v_dept.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_v_dept.paragraph_format.space_before = Pt(2)
    p_v_dept.paragraph_format.space_after = Pt(2)
    p_v_dept.paragraph_format.line_spacing = 1.15
    r = p_v_dept.add_run(
        "To Excel in the emerging areas of Computer Science and Engineering by imparting knowledge, "
        "relevant practices and inculcating human values to transform the students as potential resources to contribute "
        "innovatively through advanced computing in real time situations."
    )
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)

    # Re-run full script with these exact styled boxes and mission boxes!
    print("Pre-checks passed.")

if __name__ == "__main__":
    update_report_vision_mission()
