import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class RatingStrategy(ABC):
    @abstractmethod
    def calculate_rating(self, *args) -> int:
        pass

    @staticmethod
    def get_rating(value, bins, labels, multiplier=1):
        return int(pd.cut([value], bins=bins, labels=labels, right=False)[0]) * multiplier


class GkRatingStrategy(RatingStrategy):
    def calculate_rating(self, s1, s2, s3, s4, s5, s6) -> int:
        rating = self.get_rating(s1, [0, 64, 66, 68, 70, 72, 74, 76, 78, 80, 101],
                                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], multiplier=2)
        rating += self.get_rating(s2, [-np.inf, -6, -4, -2, 0, 2, 4, 6, 8, 10, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], multiplier=2)
        rating += self.get_rating(s3, [-1, 3, 4, 5, 6, 7, np.inf], [10, 8, 6, 4, 2, 0])
        rating += self.get_rating(s4, [0, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s5, [0, 35, 40, 45, 50, 55, 60, 101], [1, 2, 4, 6, 8, 9, 10])
        rating += self.get_rating(s6, [0, 30, 35, 40, 45, 101], [2, 4, 6, 8, 10])
        return rating


class DfRatingStrategy(RatingStrategy):
    def calculate_rating(self, s1, s2, s3, s4, s5, s6, s7, s8) -> int:
        rating = self.get_rating(s1, [0, 72, 75, 78, 81, 84, 87, 90, 92, 94, 101],
                                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s2, [0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, np.inf],
                                  [1, 3, 5, 6, 7, 9, 10], multiplier=2)
        rating += self.get_rating(s3, [0, 1.5, 2.0, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, np.inf],
                                  [1, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s4, [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s5, [0, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s6, [0, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s7, [0, 5, 8, 11, 14, 17, 20, np.inf],
                                  [10, 9, 8, 6, 4, 2, 0])
        rating += self.get_rating(s8, [0, 1, 2, 3, 4, 5, np.inf], [10, 8, 6, 4, 2, 0])
        return rating


class MfRatingStrategy(RatingStrategy):
    def calculate_rating(self, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11) -> int:
        rating = self.get_rating(s1, [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.inf],
                                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s2, [0, 0.8, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s3, [-np.inf, -3, -2, -1, 0, 1, 2, 3, 4, np.inf],
                                  [1, 2, 3, 4, 6, 7, 8, 9, 10])
        rating += self.get_rating(s4, [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, np.inf],
                                  [1, 2, 3, 4, 6, 7, 8, 9, 10])
        rating += self.get_rating(s5, [0, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s6, [0, 1, 2, 3, 4, 5, 6, 7.5, 8.5, 10, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s7, [0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s8, [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s9, [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s10, [0, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        rating += self.get_rating(s11, [0, 0.5, 1, 1.5, 1.75, 2, 2.5, 3, 3.5, np.inf],
                                  [1, 2, 3, 4, 5, 7, 8, 9, 10])
        return rating


class FwRatingStrategy(RatingStrategy):
    def calculate_rating(self, s1, s2, s3, s4, s5, s6, s7, s8) -> int:
        rating = self.get_rating(s1, [0, 1.5, 2, 3, 4, 5, 6, 7, 8, np.inf],
                                 [1, 2, 3, 4, 6, 7, 8, 9, 10])
        rating += self.get_rating(s2, [0, 1, 2, 2.5, 3, 3.5, 4.5, 5.5, np.inf],
                                  [1, 2, 3, 4, 6, 7, 8, 10])
        rating += self.get_rating(s3, [-np.inf, -3.5, -2.5, -1, 1, 3.5, 5.5, np.inf],
                                  [1, 2, 3, 5, 6, 9, 10])
        rating += self.get_rating(s4, [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, np.inf],
                                  [1, 2, 3, 5, 6, 8, 9, 10])
        rating += self.get_rating(s5, [0, 0.6, 0.8, 1.2, 1.6, 2, 2.4, 2.8, np.inf],
                                  [1, 2, 3, 5, 6, 8, 9, 10], multiplier=1.5)
        rating += self.get_rating(s6, [0, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 9, 10])
        rating += self.get_rating(s7, [0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9], multiplier=2)
        rating += self.get_rating(s8, [0, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, np.inf],
                                  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        return rating


class RatingStrategyFactory:
    @staticmethod
    def create_strategy(position: str) -> RatingStrategy:
        if position == "GK":
            return GkRatingStrategy()
        elif position == "DF":
            return DfRatingStrategy()
        elif position == "MF":
            return MfRatingStrategy()
        elif position == "FW":
            return FwRatingStrategy()


class PlayerRater:
    def __init__(self, strategy: RatingStrategy):
        self._strategy = strategy

    def calculate_rating(self, *args):
        return self._strategy.calculate_rating(*args)


# ================================================================================================================

def make_data():
    tables = [pd.read_csv(f"data/tables/stats{i}.csv") for i in range(1, 10)]
    g1, g2, g3, g4, g5, g6, g7, g8, g9 = tables
    gk_data, df_data, mf_data, fw_data = [], [], [], []
    j = 0
    for i in range(len(g3)):
        strategy = RatingStrategyFactory.create_strategy(g3.iloc[i]["Pos"])
        rater = PlayerRater(strategy)
        if g3.iloc[i]["Pos"] == "GK" and int(g3.iloc[i]["90s"]) > 10:
            potential = rater.calculate_rating(
                g1.iloc[j]["Save%"],
                g2.iloc[j]["PSxG+/-"],
                g7.iloc[i]["Err"] + g8.iloc[i]["Dis"] + g8.iloc[i]["Mis"],
                g2.iloc[j]["#OPA/90"],
                g4.iloc[i]["Cmp%.3"],
                g2.iloc[j]["Cmp%"]
            )
            table = {"Team": g3.iloc[i]["Team"],
                     "Player": g3.iloc[i]["Player"],
                     "Age": g3.iloc[i]["Age"],
                     "Matches": g3.iloc[i]["90s"],
                     "GA90": g1.iloc[j]["GA90"],
                     "Save%": g1.iloc[j]["Save%"],
                     "CS%": g1.iloc[j]["CS%"],
                     "PSXG+/-": g2.iloc[j]["PSxG+/-"],
                     "Launched CMP% (40+ yards)": g2.iloc[j]["Cmp%"],
                     "CMP% (15-30 yards)": g4.iloc[i]["Cmp%.2"],
                     "CMP% (30+ yards)": g4.iloc[i]["Cmp%.3"],
                     "Launch% goal kicks": g2.iloc[j]["Launch%.1"],
                     "Defensive actions": g2.iloc[j]["#OPA/90"],
                     "Errors": g7.iloc[i]["Err"],
                     "Errors under pressure": g8.iloc[i]["Dis"],
                     "Miscontrol": g8.iloc[i]["Mis"],
                     "Rating": potential
                     }
            gk_data.append(table)
            gk_table = pd.DataFrame(gk_data).sort_values("Rating", ascending=False)
            j = j + 1
        elif g3.iloc[i]["Pos"] == "GK":
            j = j + 1
        if g3.iloc[i]["Pos"] == "DF" and int(g3.iloc[i]["90s"]) > 10:
            potential = rater.calculate_rating(
                g4.iloc[i]["Cmp%"],
                round((g7.iloc[i]["Tkl+Int"] / g7.iloc[i]["90s"]), 1),
                round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                round((g7.iloc[i]["Blocks"] / g7.iloc[i]["90s"]), 1),
                round(g9.iloc[i]['Won'] / g7.iloc[i]["90s"], 1),
                (g9.iloc[i]["CrdY"] + (g9.iloc[i]["CrdR"]) * 5 + (g9.iloc[i]["2CrdY"]) * 3 + (g9.iloc[i]["PKcon"]) * 3),
                g7.iloc[i]["Err"]
            )

            table = {"Team": g3.iloc[i]["Team"],
                     "Player": g3.iloc[i]["Player"],
                     "Age": g3.iloc[i]["Age"],
                     "Matches": g3.iloc[i]["90s"],
                     "Cmp%": g4.iloc[i]["Cmp%"],
                     "Progressive Paces": round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                     "Progressive Carries": round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                     "Tackles+Interception": round((g7.iloc[i]["Tkl+Int"] / g7.iloc[i]["90s"]), 1),
                     "Blocks": round((g7.iloc[i]["Blocks"] / g7.iloc[i]["90s"]), 1),
                     "Aerial Won": round(g9.iloc[i]['Won'] / g7.iloc[i]["90s"], 1),
                     "Fouls Commited": round(g9.iloc[i]["Fls"] / g9.iloc[i]["90s"], 1),
                     "Dangerous Fouls": (g9.iloc[i]["CrdY"] + (g9.iloc[i]["CrdR"]) * 5 + (g9.iloc[i]["2CrdY"]) * 3 + (g9.iloc[i]["PKcon"]) * 3),
                     "Errors": g7.iloc[i]["Err"],
                     "Rating": potential
                     }

            df_data.append(table)
            df_table = pd.DataFrame(df_data).sort_values("Rating", ascending=False)

        if g3.iloc[i]["Pos"] == "MF" and int(g3.iloc[i]["90s"]) > 10:
            potential = rater.calculate_rating(
                round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                g3.iloc[i]["G-xG"], round(g4.iloc[i]["xAG"] / g4.iloc[i]["90s"], 2),
                round(g4.iloc[i]["KP"] / g4.iloc[i]["90s"], 1),
                round(g4.iloc[i]["1/3"] / g4.iloc[i]["90s"], 1),
                g6.iloc[i]["SCA90"],
                g6.iloc[i]["GCA90"],
                round((g7.iloc[i]["Tkl+Int"] / g7.iloc[i]["90s"]), 1),
                round((g8.iloc[i]["Succ"] / g7.iloc[i]["90s"]), 1),
                round((g8.iloc[i]["1/3"] / g7.iloc[i]["90s"]), 1)
            )

            potential = potential + g3.iloc[i]["Gls"] // 3 + g4.iloc[i]["Ast"] // 3

            table = {"Team": g3.iloc[i]["Team"],
                     "Player": g3.iloc[i]["Player"],
                     "Age": g3.iloc[i]["Age"],
                     "Matches": g3.iloc[i]["90s"],
                     "Progressive Paces": round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                     "Progressive Carries": round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                     "Goal realization": g3.iloc[i]["G-xG"],
                     "xAG/90": round(g4.iloc[i]["xAG"] / g4.iloc[i]["90s"], 2),
                     "Cmp/90": round(g4.iloc[i]["Cmp"] / g4.iloc[i]["90s"], 1),
                     "Key passes": round(g4.iloc[i]["KP"] / g4.iloc[i]["90s"], 1),
                     "Passes into 1/3": round(g4.iloc[i]["1/3"] / g4.iloc[i]["90s"], 1),
                     "Shot-Creating Actions": g6.iloc[i]["SCA90"],
                     "Goal-Creating Actions": g6.iloc[i]["GCA90"],
                     "Tackles+Interception": round((g7.iloc[i]["Tkl+Int"] / g7.iloc[i]["90s"]), 1),
                     "Dribbling": round((g8.iloc[i]["Succ"] / g7.iloc[i]["90s"]), 1),
                     "Carriers into 1/3": round((g8.iloc[i]["1/3"] / g7.iloc[i]["90s"]), 1),
                     "Fouls Commited": round(g9.iloc[i]["Fls"] / g9.iloc[i]["90s"], 1),
                     "Rating": potential
                     }

            mf_data.append(table)
            mf_table = pd.DataFrame(mf_data).sort_values("Rating", ascending=False)

        if g3.iloc[i]["Pos"] == "FW" and int(g3.iloc[i]["90s"]) > 10:
            potential = rater.calculate_rating(
                round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                g3.iloc[i]["G-xG"],
                round(g4.iloc[i]["xAG"] / g4.iloc[i]["90s"], 2),
                round(g4.iloc[i]["KP"] / g4.iloc[i]["90s"], 1),
                g6.iloc[i]["SCA90"],
                g6.iloc[i]["GCA90"],
                round((g8.iloc[i]["Succ"] / g7.iloc[i]["90s"]), 1))

            potential = potential + g3.iloc[i]["Gls"] // 5 + g4.iloc[i]["Ast"] // 3

            table = {"Team": g3.iloc[i]["Team"],
                     "Player": g3.iloc[i]["Player"],
                     "Age": g3.iloc[i]["Age"],
                     "Matches": g3.iloc[i]["90s"],
                     "Goals": g3.iloc[i]["Gls"],
                     "Goal realization": g3.iloc[i]["G-xG"],
                     "Sh/90": g3.iloc[i]["Sh/90"],
                     "xAG/90": round(g4.iloc[i]["xAG"] / g4.iloc[i]["90s"], 2),
                     "Cmp/90": round(g4.iloc[i]["Cmp"] / g4.iloc[i]["90s"], 1),
                     "Progressive Paces": round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1),
                     "Progressive Carries": round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1),
                     "Key passes": round(g4.iloc[i]["KP"] / g4.iloc[i]["90s"], 1),
                     "Dribbling": round((g8.iloc[i]["Succ"] / g7.iloc[i]["90s"]), 1),
                     "Shot-Creating Actions": g6.iloc[i]["SCA90"],
                     "Goal-Creating Actions": g6.iloc[i]["GCA90"],
                     "Rating": potential
                     }
            fw_data.append(table)
            fw_table = pd.DataFrame(fw_data).sort_values("Rating", ascending=False)

    tables = [gk_table, df_table, mf_table, fw_table]
    names = ["gk", "df", "mf", "fw"]
    for name, table in zip(names, tables):
        table.to_csv(f"web/templates/tables/{name}.csv", index=False)