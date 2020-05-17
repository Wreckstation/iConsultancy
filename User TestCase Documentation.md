# UMD iConsultancy ActiveCampaign API Deals Extractor - User Guide

## Make sure the instructions in README.md have been followed the User Testing Documentation

## How to use
1. Go to config.yml and enter in our ActiveCampaign Sandbox Developer credential for the URL and KEY.
2. Save the config.yml file and return to the Jupyter Dashboard.
3. Locate `Main.ipynb` in Jupyter Notebook and open this file.
4. Run all cells. (Cells > Run All)
5. Enter in the listed parameters to filter/sort the output as listed in the Test Cases `Test Steps`
6. Make sure to uncheck the JSON  checkbox.
8. Press `Get .CSV Report` to output a .CSV report of the Test Case under implementation.
9. Repeat steps 1 through steps 7 for each Test Case performed.

Notes:
- Kernel only reads config.yml file once at start up, so if you make any changes to URL and KEY it might not read it. 
  - Try restarting the kernel and running all the cells. 
  - Try shutting down Jupyter Notebook and restart it if resetting the kernel doesnt work.
- Ensure your `File Name` when you click ` Get CSV report` is not the same as another filename; it will override and replace it.
- If `TimeOutError` occurs, click `Get CSV Report` button again.

## Test Cases

### Default Test Case
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1| Check to ensure CSV report output extracts every Deal| 1. Ensure all criteria is by default: <br/> `Search`: N/A </br> `Status` Any <br/> `Next Date`: Any <br/> `Before`: mm/dd/yyyy <br/> `After`: mm/dd/yyyy <br/> 0 `≤ Value ≤` 0 <br/> `Score =` 0 <br/> 0 `< Score <` 0 <br/> `Sort by` N/A `in this order:` Descending <br/> uncheck box for `return as JSON (debug)` <br/> check box for `Notices`| Should generate a CSV report containing 14 Deals| As Expected | Pass|

### `Search: Title` Test Cases
#### Specific Title & Specific Deal Stage Titles
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for Deal `Title` with valid Deal Title  data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4. Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunny Bonanza <br/> | Should generate a CSV report for Bunny Bonanza| As Expected| Pass|    
|2 | Check `Search` filter for Deal `Title` with invalid Deal Title data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4.  Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunnie Bonanaza <br/> | Should generate an empty CSV report| As Expected| Pass| 
|3 | Check `Search` filter for Deal `Title` with valid Deal Title and Deal Stage data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `DealStageId` in `Deal Stage`<br/> 4. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify <br/> | Should generate a CSV report with 2 Deals from the Identify Deal Stage, Bunny Bonanza and Lipbalm Website| As Expected| Pass| 


### `Search: Contacts` Test Cases
#### Sepcific Contact Name 
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for `Contacts` with valid ContactId | 1. Click Drop Down for Search and select `Contacts`<br/> 2. Enter `ContactId` in `Search here `<br/> 3. Press `Get .CSV Report` to output a .CSV report| **ContactId**: Bunny Lady <br/> | Should generate a CSV report for Bunny Bonanza with 2 Deals, Bunny Bonanza and Bunny Statistic| As Expected| Pass|
|2 | Check `Search` filter for `Contacts` with invalid ContactId | 1. Click Drop Down for Search <br/> 2. Select `Contacts`<br/> 3. Enter `ContactId` in `Search here `<br/> 4. Press `Get .CSV Report` to output a .CSV report| **ContactId**: Bunnie Lady <br/> | Should generate an empty CSV report| As Expected| Pass|

### `Search: Organization` Test Cases
#### Specific Organization Name 
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for Deal `Organizations` with valid Deal Organization data| 1. Click Drop Down for Search <br/> 2. Select `Organizations`<br/> 3. Enter `OrganizationId` in `Search here `<br/> 4. Press `Get .CSV Report` to output a .CSV report| **OrganizationId**: Treat Beauty <br/> | Should generate a CSV report for 1 deal, Lipbalm Website| As Expected| Pass|    


### `Deal Status` Test Cases
#### Won, Lost, and Open Deal Status

| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Deal `Status` filter for valid `Open` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Open` <br/> 2.  Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing all Open Deals| Not As Expected; generates for a default stage `To Contact`| Fail|    
|2 | Check Deal `Status` filter for valid `Lost` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Lost` <br/> <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing 1 Deal (Aquire Amazon)| As Expected| Fail| 
|3 | Check Deal `Status` filter for valid `Won` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Won` <br/> <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing 1 Deal (Toliet Paper)| Not As Expected; generates for a default stage `To Contact`| Fail | 

### Deal Stage
### Specific Deal Stage 
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify| Should generate a CSV report for 2 Deals (Bunny Bonanza and Lipbalm Website)| As Expected| Pass|    
|2 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Materialize| Should generate a CSV report for 2 Deals (Bunny Statistics and H4U Vending Machines)| As Expected| Pass| 

### Owner

### `Tag Name` Test Cases
#### Specific Tag Names & Specific Tag Name for Specified Deal Stage

| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Tag Name` filter for `Deal Title` with valid data| 1.  Enter `TagId` in the `Tag Name` search box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **TagId**: Capstone Fall 2020| Should generate a CSV report for 3 Deals (Bunny Bonanza, Lipbalm Website, and H4U Vending Machines)| As Expected| Pass| 
|1 | Check `Tag Name` filter for `Deal Title` with valid data| 1.  Enter `TagId` in the `Tag Name` search box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **TagId**: Capstone Fall 2020| Should generate a CSV report for 3 Deals (Bunny Bonanza, Lipbalm Website, and H4U Vending Machines)| As Expected| Pass|   



### Sort by in Ascending/Desending Order
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal Title in Ascending order with created date valid data.| 1. Click Drop Down for `Sort by ` and select `Title` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal Title's from pipeline in ascending alphabetical order.| Not As Expected; generates for a default stage `To Contact`| Fail |    
|2 | Check Sort by widget for Deal Title in Descending order with created date valid data.| 1. Click Drop Down for `Sort by ` and select `Title` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal Title's from pipeline in descending alphabetical order.| Not As Expected; generates for a default stage `To Contact`| Fail| 

### Project Creation Date
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Created` filter for Deal creation date with valid data| 1. Click Drop Down for `Before:` and enter "04/16/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for the Deals created before April 16th, 2020| As Expected| Pass|    
|2 | Check `Created` filter for Deal creation date with invalid data.| 1. Click Drop Down for `After:` and enter "04/16/3020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate an empty CSV report.| As Expected| Pass| 


### Project Updated

### Project Monetary Value

| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1 | Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value data| 1.  Enter `150` in the search box to the left of the <br/> `≤ Value ≤` filter and `10000` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 4 Deals (Bunny Bonanza, Lipbalm Website, Bunny Statistics, and Debug| Not As Expected; generates for a default stage `To Contact`| Fail|    
|2 | Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value and `Deal Stage` data|1.  Enter `Identify` in the `Deal Stage` search box <br/> 2.  Enter `600` in the search box to the left of the <br/> `≤ Value ≤` filter and `2500` in the search box to the right <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 2 Deals (Bunny Bonanza and Lipbalm Website| As Expected| Pass|  

### Filename
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1| Check `File Name:` for valid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report of all Deals| As Expected| Pass|
|2| Check `File Name:` for invalid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report but saved in an improper file format unable to open as CSV| As Expected| Pass|

