import os
from re import split

""" Required """

BOT_TOKEN = os.environ.get("BOT_TOKEN")
GOOGLE_API_KEY = split(r'[ ,;，；]+', os.environ.get("GOOGLE_API_KEY"))

""" Optional """

ALLOWED_USERS = split(r'[ ,;，；]+', os.getenv("ALLOWED_USERS", '').replace("@", "").lower())
ALLOWED_GROUPS = split(r'[ ,;，；]+', os.getenv("ALLOWED_GROUPS", '').replace("@", "").lower())

#Whether to push logs and enable some admin commands
IS_DEBUG_MODE = os.getenv("IS_DEBUG_MODE", '0')
#The target account that can execute administrator instructions and log push can use /get_my_info to obtain the ID.
ADMIN_ID = os.getenv("ADMIN_ID", "1234567890")

#Determines whether to verify identity. If 0, anyone can use the bot. It is enabled by default.
AUCH_ENABLE = os.getenv("AUCH_ENABLE", "1")

#"1"to use the same chat history in the group, "2"to record chat history individually for each person
GROUP_MODE = os.getenv("GROUP_MODE=", "1")

#After setting up 3 rounds of dialogue, prompt the user to start a new dialogue
prompt_new_threshold = int(3)

#The default prompt when the photo has no accompanying text
defaut_photo_caption = "опиши эту картинку"

""" Below is some text related to the user """
help_text = "Ты можешь послать мне текст или картинку. Когда посылаешь картинку - пожалуйста, задавай вопрос в этом же сообщении как описание к ней."
command_list = "/new Начать новый чат\n/get_my_info Получить информацию о себе\n/get_allowed_users Список пользователей, допущенных к боту (admin only)\n/list_models Список моделей (admin only)\n/get_api_key Список gemini's apikeys. It is currently useless. Multiple keys may be added to automatically switch in the future.(admin only)\n/help Получить помощь"
admin_auch_info = "You are not the administrator or your administrator ID is set incorrectly!!!"
debug_mode_info = "Debug mode is not enabled!"
command_format_error_info = "Command format error"
command_invalid_error_info = "Invalid command, use /help for help"
user_no_permission_info = "Я вас не звал, идите..."
group_no_permission_info = "Я вас (группу) не звал, идите..."
gemini_err_info = f"Something went wrong!\nВведенный тобой контент может быть неприемлемым. Измени его и повтори попытку."
new_chat_info = "У нас теперь свежий чат."
prompt_new_info = "Выполни /new для начала нового чата."
unable_to_recognize_content_sent = "Твой контент не распознан!"

""" Below is some text related to the log """
send_message_log = "Send a message. The content returned is:"
send_photo_log = "Send a photo. The content returned is:"
unnamed_user = "UnnamedUser"
unnamed_group = "UnnamedGroup"
event_received = "event received"
group = "group"
the_content_sent_is = "The content sent is:"
the_reply_content_is = "The reply content is:"
the_accompanying_message_is = "The accompanying message is:"
the_logarithm_of_historical_conversations_is = "The logarithm of historical conversations is:"
no_rights_to_use = "No rights to use"
send_unrecognized_content = "Send unrecognized content"


""" read https://ai.google.dev/api/rest/v1/GenerationConfig """
generation_config = {
    "max_output_tokens": 1024,
}

""" read https://ai.google.dev/api/rest/v1/HarmCategory """
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    },
]
