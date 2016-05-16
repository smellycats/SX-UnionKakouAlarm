from main import BKCPAlarm


if __name__ == "__main__":
    fd = BKCPAlarm()
    fd.loop_get_data()
