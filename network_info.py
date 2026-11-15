
import subprocess
import re
import platform
import ipaddress


def get_windows_network_info():

    system = platform.system()

    try:

        if system == "Windows":

            result = subprocess.run(
                ["ipconfig"],
                capture_output=True,
                text=True,
                check=True
            )

            output = result.stdout

            adapters = re.split(
                r"\r?\n(?=\S.*adapter .*:)",
                output
            )

            interfaces = []

            for adapter in adapters:

                ip_match = re.search(
                    r"IPv4 Address[ .]*: ([\d.]+)",
                    adapter
                )

                mask_match = re.search(
                    r"Subnet Mask[ .]*: ([\d.]+)",
                    adapter
                )

                gateway_match = re.search(
                    r"Default Gateway[ .]*: ([\d.]+)",
                    adapter
                )

                if ip_match and mask_match:

                    interfaces.append({
                        "ip": ip_match.group(1),
                        "mask": mask_match.group(1),
                        "gateway": gateway_match.group(1)
                        if gateway_match else None
                    })

            return interfaces

        else:

            result = subprocess.run(
                ["ip", "-o", "-4", "addr", "show"],
                capture_output=True,
                text=True,
                check=True
            )

            route_result = subprocess.run(
                ["ip", "route", "show", "default"],
                capture_output=True,
                text=True,
                check=True
            )

            gateway_by_interface = {}

            for line in route_result.stdout.splitlines():

                gateway_match = re.search(
                    r"default via ([\d.]+) dev (\S+)",
                    line
                )

                if gateway_match:
                    gateway_by_interface[gateway_match.group(2)] = (
                        gateway_match.group(1)
                    )

            interfaces = []

            for line in result.stdout.splitlines():

                match = re.search(
                    r"\d+:\s+(\S+)\s+inet\s+([\d.]+)/(\d+)",
                    line
                )

                if match:

                    interface_name = match.group(1)
                    ip_address = match.group(2)
                    prefix = match.group(3)

                    subnet_mask = str(
                        ipaddress.IPv4Network(
                            f"0.0.0.0/{prefix}"
                        ).netmask
                    )

                    interfaces.append({
                        "ip": ip_address,
                        "mask": subnet_mask,
                        "gateway": gateway_by_interface.get(
                            interface_name
                        )
                    })

            return interfaces

    except (OSError, subprocess.SubprocessError) as error:
        print("Error retrieving network information:", error)
        return []


if __name__ == "__main__":

    for interface in get_windows_network_info():
        print(interface)
