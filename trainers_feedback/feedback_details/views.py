from django.shortcuts import render
from django.http import HttpResponse
from feedback_details.models import trainer_data, trainer_feedback
# Create your views here.


def index(request):
    trainer_list = trainer_data.objects.all()
    average_score = []

    for trainer in trainer_list:
        feed_details = trainer_feedback.objects.filter(train_id=trainer.id)
        average = 0
        for feed in feed_details:
            average += feed.communicatin_skill + feed.content_delivered + \
                feed.doubt_clarification + feed.technical_skill
        average_score.append(average)

    return render(request)
