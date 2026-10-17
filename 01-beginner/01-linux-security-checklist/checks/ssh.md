** SSH Security Review **

** Objective **

Determine whether the OpenSSH server is installed, enabled, running, or listing for incoming connections.

** Commands Executed **

- systemctl is-active ssh
- systemctl is-enabled ssh
- dpkg -l openssh-server
- sudo ss -tlnp | grep ':22 '

** Findings **

** SSH Service **

-Service active state: inactive.
-Service enabled state: not-found.
-The ssh systemd unit was not found.

** OpenSSH Server Package **

The package query reported openssh-server with status "un", indicating that the server package is not installed.

** Listening Ports **

The TCP port 22 query returned no output. No listening process matching this query was identified.

** Assessment **

The OpenSSH server does not appear to be installed, and no SSH listener was identified by the checks performed.

For a virtual machine that does not require remote SSH access, leaving the server uninstalled reduces the number of services available for inbound connections.

** Limitations ** 

These checks focused on the OpenSSH server package, the "ssh" systemd unit, and TCP port 22. They do not constitute a comprehensive review of every remote-access mechanism on the system.

** Recommendation **

Keep the SSH server uninstalled unless remote SSH access becomes necessary. If it is installed in the future, review its authentication settings and firewall rules before enabling remote access.
