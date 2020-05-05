# UMD iConsultancy ActiveCampaign API Deals Extractor - User Guide

## Make sure the instructions in README.md have been followed before using this program.

---
## How to use
1. Run `Main.ipynb` in Jupyter Notebook.
2. Run all cells. (Cells > Run All) These fields should appear on your screen: ![](UI.png)  
3. Enter in desired parameters to filter and/or sort the output, if applicable.
4. Check if you would like to output as JSON and/or output w/ notices.
4. Press `Get .CSV Report` to output a .CSV report of the ActiveCampaign Deals.
---

## Components

### Search
<img align="left" src="user guide gfx\searchUI.png"><br/><br/><br/><br/><br/>

Searches deals by keyword. The dropdown lets you specify searching by: 
- **Title:** Project title.
- **Contacts:** 1st name of the project's primary contact.
- **Organization:** Name of the project's primary contact's organization.

### Status
<img align="left" src="user guide gfx\statusUI.png"><br/><br/><br/><br/><br/>

Filters deals by their status. The dropdown lets you filter by:
- **Open:** Current projects in progress.
- **Won:** Successfully completed & closed projects.
- **Lost:** Incomplete and closed projects.

### Deal Stage
<img align="left" src="user guide gfx\dealstageUI.png"><br/><br/>

Filters deals based on its pipeline stage. Type the name of the deal stage to filter by.

Deal Stage Options: 
- Identify
- Qualify
- Pursue
- Materialize
- Capture
- Work in Process
- Close

### Owner
<img align="left" src="user guide gfx\ownerUI.png"><br/><br/>

Filters deals based on the name of the deal owner. Type the name of the deal owner to filter by. 

### Tag Name
<img align="left" src="user guide gfx\tagnameUI.png"><br/><br/>

Filters deals based on a deal's tag name within the Deals pipeline associated w/ deal's primary contact. Type the name of the tag name to filter by. 

### Next Date
<img align="left" src="user guide gfx\nextdateUI.png"><br/><br/><br/><br/><br/><br/>

Filters deals based on a deal's tasks due dates. The dropdown lets you filter by:
- **Any:** occurs by default; orders projects based by deal's next task's due date first. Then append projects w/ no next task. Lastly append projects w/ overdue tasks. 
- **Upcoming:** Deals w/ next task's date. 
- **Scheduled:** Deals w/ scheduled task dates.
- **Overdue:** Deals w/ tasks that have past dates.
- **No tasks:** Deals w/ no scheduled/upcoming tasks.

If dates are the same, it will order by the deal's ID.

### Sorting
<img align="left" src="user guide gfx\sortUI.png"><br/><br/><br/><br/><br/><br/><br/><br/>

Sorts deals based on the following in ascending/descending order:
- **Title:** alphabetically by their given deal title name.
- **Value:** numerically based on a deal's value.
- **Created date:** chronologically by the deal's creation date .
- **Primary contact first name:** alphabetically by the primary contact's first name.
- **Primary contact organization name:** alphabetically by the primary contact's organization name.
- **Next task due date:** chronologically by next task due date (then it appends projects with no next task, then deals with overdue tasks - if project task dates are the same, it will order by their deal id).

### Created & Updated
<img align="left" src="user guide gfx\createdupdatedUI.png"><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> 

Filters deals between dates before/after they were created and/or updated. You may type the date, increment/decrement the day/month/year, or select a calendar date via the dropdown arrow.

### Value
<img align="left" src="user guide gfx\valueUI.png"><br/><br/>

Filters deals based on a deal's monetary value. Type the min/max values to filter by.

### Score
<img align="left" src="user guide gfx\scoreUI.png"><br/><br/><br/><br/><br/>

Filters deals based on a deal's score. Type the score name, and/or the score values that it equals/is between.

### Output
<img align="left" src="user guide gfx\outputUI.png"><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/> 

Check if you would like to output as JSON and/or output w/ notices, set the output filename as desired, then press `Get .CSV Report`.

