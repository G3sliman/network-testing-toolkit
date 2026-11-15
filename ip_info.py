
import ipaddress
from network_info import get_windows_network_info


def get_ip_information():

    user_input = input("Enter an IP address: ")

    try:
        ip = ipaddress.ip_address(user_input)

        print("\n========== IP INFORMATION ==========")
        print("IP Address:", ip)
        print("IP Version:", f"IPv{ip.version}")

        if ip.is_private:
            print("IP Type: Private")
        elif ip.is_global:
            print("IP Type: Public")
        elif ip.is_loopback:
            print("IP Type: Loopback")
        else:
            print("IP Type: Special-purpose")

        if ip.version == 4:
            interfaces = get_windows_network_info()

            matched = False

            for interface in interfaces:
                if interface["ip"] == str(ip):
                    matched = True

                    network = ipaddress.ip_interface(
                        f'{ip}/{interface["mask"]}'
                    ).network

                    print("\n--- Local Network Details ---")
                    print("Subnet Mask:", interface["mask"])
                    print("Network Address:", network.network_address)
                    print("Broadcast Address:", network.broadcast_address)
                    print("Default Gateway:", interface["gateway"] or "Not detected")

                    if network.prefixlen <= 30:
                        print("First Usable Host:", network.network_address + 1)
                        print("Last Usable Host:", network.broadcast_address - 1)
                        print("Usable Hosts:", network.num_addresses - 2)
                    else:
                        print("Usable Hosts: Not calculated for this subnet")

                    break

            if not matched:
                print("\nLocal subnet details unavailable.")
                print("This IP was not found on your Windows network interfaces.")

        print("\n====================================")

    except ValueError:
        print("\nError: Invalid IP address.")


if __name__ == "__main__":
    get_ip_information()
