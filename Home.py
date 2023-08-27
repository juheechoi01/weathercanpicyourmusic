import streamlit as st

# Set the page configuration to have a custom title and icon
st.set_page_config(page_title="Weather Can 'Pic' Your Music", page_icon="📸")

st.image('./image/main.png', use_column_width=True)

# Add a custom CSS to make the header center-aligned and have better spacing
st.markdown('''
<style>
    .big-header {
        text-align: center;
        padding: 30px 0;
        margin-bottom: 20px;
        border-bottom: 3px solid #ffd700;
    }
</style>
''', unsafe_allow_html=True)

# Use the custom CSS class for the header and use the color scheme
st.markdown('''
<div class="big-header">
    <h2><span style="color: #ffd700;">Weather Can "Pic" Your Music</span></h2>
    <p>에 오신 것을 환영합니다! ⛅️📸🎧</p>
</div>
''', unsafe_allow_html=True)

# Add instructions with a bit more spacing and clearer emphasis
st.markdown('''
본인이 **직접** 찍은 사진에 어울리는 음악을 추천해드립니다.
''')

st.markdown("**사용법은 다음과 같습니다!**")

# Use HTML to create an ordered list for clearer instructions
st.markdown('''
<ol>
    <li><strong>📸 Upload Your Picture</strong> 메뉴 버튼을 클릭해주세요!</li>
    <li>사진 업로드만 하시면, 음악은 저희가 추천해드리니 편하게 기다리시면 됩니다 🙂</li>
</ol>
''', unsafe_allow_html=True)