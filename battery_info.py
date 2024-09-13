import psutil
from plyer import notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 30 and not plugged:
    notification.notify(
        title="Low Battery",
        message=str(percent) + "% Battery remaining!!",
        timeout=5
    )
