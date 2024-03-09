class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")
    
if __name__ == "__main__":
    
    student_instance = Student(first_name="Alice", last_name="Smith")

    
    student_instance.hello()
    student_instance.raise_hand()    
    pass

class ChattyStudent(Student):
    
    def hello(self):
        super().hello()
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        for _ in range(10):
            super().raise_hand()


if __name__ == "__main__":
    
    chatty_student_instance = ChattyStudent(first_name="Bob", last_name="Johnson")

    
    chatty_student_instance.hello()
    chatty_student_instance.raise_hand()

    pass
