from django.shortcuts import render
from django.http import HttpResponse
from feedback_details.models import trainer_data, trainer_feedback
import json
# Create your views here.


def index(request):
    # Trainer data set
    trainer_list = trainer_data.objects.all()
    trainer_list_json = json.dumps(list(trainer_list.values()))

    # List to score the variables

    average_score = []
    name_list = []

    # checking the database

    temp = trainer_data.objects.get(id="EM0005")
    print(temp.name)

    # Caculating the average score

    for trainer in trainer_list:
        feed_details = trainer_feedback.objects.filter(train_id=trainer.id)
        name_list.append(trainer.name)
        average = 0
        print("Name :", trainer.name)
        count = 0

        # Iterating through all the train_id
        for feed in feed_details:
            print("feed :", feed.train_id)
            average += feed.communicatin_skill + feed.content_delivered + \
                feed.doubt_clarification + feed.technical_skill
            count += 1
        try:
            average_score.append(int(average/count))
        except:
            average_score.append(0)
    print(average_score)

    # Conveerting list to JSON

    name_list_json = json.dumps(name_list)
    average_score_json = json.dumps(average_score)

    # Zipping the average score and name of the trainer
    table_zip = zip(average_score, trainer_list)

    return render(request, 'index.html', {'table_zip': table_zip, 'scores': average_score, 'trainer_data': trainer_list, "trainer_list_json": trainer_list_json, "average_score_json": average_score_json})
