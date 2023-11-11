# 6. (20 points) Human Emotions

## Installation
Create a virtual environment in the 6_HumanEotions folder and install the required packages:

``` pip install -r requirements.txt ```

## Project Structure
There are three projects:
1. LiveFER - facial emotion recognition from live webcam feed.
2. VideoFER - facial emotion recognition and analysis from prerecorded video files.
3. NLP - Natural language processing emotion analysis.

### LiveFER
LiveFER can be run from any directory by running liveAnalyze.py. It will open the webcam and begin live emotion detection.

### VideoFER
VideoFER must be run from within the VideoFER directory. Running analyze.py will analyze the emotions of the file pointed to on line 9:

``` location_videofile = "content/random_faces.mp4" ```

A new video will be created in the output folder.

Running videoToFrames.py, performanceCheck.py, then performance_plot.py will analyze and plot the performance of fer.

The plot contains 3 performance tests:
1. Rasberry Pi 3 running Ubuntu Server 22.04.3(specs. Quad Core 1.2GHz, Broadcom BCM2837, 64bit CPU, 1GB RAM)
2. Macbook Pro 2018 running mac OSX Monterey(specs. Processor: 2.6 GHz 6-Core Intel Core i7, Memory: 16 GB 2400 MHz DDR4, Graphics: Radeon Pro 560X 4 GB + Intel UHD Graphics 630 1536 MB)
3. Lenovo Yoga laptop (specs. Processor: 2.1 GHz AMD Ryzen 5 5500U with Radeon Graphics, Memory: 8 GB)

### NLP
This program generates a model to to analyze the emotion of a sentence. It uses "emotion-dataset.csv" to create a model, then uses "test-dataset.csv" to try and guess the emotions of each sentence, printing the results to the console.