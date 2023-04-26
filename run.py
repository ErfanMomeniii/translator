import argparse
from app.app import app


def get_args():
    parser = argparse.ArgumentParser(
        description="Translator Service"
    )
    parser.add_argument(
        "--host",
        type=str,
        help="Hostname (%(default)s)",
        default="127.0.0.1"
    )
    parser.add_argument(
        "--port",
        type=int,
        help="Port (%(default)s)",
        default=5000)

    return parser.parse_args()


if __name__ == "__main__":
    args = get_args()
    app.run(host=args.host, port=args.port, debug=True)
