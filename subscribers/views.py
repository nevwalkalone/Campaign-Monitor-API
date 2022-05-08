from django.shortcuts import render, redirect
from .forms import SubscriberForm
from createsend import *


# replace it with your Campaign Monitor API key
api_key = 'COVVLZjeGCvrNkl9Q8kajdOE0UGAv2co0DKejHI8l6Kth+vHnc7QmaB8G65ONeEME7DWxSmZ1tbkr8DJKRhEzOv0Ifclf2CDbawlHZHumPuuekl4vqgYLb+FP9/zCY2EdL1qhM7aFwmydvQuNBlDnw=='
auth = {'api_key': api_key}

# replace it with the list id of your choice
list_id = "a94f7e69caaf3e3193897af3b643c0d0"


def get_active_subs():
    """
    Helper function to get a List with the Active Subscribers
    from the Campaign Monitor API
    """

    message = "not-empty"
    sub_list = List(auth, list_id)
    active_subs = sub_list.active().Results

    if len(active_subs) == 0:
        message = "empty"

    return active_subs, message


def subscribers_list(request):
    """
    Displays the Subscribers List with the use of a
    helper function.
    """

    active_subs, message = get_active_subs()
    context = {"subscribers_list": active_subs, "message": message}
    return render(request, "subscribers/subscribers_list.html", context)


def subscribers_form(request):
    """
    Displays the Subscription Form. Adds user if the 
    "submit" button is selected.
    """

    if request.method == "POST":
        form = SubscriberForm(request.POST)

        if form.is_valid():

            form_data = form.cleaned_data
            email = form_data['email']
            name = form_data['full_name']

           
            new_subscriber = Subscriber(auth, email_address=email)
            new_subscriber.add(list_id, email, name, [], True, "Unchanged")
          
        return redirect('subscribers_list')

    form = SubscriberForm()

    return render(request, "subscribers/subscribers_form.html", {"form": form})


def subscribers_delete(request, email):
    """
    Deletes a User from the Campaign Monitor API List and
    redirects to the subscribers_list page.
    """

    deleted_sub = Subscriber(auth, list_id, email)
    deleted_sub.delete()


    return redirect('subscribers_list')


  