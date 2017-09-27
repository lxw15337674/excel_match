import xlrd, xlwt, jieba
from datetime import date, datetime
import match


# a,b作为需要读取数据的开始行数和第几列
# c,d作为被读取数据的开始行数和第几列
def read_match_data(a=0, b=0, match_sheet_num=0):
    mlist = []
    match = xlrd.open_workbook(r'demo.xlsx')
    match_sheet = match.sheet_by_index(match_sheet_num)
    for row in range(a - 1, match_sheet.nrows):
        value = match_sheet.cell(row, b - 1).value
        seg_list = jieba.lcut(value, cut_all=False)
        mlist.append(seg_list)
    print("匹配读入完成")
    return mlist


# c,d作为被读取数据的开始行数和第几列
def read_bemathch_data(c=0, d=0, bematch_sheet_num=0):
    bmlist = []
    bematch = xlrd.open_workbook(r'demo2.xlsx')
    match_sheet = bematch.sheet_by_index(bematch_sheet_num)
    for row in range(c - 1, match_sheet.nrows):
        value = match_sheet.cell(row, d - 1).value
        # seg_list = jieba.lcut(value, cut_all=False)
        bmlist.append(value)
    print("被匹配数据读入完成")
    return bmlist
if __name__ == '__main__':
    mlist = read_match_data(4, 2)
    bmlist= read_bemathch_data(4, 2)
    for a in mlist:
        # print(a)
        match.match(a,bmlist)



