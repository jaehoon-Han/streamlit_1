###### 파일을 업로드 하는 방법 ######
###### 이미지 파일, csv 파일 업로드

import streamlit as st
from PIL import Image
import pandas as pd
import os
from datetime import datetime

def save_uploaded_file(directory, file) :
    # 1.디렉토리가 있는지 확인하여, 없으면 디렉토리부터만든다.
    if not os.path.exists(directory) :
        os.makedirs(directory)
    # 2. 디렉토리가 있으니, 파일을 저장.
    with open(os.path.join(directory, file.name), 'wb') as f :
        f.write(file.getbuffer())
    return st.success("Saved file : {} in {}".format(file.name, directory))

def main():

    #사이드바 만들기
    st.title('파일 업로드 프로젝트')

    menu = ['Image', 'CSV', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == menu[0] :
        st.subheader('이미지 파일 업로드')
        upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'])
        if upload_file is not None :
            print(upload_file.name)
            print(upload_file.size)
            print(upload_file.type)

            # 파일명을 유니크하게 만들어서 저장
            # 현재시간을 활용해서, 파일명을 만든다.
            current_time = datetime.now()
            print(current_time.isoformat().replace(':', '_'))

            new_filename = current_time.isoformat().replace(':', '_') + '.jpg'
          
            upload_file.name = new_filename
            save_uploaded_file('temp', upload_file)



    elif choice == menu[1] :
        st.subheader('CSV 파일 업로드')
    else :
        st.subheader('파일 업로드 프로젝트입니다.')

if __name__ == '__main__' :
        main()