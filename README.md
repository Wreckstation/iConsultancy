
<img src="ischool.png" width="300" markdown="1">

# iConsultancy
The University of Maryland iConsultancy Experimental Learning program provides overall project management and support to students from three of the iSchool’s degree programs: Human-Computer Interaction, Master of Information Management, and Bachelor of Science in Information Science. iConsultancy servers from initial scoping to final deliverables of these projects by providing resources to help those students complete their projects. To track progress on individual projects and store client contacts, iConsultancy uses customer relationship management system ActiveCampaign Deals.

This repository contains written and built code that exports data from ActiveCampaign Deals via ActiveCampaign's API features into a CSV fileformat. The ability to extract their data into a csv file will increase efficiency, save time, and ensure consistent up-to-date data to keep track of the current state of multiple projects. 

## 1st time installation
1. Installation of Python version 3.8 is needed. This step is only necessary for a one-time installation.
   [Download the latest Python update here!](https://www.python.org/) 
   - If Python is already installed, check to ensure the Python version installed is correct:
   
     | Operating System |                             Method                               |
     | ---------------- | ---------------------------------------------------------------- |
     | Windows          | Open Windows Powershell and run `python --version` or `python -V`|
     | MacOS & Linux    | Open terminal window and run `python --version` or `python -V`   | 
    
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

6. `ipywidgets` requires a separate set of instructions to enable for older Jupyter Notebook versions (<5.3).
      - Run the pipenv shell in the folder by using `pipenv shell` and run this command: 
      ```
      jupyter nbextension enable --py --sys-prefix widgetsnbextension
      ```
      - Exit the pipenv shell by typing `exit`. 
7.  In `config.yml.example`, replace the URLHERE and KEYHERE fields with your own ActiveCampaign URL and KEY. Save and rename the file `config.yml`.
    - Your ActiveCampaign API URL and KEY can be found within your Account Settings page under the "Developer" tab. Each user that is a part of the ActiveCampaign account has their own unique API key. [More info here.](https://help.activecampaign.com/hc/en-us/articles/207317590-Getting-started-with-the-API#how-to-obtain-your-activecampaign-api-url-and-key)
    ![](URL_KEY_tutorial_README.gif)

      
## Usage
8. Ensure the `config.yml` file has the up-to-date ActiveCampaign URL and KEY.

9. Jupyter Notebook can now be properly executed in the pipenv virtual environment. To start the program, run:
   ```
   pipenv run jupyter notebook
   ```
    - The command `pipenv run jupyter notebook` is needed everytime to access the Jupyter Notebook. Make sure to always navigate to the directory of the repository in the terminal prior to running the program.

10. Navigate to `Main.ipynb` and run all cells to start the UI and make your queries!
