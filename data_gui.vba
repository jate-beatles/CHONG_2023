Sub SelectData()
    Dim lastRow As Long
    Dim dataRange As Range
    Dim sheet As Worksheet
    
    ' Set the number of columns to select
    Const numColumns As Long = 66
    
    ' Loop through all the worksheets in the workbook
    For Each sheet In ActiveWorkbook.Worksheets
        ' Get the last row of data in the first 21 columns
        lastRow = sheet.Cells(Rows.Count, 1).End(xlUp).Row
    
        ' Set the data range to the 21 columns of data
        Set dataRange = sheet.Range(sheet.Cells(2, 1), sheet.Cells(lastRow, numColumns))
    
        ' Select the data range
        dataRange.Select
        
        ' Show the total number of rows in the selected range
        MsgBox "The selected data range has " & dataRange.Rows.Count & " rows."
    Next sheet
End Sub