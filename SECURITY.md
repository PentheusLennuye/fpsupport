# FP Support Security Policy

fpsupport is in scope for security auditing as it is a library with the
potential use in sensitive programming. Although the [LICENSE](LICENSE) is
clear that the software is freely given on an AS-IS basis, the author is a
professional and cares.

## Supported Versions

| Version | Supported  |
| --------| ---------- |
| 0.1.x   | Y          |

## Reporting a Vulnerability

If you detect a vulnerability in this software, ensure the author is aware. The
preferred method is to create an issue in this project's GitHub repository:
<https://github.com/PentheusLennuye/fpsupport/issues>.

### In GitHub

1. Open <https://github.com/PentheusLennuye/fpsupport/issues>
2. Click on _New Issue_ and fill out the following fields:
   - Add a title: A one-sentence summary of the bug, prefixed with SECURITY
                  CRIT, HIGH, MODERATE, LOW. Example: _SECURITY CRIT SQL
                  injection_
   - Add a description: For example,
      ```text
      SECURITY CRIT SQL injection.
      The user input in `main.py line 23` was never escaped before being accepted
      in `secrets_manager_service/backends/postgres.py line 423`
      ```

### Time to Respond / Time to Recover

This library is maintained on a best-effort basis. The author is neither
compensated nor supported for this work. His motivation is internal.

### Follow-Up

Vulnerabilities are treated as bugs by the author and processed in the same way:

- Assess
- Accept/Decline: Acceptance includes agreeing with or modifying the priority.
                  A decline will be published with the reason.
- Assign
- Develop
- Deploy to Staging
- Deploy to Production

Testing is inherent in the develop/deploy pipeline. The status of the issue
will be updated in the GitHub issue. Details will be discussed in GitHub, and
any changes placed in the [CHANGELOG](CHANGELOG.md).

