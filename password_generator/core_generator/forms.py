from django import forms


class RandomPasswordGeneratorForm(forms.Form):
    password_length = forms.IntegerField(
        label="Password length", max_value=200, initial=16, min_value=1)
    include_uppercase = forms.BooleanField(
        label="Include upper case letters ==> e.g. ABCDEFGH..", required=False, initial=True)
    include_lowercase = forms.BooleanField(
        label="Include lower case letters ==> e.g. abcdefgh..", required=False, initial=True)
    include_numbers = forms.BooleanField(
        label="Include numbers ==> e.g. 123456..", required=False, initial=True)
    include_symbols = forms.BooleanField(
        label="Include symbols ==> e.g. @#$%..", required=False, initial=True)
