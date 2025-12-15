from django.shortcuts import render

def calculate_bmii(request):
    bmii = None   # Default value

    if request.method == "POST":
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        bmii = weight / (height * height)

        # Print to server console for debugging
        print("Height:", height)
        print("Weight:", weight)
        print("BMI calculated:", bmii)

    return render(request, "bmiiapp/web.html", {"BMI": bmii})