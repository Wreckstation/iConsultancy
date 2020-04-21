# iConsultancy

## Config
To properly use the ActiveCampgain API features in our code, an URL and key must be specified in a file called `Config.yml`. Use `Config.yml.example` and replace the fields with your own URL and key. Rename this file to Config.yml.

To access the fields in code, first import the file using ```from iConsultancy/config import config``` and you can call on it like a dictionary.

## How to run
1. Installation of python version 3.8 is needed. [Download the latest Python update here](https://www.python.org/)
2. Installation of `ipywidgets`, an interactive widgets for the Jupyter Notebook.
   - With pip:
    ```
    pip install ipywidgets`
    jupyter nbextension enable --py --sys-prefix widgetsnbextension  # can be skipped for notebook version 5.3 and above
    ```
3. Clone the git repository.
4. Navigate to the unzipped repository in the terminal.
5. Install `pipenv` by running `pip install pipenv`
   - With pipenv: 
   ```
   pipenv lock #creates a pipfile.lock
   ```
   - `pipenv lock` checks your system to ensure all necessary dependencies are installed and updated

6. Run these commands:
```
pipenv sync --dev
pipenv run jupyter notebook #opens Jupyter Notebook in a virtual environment
```
6. Once Juypter Notebook is running, enter the `config.yml.example` file.
7. Replace the URLHERE and KEYHERE fields with your own ActiveCampaign URL and KEY, save, and rename the file `config.yml`
   ```
   URL: https://URLHERE.api-us1.com/api/3/
   KEY: KEYHERE
   ```
