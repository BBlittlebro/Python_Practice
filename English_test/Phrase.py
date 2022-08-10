import tkinter as tk
import random

input_name = input('Please enter your word dictionary: ')
fopen = open(input_name, 'r')
dict1 = fopen.read().split('、')
words = dict()
for item in dict1:
    if item:                            # 避免最後一個空格
        en = item.split('_')[0].strip() # 去掉換行字元
        ch = item.split('_')[1].strip()
        words[en] = ch
fopen.close()

from datetime import date
now = date.today().isoformat()
output_name = input_name + '-' + now
wrong_list = []

#######################################

def button_check(btn, answer):
    if btn['text'] == answer[0] or btn['text'] == answer[1]:
        renew()
    else:
        btn['bg'] = '#b01e13'
        with open(output_name, 'a') as fout:
            with open(output_name, 'r') as temp:
                if answer[0] not in temp.read():
                    en = answer[0]
                    ch = answer[1]
                    fout.write(en + ' ' + ch + '、')

def create_question():
    global answer
    if len(words) < 4:
        question_str = 'Finished this test!!'
        btn1_str = ''
        btn2_str = ''
        btn3_str = ''
        btn4_str = ''
    else:
        temp_arr = random.sample(list(words.items()), 4)            # 隨機挑選4個, 變成 tuple ('apple', '蘋果')
        rand = random.randrange(4)                                  # 4 取 1 當正解
        ch_or_en = random.randrange(2)                              # 0 for en, 1 for ch
        if ch_or_en == 0:
            question_str = temp_arr[rand][0]
            btn1_str = temp_arr[0][1]
            btn2_str = temp_arr[1][1]
            btn3_str = temp_arr[2][1]
            btn4_str = temp_arr[3][1]
        else:
            question_str = temp_arr[rand][1]
            btn1_str = temp_arr[0][0]
            btn2_str = temp_arr[1][0]
            btn3_str = temp_arr[2][0]
            btn4_str = temp_arr[3][0]
        answer = temp_arr[rand]
        del words[answer[0]]

    return question_str, btn1_str, btn2_str, btn3_str, btn4_str

def renew():
    question_str, btn1_str, btn2_str, btn3_str, btn4_str = create_question()
    global question, btn1, btn2, btn3, btn4
    question['text'] = question_str
    btn1['text'] = btn1_str
    btn2['text'] = btn2_str
    btn3['text'] = btn3_str
    btn4['text'] = btn4_str
    btn1['bg'] = 'white'
    btn2['bg'] = 'white'
    btn3['bg'] = 'white'
    btn4['bg'] = 'white'


#######################################
win = tk.Tk()
win.title("Phrase test!!!")
win.geometry('800x500')
win.resizable(False, False)

fm = tk.Frame(win, width=800, height=100)
fm.pack()

#######################################    

question = tk.Label(fm, width=45, height=3 ,font=('微軟正黑體', 40))
question.pack()

btn1 = tk.Button(win, width=45, height=3, bg='white', font=('微軟正黑體', 20))
btn1.configure(command=lambda: button_check(btn1, answer))
btn2 = tk.Button(win, width=45, height=3, bg='white', font=('微軟正黑體', 20))
btn2.configure(command=lambda: button_check(btn2, answer))
btn3 = tk.Button(win, width=45, height=3, bg='white', font=('微軟正黑體', 20))
btn3.configure(command=lambda: button_check(btn3, answer))
btn4 = tk.Button(win, width=45, height=3, bg='white', font=('微軟正黑體', 20))
btn4.configure(command=lambda: button_check(btn4, answer))

answer = 0
renew()

OpeningFile = tk.Button(win, width=45, fg="black", text="OPEN", highlightbackground="#82CC6C")
btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()

#######################################


win.mainloop()