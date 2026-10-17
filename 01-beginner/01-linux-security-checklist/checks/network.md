** Network Services Security Check **

** Objective **

Identify network services listening on the Ubuntu lab system and review the current firewall status and network interface configuration.

** Environment **

- Operating System: Ubuntu 26.04.1 LTS
- Virtualization: VirtualBox
- Network Mode: NAT network

** Commands Executed **

- sudo ss -tulpen
- systemctl --type=service --state=running
- systemctl is-active ssh
- sudo ufw status verbose
- systemctl status avahi-daemon --no-pager
- ip -brief address

** Results **

** Listening Network Sockets **

- DNS resolver sockets were observed on loopback addresses using TCP and UDP port 53.
- Chrony was observed on UDP por 323 bound to loopback addresses.
- Avahi was observed listening on UDP port 5353 on wildcard IPv4 and IPv6 addresses.
- CUPS was observed listening on TCP port 631 on loopback addresses.
- No SSH listening socket was observed in the captured output.

** Running Services **

Multiple system services were running. A running service does not necessarily expose a network port.

The SSH service check returned *inactive*.

** Firewall **

The UFW status command reported that the firewall was inactive.

This only describes UFW. It does not establish whether other firewall rules or network-level filtring are present.

** Network Interface **

The enp0s3 interface was active and had the IPv4 address 10.0.2.15/24, consistent with a typical VirtualBox NAT network configuration.

An IPv6 link-local address was also present.

Avahi provides multicast DNS and service discovery. Whether this exposure is necessary depends on the lab's requirements and network configuration.

** Findings **

** Finding 1: UFW is inactive **

UFW is not currently enforcing its own configured firewall policy.

*Recommendation:* Review the intended firewall policy and assess whether enabling UFW is appropriate for this lab.

** Finding 2: ** Avahi listens on wildcard addresses

Avahi listens on all available IPv4 and IPv6 interfaces rather than only loopback.

*Recommendation:* Determine whether multicast DNS and service discovery are required. If not, consider restricting or disabling the service after assessing dependencies.

** Finding 3: ** SSH is inactive

The SSH service check returned inactive, and no SSH listening socket appeared in the captured socket listing.

*Assessment:* No active SSH listener was identified during this check.

** Finding 4: **  

The SSH service check returned inactive, and no SSH listening socket appeared in the captured socket listing.

*Assessment:* No active SSH listener was identified during this check.

** Security Context **

The virtual machine uses VirtualBox NAT networking. NAT affexts how the guest communicates with external networks, but it is not a replacement for host or guest firewall policies.

Listening on a wildcard address does not, by itself, prove that a service is reachable from another deive. Reachability depends on routing, filtering, and virtualization settings.

** Limitations **

This checks records the observed socket and service state. It does not perform an external port scan, test reachability from another machine, audit all firewall rules, or establish the presence or absence of every possible network exposure.

** Conclusion **

The assessment identified an inactive UFW firewall and an active Avahi service listenign on wildcard addresses. SSH was inactive, and the observed DNS resolver and CUPS listeners were bound to loopback.

Further review is recommended before making configuration changes or drawing conclusions about external reachability.
