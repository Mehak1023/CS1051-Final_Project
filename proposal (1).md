# Proposal

## What will (likely) be the title of your project?

Object Tracking

## In just a sentence or two, summarize your project. (E.g., "A website that lets you buy and sell stocks.")

An algorithm in which you upload a video, and it can track the movement of specified objects, such as cars, people, or animals. It can also give the acceleration, velocity, and displacement of the chosen object(s).

## In a paragraph or more, detail your project. What will your software do? What features will it have? How will it be executed?

The program will first recognize objects and classify them as an animal, car, or person. Then the program will isolate each object, and track it's motion through time. The program will require "mp3" videos. Based on the time and displacement, the program will also calculate velocity and acceleration.

## If planning to combine 1051's final project with another course's final project, with which other course? And which aspect(s) of your proposed project would relate to 1051, and which aspect(s) would relate to the other course?

Not a final project, but I have made a somewhat similar code in MATLAB for a previous class. However, the current code was specified for a video in which only two objects (toy cars) were involved. I want to expand on that code to also conduct object recognition, and generalize it for various videos. In my previous code, the code is based solely on RGB recognition.

## If planning to collaborate with 1 or 2 classmates for the final project, list their names, email addresses, and the names of their assigned TAs below.

N/A

## In the world of software, most everything takes longer to implement than you expect. And so it's not uncommon to accomplish less in a fixed amount of time than you hope.

### In a sentence (or list of features), define a GOOD outcome for your final project. I.e., what WILL you accomplish no matter what?

The object recognition is my goal, I want to write a code which can identify and classify objects into various categories. I want it to be able to at least be able to classify an object as a car, human, or animal. Additionally, I want to be able to track the object, for at least a minimal distance (even it can not for the entirety of the video).

### In a sentence (or list of features), define a BETTER outcome for your final project. I.e., what do you THINK you can accomplish before the final project's deadline?

The Code can most of the time, regardless the video, classify objects into human, animal, and car. The program can track the objects for most of the duration of the video. The program can track each object independently, without merging paths.

### In a sentence (or list of features), define a BEST outcome for your final project. I.e., what do you HOPE to accomplish before the final project's deadline?

In every given video input, the program can correctly identify each object independently, and track the path of each object independently. The code is accurate for the entire duration of the video. The code projects accurate distance, displacement, velocity, and acceleration plots. Additionally, the I have code for both MATLAB and Python.

## In a paragraph or more, outline your next steps. What new skills will you need to acquire? What topics will you need to research? If working with one of two classmates, who will do what?

First, I need to conduct research on python's image& video processing toolbox. How does it work? What files it can read? What filtering and identifying functions the program contains. Then I need to accurately be able to write identifying criteria for the code to recognize certain patterns in my chosen categories. Then I will work on converting my current MATLAB code into a python code which can track the objects, and plot their corresponding kinematics.
