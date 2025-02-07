from typing import Tuple

def bf(planet1: str, planet2: str) -> Tuple[str,...]:
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    if planet1 not in planets or planet2 not in planets:
        return ()
    idx1, idx2 = planets.index(planet1), planets.index(planet2)
    if idx1 > idx2:
        idx1, idx2 = idx2, idx1
    return tuple(planets[idx1 + 1:idx2])