import argparse


def main():
    pars = argparse.ArgumentParser("CLI for Uniter.")

    pars.add_argument(
        "-t",
        "--type",
        type=str,
        choices=["weight", "length"],
        help="Unit type",
        required=True,
    )
    pars.add_argument("-m", "--main", type=str, help="Main unit type", required=True)
    pars.add_argument(
        "-d", "--dest", type=str, help="Destination unit type", required=True
    )
    pars.add_argument(
        "-v", "--value", type=float, help="Value being converted", required=True
    )

    args = pars.parse_args()

    match args.type:
        case "weight":
            from units import weight

            match args.main:
                case "kg" | "kilogram":
                    w = weight.Kilogram(args.value)
                    print(w.convert_to(args.dest))
                case "g" | "gram":
                    w = weight.Gram(args.value)
                    print(w.convert_to(args.dest))
        case "length":
            from units import length

            match args.main:
                case "mm" | "millimeter":
                    l = length.Millimeter(args.value)
                    print(l.convert_to(args.dest))
                case "cm" | "centimeter":
                    l = length.Centimeter(args.value)
                    print(l.convert_to(args.dest))
                case "m" | "meter":
                    l = length.Meter(args.value)
                    print(l.convert_to(args.dest))
                case "km" | "km":
                    l = length.Kilometer(args.value)
                    print(l.convert_to(args.dest))


if __name__ == "__main__":
    main()
