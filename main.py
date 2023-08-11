import argparse
import api


def main():
    parser = argparse.ArgumentParser(description="Discogs Vinyl Sellers Tool")
    parser.add_argument(
        "input_file", type=str, help="Path to the text file containing vinyl IDs"
    )
    args = parser.parse_args()

    with open(args.input_file, "r") as file:
        vinyl_ids = file.read().splitlines()

    for vinyl_id in vinyl_ids:
        info = api.get_info(vinyl_id)
        current_snapshot = api.get_market_snapshot(vinyl_id)
        price_suggestions = api.get_price_suggestions(vinyl_id)
        have_want_ratio = api.get_have_want_ratio(vinyl_id)

        print(f"Info: {info}")
        print(f"Current Snapshot: {current_snapshot}")
        print(f"Price Suggestions: {price_suggestions}")
        print(f"Have/Want Ratio: {have_want_ratio}")


if __name__ == "__main__":
    main()
