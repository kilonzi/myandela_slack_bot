# SLACK BOT FOR MY ANDELA


## Problem Statement
Everyone knows that https://my.andela.com/ is a great tool as we expand as a talent marketplace
But it's utilization is hindered by: -
1. Having to remember to fill every week
2. Having to log in to another system (It's a huge cost for context switching )
3. My Andela seems to be down 

## Installation

## Source code and repository

Clone this repository and go to branch into a folder in your computer

    git clone https://github.com/kilonzi/my_andela_bot.git
    git checkout -b main

## Python installation
Make sure you have python installed or it's Python 3+  onwards
Run the command below to check your specific version

    python --version

If an earlier version exists or you want to upgrade then follow this tutorial
*https://realpython.com/installing-python/*

## Virtual environment
With Python 3 installed:- 
Navigate using the computer terminal, to the folder you downloaded source code into
  

    cd  path/to/downloaded


The folder **should** contain the folder
    src
Type in the command below to create a virtual environment.

    python3 -m venv venv

In the terminal, run the below command to activate virtual environment

    source venv/bin/activate

## Requirements installation

with Virtual Environment now active: -
Run the command below to install all the requirements to run the program

    pip3 install -r requirements.txt

## Slack 
Create an app on slack and obtain the

SLACK_BOT_TOKEN   => OAuth & Permissions
SLACK_SIGNING_SECRET => Basic Information

## NGROK

Navigate to https://dashboard.ngrok.com/get-started/setup
(Why??? Because slack will not allow sending of HTTP requests to https://localhost:3000)
To download ngrok and run

    ./ngrok http 3000


## Slack Updating

You will need to go to your slack app and add the URL obtained from NGROK

1. Interactivity & Shortcuts => Update Interactivity URL so its something like 
https://bd1eafaee6c3.ngrok.io/slack/interactions

2. Event Subscriptions => Update request URL
https://bd1eafaee6c3.ngrok.io/slack/events

## Install your app on your workplace

You will already have done this 

## Running the program

    python3 run.py

## Run

Go to Weekly CheckIn

