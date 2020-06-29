#encoding=utf-8
import jieba
INPUT_FILE='fenci_input_data.txt'
OUTPUT_FILE='fenci_output_result.txt'
def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False
 
data=""
with open(INPUT_FILE, 'r') as f1:
    lines=f1.readlines()
    data = ",".join(lines)
# print(data)
seg_list = jieba.lcut(data)    #默认是精确模式
seg_set = set()
for i in range(len(seg_list)):
    if is_Chinese(seg_list[i]) and len(seg_list[i])>=2: 
    	#中文，并且长度大于2 才保存
        seg_set.add(seg_list[i])

print(",".join(seg_set))

with open(OUTPUT_FILE, 'w') as file_object:
    file_object.write(",".join(seg_set))