# ---------------------
# Module 3: Enhanced Multilingual Alert System
# ---------------------
from datetime import datetime
import random
import pandas as pd
import json


class MultilingualAlertSystem:
    def __init__(self, shelters_file='mumbai_shelters.csv', lang_config='language_templates.json'):
        """
        Enhanced alert generator with:
        - Real shelter data from CSV
        - Localized templates from JSON
        - Fallback mechanisms
        """
        self.shelters = self._load_shelters(shelters_file)
        self.templates = self._load_language_config(lang_config)
        self.default_lang = 'en'

    def _load_shelters(self, file_path):
        """Load real shelter data from CSV"""
        try:
            df = pd.read_csv(file_path)
            return df.to_dict('records')
        except FileNotFoundError:
            return [
                {'name': 'BMC School', 'address': 'Dadar East', 'capacity': 200},
                {'name': 'Municipal Hospital', 'address': 'Andheri West', 'capacity': 150}
            ]

    def _load_language_config(self, file_path):
        """Load language templates from JSON"""
        default_templates = {
            'en': {
                'alert': "🚨 Flood Alert! {location} | Risk: {risk} | Shelter: {shelter} ({address})",
                'severity': {'high': 'Critical', 'medium': 'Warning', 'low': 'Advisory'}
            },
            'mr': {
                'alert': "🚨 पूर चेतावनी! {location} | धोका: {risk} | आश्रय: {shelter} ({address})",
                'severity': {'high': 'गंभीर', 'medium': 'सावधान', 'low': 'सल्ला'}
            }
        }
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return default_templates

    def _get_nearest_shelter(self, location):
        """Simple shelter selection logic"""
        return random.choice(self.shelters) if self.shelters else None

    def _localize_severity(self, risk_level, language):
        """Get localized severity terms"""
        return self.templates.get(language, self.templates[self.default_lang])['severity'].get(
            risk_level, risk_level
        )

    def generate_alert(self, location, risk_level, language='en'):
        """Generate localized alert with real shelter data"""
        # Validate language support
        if language not in self.templates:
            language = self.default_lang
            print(f"Language {language} not supported. Defaulting to English.")

        # Get shelter information
        shelter = self._get_nearest_shelter(location)
        if not shelter:
            raise ValueError("No shelters available in database")

        # Localize components
        localized_risk = self._localize_severity(risk_level, language)
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M IST")

        return self.templates[language]['alert'].format(
            location=location,
            risk=localized_risk,
            shelter=shelter['name'],
            address=shelter['address'],
            time=timestamp
        )