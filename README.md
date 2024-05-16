## Telegram Bot

This Telegram bot implements basic functionalities for interacting with users, including sending images and video clips based on provided URLs.

## Installation

1. Clone the repository to your local machine using `git clone`.
2. Install Python (if not already installed).
3. Install the required libraries using `pip install -r requirements.txt`.

## Running

1. Set up the `.env` file with your bot token. If you don't have a bot token, you can obtain one by creating a new bot using [BotFather](https://core.telegram.org/bots#6-botfather).
2. Start the Docker container using `docker-compose up -d`.
3. The bot will be available for use in the Telegram application.

## Usage

The bot responds to specific commands sent by the user. Here are some of the supported commands:

- `/hi`, `/hello`: Greeting message.
- `/image <URL>`, `/photo <URL>`: Retrieves an image from the provided URL and sends it to the user.
- `/video <URL>`: Retrieves a video from the provided URL, converts it to MP4 format, and sends it to the user.
