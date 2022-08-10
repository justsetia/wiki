

from django import forms

from encyclopedia import util
from encyclopedia.util import get_entry


from django.core.exceptions import ValidationError

from encyclopedia.util import delete_entry


class entriesform(forms.Form):
    name = forms.CharField(max_length=100)
    about = forms.CharField(widget=forms.Textarea)

    def clean(self):

        name = self.cleaned_data['name']
        about = self.cleaned_data['about']

        if get_entry(name) is not None:
            raise ValidationError('It has already been taken')
        else:
            util.save_entry(name, about)

        return self.cleaned_data


# class entriesdelete(forms.Form):
    #title = forms.CharField()

    # def delete(title):
        # delete_entry(title)
