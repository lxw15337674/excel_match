import xlrd, xlwt, jieba
from xlutils.copy import copy
from datetime import date, datetime
import match


# a,b作为需要读取数据的开始行数和第几列
# c,d作为被读取数据的开始行数和第几列
def read_match_data(a=1, b=1, match_sheet_num=0):
    mlist = []
    match = xlrd.open_workbook(r'Demo.xls')
    match_sheet = match.sheet_by_index(match_sheet_num)
    for row in range(a - 1, match_sheet.nrows):
        value = match_sheet.cell(row, b).value
        # print(value)
        seg_list = jieba.lcut(value, cut_all=False)
        mlist.append(seg_list)
        # print(seg_list)
    print("匹配读入完成")
    return mlist


# c,d作为被读取数据的开始行数和第几列
def read_bemathch_data(c=1, d=1, bematch_sheet_num=0):
    bmlist = []
    bematch = xlrd.open_workbook(r'Demo2.xlsx')
    match_sheet = bematch.sheet_by_index(bematch_sheet_num)
    for row in range(c - 1, match_sheet.nrows):
        value = match_sheet.cell(row, d - 1).value
        # seg_list = jieba.lcut(value, cut_all=False)
        bmlist.append(value)
    print("被匹配数据读入完成")
    return bmlist


def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式

    font = xlwt.Font()  # 为样式创建字体
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


def write_data(ril, rl, wbr, write_col, rml, match_sheet_num=0):
    # 创建工作簿
    # workbook = xlwt.Workbook(r'demo.xlsx')

    r_xls = xlrd.open_workbook(r'Demo.xls', formatting_info=True)
    w_xls = copy(r_xls)
    w_sheet = w_xls.get_sheet(0)
    style = xlwt.easyxf('font: bold on')
    redstyle = xlwt.easyxf('font: color-index red, bold on')

    # 创建sheet
    # w_sheet = workbook.add_sheet(u'sheet1', cell_overwrite_ok=True)
    try:
        w_sheet.write(wbr - 2, write_col, '匹配位置', style)
        w_sheet.write(wbr - 2, write_col + 1, '匹配事项', style)
        w_sheet.write(wbr - 2, write_col + 2, '匹配度', style)
    except:
        print("从第一行开始没有提示标题" )
    # 写入
    for i in range(len(ril)):
        w_sheet.write(i + wbr - 1,write_col,ril[i] + wbr - 1,style)
        w_sheet.write(i + wbr - 1, write_col + 1, rl[i], style)
        if (int(rml[i])<50):
            w_sheet.write(i + wbr - 1, write_col + 2, '%s %%' % rml[i], redstyle)
        else:
            w_sheet.write(i + wbr - 1, write_col + 2, '%s %%' % rml[i], style)
        # 保存文件
    w_xls.save('demo3.xls')


if __name__ == '__main__':
    mrbr = 1  # match_read_begin_rows
    mrc = 2  # match_read_cols
    bmrbr = 4  # bematch_read_begin_rows
    bmrc = 2  # bematch_read_cols
    write_col = 5
    ril = []  # result_index_list
    rl = []  # result_list
    rml = []  # result_matching_list
    mlist = read_match_data(mrbr, mrc)
    bmlist = read_bemathch_data(bmrbr, bmrc)
    success_num = 0
    for a in mlist:
        # print(a)
        result_index, result, matching = match.match(a, bmlist)
        ril.append(result_index)
        rl.append(result)
        rml.append(matching)
        success_num += 1
        print("已成功匹配%s个" % success_num)
    write_data(ril, rl, mrbr, write_col, rml)
