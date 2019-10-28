import openpyxl

attendance_d=openpyxl.load_workbook('attendance.xlsx')

sheet = attendance_d.get_sheet_by_name('Sheet1')

for i in range(3,7):
	sheet.cell(row=i, column=2).value ="Absent"

attendance_d.save('attendance.xlsx')
