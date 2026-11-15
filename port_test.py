
from report import save_report
import socket


def port_test():

    host = input("Enter destination IP or hostname: ").strip()

    if not host:
        print("\nError: Host cannot be empty.")
        return

    try:
        port = int(input("Enter TCP port number: "))

        if not 1 <= port <= 65535:
            print("\nError: Port must be between 1 and 65535.")
            return

    except ValueError:
        print("\nError: Please enter a valid port number.")
        return

    print(f"\nTesting {host}:{port}...\n")

    try:
        with socket.create_connection((host, port), timeout=5):
            print("========== TCP PORT TEST ==========")
            print("Host:", host)
            print("Port:", port)
            print("Status: OPEN (connection successful)")
            print("===================================")

            save_report("TCP Port Test", {
                "host": host,
                "port": port,
                "status": "OPEN"
            })

    except ConnectionRefusedError:
        print("Status: CONNECTION REFUSED")

        save_report("TCP Port Test", {
            "host": host,
            "port": port,
            "status": "CONNECTION REFUSED"
        })

    except socket.timeout:
        print("Status: TIMEOUT (no response in time)")

        save_report("TCP Port Test", {
            "host": host,
            "port": port,
            "status": "TIMEOUT"
        })

    except socket.gaierror:
        print("Error: Could not resolve the hostname.")

    except OSError as error:
        print("Network error:", error)


if __name__ == "__main__":
    port_test()
