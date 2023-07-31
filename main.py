import textbase
from user_progress import UserProgress
from cultural_insights import CulturalInsights
from language_model import LanguageModel
from lessons import LanguageLessons

def main():
    # Parse the file 'data.txt'
    textbase_obj = textbase.parse('data.txt')

    # Iterate over the entries
    for entry in textbase_obj:
        print(entry)

    # Create instances of the required classes
    language_model = LanguageModel()
    lessons = LanguageLessons()
    user_progress = UserProgress()
    cultural_insights = CulturalInsights()

    # Initialize the chatbot and welcome the user
    chatbot = textbase.Chatbot()
    chatbot.add_system_message("Welcome to the Language Learning Chatbot!")
    chatbot.add_system_message("You can learn a new language through interactive lessons and quizzes.")
    chatbot.add_system_message("Type 'exit' at any time to end the conversation.")

    # Start the conversation loop
    while True:
        user_input = chatbot.get_user_input()
        if user_input.lower() == "exit":
            chatbot.add_system_message("Goodbye! See you soon.")
            break

        # Assess the user's language proficiency level
        user_level = language_model.get_user_language_level(user_input)
        chatbot.add_system_message(f"Your language proficiency level: {user_level}")

        # Provide interactive lessons and quizzes
        total_lessons = lessons.get_total_lessons()
        for lesson_number in range(1, total_lessons + 1):
            if lesson_number in user_progress.get_completed_lessons():
                continue  # Skip completed lessons

            chatbot.add_system_message(f"Lesson {lesson_number}:")
            lesson_prompt, _ = lessons.get_lesson(lesson_number)
            chatbot.add_system_message(lesson_prompt)

            # Get user response and check if it's correct
            user_response = chatbot.get_user_input()
            is_correct = lessons.is_correct_response(lesson_number, user_response)

            if is_correct:
                user_progress.mark_lesson_as_completed(lesson_number)
                chatbot.add_system_message("Congratulations! You answered correctly.")
                user_progress.set_quiz_score(lesson_number, 1)
            else:
                chatbot.add_system_message("Sorry, that's not the correct answer. Try again later.")

        # Update the user's language proficiency level based on their progress
        user_progress.update_language_level("intermediate")  # Placeholder logic; update as needed.

        # Provide cultural insights based on the user's interest
        chatbot.add_system_message("Would you like to learn about the culture? (yes/no)")
        user_interest = chatbot.get_user_input().lower()
        if user_interest == "yes":
            chatbot.add_system_message("Choose a topic to learn more:")
            cultural_topics = cultural_insights.get_all_topics()
            chatbot.add_system_message(", ".join(cultural_topics))

            topic_choice = chatbot.get_user_input()
            cultural_insight = cultural_insights.get_cultural_insight(topic_choice)
            if cultural_insight:
                chatbot.add_system_message(cultural_insight)
            else:
                chatbot.add_system_message("Sorry, that topic is not available.")

        # End the conversation
        chatbot.add_system_message("That's all for now. Feel free to continue your language learning journey.")
        chatbot.add_system_message("Type 'exit' to end the conversation or continue practicing.")


def main():
    # Replace "YOUR_OPENAI_API_KEY" with your actual OpenAI API key
    api_key = "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"

    # Create an instance of the LanguageModel class with the api_key
    language_model = LanguageModel(api_key)

    # Create an instance of the LanguageLessons class
    language_lessons = LanguageLessons()

    # Start the simulated conversation with the chatbot
    language_lessons.simulate_conversation(language_model)

if __name__ == "__main__":
    main()

