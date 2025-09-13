import pathlib
import logging
import logging.config


from datetime import datetime

logging_path = pathlib.Path(__file__).parent/"logging.conf"
logging.config.fileConfig(logging_path, disable_existing_loggers=False)

logger = logging.getLogger("hb_test.log")


def key ():
    log_file = pathlib.Path(__file__).parent / "hblog.txt"
    with open(log_file, "r", encoding="utf-8") as f:
        logs = f.readlines()
        with open("new_log.log", "w", encoding="utf-8") as f2:
            for line in logs:
                if "TSTFEED0300|7E3E|0400" in line:
                    f2.write(line)
                    #print(line.strip())

    heart_beat_time = []
    with open("new_log.log", "r", encoding="utf-8") as f:
        for line in f:
            if "Timestamp" in line:
                timestamp_str = line.split("Timestamp",1)[1].strip().split()[0]
                # Перетворюємо у datetime, щоб можна віднімати
                date_time = datetime.strptime(timestamp_str, "%H:%M:%S")
                heart_beat_time.append(date_time)

    for i in range(len(heart_beat_time) - 1):
        time1 = heart_beat_time[i]
        time2 = heart_beat_time[i + 1]
        delta = (time1 - time2).total_seconds()
        if delta <= 31:
            continue
        elif 31 < delta < 33:
            logger.warning(f"Інтервал між {time1.time()} та {time2.time()} дорівнює {delta}")
        else: # delta >= 33:
            logger.error(f"Інтервал між {time1.time()} та {time2.time()} дорівнює {delta}")

key()