#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QGroupBox, QHBoxLayout, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
question_list.append(Question('Когда Наполеон напал на Российскую империю?', '1815', '1812', '1941', '2022'))
question_list.append(Question('Какой город был столицей Советского Союза?', 'Киев', 'Ленинград', 'Москва', 'Баку'))
app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
text = QLabel('Какой национальности не существует?')
button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
one = QRadioButton('Энцы')
two = QRadioButton('Смурфы')
three = QRadioButton('Чулымцы')
four = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(one)
layout_ans2.addWidget(two)
layout_ans3.addWidget(three)
layout_ans3.addWidget(four)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Прав ты или нет?')
correct = QLabel('Ответ будет тут!')

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(text, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
layout_line3.addWidget(button, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    radio_group.setExclusive(False)
    one.setChecked(False)
    two.setChecked(False)
    three.setChecked(False)
    four.setChecked(False)
    radio_group.setExclusive(True)

answer = [one, two, three, four]

radio_group = QButtonGroup()
radio_group.addButton(one)
radio_group.addButton(two)
radio_group.addButton(three)
radio_group.addButton(four)

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    text.setText(q.question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    '''проверка выбраного варианта ответа'''
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score+=1
        print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:',window.score)
        print('Рейтинг:', (window.score/window.total*100),'%')
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:', (window.score/window.total*100),'%')
def next_question():
    window.total += 1
    print('Статистика\n-Всего вопросов:', window.total,'\n-Правильных ответов:',window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
window.score = 0
window.total = 0


next_question()
button.clicked.connect(click_OK)

window.resize(400, 300)
window.show()
app.exec()