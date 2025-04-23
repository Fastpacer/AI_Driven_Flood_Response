# ---------------------
# Module 4: Simplified Alert Dispatcher
# ---------------------
import datetime
class AlertDispatcher:
    @staticmethod
    def send_alert(message, phone_number, channel='sms'):
        """
        Unified alert sender with mock implementations
        Channels: sms/whatsapp/ivr
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if channel == 'sms':
            print(f"[SMS] {timestamp} | To: {phone_number} | Message: {message}")
        
        elif channel == 'whatsapp':
            print(f"[WhatsApp] {timestamp} | To: {phone_number} | Message: {message}")
        
        elif channel == 'ivr':
            print(f"[IVR Call] {timestamp} | To: {phone_number} | Voice Message: {message[:30]}...")
        
        else:
            print(f"⚠️ Unknown channel: {channel}")

    @staticmethod
    def send_bulk_alerts(message, phone_numbers, channel='sms'):
        """Send alerts to multiple numbers"""
        for number in phone_numbers:
            AlertDispatcher.send_alert(message, number, channel)