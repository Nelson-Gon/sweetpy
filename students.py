# A simple 'program' to play around with classes and data structures.
# Define student's names, classes, ages, favorites, career goals.
# Build a data frame of this data.
import io
import os
os.getcwd()
os.listdir()
import re



class student:
    level = 'postdoc'
    interests = []

    # Put all 'students'(researchers) at the level of post doc
    def __init__(self, name, field, subfield, age):
       self.name = name
       self.field = field
       self.subfield = subfield
       self.age = age



    def add_interests(self, *interest):
        self.interests.append(interest)


Peter = student(name= "Peter", field= "Biomedicine", subfield= "Neuroscience", age= 35)

Peter.name
Peter.add_interests("Neurohacking", "Neuroendocrinology", "Learning and Memory")

Peter.interests


def form_fill():
    answer = input("Please provide your name, field, subfield, age and interets. Separate with a ','").split(",")
    user_input = [x.strip() for x in answer]
    return user_input

form_fill()
