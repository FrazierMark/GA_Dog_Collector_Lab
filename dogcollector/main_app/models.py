from django.db import models
from django.urls import reverse

# A tuple of 2-tuples
# B will be the value, so this what we'll store in the db
# Breakfast is the user friendlyu view, so what you see when you use a dropdown
MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

 # once POST request is made, this redirects client to detail page
    #  w/ that dog_id that was just made
  def get_absolute_url(self):
    return reverse('toys_detail', kwargs={'pk': self.id})


class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    # Many to Many relationship
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return f"The dog named {self.name} has an id of {self.id}"

    # once POST request is made, this redirects client to detail page
    #  w/ that dog_id that was just made
    def get_absolute_url(self):
        return reverse('detail', kwargs={'dog_id': self.id})





class Feeding(models.Model):
    date = models.DateField()
    meal = models.CharField(
        max_length=1,
        # add the 'choices' field option
        choices=MEALS,
        # set the default value for meal to be 'B'
        default=MEALS[0][0]
  )

    # the foregin key always goes on the many side
    # internally it will be cat_id the _id automatically gets added
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        # is method will give us friendly value of a Field.choice
        # # django built-in method for easy display...
        return f"{self.get_meal_display()} on {self.date}"

    # change the defaul sort

    class Meta:
        ordering = ['-date']
