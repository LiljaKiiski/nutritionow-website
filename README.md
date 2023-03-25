# Nutrition Now

Unfortunately for the moment the only way to host our website is to do so locally. Our website has been made utilizing Django. Please follow the following instructions to setup our website for use on your computer

### Download the following:
1. Clone this repository
2. Download our secret key from [here](https://drive.google.com/file/d/1SDcU2lSzQFbVrcB-w9xvu04spPzh3Oab/view?usp=sharing)
3. Download our model from [here](https://drive.google.com/file/d/1mYde9TVIpSo6sb2iU9VQdUuB8l4KAvZJ/view?usp=sharing)

### Open the clone repository
1. Place the env file (rename to .env) in nutritionnow-website/nutritionproject/
2. Place the model(ggml-model-q4_0.bin) in nutritionapp/static/models/dalai/alpaca/models/7B/

### Installation and setup
1. Make sure you have the following installed
- python3
- python3.10-venv
- django
- django-environ
2. Setup your virtual environment with the following commands
- python3 -m venv venv
- source venv/bin/activate
- pip install django-environ
3. Compile the model runner code
- Go to nutritionow-website/staticfiles/models/dalai/alpaca
- Run make
    - Literally type "make"

### Congrats! You're ready to run
1. To run just run run.sh[Linux/MacOS] or run.bat[Windows]