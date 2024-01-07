# Lyrics_for_Learning

## Introduction
Welcome to the future of learning! The ChatGPT Q&A to Song Translator is an innovative project designed to ignite the curiosity of young minds while making the learning process fun and memorable. In the fast-paced world of today, it's essential to harness technology's power to ensure that kids remain engaged and interested in learning. Our mission is to create a bridge between traditional education and modern technology, helping students of all ages explore knowledge playfully and interactively.

## Project Description
Our FLL Robotics project centers on the development of a program that allows users to ask questions on any topic. What makes this project unique is its ability to take those questions and transform them into catchy songs. The program leverages ChatGPT, a state-of-the-art language model, to convert plain questions into fun and memorable tunes. By doing so, we aim to achieve two primary objectives:

Sustained Interest in Learning: Music is a universal language that resonates with people of all ages. By turning questions into songs, we hope to foster a sense of joy and excitement around learning. This, in turn, can help children stay engaged with their studies.

Enhanced Memory Retention: Music has a remarkable impact on memory. By creating songs from questions, we believe that the information becomes easier to remember. This can be particularly useful for studying and retaining educational content.


## How It Works
Ask a Question: Users type their questions into the program.

Genre Selection: Users choose the style of song they want the answer to be transformed into.

Song Generation: The program uses ChatGPT to translate the question into lyrics and music, producing a fun and educational song.

Enjoy and Learn: Users can listen to their custom-made songs, reinforcing their understanding of the topic.

```mermaid

sequenceDiagram
    actor Student
    actor Teacher
    Student->>Teacher: What are all the planets in order from closest to the Sun to farthest from the Sun?
    Teacher->>Student: Let's ask Lyrics for Learning.
    Teacher->>Lyrics_for_Learning: What are all the planets in order from closest to the Sun to farthest from the Sun?
    Teacher->>Lyrics_for_Learning: Use the song Rudolph the Red Nose Reinder
    Lyrics_for_Learning->>OpenAI: Ask question**
    OpenAI ->> Lyrics_for_Learning: Return the lyrics**
    Lyrics_for_Learning->> Voicemod: Here are the lyrics for the song, will you sing them to me?
    Voicemod ->> Lyrics_for_Learning: Here is the song.mp3
    Lyrics_for_Learning ->> Teacher: Here is the song.
    Teacher ->> Student: Plays the song**
```

Example of questions: 
```
Write me lyrics that list all the planets in order from closest to the Sun to farthest from the Sun that rhymes with the song Rudolph the Red Nose Reindeer
```

Example of the answered question from the question above:
```
Mercury, the innermost one, closest to the sun, so hot, like an oven.
Venus is next, with clouds, it's a mystery, we can't see through, 
Earth is our home, with oceans blue and land so green.
Mars is the red one, rusty and grand, with canyons and rovers exploring the land.
Jupiter's huge, a gas giant so wide, with swirling storms
Saturn has rings, a sight to behold, icy and bright, they never get old.
Uranus spins sideways, an ice giant, it's true, 
Neptune, the last one, so far away, icy and blue

```

    
## For Local Developments
1. run below command to install all dependencies  
```
pip install  singing-bot/requirement.txt
``` 
2. run below command to start up Flask server 
```
python routing_question.py 
```
3. Install HTML Previewer then open as preview in the browser to start testing the code
