# Joke Telling API

## Description
The Joke Telling API is an application that allows users to log in and choose a topic for a joke. The app uses the OpenAI API to generate a funny joke on the selected topic. Users can choose to receive the joke in text form or as an audio file. If the audio option is chosen, the generated text is converted to speech using Amazon Polly, and the user can download the MP3 file. The generated audio files are stored in an S3 bucket and can only be downloaded by the user who generated them.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)
- [Acknowledgements](#acknowledgements)

## Installation
To install and run the app, you need to have Docker installed. Follow these steps:

1. Clone the repository:
  ```
  git clone https://github.com/yourusername/joke-telling-api.git
  cd joke-telling-api
  ```
2. Build the Docker container:
  ```
  docker build -t joke-telling-api .
  ```
3. Run the Docker container:
  ```
  docker run -p 5000:5000 joke-telling-api
  ```

## Usage
The app provides two main endpoints:

/text/topic: Generates the text form of the joke on the selected topic.
/audio/topic: Generates the audio of the joke.
/download/key: Downloads the audio file using a secret key.

Example usage:

To get a joke in text form:
```
curl -X GET "http://localhost:5000/text/your-topic"
```
To get a joke in audio form:
```
curl -X GET "http://localhost:5000/audio/your-topic"
```
To download the audio file:
```
curl -X GET "http://localhost:5000/download/your-secret-key"
```

## Features
Creation of a joke based on a chosen topic.
Text-to-speech conversion using Amazon Polly.
Secure, dedicated download links for audio files stored in an S3 bucket.

## Contributing
If you are interested in contributing to this project, please contact me at the e-mail address provided below.

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. For more information, see the LICENSE file.

## Contact Information
For any questions or inquiries, please reach out to soltysik.ewa@gmail.com.

## Acknowledgements
Thanks to Kacper Garbacinski for code review.
