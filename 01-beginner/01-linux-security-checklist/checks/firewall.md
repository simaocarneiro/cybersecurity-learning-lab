** Firewall Configuration Review **

** Objective **

Assess the current host firewall configuration in the Ubuntu virtual machine.

** Commands Executed **

- sudo ufw status numbered
- systemctl is-enabled ufw
- systemctl is-active ufw
- sudo nft list ruleset
- sudo ufw show raw

** Findings **

*UFW*

- UFW status: inactive.
- UFW unit enabled state: enabled.
- UFW unit active state: active.
- No numbered UFW filtering rules were displayed by the status command.

The active systemd unit does not mean that UFW firewall filtering is enabled.

** nftables and Raw Rules **

- sudo nft list ruleset returned no output.
- sudo uf show raw displayed IPv4 and IPv6 chains with ACCEPT policies and no visible filtering rules in the output.

These observations indicate that no effective filtering rules were visible in the inspected output. They do not establish that the virtual machine is reachable from external networks.

** Network Context **

The virtual machine uses VirtualBox NAT networking. NAT can limit unsolicited inbound connectivity, but it is not a replacement for a host firewall.

** Assessment **

The UFW firewall is currently inactive, and the inspected outputs did not show active filtering rules. Enabling and configuring a host firewall should be considered as a hardening measure.

** Limitations **

This review did not test reachability from another machine, isnpect VirtualBox port-forwarding rules, or perform a comprehensive audit of all possible packet-filtering mechanisms.

** Next Steps **

- Review the current network requirements before changing firewall settings.
- Enable UFW with a suitable baseline policy.
- Verify the resulting rules and confirm that normal networl connectivity still works.

** Hardening Applied **

The UFW firewall was enabled with the following default policies:
- Incoming traffic: deny.
- Outgoing traffic: allow.
- Route traffic: disabled.

The resulting firewall status was active, with low-level logging enabled.

** Connectivity Verification **

** Test 1: Direct IP Conectivity **

Command: ping -c 4 1.1.1.1

Result: 4 packets transmitted, 4 received, 0% packet loss.

** Test 2: DNS Resolution and Connectivity **

Command: ping -c 4 ubuntu.com

Result: The hostname resolved to an IP address, and 4 packets were transmitted and received with 0% packet loss.

** Conclusion **

The firewall was enabled with a basic default-deny incoming policy and allow-outgoing policy. Both connectivity tests succeeded after the change.

These tests confirm basic IP connectivity and hostname resolution at the time of testing. They do not constitute a comprehensive firewall or security test.
