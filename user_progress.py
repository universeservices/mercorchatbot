class UserProgress:
    def __init__(self):
        # Initialize user progress variables here.
        self.completed_lessons = set()
        self.quiz_scores = {}
        self.language_level = "beginner"  # Default language level is set to "beginner."

    def mark_lesson_as_completed(self, lesson_number):
        # Mark a lesson as completed by adding the lesson number to the completed_lessons set.
        self.completed_lessons.add(lesson_number)

    def set_quiz_score(self, lesson_number, score):
        # Set the user's quiz score for a specific lesson.
        # If the user has attempted the quiz more than once, store the highest score.
        if lesson_number not in self.quiz_scores or score > self.quiz_scores[lesson_number]:
            self.quiz_scores[lesson_number] = score

    def get_highest_quiz_score(self, lesson_number):
        # Retrieve the highest quiz score for a specific lesson.
        return self.quiz_scores.get(lesson_number, 0)  # Default to 0 if the lesson has not been attempted.

    def update_language_level(self, new_level):
        # Update the user's language proficiency level.
        self.language_level = new_level

    def get_language_level(self):
        # Retrieve the user's current language proficiency level.
        return self.language_level

    def get_completed_lessons(self):
        # Retrieve the set of completed lesson numbers.
        return self.completed_lessons

# Additional helper functions or classes can be added as needed.

