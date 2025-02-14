import joblib
import os
import re
import jieba
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

# 获取所有的文件
def getfilelist(root_path):
    file_path_list = []
    file_name = []
    walk = os.walk(root_path)
    for root, dirs, files in walk:
        for name in files:
            filepath = os.path.join(root, name)
            file_name.append(name)
            file_path_list.append(filepath)
    return file_path_list


class Question_classify():
    def __init__(self):
        # 获取脚本所在目录
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.model_path = os.path.join(self.base_path, "model_nb.pkl")
        self.vectorizer_path = os.path.join(self.base_path, "vectorizer.pkl")

        # 尝试加载已有模型
        if os.path.exists(self.model_path) and os.path.exists(self.vectorizer_path):
            self.model = self.load_model(self.model_path)
            self.tv = self.load_vectorizer(self.vectorizer_path)
        else:
            # 读取训练数据
            self.train_x, self.train_y = self.read_train_data()
            # 训练模型
            self.model = self.train_model_NB()
            # 保存模型和矢量化器
            self.save_model(self.model, self.model_path)
            self.save_vectorizer(self.tv, self.vectorizer_path)

    # 保存模型
    def save_model(self, model, model_path):
        joblib.dump(model, model_path)

    # 加载模型
    def load_model(self, model_path):
        return joblib.load(model_path)

    # 保存矢量化器
    def save_vectorizer(self, vectorizer, vectorizer_path):
        joblib.dump(vectorizer, vectorizer_path)

    # 加载矢量化器
    def load_vectorizer(self, vectorizer_path):
        return joblib.load(vectorizer_path)

    # 获取训练数据
    def read_train_data(self):
        train_x = []
        train_y = []
        file_list = getfilelist("./static/TrainTexts")
        # 遍历所有文件
        for one_file in file_list:
            # 获取文件名中的数字
            num = re.sub(r'\D', "", one_file)
            # 如果该文件名有数字，则读取该文件
            if str(num).strip() != "":
                # 设置当前文件下的数据标签
                label_num = int(num)
                # 读取文件内容
                with (open(one_file, "r", encoding="utf-8")) as fr:
                    data_list = fr.readlines()
                    for one_line in data_list:
                        word_list = list(jieba.cut(str(one_line).strip()))
                        # 将这一行加入结果集
                        train_x.append(" ".join(word_list))
                        train_y.append(label_num)
        return train_x, train_y

    # 训练并测试模型-NB
    def train_model_NB(self):
        X_train, y_train = self.train_x, self.train_y
        self.tv = TfidfVectorizer()

        train_data = self.tv.fit_transform(X_train).toarray()
        clf = MultinomialNB(alpha=0.01)
        clf.fit(train_data, y_train)
        print(f'新训练了贝叶斯分类模型，与模板上准确率：{clf.score(train_data,y_train)}')
        return clf

    # 预测
    def predict(self, question):
        question = [" ".join(list(jieba.cut(question)))]
        test_data = self.tv.transform(question).toarray()
        y_predict = self.model.predict(test_data)[0]
        # print("question type:", y_predict)
        return y_predict


if __name__ == '__main__':
    qc = Question_classify()
    print(qc.predict("张学友的个人信息"))
