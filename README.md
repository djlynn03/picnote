# PicNote
- Visit our website: [picnote.tech](https://www.picnote.tech)
- Program designed to analyze a picture using Vision API from Google to create a .docx file to give to the user with the texts shown as plain text in .docx file while keeping pictures/diagrams.

# Features
- Transcribes handwriting to text
- Places pictures in the same relative location to the text

# Design
- The website is hosted using Google Cloud Run in a Docker container. 
- We recieved our domain, picnote.tech, from Domain.com.
- We are using the python-docx library to create the output document
- This application uses Django for the backend, which makes it easy to parse the response from the Google Cloud Vision API, construct the docx output file, and send it to the web page. 
- On our frontend, we are using Bootstrap 5.
