# UMD iConsultancy ActiveCampaign API Deals Extractor - User Guide

## Make sure the instructions in README.md have been followed the User Testing Documentation

## How to use
1. Go to config.yml and enter in our ActiveCampaign Sandbox Developer credential for the URL and KEY.
2. Save the config.yml file and return to the Jupyter Dashboard.
3. Locate `Main.ipynb` in Jupyter Notebook and open this file.
4. Run all cells. (Cells > Run All)
5. Enter in the listed parameters to filter/sort the output as listed in the Test Cases `Test Steps`
6. Ensure other parameters not mentioned in the `Test Steps` are left at their default values.
7. Make sure to uncheck the JSON  checkbox.
8. Press `Get .CSV Report` to output a .CSV report of the Test Case under implementation.
9. Repeat steps 1 through steps 7 for each Test Case performed.

Notes:
- Kernel only reads config.yml file once at start up, so if you make any changes to URL and KEY it might not read it. 
  - Try restarting the kernel and running all the cells. 
  - Try shutting down Jupyter Notebook and restart it if resetting the kernel doesnt work.
- Ensure your `File Name` when you click ` Get CSV report` is not the same as another filename; it will override and replace it.
- If `TimeOutError` and/or `ConnectionError` occurs, click `Get CSV Report` button again.
- Refer to picture below for default values for each criteria:
<img align="center" src="default criteria.png" width = "600" markdown="1">


## Test Cases

### Default Test Case
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1| Check to ensure CSV report output extracts every Deal| 1. Ensure all criteria is by default: <br/> `Search`: N/A </br> `Status` Any <br/> `Next Date`: Any <br/> `Before`: mm/dd/yyyy <br/> `After`: mm/dd/yyyy <br/> 0 `≤ Value ≤` 0 <br/> `Score =` 0 <br/> 0 `< Score <` 0 <br/> `Sort by` N/A `in this order:` Descending <br/> uncheck box for `return as JSON (debug)` <br/> check box for `Notices`| Should generate a CSV report containing 15 Deals| As Expected | Pass|

### `Search: Title` Test Cases
#### Specific Title & Specific Deal Stage Titles
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for Deal `Title` with valid Deal Title  data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4. Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunny Bonanza <br/> | Should generate a CSV report for Bunny Bonanza| As Expected| Pass|    
|2 | Check `Search` filter for Deal `Title` with invalid Deal Title data| 1. Click Drop Down for Search <br/> 2. Select `Title`<br/> 3. Enter `TitleId` in `Search here `<br/> 4.  Press `Get .CSV Report` to output a .CSV report| **TitleId**: Bunnie Bonanaza <br/> | Should generate an empty CSV report| As Expected| Pass| 
|3 | Check `Search` filter for Deal `Title` with valid Deal Title and Deal Stage data| 1. Click Drop Down for Search <br/> 2. Select `Title` and leave `Search:here` text input box empty <br/> 3. Enter `DealStageId` in `Deal Stage`<br/> 4. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify <br/> | Should generate a CSV report with 3 Deals from the Identify Deal Stage: Bunny Bonanza Lipbalm Website, and Pizza Bingo| As Expected| Pass| 

### `Search: Contacts` Test Cases
#### Sepcific Contact Name 
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Search` filter for `Contacts` with valid ContactId | 1. Click Drop Down for Search and select `Contacts`<br/> 2. Enter `ContactId` in `Search here `<br/> 3. Press `Get .CSV Report` to output a .CSV report| **ContactId**: Bunny Lady <br/> | Should generate a CSV report for Bunny Bonanza with 2 Deals, Bunny Bonanza and Bunny Statistic| As Expected| Pass|
|2 | Check `Search` filter for `Contacts` with missplled ContactId for `Bunny Lady` | 1. Click Drop Down for Search <br/> 2. Select `Contacts`<br/> 3. Enter `ContactId` in `Search here `<br/> 4. Press `Get .CSV Report` to output a .CSV report| **ContactId**: Bunnie Lady <br/> | Should generate an empty CSV report, since `Contacts` is mispelled| As Expected| Pass|

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

All Test cases resulted in an `AttributeError`
```
AttributeError                            Traceback (most recent call last)
~\Documents\GitHub\iConsultancy\iConsultancy\widgets.py in on_button_clicked(_)
    168         for filter in filters_dict_text:
    169             val = filters_dict_text[filter]
