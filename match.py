import re, jieba


# a:需要匹配的分词列表，b：匹配的列表
def match(seg_list, b):
    result_index = 0  # 记录结果的位置
    result = ''  # 结果
    max_match = 0  # 最大匹配度
    index = 0  # 记录循环的位置
    for tar in b:
        # print(tar)
        Matching_degree = 0  # 匹配度
        for seg in seg_list:
            match = re.search(seg, tar)
            if match:
                Matching_degree += 1
        if max_match < Matching_degree:
            max_match = Matching_degree
            result = tar
            result_index = index
        index += 1
    print("匹配位置: %d" % (result_index+1))
    print(result)
