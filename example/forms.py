from django import forms

LOREM = (
    'Consequuntur consequatur commodi ut doloremque voluptatum quo ipsa '
    'debitis. Nesciunt voluptatibus possimus maxime sint expedita sit quia '
    'perferendis. Amet voluptatem sed sed molestiae. Magni totam est aut et '
    'eaque autem omnis.'
)
CHOICES = [
    ('apple', 'apple'),
    ('orange', 'orange'),
    ('banana', 'banana'),
]


class ExampleForm(forms.Form):
    char = forms.CharField(help_text=LOREM)
    disabled = forms.CharField(disabled=True)
    hidden = forms.CharField(widget=forms.HiddenInput)
    text = forms.CharField(widget=forms.Textarea)
    boolean = forms.BooleanField()
    file = forms.FileField()
    select = forms.ChoiceField(choices=CHOICES)
    select_multiple = forms.MultipleChoiceField(choices=CHOICES)
    radio = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    checkbox_multiple = forms.MultipleChoiceField(
        choices=CHOICES, widget=forms.CheckboxSelectMultiple
    )
    date = forms.DateField(widget=forms.SelectDateWidget())
    date_time = forms.SplitDateTimeField()
    required_css_class = 'required'

    def clean(self):
        cleaned_data = super().clean()
        self.add_error(None, 'This is a non-field error')
        return cleaned_data
