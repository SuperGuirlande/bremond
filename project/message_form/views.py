from django.shortcuts import get_object_or_404, redirect, render
from .models import ContactMessage


def confirm_delete_message(request, id):
    message = get_object_or_404(ContactMessage, id=id)

    context = {
        'message': message,
    }

    return render(request, 'message_form/confirm_delete_message.html', context)


def delete_message(request, id):
    message = get_object_or_404(ContactMessage, id=id)
    message.delete()
    request.session['success'] = "Le message à bien été supprimé"
    return redirect('admin_index')