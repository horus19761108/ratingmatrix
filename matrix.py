import pandas as pd
import tkinter
import tkinter.filedialog as tkfl
import glob
import os

# グローバル変数
files = None
header = None
headerfile = ".\\data\\matrix_columns.txt"

# 読み込むフォルダパスを取得(返り値：フォルダパス(str))
def getreaddir_path():
    tk = tkinter.Tk()
    tk.withdraw()  
    readf_path = tkfl.askdirectory().replace('/',os.sep)

    return readf_path

# 入力ファイル名の取得
def getreadf_path():
    tk = tkinter.Tk()
    tk.withdraw()  
    readf_path = tkfl.askopenfilenames(filetypes=[('csv file','*.csv')])

    return readf_path

# 出力ファイル名の取得
def getwritef_path():
    tk = tkinter.Tk()
    tk.withdraw()  
    writef_path = tkinter.filedialog.asksaveasfilename(filetypes=[('csv file','*.csv')]).replace('/',os.sep)

    return writef_path
    
# 指定されたフォルダ内のcsvを結合しデータフレーム化する
def read(f_path):
    global files, header
    data_list = []

    # 指定のフォルダからすべてのcsvファイルのパスをリスト化
    files = glob.glob(os.path.join(f_path,'*.csv')) 

    # ヘッダーファイルの読み込み
    with open (headerfile, 'r', encoding='utf-8') as input:
        header = input.read()
        header = header.split('\n')

    # フォルダ内のCSVファイルをすべて読み込む
    for file in files:
        data_list.append(pd.read_csv(file,names=header,encoding='shift_jis',dtype='object'))

    # リスト化されたデータフレームを結合。indexも降りなおす
    data_f = pd.concat(data_list, ignore_index=True)

    return data_f

# データフレーム内から指定した条件でデータを抽出する
def select(data_f, name, value):
    select_f = data_f[data_f[name].isin(value)]

    return select_f
    

# データフレームをファイル出力
def matrix_to_csv(data_f, wf_path):
    try:
        data_f.to_csv(path_or_buf=wf_path)
    except:
        return False

    return True

# 読み込んだファイル名を取得する
def getreadfiles():
    if files != None:
        return files
    else:
        return False

# ヘッダー項目を取得する
def getheader():
    # ヘッダーファイルの読み込み
    with open (headerfile, 'r', encoding='utf-8') as input:
        header = input.read()
        header = header.split('\n')
    if header != None:
        return header
    else:
        return False

if __name__ == "__main__":
    data_f = read(getreaddir_path())

    name  = '格付会社コード'
    value = [1]
    select_f = select(data_f, name, value)

    matrix_to_csv(select_f, getwritef_path())
