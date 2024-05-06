from django import forms

class TaskForm(forms.Form):#inheriting the class to extend functionality
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control f_name'}), required=False)
    details = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)
    no_people = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    # date_created = forms.DateInput()
    day_of_week = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}), required=False)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        details = cleaned_data.get('details')
        no_people = cleaned_data.get('no_people')
        # date_created = cleaned_data.get('date_created')
        day_of_week = cleaned_data.get('day_of_week')

        if not name:
            self.add_error('name', 'Please provide a name')
        elif len(name) < 3:
            self.add_error('name', 'Name must be at least 3 characters')
        
        if not details:
            self.add_error('details', 'Please provide clear details')
        elif len(details) < 10:
            self.add_error('details', 'Details must be at least 3 characters')

        if not no_people:
            self.add_error('no_people', 'Please provide the number of people')
        
        if not day_of_week:
            self.add_error('day_of_week', 'Please provide the day of the week')
        
        return cleaned_data
        