--> 170             if not val.isspace() and len(val) != 0:
    171                 filters[filter] = val
    172         for filter in filters_dict_numeric:

AttributeError: 'int' object has no attribute 'isspace'

```

### Deal Stage
### Specific Deal Stage 
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify| Should generate a CSV report for 3 Deals: Bunny Bonanza, Lipbalm Website, and Pizza Bingo| As Expected| Pass|    
|2 | Check `Deal Stage` filter for `Deal Title` with valid data| 1.  Enter `DealStageId` in the `Deal Stage` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Materialize| Should generate a CSV report for 2 Deals: Bunny Statistics and H4U Vending Machines | As Expected| Pass| 

### Owner
#### Specific Owner & Specific Owner for Specified Deal Stage
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Owner` filter with valid data| 1.  Enter `OwnerId` in the `Owner` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **OwnerId**: Rachel Tao| Should generate a CSV report for all Deals owned by Rachel Tao| Not As Expected| Fail|  
|2 | Check `Owner` filter  with valid data| 1.  Enter `OwnerId` in the `Owner` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **OwnerId**: 1| Should generate a CSV report for all Deals owned by Owner 1, which is the numeric representation for Rachel Tao| As Expected| Pass|
|3 | Check `Owner` filter  with invalid data| 1.  Enter `OwnerId` in the `Owner` text input box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **OwnerId**: 2| Should generate an empty CSV report, since Owner 2 does not exist| As Expected| Pass|
|4| Check `Owner` filter with specified `Deal Stage` with valid data| 1.  Enter `OwnerId` in the `Owner` text input box <br/> 2. Enter `DealStageId` in `Deal Stage` text input box <br/> 3. Press `Get .CSV Report` to output a .CSV report| **OwnerId**: 1 <br/> **DealStageId**: Identify| Should generate a CSV report for 2 Deals(Bunny Bonanza and Lipbalm Website) owned by Owner 1 in the Identify Stage| As Expected| Pass|

From the Test Cases performed for `Owner` filter, we noticed that we are unable to generate a report for a specific `Owners` name from our Deals Pipeline. However, we are able to generate a CSV output with the owner as its numeric value.
Rachel Tao is OwnerId 1 from our Pipeline.


### `Tag Name` Test Cases
#### Specific Tag Names & Specific Tag Name for Specified Deal Stage

| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Tag Name` filter for `Deal Title` with valid data| 1.  Enter `TagId` in the `Tag Name` search box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **TagId**: Capstone Fall 2020| Should generate a CSV report for 3 Deals (Bunny Bonanza, Lipbalm Website, and H4U Vending Machines)| As Expected| Pass| 
|2 | Check `Tag Name` filter for `Deal Title` with valid data| 1.  Enter `TagId` in the `Tag Name` search box <br/> 2. Press `Get .CSV Report` to output a .CSV report| **TagId**: Capstone Fall 2020| Should generate a CSV report for 3 Deals (Bunny Bonanza, Lipbalm Website, and H4U Vending Machines)| As Expected| Pass|   

### `Next Date` Test Cases
#### Upcoming, Scheduled, Overdue, No Tasks
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Next Date` filter for Deal's with `Upcoming` Tasks| 1. Click Drop Down for `Next Date` and select `Upcoming` <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for the Deals with Upcoming Tasks| Not As Expected| Fail|
|2 | Check `Next Date` filter for Deal's with `Scheduled` Tasks| 1. Click Drop Down for `Next Date` and select `Scheduled` <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for the 1 Deal, Bunny Bonanza, which is the only Deal that has an upcoming task| As Expected| Pass| 
|3 | Check `Next Date` filter for Deal's with `Overdue` Tasks| 1. Click Drop Down for `Next Date` and select `Overdue` <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for the 1 Deal, H4U Vending Machines, which is the only Deal that has an overdue task | As Expected| Pass| 
|4| Check `Next Date` filter for Deal's with `No Tasks` Tasks| 1. Click Drop Down for `Next Date` and select `No Tasks` <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for 12 Deals that have `No Tasks` | As Expected| Pass| 

For Test Case 1, where it tests for the `Next Date` filter for Deal's with `Upcoming` tasks, we believe this test failed due to failure to create dummy data that had `Upcoming` tasks.

