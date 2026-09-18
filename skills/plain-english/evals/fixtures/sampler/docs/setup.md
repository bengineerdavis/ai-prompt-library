# Setting Up The Verification Gate

The output is quarantined by the verify gate when a leftover is found. The user
should then run the migrations. The tool will refuse uploads without a profile.
Delete the mapping file if the retention policy expired it.

Simply run the new command — this ensures the fastest possible setup. Please
note that the DSN is redacted before sharing.

```bash
raise pii redact capture.har --out share/capture.redacted.har
```

The command above must be run from the workspace root, or the DSN lookup will
fail.
