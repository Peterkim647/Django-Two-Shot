from django.shortcuts import render
from receipts.models import Receipt
from django.contrib.auth.decorators import login_required


@login_required
def receipt_list(request):
    logged_in_user = request.user
    receipt_list = Receipt.objects.filter(purchaser=logged_in_user)
    context = {
        "receipt_list": receipt_list
        }
    return render(request, "receipts/list.html", context)
