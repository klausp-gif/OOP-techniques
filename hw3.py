class Course:
    def __init__(self, name, topic, name_of_teacher, number_of_participants):
        self.name = name
        self.topic = topic
        self.name_of_teacher = name_of_teacher
        self.number_of_participants = number_of_participants

    def __str__(self):
        return f'Name: {self.name}, Topic: {self.topic}, Teacher: {self.name_of_teacher}, Num of participants: {self.number_of_participants}'
    
print(Course('Klaus', 'MathHL', 'xxx', 67))