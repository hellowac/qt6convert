import os
from typing import List

import thulac


# print(os.path.dirname(thulac.__file__))

# 机器学习
# import hanlp
# from hanlp.components.mtl.multi_task_learning import MultiTaskLearning
# from hanlp_common.document import Document

line_max_length = 20

# 保留的字符
keep_group_chars = ("“", "”")

# 换行并保留的字符
delimiters = (
    ",",
    "，",
    "。",
    "?",
    "？",
    "!",
    "！",
    ":",
    "：",
    ";",
    "；",
    "“",
    "”",
    "‘",
    "'",
    "（",
    "）",
    "(",
    ")",
    "〈",
    "〉",
)

# 替换为空格的字符
replace_space = ("、",)

# 编译
# re.split(r'(\.|\!|\?|。|！|？|\.{6})', line)
# compiled = re.compile(r'|'.join(delimiters))

# def cut_sentences(line: str):
# 	sentences = compiled.split(line)
# 	return "\n\n".join(sentences)

# 自然语言分析
# HanLP: MultiTaskLearning = hanlp.load(hanlp.pretrained.mtl.CLOSE_TOK_POS_NER_SRL_DEP_SDP_CON_ELECTRA_BASE_ZH)

# 自定义词典 参考: https://github.com/hankcs/HanLP/blob/doc-zh/plugins/hanlp_demo/hanlp_demo/zh/tok_mtl.ipynb
# tok = HanLP['tok/coarse']
# tok.dict_force = {"万辆", }

thu1 = thulac.thulac(seg_only=True)  #默认模式


def need_keep(line: str) -> bool:
    # 例如： “ 和 ” 之间的文本保留

    length = len(keep_group_chars)
    hasd_len = 0
    for char in keep_group_chars:
        if char in line:
            hasd_len += 1

    return hasd_len == length  # 如果改行同时包含 “ 和 ” 则保留


def replace_flag(line: str):
    txt = line
    # 替换为空格
    for flag in replace_space:
        txt = txt.replace(flag, " ")

    return txt


def newline_flag(line: str):
    txt = line

    # 换行
    for delimiter in delimiters:

        if delimiter in keep_group_chars and need_keep(txt):
            continue

        txt = txt.replace(f"{delimiter}", f"\n\n")

    return txt.split()


def split_flag(line: str):
    # 参考zhon 文档: https://zhon.readthedocs.io/en/latest/#using-zhon
    # 过长的行分割
    txt = line

    if len(txt) > line_max_length:
        txts = split_line(txt)
    else:
        txts = [
            txt,
        ]

    return ["{:>2d}:    {}".format(len(t), t.strip()) for t in txts]

def split_line(line:str) -> List[str]:
    
    # 参考: http://thulac.thunlp.org/ 的 1.4 节
    result_arr = thu1.cut(line)  #进行一句话分词
    word_arr = [group[0] for group in result_arr]

    centence = ''
    result_arr = []

    for word in word_arr:
        centence += word

        if len(centence) >= 10:
            result_arr.append(centence)
            centence = ''
        
    if len(centence) < 10:
        last = result_arr[-1]
        last += centence
        result_arr[-1] = last
    else:
        result_arr.append(centence)

    return result_arr


def split_line_back(line: str) -> List[str]:

    result: Document = HanLP(line, tasks='tok/coarse')
    word_arr = result.pop('tok/coarse')

    centence = ''
    result_arr = []

    for word in word_arr:
        centence += word

        if len(centence) >= 10:
            result_arr.append(centence)
            centence = ''
        
    if len(centence) < 10:
        last = result_arr[-1]
        last += centence
        result_arr[-1] = last
    else:
        result_arr.append(centence)

    return result_arr
