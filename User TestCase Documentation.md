# UMD iConsultancy ActiveCampaign API Deals Extractor - User Guide

## Make sure the instructions in README.md have been followed the User Testing Documentation

## How to use
1. Go to config.yml and enter in our ActiveCampaign Sandbox Developer credential for the URL and KEY.
2. Save the config.yml file and return to the Jupyter Dashboard.
3. Locate `Main.ipynb` in Jupyter Notebook and open this file.
4. Run all cells. (Cells > Run All) These fields should appear on your screen: ![](UI.png)
5. Enter in the listed parameters to filter/sort the output as listed in the test case `test steps`.
6. Make sure to uncheck the JSON  checkbox.
8. Press `Get .CSV Report` to output a .CSV report of the Test Case under implementation.
9. Repeat steps 1 through steps 7 for each Test Case performed.

- Kernel only reads config.yml file once at start up, so if you make any changes to URL and KEY it might not read it. 
  - Try restarting the kernel and running all the cells. 
  - Try shutting down Jupyter Notebook and restart it if resetting the kernel doesnt work.


## Test Cases

### Search: Title

| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for Deal `Title` with valid Deal title and Deal stage data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4. Enter `DealStageId` in the `Deal Stage` text input box <br/> 5. Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunny Bonanza <br/> **DealStageId**: Identify| Should generate a CSV report for Bunny Bonanza| As Expected| Pass|    
|2 | Check `Search` filter for Deal `Title` with invalid Deal title and Deal stage data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4. Enter `DealStageId` in the `Deal Stage` text input box <br/> 5. Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunnie Bonanaza <br/> **DealStageId**: Identify| Should generate an empty CSV report| As Expected| Pass|    


### Search: Contacts

### Search: Organization

## Deal Status
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Deal `Status` filter for valid `Open` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Open` <br/> 2.  Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing Deals| Not As Expected; generates for a default stage `To Contact`| Fail|    
|2 | Check Deal `Status` filter for valid `Lost` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Lost` <br/> <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing 1 Deal (Aquire Amazon)| As Expected| Pass| 
|3 | Check Deal `Status` filter for valid `Won` Deals data exportation.| 1. Click Drop Down for `Status ` and select `Won` <br/> <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report containing 1 Deal (Toliet Paper)| Not As Expected; generates for a default stage `To Contact`| Fail | 



### Deal Stage
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify| Should generate a CSV report for 2 Deals (Bunny Bonanza and Lipbalm Website)| As Expected| Pass|    
|2 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Materialize| Should generate a CSV report for 2 Deals (Bunny Statistics and H4U Vending Machines)| As Expected| Pass|    


### Owner

## Tag Name
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
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
|1 | Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value data| 1.  Enter `150` in the search box to the left of the <br/> `≤ Value ≤` filter and `10000` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 4 Deals (Bunny Bonanza, Lipbalm Website, Bunny Statistics, and Debug| Not As Expected; | Fail|    
|2 | Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value and `Deal Stage` data|1.  Enter `Identify` in the `Deal Stage` search box <br/> 2.  Enter `600` in the search box to the left of the <br/> `≤ Value ≤` filter and `2500` in the search box to the right <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 2 Deals (Bunny Bonanza and Lipbalm Website| As Expected| Pass|  

### Filename
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1| Check `File Name:` for valid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report of all Deals| As Expected| Pass|
|2| Check `File Name:` for invalid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report but saved in an improper file format unable to open as CSV| As Expected| Pass|

