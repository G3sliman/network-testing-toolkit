

import json
from datetime import datetime
from pathlib import Path


def save_report(tool_name, results):

    reports_folder = Path("reports")
    reports_folder.mkdir(exist_ok=True)

    report = {
        "tool": tool_name,
        "timestamp": datetime.now().astimezone().isoformat(
            timespec="seconds"
        ),
        "results": results
    }

    filename = (
        f"{tool_name.lower().replace(' ', '_')}_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S_%f')}.json"
    )

    file_path = reports_folder / filename

    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        print(f"\nReport saved successfully: {file_path}")

    except OSError as error:
        print("\nError saving report:", error)
        

def view_reports():

    reports_folder = Path("reports")

    if not reports_folder.exists():
        print("\nNo reports folder found.")
        return

    report_files = sorted(
        reports_folder.glob("*.json"),
        key=lambda file: file.stat().st_mtime,
        reverse=True
    )

    if not report_files:
        print("\nNo saved reports available.")
        return

    print("\n========== SAVED REPORTS ==========")

    for index, file in enumerate(report_files, start=1):
        print(f"{index}. {file.name}")

    print("0. Back to main menu")

    choice = input("\nSelect a report to view: ")

    if choice == "0":
        return

    try:
        selected_index = int(choice) - 1

        if not 0 <= selected_index < len(report_files):
            print("\nInvalid selection.")
            return

        with open(report_files[selected_index], "r", encoding="utf-8") as file:
            report_data = json.load(file)

        print("\n========== REPORT DETAILS ==========")
        print(json.dumps(report_data, indent=4))
        print("====================================")

    except ValueError:
        print("\nPlease enter a valid number.")

    except (OSError, json.JSONDecodeError) as error:
        print("\nError reading report:", error)