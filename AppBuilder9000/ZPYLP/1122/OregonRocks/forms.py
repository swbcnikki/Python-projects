from django.forms import ModelForm
from .models import RockLoc
# from .models import EditRockLoc

class RockForm(ModelForm):
    class Meta:
        model = RockLoc
        fields = '__all__'

# class EditForm(ModelForm):
#     class Meta:
#         model = RockLoc
#         fields = ('updated_at', 'address', 'location_description')

    # def save(self, name=None):
    #     loc = super(EditForm, self).save(commit=False)
    #     if name:
    #         loc.name = name
    #     loc.save()
    #     return loc