#### Scheduled for Specified Contact & Scheduled for Specified Deal Stage
| Tast Case | Test Case Scenario   | Test Steps      | Test Data      |Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|--------------|-------------|--------|
|1 | Check `Next Date` filter for specifed `ContactId` Deals with `Scheduled` tasks| 1. Click Drop Down for Search and select `Contacts`<br/> 2. Enter `ContactId` in `Search here `<br/> 3. Click Drop Down for `Next Date` and select `Scheduled`  <br/> 3. Press `Get .CSV Report` to output a .CSV report| **ContactId**: Bunny Lady| Should generate a CSV report for 1 Deal with Scheduled task for Bunny Lady: Bunny Bonanza| As Expected| Pass| 
|2 | Check `Next Date` filter for specified `DealStageId` Deals with `Scheduled` tasks| 1. Click Drop Down for Search and select `Contacts`<br/> 2. Enter `ContactId` in `Search here `<br/> 3. Click Drop Down for `Next Date` and select `Scheduled`  <br/> 3. Press `Get .CSV Report` to output a .CSV report| **DealStageId**: Identify| Should generate a CSV report for 2 Deals with Scheduled task from Identify Deal Stage: Bunny Bonanza and Lipbalm Website| As Expected| Pass| 

### `Created` Test Cases
#### `Before`
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Created` filter for Deal creation date with valid data| 1. Click Drop Down for `Before:` and enter "04/16/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for with 3 Deals, which were created before April 16th, 2020| As Expected| Pass|    
|2 | Check `Created` filter for Deal creation date with invalid data.| 1. Click Drop Down for `Before:` and enter "04/16/3020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate an empty CSV report.| As Expected| Pass| 

#### `After`
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Created` filter for Deal creation date with valid data| 1. Click Drop Down for `After:` and enter "05/01/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for with 6 Deals, which were created after May 1st, 2020| As Expected| Pass|    
|2 | Check `Created` filter for Deal creation date with invalid data.| 1. Click Drop Down for `Before:` and enter "05/20/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate an empty CSV report.| As Expected| Pass| 

#### `Before` & `After`
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Created` filter for Deal creation date with valid `Before` and `After` data| 1. Click Drop Down for `Before:` and enter "05/18/2020" <br/> 1. Click Drop Down for `After:` and enter "05/14/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for with 5 Deals: Lipbalm Website, H4U Vending, Bunny Bonanaza, Bunny Statistics, and Pizza Bingo | As Expected| Pass| 

### Project Updated
#### `Before` and `After`
Assumption that is test case works for valid `Before` and `After` that it will work for them on their own.

| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|--------------|-------------|--------|
|1 | Check `Created` filter for Deal creation date with valid `Before` and `After` data| 1. Click Drop Down for `Before:` and enter "05/18/2020" <br/> 1. Click Drop Down for `After:` and enter "05/01/2020" <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for with 5 Deals: Lipbalm Website, H4U Vending, Bunny Bonanaza, Bunny Statistics, and Pizza Bingo | As Expected| Pass| 

### Project Monetary Value
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1 | Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value data| 1.  Enter `150` in the search box to the left of the <br/> `≤ Value ≤` filter and `10000` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 3 Deals (Bunny Bonanza, Lipbalm Website, Bunny Statistics| As Expected| Pass| 
|2| Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value data| 1.  Enter `0` in the search box to the left of the <br/> `≤ Value ≤` filter and `2500` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 4 Deals (Bunny Bonanza, Lipbalm Website, Bunny Statistics, and Pizza Bingo| As Expected| Pass| 
|3| Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value data| 1.  Enter `2500` in the search box to the left of the <br/> `≤ Value ≤` filter and `0` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 1 Deal: H4U Vending Machines| As Expected| Pass| 
|4 | Check <br/> ` ≤ Value ≤` filter for Deals with invalid Deal Value data| 1.  Enter `012` in the search box to the left of the <br/> `≤ Value ≤` filter and `-23` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate an empty CSV report| As Expected| Pass| 
|5| Check <br/> ` ≤ Value ≤` filter for Deals with valid Deal Value and `Deal Stage` data|1.  Enter `Materialize` in the `Deal Stage` search box <br/> 2.  Enter `150` in the search box to the left of the <br/> `≤ Value ≤` filter and `2500` in the search box to the right <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with 1 Deal: Bunny Bonanza| As Expected| Pass|  

### Sort by in Ascending/Desending Order
#### Title
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Title` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Title` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal `Title` in ascending alphabetical order.| As Expected| Pass | 
|2 | Check Sort by widget for Deal `Title` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Title` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal `Title` in descending alphabetical order.| As Expected| Pass |   


