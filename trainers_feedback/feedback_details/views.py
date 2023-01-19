from django.shortcuts import render
from django.http import HttpResponse
from feedback_details.models import trainer_data, trainer_feedback
import json
# Create your views here.


def index(request):
    trainer_list = trainer_data.objects.all()
    trainer_list_json = json.dumps(list(trainer_list.values()))
    average_score = []
    temp = trainer_data.objects.get(id="EM0005")
    print(temp.name)
    for trainer in trainer_list:
        feed_details = trainer_feedback.objects.filter(
            train_data=trainer.id)
        average = 0
        print("Name :", trainer.name)
        count = 0
        for feed in feed_details:
            print("feed :", feed.train_data)
            average += feed.communicatin_skill + feed.content_delivered + \
                feed.doubt_clarification + feed.technical_skill
            count += 1
        try:
            average_score.append(average/count)
        except:
            average_score.append(0)
    print(average_score)
    table_zip = zip(average_score, trainer_list)

    return render(request, 'index.html', {'table_zip': table_zip, 'scores': average_score, 'trainer_data': trainer_list, "trainer_list_json": trainer_list_json})
