# ratingmatrix
  
  
# 概要
* python3練習用スクリプト
    * 日本証券業協会にて公表されている「格付マトリクス(CSVファイル)」を複数読み込み、指定した条件でレコードを抽出する  
    * Tkinterを使ったUIを作成  
    * 任意のフォルダ配下にある全てのCSVファイルを読み込む  
    * 結果(CSVファイル)を、任意のフォルダ、ファイル名で出力する  

# UIイメージ  
  ![Alt text](/data/ui_image.jpg)
  
# 開発環境
* OS  
    * Windows10(1709) Home  
* 開発言語  
    * Python 3.6.1  

# 必要なもの  
* 日本証券業協会が公表している「格付マトリクス(CSVファイル)」  
    * ダウンロードページ  
      Japanese: <http://market.jsda.or.jp/html/saiken/kehai/downloadInput.php>  
      English : <http://market.jsda.or.jp/eigo/html/saiken/kehai/downloadInput_e.php?_ga=2.188697448.1780810083.1508666206-1991158651.1492664028>  
  
# 開発履歴
[2017/10/22]  
* matrix.py  
    * 関数[getreaddir_path()]  
        * tkinter.askdirectoryを使って、読込フォルダのフルパスをstrで返す  
    * 関数[getwritef_path()]  
        * tkinter.filedialog.asksaveasfilenameを使って、書込むファイルのフルパスをstrで返す  
    * 関数[read(f_path)]  
        * 引数f_path(フォルダパス)のフォルダ配下に存在するCSVファイルを全て結合し、データフレームとして返す  
    * 関数[select(data_f, name, value)]  
        * 引数data_f(データフレーム)から、引数nameに指定した項目が、引数valueに一致するレコードを抽出しデータフレームとして返す  
    * 関数[matrix_to_csv(data_f, wf_path)]  
        * 引数data_f(データフレーム)を、引数wf_path(ファイルパス)へCSVファイルとして作成する
* matrix_tk.py
    * UIの描画と各種部品の動作を設定  
    * 関数[message()]  
        * 完了メッセージのメッセージボックスの設定  
    * 関数[get_matrix_r_path()]  
        * 読取フォルダ用参照ボタンの動作  
    * 関数[get_matrix_w_path()]  
        * 書込みファイル用参照ボタンの動作  
    * 関数[matrix_select()]
        * 実行ボタンの動作