#-*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox as tkmsg
import matrix

# 完了メッセージ表示
def message():
    mBox = tkinter.Tk()
    mBox.withdraw()    #←これでTkの小さいウィンドウが非表示になる。

    tkmsg.showinfo('showinfo','完了しました')

def get_matrix_r_path():
    r_path = matrix.getreaddir_path()
    entry_r.insert(0, r_path)

def get_matrix_w_path():
    w_path = matrix.getwritef_path()
    entry_w.insert(0, w_path)

def matrix_select():
    data_f = matrix.read(entry_r.get())

    name  = '格付会社コード'
    value = [1]
    select_f = matrix.select(data_f, name, value).reset_index(drop = True)

    matrix.matrix_to_csv(select_f, entry_w.get())

    message()

    root.destroy()


### インターフェースの作成 ###
root = tkinter.Tk()
# キャンバスの設定
root.geometry('800x150')
root.title('格付マトリクス抽出')

## メニューバーの作成
menubar = tkinter.Menu(root)
root.config(menu = menubar)
# 「ファイル」メニュー
filemenu = tkinter.Menu(menubar)
menubar.add_cascade(label='ファイル', menu=filemenu)
filemenu.add_command(label='閉じる', command=root.destroy)

## 読み取りファイルエリア
# 読み取りフォルダラベル
buff_label_r = tkinter.StringVar()
buff_label_r.set("読み込むフォルダ：")
label_path_r = tkinter.Label(root, textvariable = buff_label_r)
label_path_r.place(x=10,y=10)
# 読み取りファイルパス表示エリア
entry_r = tkinter.Entry(root, width=100)
entry_r.place(x=110,y=10)
# 読み取りファイルパスの参照用ボタン
button_matrix_r = tkinter.Button(root, text = '参照', command = get_matrix_r_path)
button_matrix_r.place(x=730,y=5)

## 書き込みファイルエリア
# 書き込みファイル用ラベル
buff_label_w = tkinter.StringVar()
buff_label_w.set("作成ファイル名：")
label_path_w = tkinter.Label(root, textvariable = buff_label_w)
label_path_w.place(x=10,y=40)
# 書き込みファイルパス表示エリア
entry_w = tkinter.Entry(root, width=100)
entry_w.place(x=110,y=40)
# 書き込みファイルパスの参照用ボタン
button_matrix_w = tkinter.Button(root, text = '参照', command = get_matrix_w_path)
button_matrix_w.place(x=730,y=35)

## 処理開始用ボタンの作成
button_submit = tkinter.Button(root, text = '実行', command = matrix_select)
button_submit.place(x=380,y=80)



###メインループ
root.mainloop()
