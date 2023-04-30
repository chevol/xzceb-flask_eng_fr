import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
import json

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-04-07',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)


def english_to_french(english_text):
    """
    Convert english to french
    """
    result = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    translation_value = result['translations'][0]['translation']

    return translation_value

def french_to_english(french_text):
    """
    Convert french to english
    """
    result = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    translation_value = result['translations'][0]['translation']

    return translation_value
