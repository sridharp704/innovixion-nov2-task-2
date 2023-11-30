import time
import winsound

def set_alarm():
    print("Enter the time for the alarm in 24-hour format (HH:MM):")
    alarm_time = input()

    try:
        # Validate input format
        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))
        if 0 <= alarm_hour < 24 and 0 <= alarm_minute < 60:
            return alarm_hour, alarm_minute
        else:
            print("Invalid time format. Please use HH:MM.")
            return set_alarm()
    except ValueError:
        print("Invalid time format. Please use HH:MM.")
        return set_alarm()

def main():
    print("Welcome to the Alarm Clock App!")

    alarm_hour, alarm_minute = set_alarm()
    alarm_time = f"{alarm_hour:02d}:{alarm_minute:02d}"

    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!")
            winsound.Beep(1000, 2000)  # Beep for 2 seconds
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
