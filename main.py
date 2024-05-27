from openpyxl import Workbook
from openpyxl.styles import Font, Alignment

wb = Workbook()

ws = wb.active

ws['A1'] = '건설프로그래밍 2조 설계 프로그램 보고서'
ws['A2'] = '날짜'
ws['B2'] = '2024-05-27'
ws['A3'] = '내용'
ws['B3'] = '내용이 들어가는 곳.'

title_font = Font(size=25, bold=True)
ws['A1'].font = title_font
ws.merge_cells('A1:B6')

date_cell = ws['B2']
date_cell.alignment = Alignment(horizontal='right')

wb.save("건설프로그래밍 2조 보고서.xlsx")