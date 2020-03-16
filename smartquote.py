"""Substitutes or removes smart quotes."""


def substitute(s: str) -> str:
    return (
        s.replace("“", '"')
        .replace("”", '"')
        .replace("‘", "'")
        .replace("’", "'")
    )


def remove(s: str) -> str:
    return (
        s.replace("“", "").replace("”", "").replace("‘", "").replace("’", "")
    )
