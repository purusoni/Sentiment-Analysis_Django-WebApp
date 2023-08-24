from django import forms


# Create a subclass of the CharField to add a class to the widget
class CharFieldWithClass(forms.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('widget', forms.TextInput(attrs={'class': 'form-control form-control-lg w-75', 'type': "text", }))
        super().__init__(*args, **kwargs)


class TextInputForm(forms.Form):
    text_input = CharFieldWithClass(
        label='Enter a sentence to analyze', 
        max_length=128, 
        initial='I am so happy to see you',
    )

