# ---------------------
# Module 5: Monitoring Dashboard
# ---------------------
import datetime
class MonitoringDashboard:
    def __init__(self):
        self.alert_history = []
        self.system_status = {
            'last_checked': None,
            'api_healthy': True
        }

    def log_alert(self, alert_message, channel):
        """Record sent alerts"""
        self.alert_history.append({
            'timestamp': datetime.now().isoformat(),
            'message': alert_message,
            'channel': channel
        })

    def show_summary(self):
        """Display key metrics"""
        print("\n=== FLOOD ALERT SYSTEM STATUS ===")
        print(f"Total Alerts Sent: {len(self.alert_history)}")
        print("Last Alert:")
        if self.alert_history:
            last = self.alert_history[-1]
            print(f" - Time: {last['timestamp']}")
            print(f" - Channel: {last['channel'].upper()}")
            print(f" - Content: {last['message'][:50]}...")
        else:
            print(" - No alerts sent yet")
        
        if alert:
         print("\nRecent Alerts:")
         for alert in alert:
            print(f" - {alert}")

    def check_system_health(self):
        """Basic health check"""
        self.system_status['last_checked'] = datetime.now().isoformat()
        # Simple mock check - always returns True
        return self.system_status['api_healthy']