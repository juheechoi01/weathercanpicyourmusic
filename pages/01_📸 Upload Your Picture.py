import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import pandas as pd

def preprocess_image(uploaded_file, target_size=(224, 224)):
    # Use PIL to open the image
    image = Image.open(uploaded_file)
    
    # Resize the image to the target size and convert to numpy array
    image = image.resize(target_size)
    image_array = np.array(image)
    
    # Ensure the image is in the range [0, 1] (normalize if your model was trained this way)
    image_array = image_array / 255.0
    
    # Expand dimensions to match the input shape of the model (batch_size, height, width, channels)
    image_array = np.expand_dims(image_array, axis=0)
    
    return image_array

def classify_image(uploaded_file):
    # Preprocess the uploaded image
    preprocessed_image = preprocess_image(uploaded_file)
    
    # Get the model prediction
    predictions = model.predict(preprocessed_image)
    
    # Get the index of the highest predicted value
    predicted_index = np.argmax(predictions[0])
    
    class_names = ['foggy', 'rainy', 'snowy', 'sunny', 'sunrise_sunset']
    
    return class_names[predicted_index]

def recommend(input):
    df_input = df[df['label']==input]
    df_input.sort_values(by='final', ascending=False, inplace=True)
    df_input = df_input[:len(df_input)//20] # 상위 5% 추출
    output = df_input.sample(n=10, replace=False)

    return output

def show_output(input):
    for index, row in input.iterrows():
        # Create columns for album image and song details
        col1, col2 = st.columns([1, 3])  # adjust the ratio if needed
        
        # Display album image in the left column
        col1.image(row['image'], use_column_width=True)
        
        # Display song details in the right column with custom styles
        col2.markdown(f"<span class='title-style'>**Title:** **{row['title']}**</span>", unsafe_allow_html=True)
        col2.markdown(f"<span class='artist-style'>**Artist:** **{row['artist']}**</span>", unsafe_allow_html=True)
        col2.markdown(f"<span class='tag-style'>**Tag:** {row['specific_tag']}</span>", unsafe_allow_html=True)
        
        # Embed the YouTube video
        st.video(row['first video link'])
        
        # Optionally, add a separator for better visual distinction between rows
        st.markdown("---")

    # Add the custom styles at the end of the function
    st.markdown("""
    <style>
        .title-style {
            font-size: 20px;
        }
        .artist-style {
            font-size: 20px;
        }
        .tag-style {
            font-size: 15px;
        }
    </style>
    """, unsafe_allow_html=True)


# Create a file uploader widget
uploaded_file = st.file_uploader("📸 이미지를 업로드해주시길 바랍니다!", type=['png', 'jpg', 'jpeg'])

# Load the trained model
model = tf.keras.models.load_model('./final_model/xception_model_1.h5')

df = pd.read_csv('./real_final.csv')

# If an image has been uploaded, process and display the results
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption='Uploaded Image.')
    
    # get label of image
    label = classify_image(uploaded_file)
    
    # Define the emoji based on the label
    if label == 'sunny':
        emoji = '☀️'
        color = '#ffd700'
    elif label == 'rainy':
        emoji = '☔️'
        color = '#b0c4de'
    elif label == 'foggy':
        emoji = '🌁'
        color = '#ffffe0'
    elif label == 'sunrise_sunset':
        emoji = '🌅'
        color = '#f08080'
    elif label == 'snowy':
        emoji = '☃️'
        color = '#6495ed'
    else:
        emoji = ''  # Default to no emoji for other labels

    st.markdown(f'''
    <div class="big-header">
        <h2>오늘의 날씨: {label}{emoji}</h2>
    </div>
    ''', unsafe_allow_html=True)

    # get the top 10 music of the label
    music = recommend(label)

    st.markdown(f'''
    <div class="header">
        <h2><span style="color: {color};">날씨에 어울리는 노래를 추천해드립니다 🎧{emoji}</span></h2>
    </div>
    ''', unsafe_allow_html=True)

    # line them in order
    show_output(music)
