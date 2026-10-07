import docx
from docx.shared import Inches, Pt
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def add_vml_double_roundrect(p, width_pt=430, height_pt=80, stroke_color="#E36C09", stroke_weight="3.5pt", paragraphs_data=[]):
    """
    Inserts a VML rounded rectangle with DOUBLE LINES and THICKNESS.
    """
    xml_str = (
        f'<w:r {nsdecls("w")} xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">\n'
        f'  <w:pict>\n'
        f'    <v:roundrect arcsize="0.08" style="width:{width_pt}pt;height:{height_pt}pt;mso-position-horizontal:center" '
        f'      strokecolor="{stroke_color}" strokeweight="{stroke_weight}" fillcolor="#FFFFFF">\n'
        f'      <v:stroke linestyle="thinThin" joinstyle="round" color="{stroke_color}" weight="{stroke_weight}"/>\n'
        f'      <v:textbox inset="14pt,10pt,14pt,10pt">\n'
        f'        <w:txbxContent>\n'
    )
    for p_info in paragraphs_data:
        align = p_info.get("align", "both")
        sp_before = p_info.get("space_before", 0)
        sp_after = p_info.get("space_after", 40)
        xml_str += f'          <w:p><w:pPr><w:jc w:val="{align}"/><w:spacing w:before="{sp_before}" w:after="{sp_after}" w:line="240" w:lineRule="auto"/></w:pPr>\n'
        for run in p_info.get("runs", []):
            bold = '<w:b/>' if run.get("bold") else ''
            italic = '<w:i/>' if run.get("italic") else ''
            color = f'<w:color w:val="{run["color"]}"/>' if "color" in run else ''
            sz = f'<w:sz w:val="{run.get("size_half_pt", 22)}"/>'
            txt = run.get("text", "")
            txt = txt.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            xml_str += f'            <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>{bold}{italic}{color}{sz}</w:rPr><w:t>{txt}</w:t></w:r>\n'
        xml_str += '          </w:p>\n'
    xml_str += (
        '        </w:txbxContent>\n'
        '      </v:textbox>\n'
        '    </v:roundrect>\n'
        '  </w:pict>\n'
        '</w:r>'
    )
    r_elem = parse_xml(xml_str)
    p._p.append(r_elem)

doc = docx.Document()
p = doc.add_paragraph()
p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER

v_data = [
    {
        "align": "both",
        "space_before": 0,
        "space_after": 0,
        "runs": [
            {"text": "To be an eminent centre for Academia, Industry and Research by imparting knowledge, relevant practices and inculcating human values to address global challenges through novelty and sustainability.", "size_half_pt": 21, "bold": False}
        ]
    }
]
add_vml_double_roundrect(p, width_pt=430, height_pt=75, stroke_color="#E36C09", stroke_weight="3.5pt", paragraphs_data=v_data)

doc.save(r"C:\Users\Dell\.gemini\antigravity\scratch\ML project\test_double_line.docx")
print("Double line VML roundrect created successfully!")
