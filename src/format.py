from operator import itemgetter
from collections import defaultdict
from itertools import islice
import calculate


def _take(input: dict[str, float], n: int) -> dict[str, float]:
    return dict(islice(input.items(), n))


def _sum(
    scores: dict[str, dict[int, tuple[int, int, float, float]]],
) -> dict[str, float]:
    scores_summed = defaultdict(float)

    for ticker, submissions in scores.items():
        for _, submission in submissions.items():
            comments, score, ratio, epoch = submission
            scores_summed[ticker] += calculate.score(comments, score, ratio, epoch)

    return scores_summed


def _sort(scores: dict[str, float]) -> dict[str, float]:
    scores_sorted = sorted(scores.items(), key=itemgetter(1), reverse=True)

    return dict(scores_sorted)


def _format(scores: dict[str, float]) -> str:
    scores_formatted = []

    for ticker, score in scores.items():
        line = f"{ticker:<5} {score:>4.0f}"
        scores_formatted.append(line)

    return "\n".join(scores_formatted)


def scores_str(
    scores: dict[str, dict[int, tuple[int, int, float, float]]], n: int
) -> str:
    scores_summed = _sum(scores)
    scores_sorted = _sort(scores_summed)
    scores_sorted = _take(scores_sorted, n)
    scores_formatted = _format(scores_sorted)

    return scores_formatted


def scores_data(
    scores: dict[str, dict[int, tuple[int, int, float, float]]], n: int
) -> dict[str, float]:
    scores_summed = _sum(scores)
    scores_sorted = _sort(scores_summed)
    scores_sorted = _take(scores_sorted, n)

    return scores_sorted
