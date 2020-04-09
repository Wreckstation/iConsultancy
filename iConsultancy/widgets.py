# some handy functions to use along widgets
from IPython.display import display, Markdown, clear_output
# widget packages
import ipywidgets as widgets # defining some widgets

from iConsultancy.get_deals import request
from iConsultancy.to_csv import json_to_csv

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
       description='Search:')
search_text = widgets.Text(
       placeholder='Search here',
       description=':')
status_menu = widgets.Dropdown(
       options=[('Any', ''), ('Open', 0), ('Won', 1), ('Lost', 2)],
       value='',
       description='Status:')
stage_text = widgets.Text(
       placeholder='',
       description='Deal Stage:')

checkbox = widgets.Checkbox(
           description='return as CSV',
           value=True)

#Choose date
tempbox = widgets.HBox([calendar, calendar])

#search term
box = widgets.VBox([text, slider, tempbox, checkbox ])
search_box = widgets.Box(children=[search_field_menu, search_text], layout=widgets.Layout(justify_content="flex-start"))

button = widgets.Button(description='My Button')
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
                     'stage': stage_text.value}
          response = request(filters)
          if checkbox.value == True:
            a = json_to_csv(response.json())
          else:
            a = response.text
          print(a)
          
# linking button and function together using a button's method
button.on_click(on_button_clicked)

button_with_check = widgets.HBox([button, checkbox])
#final search menu
full_display = widgets.VBox([search_box, status_menu, stage_text, button_with_check,out])