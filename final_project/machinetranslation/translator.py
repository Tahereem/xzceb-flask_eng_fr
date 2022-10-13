"""
high level support for doing this and that.
"""
# import json
# import os
# from ibm_watson import LanguageTranslatorV3
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# from dotenv import load_dotenv

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


# load_dotenv()

apikey = "UxfvmpzGlHXK7loIg5sjOGCWweLneBkkG5ehXHRyCl_E"  
# os.environ['apikey']
url = "https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d48d5030-42ac-4346-a0e0-78efb85880f5"
# os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

def english_to_french(english_text):
    """A dummy docstring."""
    #translates English to French
    french_translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    french_text = french_translation["translations"][0]["translation"]
    return french_text

def french_to_english(french_text):
    """A dummy docstring."""
    #translates French to English
    english_translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = english_translation["translations"][0]["translation"]
    return english_text
