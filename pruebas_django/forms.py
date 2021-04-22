from django import forms

class TodoForm(forms.Form):
    descripcion = forms.CharField(label='Descripción', max_length=100)
    done = forms.BooleanField(label='Is done')