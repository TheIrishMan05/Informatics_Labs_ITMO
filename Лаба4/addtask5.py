import csv
import yaml


def task_5(output_f):
    fields = {
        "Время": "Время",
        "Предмет": "Предмет",
        "Преподаватель": "Преподаватель",
        "Аудитория": "Аудитория",
    }
    with open(output_f, 'w', newline='', encoding="utf-8") as output_file:
        csv_output = csv.DictWriter(output_file, fieldnames=fields.values())
        csv_output.writeheader()

        for filename in ['Вторник.yaml']:
            with open(filename, encoding="utf-8") as input_file:
                for row_yaml in yaml.safe_load(input_file):
                    row_csv = {fields[key]: value for key, value in row_yaml.items()}
                    csv_output.writerow(row_csv)
    return csv_output


task_5(r'Вторник.csv')
