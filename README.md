# WeatherCanPicYourMusic ⛅️📸🎧

Welcome to WeatherCanPicYourMusic, where the skies set your playlist! This unique platform crafts a music recommendation list based on the day's weather, requiring just a photo from you. Below is the magic that makes it happen.

## Weather Image Classification

* **Image Understanding**: Utilized a cutting-edge image classification model, 'Xception', pre-trained to distinguish diverse weather patterns: sunny☀️, rainy☔️, foggy🌫️, snowy🌨️, and sunset/sunrise 🌅.
* **Data Sources**: Amassed an extensive dataset from Kaggle and Google Images to fine-tune our model for accurate recognition.

## Music Recommendation

* **Data Scraping Tools**: Employed Selenium and Beautiful Soup to curate a music database rich with details like song titles, artists, albums, tags, and popularity metrics.
* **Cultural Touch**: Tapped into South Korea's music platforms, such as Melon and Genie, extracting songs from weather-themed playlists (e.g., 화창한 날 for sunny days, 비 오는 날 for rainy days).

## Music - Weather Similarity

* **Semantic Analysis**: Analyzed playlist tags with 'Word2Vec' to establish the mood-weather relationship, ensuring that tags accurately reflect the atmospheric conditions they represent.

## Personalized Recommendations

* **Unique Scoring**: Combined likes, tag-weather similarity, and frequency of weather-specific mentions to generate a tailored list of 10 songs.

## Platform Accessibility

* **Streamlit Integration**: Embedded our system into Streamlit, allowing for easy access and user interaction. Simply download our model (CNN_baseline.h5) and the Streamlit page files (Home.py, 'pages' folder) to get started.
* **Open for All**: Anyone can run the website on their local machine and enjoy personalized music recommendations.

---
WeatherCanPicYourMusic bridges the gap between your sensory experience and your music. Try it out and let the weather tune your day! ⛅️📸🎧
