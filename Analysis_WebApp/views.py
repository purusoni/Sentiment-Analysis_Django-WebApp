from django.shortcuts import render
from django.shortcuts import render
from .forms import TextInputForm
from transformers import pipeline

sentiment_model_pipeline = pipeline("text-classification", model='bhadresh-savani/distilbert-base-uncased-emotion', return_all_scores=True)

test_text = "I am so happy to see you"
test_sentiment = sentiment_model_pipeline(test_text)

test_sentiment_dict = {}

for test_label_dict in test_sentiment[0]:
    test_label = test_label_dict['label']
    test_score = test_label_dict['score']
    test_sentiment_dict[test_label] = round(test_score*100, 2)


# Create your views here.
def index(request):
    form = TextInputForm()

    data = {
        'joy': 0.0,
        'sadness': 0.0,
        'love': 0.0,
        'anger': 0.0,
        'fear': 0.0,
        'surprise': 0.0,
        'form': form,
    }

    if request.method == 'POST':
        form = TextInputForm(request.POST)
        
        if form.is_valid():
            text_input = form.cleaned_data['text_input']
            sentiment = sentiment_model_pipeline(text_input)

            sentiment_dict = {}

            for label_dict in sentiment[0]:
                label = label_dict['label']
                score = label_dict['score']
                sentiment_dict[label] = round(score*100, 2)

            data = {
                'joy': sentiment_dict['joy'],
                'joy': sentiment_dict['joy'],
                'sadness': sentiment_dict['sadness'],
                'love': sentiment_dict['love'],
                'anger': sentiment_dict['anger'],
                'fear': sentiment_dict['fear'],
                'surprise': sentiment_dict['surprise'],
                'form': form,
            }

    return render(request, 'index.html', data)

