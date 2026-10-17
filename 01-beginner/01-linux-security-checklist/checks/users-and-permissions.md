** Users and Permissions Security Check **

** Objective**

Review local user accounts, administrative privileges, and home directory permissions on the Ubuntu lab system.

** Scope **

This check examines the current user identity, group membership, login shells listem in /etc/passwd, the root account, UID 0 accounts, and home directory permissions.

** Commmands Executed **

- whoami
- id
- awk -F: '$7 !~ /(nologin|false)$/ {print $1 ":" $7}' /etc/passwd
- getent group sudo
- ls -ld "$HOME"
- getent passwd root
- awk -F: '$3 == 0 {print $1 ":" $3 ":" $7}' /etc/passwd

** Findings **

** Home Directory Pemrissions **

The home directory uses mode 750. The owner has read, write and execute permissions; the group has read and execute permissions; other users have no permissions.

This restricts access by other local users, although access by members of the owning group should be assessed according to the system's requirements.

** Administrative Privileges **

The current account belongs to the sudo group. This allows administrative access through the configured sudo policy. Group membership should be limited to users who require it.

** UID 0 Accounts **

Only the root account appeared in the UID 0 check. No additional UID 0 accounts were identified by this command.

** Login Shells **
The login-shell filter is an initial indicator only. A configured shell does not, by itself, prove that an account can log in interactively.

** Recommendations **

- Review whether membership in administrative and supplementary groups is necessary.
- Keep home directory permissions restrictive where appropriate.
- Review authentication and sudo policies separately.
- Repeat these checks periodically.

** Limitations **

This check does not fully audit file ownership, access control lists, sudoers rules, password policies, SSH authentication, or all account login restrictions.

** Conclusion **

The checks identified a home directory with restrictive permissions and no additional UID 0 accounts. Further review is required before making a broader assessment of account security.
