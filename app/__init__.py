import logging
import os

from .config import settings


logging.basicConfig(level=settings.LOGGING_LEVEL)
logger = logging.getLogger(__name__)

pwd = os.path.dirname(os.path.abspath(__file__))
cards_picture = os.path.join(pwd, 'media', 'cards.png')
