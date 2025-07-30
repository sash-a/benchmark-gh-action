import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--branches",
        nargs="+",
        type=str,
        default=["develop"],
        help="Branches to run",
    )
    parser.add_argument(
        "--scenarios",
        nargs="+",
        type=str,
        default=["3s5z"],
        help="Scenarios to run",
    )
    parser.add_argument(
        "--systems",
        nargs="+",
        type=str,
        default=["ff_ippo"],
        help="Systems to run",
    )
    parser.add_argument(
        "--seeds",
        nargs="+",
        type=str,
        default=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        help="Seeds to run",
    )
    parser.add_argument(
        "--neptune_id",
        nargs=1,
        type=str,
        default="",
        help="Prefix of the neptune ID for this group of runs",
    )
    return parser.parse_args()


if __name__ == "__main__":
    print(parse_args())
