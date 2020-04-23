# some handy functions to use along widgets
from IPython.display import display, Markdown, clear_output
# widget packages
import ipywidgets as widgets # defining some widgets
from ipywidgets import Layout

from iConsultancy.get_deals import request

text = widgets.Text(
       value='My Text',
       description='Title', )

calendar = widgets.DatePicker(
           description='Select Date')
calendar1 = widgets.DatePicker(
           description='From Date')
calendar2 = widgets.DatePicker(
           description='To Date')

slider = widgets.FloatSlider(
         value=1,
         min=0,
         max=10.0,
         step=0.1,)

search_field_menu = widgets.Dropdown(
        options=[('All', 'all'), ('Title', 'title'), ('Contacts', 'contact'), ('Organizations', 'org')],
        value='all',
        description='Search:',
        layout=Layout(width = '15em'))
search_text = widgets.Text(
       placeholder='Search here',
       description='')
status_menu = widgets.Dropdown(
       options=[('Any', ''), ('Open', 0), ('Won', 1), ('Lost', 2)],
       value='',
       description='Status:')
stage_text = widgets.Text(
       placeholder='',
       description='Deal Stage:')
owner_text = widgets.Text(
       placeholder='',
       description='Owner:')

nextdate_range_menu = widgets.Dropdown(
       options=[('Any', ''),('Upcoming', 'upcoming'), ('Scheduled', 'scheduled'), ('Overdue', 'overdue'), ('No tasks', 'no-task')],
       value='',
       description='Next Date:')

tag_text = widgets.Text(
       placeholder='',
       description='Tag Name:')
multiple_tag_checkbox = widgets.Checkbox(
           description='Return all tags that match',
           value=False)
tag_box = widgets.HBox([tag_text, multiple_tag_checkbox])

tasktype_text = widgets.Text(
       placeholder='',
       description='Task type:')

sortby_menu = widgets.Dropdown(
       options=[('N/A', ''), ('Title', 'title'), ('Value', 'value'), ('Created date', 'cdate'), ('Primary contact first name', 'contact_name'), ('Primary contact organization name', 'contact_orgname'), ('Next task due date', 'next-action')],
       value='',
       description='Sort by:',
       layout=Layout(width = '15em'))   
sortorder_menu = widgets.Dropdown(
       options=[('Descending', 'DESC'), ('Ascending', 'ASC')],
       value='DESC',
       description='')

minval_floattext = widgets.FloatText(
       placeholder='0',
       description='',
       layout=Layout(width = '20%'))
maxval_floattext = widgets.FloatText(
       placeholder='0',
       description='',
       layout=Layout(width = '20%'))
val_label = widgets.Label(value='≤ Value ≤')

val_box = widgets.HBox([minval_floattext, val_label, maxval_floattext])

checkbox = widgets.Checkbox(
           description='return as JSON (debug)',
           value=True)
warning_checkbox = widgets.Checkbox(
           description='Notices',
           layout=Layout(width = '20%'),
           value=True)

file_name_text = widgets.Text(
    description='File Name:',
    layout=Layout(width = '50%'),
    value='output.csv')

#Choose date
tempbox = widgets.HBox([calendar, calendar])

#search term
box = widgets.VBox([text, slider, tempbox, checkbox ])
search_box = widgets.Box(children=[search_field_menu, widgets.Label(
    value=':'), search_text], layout=widgets.Layout(justify_content="flex-start"))

#sort
box2 = widgets.VBox([text, slider, tempbox, checkbox ])
sort_box = widgets.Box(children=[sortby_menu, widgets.Label(
    value='in this order:'), sortorder_menu], layout=widgets.Layout(justify_content="flex-start"))

button = widgets.Button(description='Get .CSV Report')
out = widgets.Output()

# Output widgets
def on_button_clicked(_):
    # "linking function with output"
    with out:
        # what happens when we press the button
        clear_output()
        filters = {'search_field': search_field_menu.value,
                   'search': search_text.value,
                   'status': status_menu.value,
                   'stage': stage_text.value,
                   'owner': owner_text.value,
                   'tags': tag_text.value,
                   'tasktype': tasktype_text.value,
                   'nextdate_range': nextdate_range_menu.value
                  }
        sort = {'sortby': sortby_menu.value, 'sortorder': sortorder_menu.value}
        response = request(filters, sort, checkbox.value, file_name_text.value, multiple_tag_checkbox.value)
        if warning_checkbox.value == True:
            print(response[1]) # return any system messages that the query returned
        print(response[0])

# linking button and function together using a button's method
button.on_click(on_button_clicked)

button_with_check = widgets.HBox([button, checkbox, warning_checkbox])
#final search menu
full_display = widgets.VBox([search_box, status_menu, stage_text, owner_text, tag_box, nextdate_range_menu, tasktype_text, sort_box, val_box, button_with_check,file_name_text,out])