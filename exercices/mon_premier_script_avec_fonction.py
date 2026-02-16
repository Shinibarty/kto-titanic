import unittest
from dataclasses import dataclass
from typing import List

LETTER_LIMIT: int = 7


@dataclass(frozen=True)
class Prenom:
    value: str

    def has_more_than_limit_letters(self, limit: int) -> bool:
        return len(self.value) > limit


def count_names_with_more_than_limit(prenoms: List[Prenom], limit: int) -> int:
    count: int = 0

    for prenom in prenoms:
        if prenom.has_more_than_limit_letters(limit):
            count += 1
            print(f"{prenom.value} est un prénom avec un nombre de lettres supérieur à {limit}")
        else:
            print(f"{prenom.value} est un prénom avec un nombre de lettres inférieur ou égal à {limit}")

    return count


class TestNamesMethod(unittest.TestCase):

    def test_count_names_with_more_than_limit(self) -> None:
        prenoms: List[Prenom] = [
            Prenom("Guillaume"),
            Prenom("Gilles"),
            Prenom("Juliette"),
            Prenom("Antoine"),
            Prenom("François"),
            Prenom("Cassandre"),
        ]

        result: int = count_names_with_more_than_limit(prenoms=prenoms, limit=LETTER_LIMIT)
        self.assertEqual(result, 4)


if __name__ == "__main__":
    unittest.main()
