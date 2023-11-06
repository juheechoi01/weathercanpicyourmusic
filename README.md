# WeatherCanPicYourMusic ⛅️📸🎧

This platform is useable for all who wish to use a platform that recommends you 10 songs relevant to the weather of the day.
For this to be possible, the user is required to upload a picture that well represents the weather, and from that moment the system will do the rest for you.

Below is the intricate process of the recommendation system.

## Weather Image Classification
- In order for the user the system to be able to classify the images, we need an image classification model.
- We implemented a pre-trained 'Xception' model appropriate for our task, which were trained with multiple images of each classes: sunny☀️, rainy☔️, foggy🌫️, snowy🌨️, and sunset/sunrise 🌅.
- The data was collected by both Kaggle and Google.

## Music Recommendation
- Music data was scraped using softwares: Selenium and Beautiful Soup.
- With the following softwares, we were able to retrieve data such as song title, artist, album title, tags, number of likes. In order to make sure we collect music data relevant to the weather, we searched playlists from various music platforms made in South Korea (Melon, Genie) using specific keywords related to the weather.
  - ex) sunny: 화창한 날, 맑은 날, 여행 / rainy: 비 오는 날, 장마, 여름비
 
## Music - Weather Similarity
- As mentioned earlier, tags were scraped as well. Tags are basically keywords that the owner of the playlist puts up when creating the playlist, which means it describes the mood or the tone of the playlist, which makes it easier for other users to choose and understand their playlist.
- In order to see if the tags were really relevant to the weather, we used a pre-trained 'Word2Vec' to check if the tags and weather were really correlated.

In conclusion, in order to properly recommend songs that go well with the weather, the following three weights were given differently: Number of likes, tag and weather similarity, and how many times a particular song was mentioned with the specific weather tag.
* Additionally, our platform was implemented on 'Streamlit', so anyone who downlaods the final model (CNN_baseline.h5) and the pages corresponding to the 'Streamlit' site is able to run the website and try it out! 😊
* Hope the WeatherCanPicYourMusic! ⛅️📸🎧
