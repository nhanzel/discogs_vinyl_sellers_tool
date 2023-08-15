import argparse
import api


def main():
    parser = argparse.ArgumentParser(description="Discogs Vinyl Sellers Tool")
    parser.add_argument(
        "-p",
        "--path",
        help="Tag denoting the absolute path to the text file containing vinyl IDs",
        action="count",
    )
    parser.add_argument(
        "-f",
        "--folder",
        help="Tag denoting that the folder name should be used to grab vinyl IDs",
        action="count",
    )
    args = parser.parse_args()

    vinyl_ids = []
    config = {}

    with open("config.txt", "r") as file:
        raw_data = file.read().splitlines()
        for line in raw_data:
            key, value = line.split("=")
            config[key] = value

    api.set_token(config["token"])

    if args.path:
        with open(config["filepath"], "r") as file:
            vinyl_ids = file.read().splitlines()
    elif args.folder:
        vinyl_ids = api.get_vinyl_ids(config["folder"], config["username"])

    print("\n")
    for vinyl_id in vinyl_ids:
        info = api.get_info(vinyl_id)
        price_suggestions = api.get_price_suggestions(vinyl_id)

        print(format_output(vinyl_id, info, price_suggestions))


def format_output(vinyl_id, info, price_suggestions):
    ratio = round(info["community"]["want"] / info["community"]["have"], 2)
    return (
        f"{info['title']} ({vinyl_id}):\n"
        f"{info['artists'][0]['name']} - {info['year']}\n"
        f"\n"
        f"Number for Sale: {info['num_for_sale']}\n"
        f"Price Suggestions: ${price_suggestions['Poor (P)']['value']: .2f} - ${price_suggestions['Mint (M)']['value']: .2f} (Poor - Mint)\n"
        f"Have/Want Ratio: {ratio} (Want - {info['community']['want']}, Have - {info['community']['have']})\n"
        f"\n----------------------------------------\n"
    )


if __name__ == "__main__":
    main()
