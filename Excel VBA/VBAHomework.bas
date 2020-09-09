Attribute VB_Name = "Module1"
Sub HomeworkVBA():
'declare
    Dim rownum As Long
    Dim firstrow As Long
    Dim rowCount As Long
    Dim total As Double
    Dim reportingRow As Long
    Dim change As Double
    Dim lastrow As Long
    
    Cells(1, 9).Value = "Ticker"
    Cells(1, 10).Value = "Yearly Change"
    Cells(1, 11).Value = "Percent Change"
    Cells(1, 12).Value = "Total Stock Volume"

    percent_change = 0
    change = 0
    total = 0
    Start = 2
    j = 0

    rowCount = Cells(Rows.Count, "A").End(xlUp).Row

    For i = 2 To rowCount
        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
            total = total + Cells(i, 7).Value
            If total = 0 Then
                Range("I" & 2 + j).Value = Cells(i, 1).Value
                Range("J" & 2 + j).Value = 0
                Range("K" & 2 + j).Value = 0 & "%"
                Range("L" & 2 + j).Value = 0
            Else
                ' Find First non zero starting value
                If Cells(Start, 3) = 0 Then
                    For find_value = Start To i
                        If Cells(find_value, 3).Value <> 0 Then
                            Start = find_value
                            Exit For
                        End If
                     Next find_value
                End If

            change = (Cells(i, 6) - Cells(i, 3))
                percent_change = Round((change / Cells(Start, 3) * 100), 2)
                Range("I" & 2 + j).Value = Cells(i, 1).Value
                Range("J" & 2 + j).Value = Round(change, 2)
                Range("K" & 2 + j).Value = "%" & percent_change
                Range("L" & 2 + j).Value = total
                
                    Select Case change
                    Case Is > 0
                        Range("J" & 2 + j).Interior.ColorIndex = 4
                    Case Is < 0
                        Range("J" & 2 + j).Interior.ColorIndex = 3
                    Case Else
                        Range("J" & 2 + j).Interior.ColorIndex = 0
                End Select
            End If
            change = 0
            total = 0
            j = j + 1
        Else
            total = total + Cells(i, 7).Value


            
    End If
Next i
End Sub


