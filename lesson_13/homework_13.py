import pathlib
import os
import csv
import json
import logging
import logging.config
import sys
import xml.etree.ElementTree as ET

course_dir = pathlib.Path().absolute()
lesson_dir = os.path.join(course_dir,"lesson_13")

logging_path = os.path.join(lesson_dir, "logging.conf")
# чомусь перестала працювати конструкція args=('%(logfile)s', 'a') у конфіг файлі. Тому переробив на жорстко прописаний шлях до лог файлу.
# log_file = os.path.join(json_dir, "json_muratov.log").replace('\\', '/')
logging.config.fileConfig(logging_path, disable_existing_loggers=False)

# -- csv --
csv_dir = os.path.join(lesson_dir,"csv")
csv_1_path = os.path.join(csv_dir,"r-m-c.csv")
csv_2_path = os.path.join(csv_dir,"random-michaels.csv")
result_csv_path = os.path.join(csv_dir, "result_muratov.csv")

unique_list_1 = []
unique_list_2 = []

def unique_csv_file(file_path):
    unique_row = []
    with open(file_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))

        for item in reader:
            if item not in unique_row:
                unique_row.append(item)
    return unique_row

unique_list_1 = unique_csv_file(csv_1_path)
unique_list_2 = unique_csv_file(csv_2_path)

# using the “set” method is more faster

# def unique_csv_file_fast(file_path):
#     unique_set = set()
#     unique_rows = []
#     with open(file_path, newline='') as csvfile:
#         reader = csv.reader(csvfile)
#         for row in reader:
#             row_tuple = tuple(row)  # щоб можна було додати у set
#             if row_tuple not in unique_set:
#                 unique_set.add(row_tuple)
#                 unique_rows.append(row)
#     return unique_rows

# unique_list_1 = unique_csv_file_fast(csv_1_path)
# unique_list_2 = unique_csv_file_fast(csv_2_path)

for item in unique_list_2:
    if item not in unique_list_1:
        unique_list_1.append(item)

with open(result_csv_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_list_1)

# -- json --
json_dir = os.path.join(lesson_dir,"json")
json_files = [
    os.path.join(json_dir,"localizations_en.json"),
    os.path.join(json_dir,"localizations_ru.json"),
    os.path.join(json_dir,"login.json"),
    os.path.join(json_dir,"swagger.json")
]

logger = logging.getLogger("json_log")

def valid_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            json.load(f)
    except Exception as e:
        logger.error(f"INVALID JSON: {file_path} — {e}")

for file_path in json_files:
    valid_json(file_path)

# -- xml --
tree = ET.parse(os.path.join(os.path.join(lesson_dir,"xml"),"groups.xml"))
root = tree.getroot()

logger = logging.getLogger("xml_log")

def group_number(root, number_value):
    for group in root.findall('group'):
        num_ber = group.find('number')
        if num_ber is not None and num_ber.text == number_value:
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                in_coming = timing_exbytes.find('incoming')
            else:
                logger.info(f"Group {number_value} found, but missing timingExbytes")
                return None

            if timing_exbytes is not None and in_coming is not None:
                logger.info(f"Group number: {num_ber.text}, incoming: {in_coming.text}")
                return timing_exbytes.text, in_coming.text
            else:
                logger.info(f"Group {number_value} found, but missing incoming")
                return None, None

    logger.info(f"Group {number_value} not found")
    return None, None

group_number(root, "2")