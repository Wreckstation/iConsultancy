# iConsultancy

## How to run
1. Installation of Python version 3.8 is needed. This step is only necessary for a one-time installation.
   [Download the latest Python update here!](https://www.python.org/) 
   - If Python is already installed, check to ensure the Python version installed is correct:
   
     |   OS   |                             Method                               |
     | ------ | ---------------------------------------------------------------- |
     | Windows| Open Windows Powershell and run `python --version` or `python -V`|
     | MacOS  | Open terminal window and run `python --version` or `python -V`   |
     | Linux  | Open terminal window and run `python --version` or `python -V`   |
    
2. Clone the git repository.

3. Navigate to the unzipped repository in the terminal.

4. Use `pip` to install `pipenv` and its dependencies
   ```
   pip install pipenv
   ```
   If pipenv is already installed on your device, skip this step. This step is only necessary for a one-time installation. 
   
5. Run `pipenv update`.
   - `pipenv update` runs `pipenv lock` and `pipenv sync`. `pipenv lock` creates a Pipfile.lock which checks your system to ensure all necessary dependencies are installed and updated based on the pipfile.  `pipenv sync` installs the packages within the .lock file.
   - Note: If `pipenv update` is taking more than a few minutes to run, you can try to run the following in the terminal instead:
      ```
      pipenv lock --clear
      pipenv sync
      ```
      
    Below is a quick demo for how to run Step 5
    ![](Step6-Step7tutorial.gif)

6.  `ipywidgets` requires a separate set of instructions to enable for older Jupyter Notebook versions (<5.3).
      - Run the pipenv shell in the folder by using `pipenv shell` and run this command: 
      ```
      jupyter nbextension enable --py --sys-prefix widgetsnbextension
      ```
      - Exit the pipenv shell by typing `exit`.
      This step is only necessary for the first installation.
      
7. Jupyter Notebook can now be properly executed in the pipenv virtual environment. To start the program, run:
   ```
   pipenv run jupyter notebook
   ```
    - The command `pipenv run jupyter notebook` is needed everytime to access the Jupyter Notebook.

8. Once Juypter Notebook is running, open the `config.yml.example` file.
9. Replace the URLHERE and KEYHERE fields with your own ActiveCampaign URL and KEY, save, and rename the file `config.yml`
   Everytime the URL and KEY change, ensure the `config.yml` file is updated to reflect the new URL and KEY.
   ![](URL_KEY_tutorial_README.gif)

10. Navigate to `Main.ipynb` and run all cells to start the UI and make your queries!
   
