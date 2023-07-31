MercerChatBot - Language Learning Chatbot
MercerChatBot is a language learning chatbot designed to help users learn a new language through interactive lessons and quizzes. The chatbot utilizes OpenAI's GPT-3 language model to provide personalized responses based on the user's input and language proficiency level. MercerChatBot is built using Python and leverages the textbase library to manipulate Inmagic/DBText style data files for interactive lesson content.



Features
Interactive Language Learning: MercerChatBot engages users in interactive language learning sessions with lessons and quizzes tailored to their language proficiency level.
Personalized Responses: The chatbot generates personalized responses based on the user's input and language level, providing a dynamic learning experience.
Exit Option: Users can exit the conversation at any time by typing 'exit,' allowing them to control the learning session's duration.
Language Proficiency Assessment: The chatbot assesses the user's language proficiency level using OpenAI's GPT-3 engine, ensuring lessons are appropriately matched to their skill level.
Getting Started
To run MercerChatBot on your local machine, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/your-username/mercerchatbot.git
cd mercerchatbot
Install the required Python packages:
bash
Copy code
pip install openai xlsxwriter
Set up OpenAI API Key:

Obtain an API key from OpenAI.
Replace YOUR_OPENAI_API_KEY in language_model.py with your actual API key.
Run the Chatbot:

bash
Copy code
python language_model.py
Start Learning:

MercerChatBot will welcome you and provide instructions.
Type your response, and the chatbot will engage in conversation with personalized feedback.
Type 'exit' to end the conversation.
Dependencies
MercerChatBot relies on the following dependencies:

OpenAI Python Library: For communication with OpenAI's GPT-3 API.
XlsxWriter: For exporting chat logs to Excel format.
TextBase: A Python library to manipulate Inmagic/DBText style data files for lesson content.
Contribution Guidelines
We welcome contributions to MercerChatBot! To contribute, follow these steps:

Fork the repository.
Create a new branch for your contribution.
Make your changes and commit them.
Push the changes to your fork.
Submit a pull request to the main branch of the original repository.
Before submitting a pull request, make sure your changes pass all tests and adhere to the project's coding standards.

License
This project is licensed under the MIT License.

Authors
Etienne Posthumus (GitHub)
John Doe (GitHub)
Contact
If you have any questions or feedback about MercerChatBot, feel free to contact the authors:

Etienne Posthumus - Email: ep@epoz.org
John Doe - Email: john.doe@example.com
Acknowledgments
We would like to thank the following individuals and organizations for their contributions and support:

OpenAI for providing the powerful GPT-3 language model and API access.
The textbase library authors for their work on the Python library to manipulate Inmagic/DBText style data files.
The language learning community for inspiring the development of MercerChatBot.