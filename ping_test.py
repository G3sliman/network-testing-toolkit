
import subprocess
import ipaddress
import re
import platform
from report import save_report


def ping_test():

    user_input = input("Enter destination IP address: ").strip()

    try:
        destination = ipaddress.ip_address(user_input)

    except ValueError:
        print("\nError: Please enter a valid IP address.")
        return

    count = 4
    system = platform.system()

    if system == "Windows":
        command = ["ping", "-n", str(count), str(destination)]
    else:
        command = ["ping", "-c", str(count), str(destination)]

    print(f"\nPinging {destination} with {count} requests...\n")

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=count * 3 + 5
        )

        output = result.stdout
        response_times = []
        received = 0

        for line in output.splitlines():

            if system == "Windows":
                successful_reply = "TTL=" in line.upper()
            else:
                successful_reply = bool(
                    re.search(r"\bbytes from\b", line, re.IGNORECASE)
                )

            if successful_reply:
                received += 1

                time_match = re.search(
                    r"time[=<]\s*(\d+(?:\.\d+)?)\s*ms",
                    line,
                    re.IGNORECASE
                )

                if time_match:
                    response_times.append(float(time_match.group(1)))

        lost = count - received
        packet_loss = (lost / count) * 100

        print("========== PING RESULTS ==========")
        print("Destination:", destination)
        print("Packets Sent:", count)
        print("Packets Received:", received)
        print("Packets Lost:", lost)
        print("Packet Loss:", f"{packet_loss:.2f}%")

        if response_times:
            average = sum(response_times) / len(response_times)
            print("Average Response Time:", f"{average:.2f} ms")
        else:
            print("Average Response Time: No replies received")

        print("==================================")

        ping_results = {
            "destination": str(destination),
            "operating_system": system,
            "packets_sent": count,
            "packets_received": received,
            "packets_lost": lost,
            "packet_loss": round(packet_loss, 2),
            "response_times_ms": response_times
        }

        if response_times:
            ping_results["average_response_time_ms"] = round(
                sum(response_times) / len(response_times), 2
            )

        save_report("Ping", ping_results)

    except subprocess.TimeoutExpired:
        print("Error: Ping operation timed out.")

    except OSError as error:
        print("Error running Ping:", error)


if __name__ == "__main__":
    ping_test()
