import argparse
import sys
import textwrap
from tempfile import NamedTemporaryFile


def main(pid: int, log_level: str) -> None:
    # BEGIN script
    script = textwrap.dedent(f"""
        import logging
        logger = logging.getLogger("main")
        print("Changing log level to {log_level!r} via remote exec...")
        logger.setLevel(logging.{log_level})
        """)
    with NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        script_path = f.name
        f.write(script)
    # END script

    print("Injecting script to change log level to", log_level)
    # BEGIN exec
    sys.remote_exec(pid, script_path)
    # END exec
    print("Log level changed ✅")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Change the log level of a remote server."
    )
    parser.add_argument(
        "--log-level",
        type=str,
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        required=True,
        help="Set the log level of the remote server.",
    )
    parser.add_argument(
        "-p",
        "--pid",
        type=int,
        required=True,
        help="PID of the remote server process.",
    )
    args = parser.parse_args()
    main(pid=args.pid, log_level=args.log_level)
