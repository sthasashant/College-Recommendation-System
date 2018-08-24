from QueAns.models import College, Review


def calc():
    data = Review.objects.all()
    form = forms.Ques()

    if request.method == 'POST':
        form = forms.Ques(request.POST)

        if form.is_valid():
            print('sashant')
            print(data)
