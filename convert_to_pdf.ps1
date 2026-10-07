$word = New-Object -ComObject Word.Application
$word.Visible = $false
try {
    $docx1 = "C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Final.docx"
    $pdf1 = "C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Final.pdf"
    if (Test-Path $docx1) {
        $doc1 = $word.Documents.Open($docx1)
        $doc1.SaveAs([ref]$pdf1, [ref]17)
        $doc1.Close()
        Write-Host "Exported PDF 1 successfully to: $pdf1"
    }

    $docx2 = "C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Updated_Final.docx"
    $pdf2 = "C:\Users\Dell\Downloads\MindMirror_AI_PBL_Report_Updated_Final.pdf"
    if (Test-Path $docx2) {
        $doc2 = $word.Documents.Open($docx2)
        $doc2.SaveAs([ref]$pdf2, [ref]17)
        $doc2.Close()
        Write-Host "Exported PDF 2 successfully to: $pdf2"
    }

    $docx3 = "C:\Users\Dell\.gemini\antigravity\scratch\ML project\MindMirror_AI_PBL_Report_Final.docx"
    $pdf3 = "C:\Users\Dell\.gemini\antigravity\scratch\ML project\MindMirror_AI_PBL_Report_Final.pdf"
    if (Test-Path $docx3) {
        $doc3 = $word.Documents.Open($docx3)
        $doc3.SaveAs([ref]$pdf3, [ref]17)
        $doc3.Close()
        Write-Host "Exported PDF 3 successfully to: $pdf3"
    }
} finally {
    $word.Quit()
}
