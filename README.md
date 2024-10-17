# Day Trips Optimization Back-End
This is the Github repository of Day Trips Optimization Back-End Flask Server.

## Table Of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Run the Server](#run-the-server)

## Installation
1. Clone the repository:
```bash
git clone -b main https://github.com/BangAjus/Days-Trip-Optimization-Flask.git
```
2. Create virtual environment and activate it:
```bash

# 1. Make venv
# This
python3 -m venv venv

# Or
python -m venv venv

# 2. Activate venv to enable using environment
# For Linux/macOS
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
Create a `.env` file to store credential and secret keys to access the server. <br>
You can follow the `.env.example` file.

## Run the Server
```bash
export FLASK_RUN_PORT=10111
flask run
```