#### Value
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Value` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal `Value` in ascending numerical order, from Deals with least monetary value to greatest monetary value.| As Expected| Pass | 
|2 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Title` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal `Value` in ascending numerical order, from Deals with greatest monetary value to least monetary value| As Expected| Pass |   

#### Created Date
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Created Date` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deals ordered from most recent to least recent creation date| As Expected| Pass | 
|2 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Created Date` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deals ordered from least recent to most recent creation date| As Expected| Pass |  

#### Primary Contact Name
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Primary contact first name` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deals ordered from most recent to least recent creation date| Not As Expected; contact name is in ascending order for the contact id value, not the name of the contact | Not As Expected| Fail | 
|2 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Primary contact first name` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deals ordered from least recent to most recent creation date|  Not As Expected; contact name is in ascending order for the contact id value, not the name of the contact | Not As Expected|Fail |  

These test cases failed to order `Contact Names` by ascending and descending order, since the Contact ID is being extracted with the API features and not the Contact Name. (Example: 10 is numeric representation for contact name `Bunny Lady`. 
However, they do order in numerical ascending and descending order for the Contact ID's. 

#### Primary contact organization name
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Primary contact organization name` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal ordered in ascending alphabetical order by Account name| Not As Expected| Fail | 
|2 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Primary contact organization name` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal ordered in descending alphabetical order by Account name| Not As Expected| Fail |  

These test cases failed to order `Contact Names` by ascending and descending order, since the Organization ID is being ordered and not the Organziation name (Example: 3 is numeric representation for orgnanization name `Bunny Lovers`. 
However, they do order in numerical ascending and descending order for the Organization ID's. 

#### Next task due date
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Next task due date` <br/> 2. Click drop down for `in this ord ...` and select  `Ascending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal ordered in descending order by `nexttask` | Not As Expected| Fail | 
|2 | Check Sort by widget for Deal `Value` in `Ascending`| 1. Click Drop Down for `Sort by ` and select `Next task due date` <br/> 2. Click drop down for `in this ord ...` and select  `Descending`. <br/> 3. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report for Deal ordered in descending order by `nexttask` | Not As Expected| Fail |  

Test cases ascending and descending with `nexttasks` that have dates, however, some `nexttask` dates are empty and are ordered inbetween valid dates, where they should appear first in ascending order and last in descending order (chronologically by next task due date, then it appends projects with no next task).

### `Score` Test Cases

#### `Score =` 
| Tast Case | Test Case Scenario   | Test Steps    | Expected Result | Actual Result | Pass/Fail|
|----------|---------------------|-----------------|-----------------|--------------|-------------|
|1| Check to see if `Score =` filter works with valid data| 1. Enter `Score 1` in the `Score Name:` textbox. <br/> 2. Enter `20` in `Score =` text box| Should generate a CSV report with 6 Deals: Bunny Bonanza, Deal 1, in contact Deal 1, in Contact Deal 2, Bunny Statistics, Another deal title, and zero value deal | As Expected| Pass|
|2| Check to see if `Score =` filter works with invalid data| 1. Enter `Score 1` in the `Score Name:` textbox. <br/> 2. Enter `25` in `Score =` text box| Should generate an empty CSV report| As Expected| Pass|

#### `< Score <`
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1 | Check <br/> `< Score <` filter for Deals with valid Score Value data| 1.  Enter `9` in the search box to the left of the <br/> `< Score <` filter and `20` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report with Deals with Score 1 value between 9 and 20| Not As Expected| Fail | 
|2 | Check <br/> `< Score <` filter for Deals with valid Score Value data| 1.  Enter `9` in the search box to the left of the <br/> `< Score <` filter and `20` in the search box to the right <br/> 2. Press `Get .CSV Report` to output a .CSV report| Should generate an empty CSV report, since all Deals have either Score 1 value of 10 or 20| Not As Expected| Pass | 

### Filename
| Tast Case | Test Case Scenario   | Test Steps      | Expected Result | Actual Result | Pass/Fail|
|----------|-------------------|-----------------|--------------|--------------|-------------|
|1| Check `File Name:` for valid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report of all Deals| As Expected| Pass|
|2| Check `File Name:` for invalid `Get .CSV Report`| 1. Enter `testcaseoutput.cvs` as filename in `File Name:` text input box. 2. Press `Get .CSV Report` to output a .CSV report| Should generate a CSV report but saved in an improper file format unable to open as CSV| As Expected| Pass|

