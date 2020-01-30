from django.db import models

# models.Model lets this class inherits all the methods from Model
class Question(models.Model):
    # will automatically have an ID as primary key that auto increments
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # this helps format how the server returns the promise, otherwise it returns 'Question Object'
    def __str__(self):
        return self.question_text

# extend the Model again
class Choice(models.Model):
    # if a question is deleted, it's choices are also deleted
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text