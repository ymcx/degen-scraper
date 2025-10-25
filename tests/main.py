from src import parse


def test_ticker_parsing() -> None:
    string = "YOLO! Holding BYND Calls, equivalent to 188,500 shares. I'm not quitting!"
    parsed = {"BYND"}
    assert parsed == parse.tickers(string)

    string = "A AA AAA AAAA AAAAA AAAAAA"
    parsed = {"A", "AA", "AAA", "AAAA", "AAAAA"}
    assert parsed == parse.tickers(string)

    string = "(A) !AA! <AAA> AAAA? _AAAAA_ $AAAAAA"
    parsed = {"A", "AA", "AAA", "AAAA", "AAAAA"}
    assert parsed == parse.tickers(string)

    string = "I'M $A'M B4E BE $ee $Ee $eE $EE"
    parsed = {"IM", "AM", "BE", "EE"}
    assert parsed == parse.tickers(string)

    string = " AA-AA -B-B- 4-B-B- "
    parsed = {"AAAA", "BB"}
    assert parsed == parse.tickers(string)

    string = "$aa $$$abcde $1 1$ABC"
    parsed = {"AA", "ABCDE"}
    assert parsed == parse.tickers(string)


def main() -> None:
    test_ticker_parsing()

    print("All tests passed successfully")


if __name__ == "__main__":
    main()
