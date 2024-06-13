from django import forms

CHOICES = [(2, "sanjeevi")]


class RadioForm(forms.Form):
    '''
def __init__(self, CHOICES):
    # self.CHOICES = kwargs.pop('CHOICES')
    super().__init__()
    # self.choices = [(1, "Sanjeevi")]
    self.fields['choose_occupation'].choices = CHOICES
    print(CHOICES)
choose_occupation = forms.ChoiceField(widget=forms.RadioSelect())
    '''
    choose_occupation = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
