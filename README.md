# ratingmatrix
  
  
# �T�v
* python3���K�p�X�N���v�g
    * ���{�،��Ƌ���ɂČ��\����Ă���u�i�t�}�g���N�X(CSV�t�@�C��)�v�𕡐��ǂݍ��݁A�w�肵�������Ń��R�[�h�𒊏o����  
    * Tkinter���g����UI���쐬  
    * �C�ӂ̃t�H���_�z���ɂ���S�Ă�CSV�t�@�C����ǂݍ���  
    * ����(CSV�t�@�C��)���A�C�ӂ̃t�H���_�A�t�@�C�����ŏo�͂���  

# UI�C���[�W  
  ![Alt text](/data/ui_image.jpg)
  
# �J����
* OS  
    * Windows10(1709) Home  
* �J������  
    * Python 3.6.1  

# �K�v�Ȃ���  
* ���{�،��Ƌ�����\���Ă���u�i�t�}�g���N�X(CSV�t�@�C��)�v  
    * �_�E�����[�h�y�[�W  
      Japanese: <http://market.jsda.or.jp/html/saiken/kehai/downloadInput.php>  
      English : <http://market.jsda.or.jp/eigo/html/saiken/kehai/downloadInput_e.php?_ga=2.188697448.1780810083.1508666206-1991158651.1492664028>  
  
# �J������
[2017/10/22]  
* matrix.py  
    * �֐�[getreaddir_path()]  
        * tkinter.askdirectory���g���āA�Ǎ��t�H���_�̃t���p�X��str�ŕԂ�  
    * �֐�[getwritef_path()]  
        * tkinter.filedialog.asksaveasfilename���g���āA�����ރt�@�C���̃t���p�X��str�ŕԂ�  
    * �֐�[read(f_path)]  
        * ����f_path(�t�H���_�p�X)�̃t�H���_�z���ɑ��݂���CSV�t�@�C����S�Č������A�f�[�^�t���[���Ƃ��ĕԂ�  
    * �֐�[select(data_f, name, value)]  
        * ����data_f(�f�[�^�t���[��)����A����name�Ɏw�肵�����ڂ��A����value�Ɉ�v���郌�R�[�h�𒊏o���f�[�^�t���[���Ƃ��ĕԂ�  
    * �֐�[matrix_to_csv(data_f, wf_path)]  
        * ����data_f(�f�[�^�t���[��)���A����wf_path(�t�@�C���p�X)��CSV�t�@�C���Ƃ��č쐬����
* matrix_tk.py
    * UI�̕`��Ɗe�핔�i�̓����ݒ�  
    * �֐�[message()]  
        * �������b�Z�[�W�̃��b�Z�[�W�{�b�N�X�̐ݒ�  
    * �֐�[get_matrix_r_path()]  
        * �ǎ�t�H���_�p�Q�ƃ{�^���̓���  
    * �֐�[get_matrix_w_path()]  
        * �����݃t�@�C���p�Q�ƃ{�^���̓���  
    * �֐�[matrix_select()]
        * ���s�{�^���̓���