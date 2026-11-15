
import subprocess
import ipaddress
import platform
import shutil
from report import save_report


def traceroute():

    user_input = input("Enter destination IP address: ").strip()

    try:
        destination = ipaddress.ip_address(user_input)

    except ValueError:
        print("\nError: Please enter a valid IP address.")
        return

    system = platform.system()

    if system == "Windows":
        command = ["tracert", "-d", str(destination)]

    else:
        traceroute_path = shutil.which("traceroute")
        tracepath_path = shutil.which("tracepath")

        if traceroute_path:
            command = [traceroute_path, "-n", str(destination)]

        elif tracepath_path:
            command = [tracepath_path, "-n", str(destination)]

        else:
            print("\nError: Neither traceroute nor tracepath is installed.")
            print("Install one of these tools on Kali Linux first.")
            return

    print(f"\nTracing route to {destination}...\n")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=120
        )

        print("========== TRACEROUTE RESULTS ==========")
        print(result.stdout)

        if result.stderr:
            print("Additional information:", result.stderr)

        print("========================================")

        traceroute_results = {
            "destination": str(destination),
            "operating_system": system,
            "return_code": result.returncode,
            "output": result.stdout,
            "error_output": result.stderr
        }

        save_report("Traceroute", traceroute_results)

    except subprocess.TimeoutExpired:
        print("\nError: Traceroute operation timed out.")

    except OSError as error:
        print("\nError running Traceroute:", error)


if __name__ == "__main__":
    traceroute()
