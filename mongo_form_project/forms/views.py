
from django.shortcuts import render, redirect
from .forms import FormDataForm
from pymongo import MongoClient


def form_view(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Now let's push this data to MongoDB Atlas
            # addjoint48
            # Temp8085
            client = MongoClient("mongodb+srv://addjoint48:Temp8085@cluster0.w6wugjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
            db = client["test"]
            collection = db["MongoDBAtlasTEST"]
            data = {
                "title": form.cleaned_data['title'],
                "description": form.cleaned_data['description'],
                "links": form.cleaned_data['links'],
                "documents": str(form.cleaned_data['documents']),
            }
            collection.insert_one(data)
            client.close()
            return redirect('success')  # Redirect to a success page
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')


def view_data(request):
    client = MongoClient("mongodb+srv://addjoint48:Temp8085@cluster0.w6wugjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["test"]
    collection = db["MongoDBAtlasTEST"]
    
    # Fetch data from MongoDB
    data = list(collection.find())
    
    # Close the MongoDB connection
    client.close()
    
    # Render the template with the fetched data
    return render(request, 'view_data.html', {'data': data})

    # views.py
from django.shortcuts import render
from pymongo import MongoClient

def show_image(request):
    client = MongoClient("mongodb+srv://addjoint48:Temp8085@cluster0.w6wugjo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    db = client["test"]
    collection = db["MongoDBAtlasTEST"]
    
    # Retrieve image data from MongoDB Atlas
    image_data = collection.find_one()["image_data"]  # Assuming you have one document with image data
    
    # Close the MongoDB Atlas connection
    client.close()
    
    # Pass image data to the template
    return render(request, 'show_image.html', {'image_data': image_data})
