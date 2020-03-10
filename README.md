# iConsultancy

## Config
To properly use the API, a URL and key must be specified in a file called `Config.yml`. Use `Config.yml.example` and replace the fields with your own URL and key. Rename that file to Config.yml.

To access the fields in code, first import the file using ```from iConsultancy/config import config``` and you can call on it like a dictionary.
## How to run
1. Clone the git repository.
2. Navigate to the unzipped repository in the terminal.
3. Install `pipenv` by running `pip install pipenv`
4. Run these commands:
```
pipenv sync --dev
pipenv run jupyter notebook
```
