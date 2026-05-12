$word = New-Object -ComObject Word.Application
$word.Visible = $false
$doc = $word.Documents.Open("C:\Users\rosar\Documents\GitHub\engineer_website\Presentazione studio.docx")
$text = $doc.Content.Text
$text | Out-File -FilePath "C:\Users\rosar\Documents\GitHub\engineer_website\.gemini\docx_content.txt" -Encoding UTF8
$doc.Close()
$word.Quit()
