# Terminal mis-invocation

The user ran `investigate -o app.log` in an interactive terminal. The copied
`app.log.txt` is synthesized evidence, but it was supplied to the **output** flag.
No input flag or positional input was supplied, and stdin is a terminal rather
than a pipe.

The investigation script should report both facts on stderr and exit non-zero
instead of waiting for terminal input. The fixture must not trigger diagnosis
of the log contents.
