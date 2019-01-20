from django.forms.widgets import ChoiceWidget
#from django.template import loader
#from django.utils.safestring import mark_safe


class TableSelect(ChoiceWidget):
    input_type = 'radio'
    template_name = 'misc/table_select.html'
    option_template_name = 'django/forms/widgets/radio_option.html'

    


# class TableSelect(ChoiceWidget):
#     template_name = 'Core/misc/table_select.html'

#     def get_context(self, name, value, attrs=None):
#         return {'widget': {
#             'name': name,
#             'value': value,
#         }}

#     def render(self, name, value, attrs=None):
#         context = self.get_context(name, value, attrs)
#         template = loader.get_template(self.template_name).render(context)
#         return mark_safe(template)