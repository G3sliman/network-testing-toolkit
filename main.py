
from report import view_reports
from traceroute import traceroute
from port_test import port_test
from ip_info import get_ip_information
from network_info import get_windows_network_info
from ping_test import ping_test
from dns_lookup import dns_lookup


def show_menu():

    print("\n========================================")
    print("   NETWORK TESTING AND DIAGNOSTICS TOOLKIT")
    print("========================================")

    print("1. IP Address Information")
    print("2. View Network Interfaces")
    print("3. Ping Testing")
    print("4. DNS Lookup")
    print("5. Traceroute")
    print("6. TCP Port Testing")
    print("7. View Saved Reports")
    print("0. Exit")

    print("========================================")


def main():

    while True:

        show_menu()

        choice = input("Select an option: ")

        if choice == "1":
            get_ip_information()

        elif choice == "2":
            interfaces = get_windows_network_info()

            print("\n========== NETWORK INTERFACES ==========")

            if not interfaces:
                print("No network interfaces found.")

            for interface in interfaces:
                print("\nIP Address:", interface["ip"])
                print("Subnet Mask:", interface["mask"])
                print("Default Gateway:", interface["gateway"] or "Not detected")

            print("========================================")
        elif choice == "3":
            ping_test()
        elif choice == "4":
            dns_lookup()
        elif choice == "5": traceroute()

        elif choice == "6": port_test()

        elif choice == "7":
            view_reports()

        elif choice == "0":
            print("\nThank you for using the toolkit!")
            break

        else:
            print("\nInvalid option. Please select again.")


if __name__ == "__main__":
    main()
