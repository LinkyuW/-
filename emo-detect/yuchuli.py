import jieba
from collections import Counter

# 停用词文件名为stopwords.txt，每行一个停用词
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f]
    return set(stopwords)

def remove_stopwords(text, stopwords):
    words = jieba.lcut(text)  # 使用jieba进行分词
    filtered_words = [word for word in words if word not in stopwords]
    return filtered_words

# 加载停用词表
stopwords_path = "C:\\Users\\30515\\Desktop\\stopwords.txt"
stopwords = load_stopwords(stopwords_path)

# 读取txt文件内容
with open("C:\\Users\\30515\\Desktop\\noxin.txt", 'r', encoding='utf-8') as file:
    text = file.read()

# 去除停用词
filtered_words = remove_stopwords(text, stopwords)


filtered_text = ' '.join(filtered_words)
print(filtered_text)
# 已经有了filtered_text，这是过滤停用词后得到的文本
# 将处理后的文本保存到新文件
output_file_path = "C:\\Users\\30515\\Desktop\\new noxin.txt"

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(filtered_text)

print(f"Filtered text has been saved to {output_file_path}")