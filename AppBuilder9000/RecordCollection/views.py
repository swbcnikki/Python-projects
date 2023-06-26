from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from .forms import RecordsForm
from .models import Records
import requests



#Home Page Req
def home(request):
    return render(request, 'RecordCollection/RecordCollection_home.html')

#View Collection Page Req
def records_view(request):
    records_db = Records.Records.all()
    content = {'records_db': records_db}
    return render(request, 'RecordCollection/RecordCollection_View.html', content)

#Add to Collection Page Req
def records_add(request):
    form = RecordsForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('records_home')
    content = {'form': form}
    return render(request, 'RecordCollection/RecordCollection_Add.html', content)

#Random Album Page
def records_random(request):
    return render(request, 'RecordCollection/RecordCollection_Random.html')

#Album Details Page
def records_details(request, pk):
    details = get_object_or_404(Records, pk=pk)
    year, cover = getDiscogs(pk)
    content = { 'details': details, 'year': year, 'cover': cover }
    return render(request, 'RecordCollection/RecordCollection_details.html', content)

#API Call function
def getDiscogs(pk):
    details = get_object_or_404(Records, pk=pk)
    fn = details.artistFN
    ln = details.artistLN
    album = details.title
    key = "zFIXJeohuNqwGIoQEMNP"
    secret = "ahKMBCZzjdDWsgHlivvuUSEPdBQWcoIC"

    discogsCall = requests.get(
        f'https://api.discogs.com/database/search?q={fn}+{ln}+{album}&key={key}&secret={secret}').json()

    #Added to print to console JSON response from Discogs, shows avail labels and specific associated info
    try:
        for item, value in discogsCall['results'][0].items():
            print(str(item) + ": " + str(value))
    except IndexError:
        print("No record found.")

    #Pulls desired information from call and returns as variable
    try:
        year = discogsCall['results'][0]['year']
        cover = discogsCall['results'][0]['cover_image']
        return(year, cover)
    except IndexError:
        year = "No info"
        cover = "https://www.ncenet.com/wp-content/uploads/2020/04/No-image-found.jpg"
        return(year, cover)





#Edit Details
def records_edit(request, pk):
    item = get_object_or_404(Records, pk=pk)
    form = RecordsForm(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('records_details', pk=pk)
        else:
            print(form.errors)
    content = {'form': form}
    return render(request, 'RecordCollection/RecordCollection_edit.html', content)

#Model Specified for Delete View
def records_delete(request, pk):
    item = get_object_or_404(Records, pk=pk)
    content = {'item': item}
    if request.method == "POST":
        item.delete()
        return redirect('records_view')
    return render(request, 'RecordCollection/RecordCollection_Delete.html', content)















