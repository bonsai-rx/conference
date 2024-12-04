Get-ChildItem -Filter "*.md" | 
Foreach-Object {
    $output = [System.IO.Path]::ChangeExtension($_.Name, ".pptx")
    $output = [System.IO.Path]::Combine("slides", $output)
    pandoc -o $output $_.Name
}