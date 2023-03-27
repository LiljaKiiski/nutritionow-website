# NutritioNow

Welcome, were glad to have you.
Currently the only way to run our website is to host it locally. Please follow the following instructions to setup our website for use on your computer.

## Download the following:
1. Clone this repository
2. Download our secret key from [here](https://drive.google.com/file/d/1SDcU2lSzQFbVrcB-w9xvu04spPzh3Oab/view?usp=sharing)
3. Download our model from [here](https://drive.google.com/file/d/1mYde9TVIpSo6sb2iU9VQdUuB8l4KAvZJ/view?usp=sharing)

## Open the cloned repository
1. Place the env file (rename to .env) in nutritionproject/
2. Place the model(ggml-model-q4_0.bin) in nutritionapp/static/models/dalai/alpaca/models/7B/

## Installation and setup
#### 1. Make sure you have the following installed
- python3 (3.10)
```
Ubuntu: sudo apt-get install python3
Windows: Install from Microsoft Store
```
- python3.10-venv
```
Ubuntu: sudo apt install pytyhon3.10-venv
```
- django
```
pip install django
```
- django-environ
```
pip install django-environ
```
- make
```
Ubuntu: sudo apt-get install make
```
#### 2. Setup your virtual environment with the following commands
```
python3 -m venv venv
source venv/bin/activate
```
#### 3. Compile the model runner code
- Go to nutritionapp/static/models/dalai/alpaca
- Build the project
```
Ubuntu: make
```
## Congrats! You're ready to run
```
Ubuntu/MacOS: ./run.sh
Windows: .\run.bat
```

## Questions?
If you have any issues whatsoever with setting up our program feel free to reach out! You can contact us at nutritionowteam@gmail.com
