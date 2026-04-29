"""Backward-compatible wrapper for the Xiaozhi MCP SDK."""

from xiaozhi_mcp.pipe import (
    build_server_command,
    connect_to_server,
    connect_with_retry,
    load_config,
    main,
    pipe_process_stderr_to_terminal,
    pipe_process_to_websocket,
    pipe_websocket_to_process,
    run,
    signal_handler,
)

__all__ = [
    "build_server_command",
    "connect_to_server",
    "connect_with_retry",
    "load_config",
    "main",
    "pipe_process_stderr_to_terminal",
    "pipe_process_to_websocket",
    "pipe_websocket_to_process",
    "run",
    "signal_handler",
]


if __name__ == "__main__":
    raise SystemExit(main())