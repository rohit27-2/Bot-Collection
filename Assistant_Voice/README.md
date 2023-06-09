# Jarvis Voice Assistant

Jarvis is a Python voice assistant that can perform various tasks such as retrieving the current time, opening websites, playing YouTube videos, fetching weather information, telling jokes, and more.

## Prerequisites

Before running the code, make sure you have the following libraries installed:

- pyttsx3
- speech_recognition
- requests
- pywhatkit
- pyjokes
- wikipedia
- webbrowser

You will also need an API key for retrieving weather information. Replace `"API_KEY"` in the code with your actual API key.

## Usage

1. Import the required libraries.
2. Initialize the pyttsx3 engine and set the voice property.
3. Define the `output()` function to speak the given text.
4. Define the `inputcommand()` function to listen for user commands through the microphone and return the recognized text.
5. Define the `greet()` function to greet the user based on the current time.
6. Define the `weather()` function to fetch and display weather information.
7. Greet the user using the `greet()` function.
8. Enter a loop to continuously listen for user commands.
9. Perform different actions based on the recognized command:
   - Retrieve and speak the current time.
   - Retrieve and speak the current date.
   - Open YouTube and play a video based on user input.
   - Open Google in the web browser.
   - Fetch and display weather information.
   - Tell a joke.
   - Exit the program when the user says "offline".

Feel free to modify the code according to your needs and add more functionality to the voice assistant.

Note: This is a simplified summary of the code functionality. For a detailed understanding, please refer to the actual code implementation.