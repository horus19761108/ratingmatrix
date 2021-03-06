#-*- coding:utf-8 -*-

import tkinter
import tkinter.messagebox as tkmsg
import matrix
from datetime import datetime

def get_matrix_r_path():
    r_path = matrix.getreaddir_path()
    entry_r.insert(0, r_path)

def get_matrix_w_path():
    w_path = matrix.getwritef_path()
    entry_w.insert(0, w_path)

def matrix_select():
    data_f = matrix.read(entry_r.get())

#    name  = '残存年'
#    value = ['01']
    name  = entry_s.get()
    value = [str(entry_v.get())]
    if name != "":
        select_f = matrix.select(data_f, name, value).reset_index(drop = True)
    else:
        select_f = data_f

    matrix.matrix_to_csv(select_f, entry_w.get())

    put_log(name,value,select_f)

def put_log(name, value, select_f):
    day = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    log = '(' + day + ')  完了しました!'
    lb.insert(tkinter.END, log)
    log = '[入力情報]'
    lb.insert(tkinter.END, log)
    files = matrix.getreadfiles()
    for i in files:
        lb.insert(tkinter.END, i)
    log = '[出力情報]'
    lb.insert(tkinter.END, log)
    log = entry_w.get()    
    lb.insert(tkinter.END, log)
    log = '[抽出条件]'
    lb.insert(tkinter.END, log)
    for j in value:
        log = name+'が'+str(j)+'と等しい'
    lb.insert(tkinter.END, log)
    log = str(len(select_f.index))+'件のレコードを抽出しました'
    lb.insert(tkinter.END, log)
    log = '----------'
    lb.insert(tkinter.END, log)

### インターフェースの作成 ###
root = tkinter.Tk()
# キャンバスの設定
root.geometry('760x270')
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
label_path_r = tkinter.Label(
                        root,
                        textvariable = buff_label_r
                    )
label_path_r.place(x=5,y=10)
# 読み取りファイルパス表示エリア
entry_r = tkinter.Entry(root, width=100)
entry_r.place(x=100,y=10)
# 読み取りファイルパスの参照用ボタン
button_matrix_r = tkinter.Button(
                        root,
                        text = '参照',
                        command = get_matrix_r_path
                    )
button_matrix_r.place(x=720,y=5)

## 書き込みファイルエリア
# 書き込みファイル用ラベル
buff_label_w = tkinter.StringVar()
buff_label_w.set("作成ファイル名：")
label_path_w = tkinter.Label(
                        root,
                        textvariable = buff_label_w
                    )
label_path_w.place(x=5,y=40)
# 書き込みファイルパス表示エリア
entry_w = tkinter.Entry(root, width=100)
entry_w.place(x=100,y=40)
# 書き込みファイルパスの参照用ボタン
button_matrix_w = tkinter.Button(
                        root,
                        text = '参照',
                        command = get_matrix_w_path
                    )
button_matrix_w.place(x=720,y=35)

## 検索条件入力エリア
# 検索条件ラベル
buff_label_s = tkinter.StringVar()
buff_label_s.set("検索条件：")
label_search = tkinter.Label(
                        root,
                        textvariable = buff_label_s
                    )
label_search.place(x=5,y=75)
# 条件１入力エリア(項目)
search_col = matrix.getheader()
search_col.insert(0,"")
entry_s  = tkinter.Spinbox(
                    root,
                    width=20,
                    value=search_col,
                    state = 'readonly'
                )
entry_s.place(x=100,y=75)

buff_label_sc = tkinter.StringVar()
buff_label_sc.set("が")
label_search_con = tkinter.Label(
                        root,
                        textvariable = buff_label_sc
                    )
label_search_con.place(x=250,y=75)

# 条件２入力エリア(値)
entry_v  = tkinter.Entry(
                    root,
                    width=20
                )
entry_v.place(x=300,y=75)
buff_label_sv = tkinter.StringVar()
buff_label_sv.set("と等しい")
label_search_val = tkinter.Label(
                        root,
                        textvariable = buff_label_sv
                    )
label_search_val.place(x=450,y=75)



## 検索開始用ボタン
button_submit = tkinter.Button(
                        root,
                        text = '検索',
                        width=30,
                        command = matrix_select
                    )
button_submit.place(x=500,y=70)

## ログ表示エリア設定
# フレームの設定
frame = tkinter.LabelFrame(
                root,
                text="実行ログ",
                relief=tkinter.RIDGE
            )
frame.place(x=5,y=100)

# ログ表示エリア用リストボックス
lb = tkinter.Listbox(
                frame,
                width = 121,
                height = 7
            )
lb.grid(row=0, column=0,sticky=tkinter.NSEW)

# ログ表示エリア用縦スクロールバー
sb1 = tkinter.Scrollbar(
                frame,
                orient = tkinter.VERTICAL,
                command = lb.yview
            )
sb1.grid(row=0,column=1,sticky=tkinter.NS)

# ログ表示エリア用横スクロールバー
sb2 = tkinter.Scrollbar(
                frame,
                orient = tkinter.HORIZONTAL,
                command = lb.xview
            )
sb2.grid(row=1,column=0,sticky=tkinter.EW)

# リストボックスとスクロールバーを連動させる
lb.configure(yscrollcommand = sb1.set)
lb.configure(xscrollcommand = sb2.set)

###メインループ
root.mainloop()
