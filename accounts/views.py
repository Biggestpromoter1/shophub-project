from django.shortcuts import render, redirect
from .models import Visitor


def register(request):
    if request.method == "POST":
        Visitor.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            location=request.POST.get("location"),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone_number")
        )

        return redirect("register")

    return render(request, "accounts/register.html")

# Create a view that allows visitors to register on ShopHub.
# Collect their first and last name, location (.e.g Lagos),
# and email, phone number.
#
# TODO:
#   1. Create a model(s).
#   2. Create a view(s).
#   3. Write up a URL pattern.
#   4. Create an HTML template.
# Submission:
#   - Create a new branch off of main.
#   - Create commit(s) with meaningful messages.
#   - Push the branch with your changes.
#   - Create a pull request (PR) to main.
#   - Request review from me (@theolujay)
# Due: 5 PM. 25th of June, 2026.
