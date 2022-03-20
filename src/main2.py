import enum
import re
import thulac
from ltp import LTP
from zhon import hanzi


raw_txt = """
    新建完成之后可以看到如果没有设置自动换行的话,默认我们比较长的句子或者段落后面需要移动才能阅读全部内容。
    """

raw_txt = """
    俄乌冲突持续，国际能源动荡冲击全球经济。在对俄罗斯挥舞制裁大棒的同时，如何填补对俄制裁造成的石油市场供不应求，成了西方目前的头等要事。

　　此时此刻，美欧官员的身影频现于战争阴云下的东欧，也在有事相求的中东产油国间来回穿梭。3月15日，美国国家安全委员会中东政策协调员布雷克·麦格克率团抵达沙特。一天后，英国首相约翰逊也踏上了这片世界最大原油出口国的土地。

　　沙特是少数几个拥有剩余产能的石油生产国之一，但在西方频频提出石油增产请求时，沙特仍然坚持遵循与俄罗斯等主要产油国先前达成的产量协定。根据13个欧佩克成员国与俄罗斯等10个非欧佩克产油国的协商，2021年7月，主要产油国同意从当年8月起将日均总产量每月上调40万桶，直至恢复2020年4月减产前的规模。分析认为，许多产油国未达到增产目标，沙特与俄罗斯是仅有的两个具有较大增产空间的国家。

　　美国总统拜登上台后一改前任特朗普的作风，对沙政策改弦更张，美沙关系也日趋紧张。在俄乌冲突爆发前，拜登并不急于与沙特领导人对话——但现在，主动权似乎开始落在沙特手中。
    """

def main():

    
    # thu1 = thulac.thulac(seg_only=True)  #默认模式
    # text = thu1.cut(raw_txt, text=True)  #进行一句话分词
    # print(type(text))
    # print(text)

    def split_by(spare):

        def split_text(txt):
            return txt.split(spare)

        return split_text

    txts = raw_txt.split()
    txts = map(split_by(','), txts)
    # txts = map(split_by(','), txts)

    for txt in txts:
        print(txt)
        print('\n')
    
def main2():

    ltp = LTP()     # 默认加载 Small 模型
                    # ltp = LTP(path="small")
                    #     其中 path 可接受的路径为下载下来的模型或者解压后的文件夹路径
                    #     另外也可以接受一些已注册可自动下载的模型名(可使用 ltp.available_models() 查看): 
                    #     base/base1/base2/small/tiny/GSD/GSD+CRF/GSDSimp/GSDSimp+CRF
    seg_centens, hidden = ltp.seg(raw_txt.split())
    dep_indexs = ltp.dep(hidden)
    
    for c_index, centence in enumerate(seg_centens):
        centence_indexs = dep_indexs[c_index]

        for dep_i in centence_indexs:
            i1, i2, _type = dep_i

            start = min((i1, i2))
            end = max((i1, i2))

            print(f"{_type}: {centence[start: end]}")


def main3():

    result = re.findall(hanzi.sentence, raw_txt)
    
    for centence in result:
        print(centence)
        print('\n')


def _cut(sentence):
    """
    将一段文本切分成多个句子
    :param sentence: ['虽然BillRoper正忙于全新游戏
    :return: ['虽然BillRoper正..接近。' , '与父母，之首。' , '很多..常见。' , '”一位上..推进。' , ''”一直坚..市场。'' , '如今，...的70%。']
    """

    new_sentence = []
    sen = []
    for i in sentence: # 虽
        sen.append(i)
        if i in ['。', '！', '？', '?', ',', '，', '.']:
            new_sentence.append("".join(sen)) #['虽然BillRoper正...接近。' , '与父母，...之首。' , ]
            sen = []

    if len(new_sentence) <= 1:  # 一句话超过max_seq_length且没有句号的，用","分割，再长的不考虑了。
        new_sentence = []
        sen = []
        for i in sentence:
            sen.append(i)
            if i.split(' ')[0] in ['，', ','] and len(sen) != 0:
                new_sentence.append("".join(sen))
                sen = []

    if len(sen) > 0:  # 若最后一句话无结尾标点，则加入这句话
        new_sentence.append("".join(sen))

    return new_sentence


def cut2(sentence):
    """
    将一段文本切分成多个句子
    :param sentence: ['虽然BillRoper正忙于全新游戏
    :return: ['虽然BillRoper正..接近。' , '与父母，之首。' , '很多..常见。' , '”一位上..推进。' , ''”一直坚..市场。'' , '如今，...的70%。']
    """

    lines = sentence.strip().split()

    delimiters = ['，', '.',  '。', '！', '？', '?', ',', ';']

    new_lines = []

    for line in lines:
        txt = line
        for delimiter in delimiters:
            txt = txt.replace(f'{delimiter}', f'{delimiter}\n\n')
        new_lines.append(txt)
    
    new_centence = '\n'.join(new_lines)

    print(new_centence)

if __name__ == "__main__":

    # main()
    cut2(raw_txt)