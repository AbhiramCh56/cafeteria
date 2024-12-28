from django.shortcuts import render,redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        # Handle form submission
        issue = request.POST.get('issue')
        name = request.POST.get('name', 'Anonymous')
        photo = request.FILES.get('photo')

        # Save the feedback data (or send an email, etc.)
        # Example: Feedback.objects.create(issue=issue, name=name, photo=photo)

        # Redirect or return a response
        return render(request, 'feedback/thank_you.html')

    return render(request, 'feedback/feedback_form.html')

def starting_page(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to thank you page after submission
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'feedback/thank_you.html')