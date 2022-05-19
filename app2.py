import streamlit as st

def main():
    st.title('웹 대시보드')
    st.text('웹 대시보드 개발하기')

    name = '홍길동'

    # 제 이름은 홍길동 입니다.
    print('제 이름은 {}입니다.'.format(name))

    st.text('제 이름은 {}입니다.'.format(name))
    st.header('이 영영은 헤더 영역')
    st.subheader(' 이 영역은 subheader 영역')
    st.success('작업이 성공했을때 사용하자.')
    st.wearning('경고 문구를 보여주고 싶을때)
    st.info('정보를 보여주고 싶을때')
    
if __name__ == '__name__' :
    main()
