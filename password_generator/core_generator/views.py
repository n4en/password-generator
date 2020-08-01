from django.shortcuts import render
from .forms import RandomPasswordGeneratorForm
import random
import string


def index(request, *args, **kwargs):
    opt_password = ''.join(random.choice(
        string.ascii_letters + string.digits + string.punctuation) for i in range(16))

    if request.method == 'POST':
        password_generator_request = RandomPasswordGeneratorForm(request.POST)

        if password_generator_request.is_valid():
            opt_password = get_random_password(request)

    else:
        password_generator_request = RandomPasswordGeneratorForm()

    context = {
        'password_generator_request': password_generator_request, 'opt_password': opt_password
    }

    return render(request, "core_generator/index.html", context)


def get_random_password(request, *args, **kwargs):
    if request.method == 'POST':
        password_generator_request = RandomPasswordGeneratorForm(request.POST)
        if password_generator_request.is_valid():
            password_length = password_generator_request.cleaned_data['password_length']
            include_uppercase = password_generator_request.cleaned_data['include_uppercase']
            include_lowercase = password_generator_request.cleaned_data['include_lowercase']
            include_numbers = password_generator_request.cleaned_data['include_numbers']
            include_symbols = password_generator_request.cleaned_data['include_symbols']

            str_input_letters = ""

            if include_uppercase == True:
                str_input_letters = str_input_letters+string.ascii_uppercase
            if include_lowercase == True:
                str_input_letters = str_input_letters+string.ascii_lowercase
            if include_numbers == True:
                str_input_letters = str_input_letters+string.digits

            if include_symbols == True:
                str_input_letters = str_input_letters+string.punctuation

            if len(str_input_letters) == 0:
                str_input_letters = string.ascii_letters+string.digits + string.punctuation

            opt_password = ''.join(random.choice(str_input_letters)
                               for i in range(password_length))

            return str(opt_password)
