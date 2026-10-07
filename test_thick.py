import docx
from docx.shared import Inches, Pt
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def test_thick_double_box():
    doc = docx.Document()
    p = doc.add_paragraph()
    p.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    
    xml_str = (
        f'<w:r {nsdecls("w")} xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">\n'
        f'  <w:pict>\n'
        f'    <v:roundrect arcsize="0.1" style="width:440pt;height:75pt;mso-position-horizontal:center" '
        f'      strokecolor="#E36C09" strokeweight="5.5pt" fillcolor="#FFFFFF">\n'
        f'      <v:stroke linestyle="thinThin" joinstyle="round" color="#E36C09" weight="5.5pt"/>\n'
        f'      <v:textbox inset="14pt,10pt,14pt,10pt">\n'
        f'        <w:txbxContent>\n'
        f'          <w:p><w:pPr><w:jc w:val="both"/><w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>\n'
        f'            <w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="21"/></w:rPr>'
        f'              <w:t>To be an eminent centre for Academia, Industry and Research by imparting knowledge, relevant practices and inculcating human values to address global challenges through novelty and sustainability.</w:t>'
        f'            </w:r>\n'
        f'          </w:p>\n'
        f'        </w:txbxContent>\n'
        f'      </v:textbox>\n'
        f'    </v:roundrect>\n'
        f'  </w:pict>\n'
        f'</w:r>'
    )
    p._p.append(parse_xml(xml_str))
    doc.save(r"C:\Users\Dell\.gemini\antigravity\scratch\ML project\test_thick_double.docx")
    print("Thick double box created successfully!")

if __name__ == "__main__":
    test_thick_double_box()
