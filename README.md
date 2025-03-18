#AI based Mental Health Support system 

Mental Health assistant that provides personalized mental health resources , including coping strategies and self care recommendations . The platform uses AI to analyze user inputs and perform sentiment analysis on user journals , offering personalized advice and resources. 

#Features
- sentiment analysis
- personalized recommendations

#Technologies used 

- Streamlit : for creating front end UI
- Pathway : for data processing and indexing 
- Gemini API : for AI generated personalized recommendations 
- Docker 


#how to run the project
- First , clone the repository and then run **docker build --network=host -t mental_health_assistant .**
- Then run **docker run -p 8501:8501 mental_health_support**

#what the project looks like :
It takes input from the user that is basically their diary entry and performs sentiment analysis on the text. It also provides copying strategies and self care recommendations for the user .
A screenshot of the website is attached below for better understanding of the working of the website/project. 

![Screenshot 2024-09-30 221455](https://github.com/user-attachments/assets/c9b05627-9023-4870-8383-9cc632b4c6e8)

