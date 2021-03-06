# some handy functions to use along widgets
from IPython.display import display, Markdown, clear_output
# widget packages
import ipywidgets as widgets # defining some widgets
from ipywidgets import Layout

from iConsultancy.get_deals import request

# Search field
search_field_menu = widgets.Dropdown(
        options=[('N/A', ''), ('Title', 'title'), ('Contacts', 'contact'), ('Organizations', 'org')],
        value='',
        description='Search:',
        layout=Layout(width = '15em'))
search_text = widgets.Text(
       placeholder='Search here',
       description='')

# Status
status_menu = widgets.Dropdown(
       options=[('Any', ''), ('Open', 0), ('Won', 1), ('Lost', 2)],
       value='',
       description='Status:')
# Stage
stage_text = widgets.Text(
       placeholder='',
       description='Deal Stage:')
# Owner
owner_text = widgets.Text(
       placeholder='',
       description='Owner:')

# Next date range
nextdate_range_menu = widgets.Dropdown(
       options=[('Any', ''),('Upcoming', 'upcoming'), ('Scheduled', 'scheduled'), ('Overdue', 'overdue'), ('No tasks', 'no-task')],
       value='',
       description='Next Date:')

# Tags
tag_text = widgets.Text(
       placeholder='',
       description='Tag Name:')
multiple_tag_checkbox = widgets.Checkbox(
           description='Return all tags that match',
           value=False)
tag_box = widgets.HBox([tag_text, multiple_tag_checkbox])

# Tasktype
tasktype_text = widgets.Text(
       placeholder='',
       description='Task type:')
       
# Created
created_label = widgets.Label(value='Created')
created_before_calendar = widgets.DatePicker(
           description='Before:')
created_after_calendar = widgets.DatePicker(
           description='After:')
created_hbox = widgets.HBox([created_before_calendar, created_after_calendar])
created_box = widgets.VBox([created_label, created_hbox])

# Sort
sortby_menu = widgets.Dropdown(
       options=[('N/A', ''), ('Title', 'title'), ('Value', 'value'), ('Created date', 'cdate'), ('Primary contact first name', 'contact_name'), ('Primary contact organization name', 'contact_orgname'), ('Next task due date', 'next-action')],
       value='',
       description='Sort by:',
       layout=Layout(width = '15em'))   
sortorder_menu = widgets.Dropdown(
       options=[('Descending', 'DESC'), ('Ascending', 'ASC')],
       value='DESC',
       description='')

# Updated
updated_label = widgets.Label(value='Updated')
updated_before_calendar = widgets.DatePicker(
           description='Before:')
updated_after_calendar = widgets.DatePicker(
           description='After:')
updated_hbox = widgets.HBox([updated_before_calendar, updated_after_calendar])
updated_box = widgets.VBox([updated_label, updated_hbox])

# Minimum and maximum value
minval_floattext = widgets.FloatText(
       placeholder='',
       description='',
       layout=Layout(width = '20%'))
maxval_floattext = widgets.FloatText(
       placeholder='',
       description='',
       layout=Layout(width = '20%'))
val_label = widgets.Label(value='≤ Value ≤')
val_box = widgets.HBox([minval_floattext, val_label, maxval_floattext])

# Score
score_name_text = widgets.Text(description='Score Name:')
score_floatext = widgets.FloatText(
    placeholder='',
    description='Score =')
score_g_floattext = widgets.FloatText(
       placeholder='',
       description='',
       layout=Layout(width = '20%'))
score_l_floattext = widgets.FloatText(
       placeholder='',
       description='',
       layout=Layout(width = '20%'))
score_label = widgets.Label(value='< Score <')
score_hbox = widgets.HBox([score_g_floattext, score_label, score_l_floattext])
score_box = widgets.VBox([score_name_text,score_floatext,score_hbox])

# Output options
checkbox = widgets.Checkbox(
           description='return as JSON (debug)',
           indent=False,
           value=False)
warning_checkbox = widgets.Checkbox(
           description='Notices',
           layout=Layout(width = '20%'),
           indent=False,
           value=True)

file_name_text = widgets.Text(
    description='File Name:',
    layout=Layout(width = '50%'),
    value='output.csv')

#search term
search_box = widgets.Box(children=[search_field_menu, widgets.Label(
    value=':'), search_text], layout=widgets.Layout(justify_content="flex-start"))

button = widgets.Button(description='Get .CSV Report',
                        layout=Layout(width = '50%'))
out = widgets.Output()

#sort
sort_box = widgets.Box(children=[sortby_menu, widgets.Label(
    value='in this order:'), sortorder_menu], layout=widgets.Layout(justify_content="flex-start"))

# Output widgets
def on_button_clicked(_):
    # "linking function with output"
    filters_dict_text = {'search_field': search_field_menu.value,
                   'search': search_text.value,
                   'status': status_menu.value,
                   'stage': stage_text.value,
                   'owner': owner_text.value,
                   'tags': tag_text.value,
                   'tasktype': tasktype_text.value,
                   'score_name': score_name_text.value
                    }
    filters_dict_date = {'created_before': created_before_calendar.value,
                   'created_after': created_after_calendar.value,
                   'updated_before': updated_before_calendar.value,
                   'updated_after': updated_after_calendar.value,
                   'nextdate_range': nextdate_range_menu.value
                   }
    filters_dict_numeric = {'minimum_value': minval_floattext.value,
                   'maximum_value': maxval_floattext.value,
                   'score_greater_than': score_g_floattext.value,
                   'score_less_than': score_l_floattext.value,
                   'score': score_floatext.value
                   }
    with out:
        # what happens when we press the button
        clear_output()
        # value and score must be altered to be used as a score
        filters = {}
        for filter in filters_dict_text:
            val = filters_dict_text[filter]
            if not val.isspace() and len(val) != 0:
                filters[filter] = val
        for filter in filters_dict_numeric:
            val = filters_dict_numeric[filter]
            if val != 0 and val != '0':
                filters[filter] = val
        for filter in filters_dict_date:
            val = filters_dict_date[filter]
            if val is not None:
                filters[filter] = val
        sort = {'sortby': sortby_menu.value, 'sortorder': sortorder_menu.value}
        response = request(filters, sort, checkbox.value, file_name_text.value, multiple_tag_checkbox.value)
        if warning_checkbox.value == True:
            print(response[1]) # return any system messages that the query returned
        if checkbox.value == False:
            print('Saved as ' + file_name_text.value +'.\nOutput:')
        else:
            print('Output:')
        print(response[0]) # If response is none it won't error because of concatenating None

# linking button and function together using a button's method
button.on_click(on_button_clicked)
button_with_check = widgets.HBox([button, checkbox, warning_checkbox])

#final search menu
full_display = widgets.VBox([search_box,
                            status_menu,
                            stage_text,
                            owner_text, 
                            tag_box, 
                            nextdate_range_menu, 
                            tasktype_text,
                            created_box,
                            updated_box, 
                            val_box,
                            score_box,
                            sort_box,
                            button_with_check,
                            file_name_text,
                            out])
