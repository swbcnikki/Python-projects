from django.shortcuts import render, get_object_or_404, redirect
from .forms import PetApplicantForm, AvailablePetForm, FilterForm
from .models import PetApplicant, AvailablePet
from datetime import datetime
import requests, json, pprint


# Create your views here.
def format_date(date):
    date = date.split('-')
    date = [int(i) for i in date]
    return date


def calculate_birthday(date):
    b_day = date
    b_day = format_date(b_day)
    current_date = datetime.today().strftime('%Y-%m-%d')
    current_date = format_date(current_date)
    b_year = current_date[0] - b_day[0]
    b_month = current_date[1] - b_day[1]
    if b_year == 0:
        if b_month == 0:
            return "Less than 1 month old!"
        elif b_month == 1:
            return "{} month old".format(b_month)
        else:
            return "{} months old".format(b_month)
    else:
        if b_month == 0:
            if b_year == 1:
                return "{} year old".format(b_year)
            else:
                return "{} years old".format(b_year)
        if b_month == 1:
            if b_year == 1:
                return "{} year and {} month old".format(b_year, b_month)
            else:
                return "{} years and {} month old".format(b_year, b_month)
        else:
            if b_year == 1:
                return "{} year and {} months old".format(b_year, b_month)
            else:
                return "{} years and {} months old".format(b_year, b_month)


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


def home(request):
    return render(request, 'FindPetApp/find_pet_home.html')


def applicants(request):
    if request.method == 'POST':
        if 'Add_Applicant' in request.POST:
            applyform = PetApplicantForm(data=request.POST)
            if applyform.is_valid():
                applyform.save()
                return redirect('confirmed')
        if 'Add_Rescue' in request.POST:
            petform = AvailablePetForm(data=request.POST)
            if petform.is_valid():
                current_pet = petform.save(commit=False)
                date = request.POST.get('birthday')
                current_pet.age = calculate_birthday(date)
                petform.save()
                return redirect('confirmed')
    applyform = PetApplicantForm()
    petform = AvailablePetForm()

    content = {'applyform': applyform, 'petform': petform}
    return render(request, 'FindPetApp/applicants.html', content)


def available_pets(request):
    available = AvailablePet.Available.all()
    applicant = PetApplicant.Applicant.all()
    content = {'available': available, 'applicant': applicant}
    return render(request, 'FindPetApp/available_pets.html', content)


def confirmed(request):
    return render(request, 'FindPetApp/confirmed.html')


def find_pet_contact(request):
    return render(request, 'FindPetApp/find_pet_contact.html')


def pet_details(request, available_id):
    pet = get_object_or_404(AvailablePet, pk=available_id)
    pet_name = pet.name
    if request.method == 'POST':
        pet.delete()
        return redirect('delete_confirmed', pet_name)
    content = {'pet': pet}
    return render(request, 'FindPetApp/pet_details.html', content)


def edit_pet_listing(request, available_id):
    pet = get_object_or_404(AvailablePet, pk=available_id)
    pet_name = pet.name
    if request.method == 'POST':
        petform = AvailablePetForm(data=request.POST, instance=pet)
        if petform.is_valid():
            current_pet = petform.save(commit=False)
            date = request.POST.get('birthday')
            current_pet.age = calculate_birthday(date)
            petform.save()
            return redirect('edit_confirmed', pet_name)
    else:
        petform = AvailablePetForm(instance=pet)
    content = {'pet': pet, 'petform': petform}
    return render(request, 'FindPetApp/edit_pet_listing.html', content)


def edit_confirmed(request, pet_name):
    pet = pet_name
    content = {'pet': pet}
    return render(request, 'FindPetApp/edit_confirmed.html', content)


def delete_confirmed(request, pet_name):
    pet = pet_name
    content = {'pet': pet}
    return render(request, 'FindPetApp/delete_confirmed.html', content)


def app_builder_home(request):
    return render(request, '/index.html')


def rescue_groups_filter(request):
    form = FilterForm(data=request.POST)
    if request.method == "POST":
        if form.is_valid():
            animal_filter = request.POST.get('animal_filter')
            number_of_results = request.POST.get("number_of_results")
            return redirect('rescue_groups', animal_filter, number_of_results)
    context = {'form': form}
    return render(request, 'FindPetApp/rescue_groups_filter.html', context)


def rescue_groups(request, animal_filter, number_of_results):
    if animal_filter == "dogs":
        animal_filter = "/dogs"
    elif animal_filter == "cats":
        animal_filter = "/cats"
    else:
        animal_filter = ""

    url = 'https://api.rescuegroups.org/v5/public/animals/search' + animal_filter + '?limit=' + str(number_of_results) + '&include=pictures,species&fields%5Banimals%5D=name,sex,breedPrimary,descriptionText,id,sizeGroup&fields%5Bpictures%5D=large&fields%5Bspecies%5D=singular'
    header = {
        'Authorization': 'KfQZGxLk'
    }
    response = requests.get(url, headers=header)
    pet_data = response.json()
    breeds = []
    descriptions = []
    names = []
    sexes = []
    species = []
    picture_ids = []
    picture_urls = []
    pet_pictures = []

    j = 0
    while j < len(pet_data['included']):
        picture_id = pet_data['included'][j]["id"]
        file_size = pet_data['included'][j]['attributes'].get('large', 'No picture provided')
        if file_size == 'No picture provided':
            j += 1
            continue
        picture_url = file_size['url']
        picture_ids.append(picture_id)
        picture_urls.append(picture_url)
        j += 1

    i = 0
    while i < len(pet_data['data']):
        breed = pet_data['data'][i]['attributes']['breedPrimary']
        breeds.append(breed)
        description = pet_data['data'][i]['attributes'].get('descriptionText', "no description provided")
        descriptions.append(description)
        name = pet_data['data'][i]['attributes'].get('name', "not provided")
        names.append(name)
        sex = pet_data['data'][i]['attributes'].get('sex', "not provided")
        sexes.append(sex)
        specie_id = pet_data['data'][i]['relationships']['species']['data'][0].get("id", "not provided")
        if specie_id == "3":
            species.append("Cat")
        elif specie_id == "8":
            species.append("Dog")

        x = 0
        for p in picture_ids:
            relationships = pet_data['data'][i]['relationships']
            picture = relationships.get('pictures', "No picture provided")
            if picture == "No picture provided":
                break
            print(picture)
            data_picture_id = picture['data'][0].get('id', "0")
            #data_picture_id = pet_data['data'][i]['relationships']['pictures']['data'][0].get('id', "0")
            if data_picture_id == p:
                picture = picture_urls[x]
                x += 1
                break
            else:
                picture = 'No picture provided'
                x += 1
        pet_pictures.append(picture)
        i += 1

    #print(names, species, breeds, sexes, descriptions, pet_pictures)
    pet_list = zip(names, species, breeds, sexes, descriptions, pet_pictures)
    content = {'pet_list': pet_list}
    return render(request, 'FindPetApp/rescue_group.html', content)
