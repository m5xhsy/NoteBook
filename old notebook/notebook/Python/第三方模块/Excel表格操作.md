# openpyxl

## 读

```python
from openpyxl import load_workbook

# 打开文件
wb = load_workbook("G:/index.xlsx",read_only=True) # 只读
wb = load_workbook("G:/index.xlsx",data_only=True)  # 将excel的函数转换为值，不写打印出来的是公式

# 获取sheet 
sheet_all = wb.sheetnames  # 返回列表，里面是所有sheet的名字

# 打开sheet
sheet = wb['sheet']

# 读取单个值
sheet["A3"].value
sheet.cell(row=1, column=3).value

# 获取每一行的值
sheet_row = sheet.rows   # 返回可迭代对象，循环后是一个元组，里面包含每行的单元格对象
[(<Cell 'index'.A1>, <Cell 'index'.A2>, <Cell 'index'.A3>), 
 (<Cell 'index'.B1>, <Cell 'index'.B2>, <Cell 'index'.B3>), 
 (<Cell 'index'.C1>, <Cell 'index'.C2>, <Cell 'index'.C3>)]

# 获取每一列的值
方法一:
sheet_column = sheet.columns # 返回可迭代对象，循环后是一个元组，里面包含每列的单元格对象,
[(<Cell 'index'.A1>, <Cell 'index'.B1>, <Cell 'index'.C1>), 
 (<Cell 'index'.A2>, <Cell 'index'.B2>, <Cell 'index'.C2>), 
 (<Cell 'index'.A3>, <Cell 'index'.B3>, <Cell 'index'.C3>)]
方法二:
for line in sheet:
	print([item.value for item in line])
    
# 获取最大行和最大列
max_column_num = sheet.max_column # 最大列
max_row_num = sheet.max_row			# 最大行


    

```

## 写

```python
from openpyxl import Workbook

wb = Workbook()		# 实例化

# 添加sheet
sheet = wb.create_sheet('index')		# 默认添加最后
sheet = wb.create_sheet('index',0)		# 根据索引添加
sheet = wb.create_sheet('index',-2)		# 添加到倒数第二个

# 单个单元格添加内容
sheet['A1'] = 5								# 给第一行一列添加值
sheet.cell(row=1, column=2, value=3) 		# 给第一行二列添加值

# 添加行
line = ['name', 'age', 'school']
sheet.append(line)

# 公式
sheet['A3'] = '=sum(A1:A2)'

# 修改sheet名字
sheet.title = "indxx"

# 保存
wb.save("G:/index.xlsx")
```

## 样式

```python
from openpyxl.styles import Font, colors, Alignment

# 设置字体
sty = Font(name="等线",size=24,italic=True,color=colors.BLUE,bold=True)
sheet['A1'].font = sty

# 对其方式
sheet['B1'].alignment = Alignment(horizontal='center', vertical='center')

# 设置行高和列宽
sheet.row_dimensions[2].height = 40		# 第2行行高
sheet.column_dimensions['C'].width = 30   # C列列宽

# 合并单元格，写数据只要写到左上角就可以了
index_sheet.merge_cells('F1:G1') # 合并一行中的几个单元格
index_sheet.merge_cells('F5:G8') # 合并一个矩形区域中的单元格

# 拆分单元格
index_sheet.unmerge_cells('F5:G8')
```



