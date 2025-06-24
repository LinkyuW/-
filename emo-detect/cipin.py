import jieba
from collections import Counter

# 读取文档并统计词频
def count_words(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        # 使用jieba进行分词
        words = jieba.lcut(text)
        # 过滤掉一些停用词
        words = [word for word in words if word not in ('的', '是', '和',' ','……','。','？','，','我','','呢','吗','吧')]
        # 统计词频
        word_counts = Counter(words)
        # 返回最常见的20个词及其计数
        return word_counts.most_common(100)

# 打印结果
def print_top_words(top_words):
    print("词频最高的100个词：")
    for word, count in top_words:
        print(f"{word}: {count}")

# 主函数
def main():
    filename = input("请输入文件的完整路径（例如：C:\\Users\\30515\\Desktop\\new yes.txt）：")
    try:
        top_words = count_words(filename)  # 统计词频
        print_top_words(top_words)  # 打印结果
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == "__main__":
    main()
#C:\\Users\\30515\\Desktop\\new yes.txt"
#C:\Users\30515\Desktop\yes.txt