import pandas as pd
import numpy as np


def get_rating_gk(s1,s2,s3,s4,s5,s6):
    b = [0, 64, 66, 68, 70, 72, 74, 76, 78, 80, 101]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating=int(pd.cut([s1], bins=b, labels=l, right=False)[0])*2

    b = [-np.inf, -6, -4, -2, 0, 2, 4, 6, 8, 10, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s2], bins=b, labels=l, right=False)[0])*2

    b = [-1, 3, 4, 5, 6, 7, np.inf]
    l = [10, 8, 6, 4, 2, 0]
    rating += int(pd.cut([s3], bins=b, labels=l, right=False)[0])

    b = [0, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s4], bins=b, labels=l, right=False)[0])

    b = [0, 35, 40, 45, 50, 55, 60, 101]
    l = [1, 2, 4, 6, 8, 9, 10]
    rating += int(pd.cut([s5], bins=b, labels=l, right=False)[0])

    b = [0, 30, 35, 40, 45, 101]
    l = [2, 4, 6, 8, 10]
    rating += int(pd.cut([s6], bins=b, labels=l, right=False)[0])
    return rating


def get_rating_df(s1, s2, s3, s4, s5, s6, s7, s8):
    rating = 0
    b = [0, 72, 75, 78, 81, 84, 87, 90, 92, 94, 101]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s1], bins=b, labels=l, right=False)[0])

    b = [0, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, np.inf]
    l = [1, 3, 5, 6, 7, 9, 10]
    rating += int(pd.cut([s2], bins=b, labels=l, right=False)[0])*2

    b = [0, 1.5, 2.0, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, np.inf]
    l = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s3], bins=b, labels=l, right=False)[0])

    b = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s4], bins=b, labels=l, right=False)[0])

    b = [0, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s5], bins=b, labels=l, right=False)[0])

    b = [0, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s6], bins=b, labels=l, right=False)[0])

    b = [0, 5, 8, 11, 14, 17, 20, np.inf]
    l = [10, 9, 8, 6, 4, 2, 0]
    rating += int(pd.cut([s7], bins=b, labels=l, right=False)[0])

    b = [0, 1, 2, 3, 4, 5, np.inf]
    l = [10, 8, 6, 4, 2, 0]
    rating += int(pd.cut([s8], bins=b, labels=l, right=False)[0])
    return rating

def get_rating_mf(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10, s11):
    rating=0
    b = [0, 2, 3, 4, 5, 6, 7, 8, 9, 10, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s1], bins=b, labels=l, right=False)[0])

    b = [0, 0.8, 1.4, 2, 2.5, 3, 3.5, 4, 4.5, 5, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s2], bins=b, labels=l, right=False)[0])

    b = [-np.inf, -3, -2, -1, 0, 1, 2, 3, 4, np.inf]
    l = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s3], bins=b, labels=l, right=False)[0])

    b = [0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, np.inf]
    l = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s4], bins=b, labels=l, right=False)[0])

    b = [0, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s5], bins=b, labels=l, right=False)[0])

    b = [0, 1, 2, 3, 4, 5, 6, 7.5, 8.5, 10, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s6], bins=b, labels=l, right=False)[0])

    b = [0, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s7], bins=b, labels=l, right=False)[0])

    b = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s8], bins=b, labels=l, right=False)[0])

    b = [0, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s9], bins=b, labels=l, right=False)[0])

    b = [0, 0.6, 0.9, 1.2, 1.5, 1.8, 2.1, 2.4, 2.7, 3, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s10], bins=b, labels=l, right=False)[0])

    b = [0, 0.5, 1, 1.5, 1.75, 2, 2.5, 3, 3.5, np.inf]
    l = [1, 2, 3, 4, 5, 7, 8, 9, 10]
    rating += int(pd.cut([s11], bins=b, labels=l, right=False)[0])
    return rating

def get_rating_fw(s1, s2, s3, s4, s5, s6, s7, s8):
    rating = 0
    b = [0, 1.5, 2, 3, 4, 5, 6, 7, 8, np.inf]
    l = [1, 2, 3, 4, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s1], bins=b, labels=l, right=False)[0])

    b = [0, 1, 2, 2.5, 3, 3.5, 4.5, 5.5, np.inf]
    l = [1, 2, 3, 4, 6, 7, 8, 10]
    rating += int(pd.cut([s2], bins=b, labels=l, right=False)[0])

    b = [-np.inf, -3.5, -2.5, -1, 1, 3.5, 5.5, np.inf]
    l = [1, 2, 3, 5, 6, 9, 10]
    rating += int(pd.cut([s3], bins=b, labels=l, right=False)[0])

    b = [0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, np.inf]
    l = [1, 2, 3, 5, 6, 8, 9, 10]
    rating += int(pd.cut([s4], bins=b, labels=l, right=False)[0])

    b = [0, 0.6, 0.8, 1.2, 1.6, 2, 2.4, 2.8, np.inf]
    l = [1, 2, 3, 5, 6, 8, 9, 10]
    rating += int(pd.cut([s5], bins=b, labels=l, right=False)[0]) * 1.5

    b = [0, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 9, 10]
    rating += int(pd.cut([s6], bins=b, labels=l, right=False)[0])

    b = [0, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    rating += int(pd.cut([s7], bins=b, labels=l, right=False)[0]) * 2

    b = [0, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, np.inf]
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    rating += int(pd.cut([s8], bins=b, labels=l, right=False)[0])
    return rating

#================================================================================================================

def make_data():
    g1=pd.read_csv("templates/tables/stats1.csv")
    g2=pd.read_csv("templates/tables/stats2.csv")
    g3=pd.read_csv("templates/tables/stats3.csv")
    g4=pd.read_csv("templates/tables/stats4.csv")
    g5=pd.read_csv("templates/tables/stats5.csv")
    g6=pd.read_csv("templates/tables/stats6.csv")
    g7=pd.read_csv("templates/tables/stats7.csv")
    g8=pd.read_csv("templates/tables/stats8.csv")
    g9=pd.read_csv("templates/tables/stats9.csv")
    gk_data=[]
    df_data=[]
    mf_data=[]
    fw_data=[]
    j=0
    potential=0
    for i in range(len(g3)):
        if g3.iloc[i]["Pos"]=="GK" and int(g3.iloc[i]["90s"])>10:
            potential=get_rating_gk(g1.iloc[j]["Save%"], g2.iloc[j]["PSxG+/-"], g7.iloc[i]["Err"]+g8.iloc[i]["Dis"]+g8.iloc[i]["Mis"],
                                    g2.iloc[j]["#OPA/90"], g4.iloc[i]["Cmp%.3"], g2.iloc[j]["Cmp%"])
            table={"Team":g3.iloc[i]["Team"], "Player":g3.iloc[i]["Player"], "Age":g3.iloc[i]["Age"], "Matches": g3.iloc[i]["90s"],
                   "GA90":g1.iloc[j]["GA90"],"Save%":g1.iloc[j]["Save%"], "CS%":g1.iloc[j]["CS%"], "PSXG+/-":g2.iloc[j]["PSxG+/-"],
                   "Launched CMP% (40+ yards)":g2.iloc[j]["Cmp%"], "CMP% (15-30 yards)":g4.iloc[i]["Cmp%.2"], "CMP% (30+ yards)":g4.iloc[i]["Cmp%.3"],
                   "Launch% goal kicks":g2.iloc[j]["Launch%.1"], "Defensive actions":g2.iloc[j]["#OPA/90"], "Errors":g7.iloc[i]["Err"], "Errors under pressure":g8.iloc[i]["Dis"], "Miscontrol":g8.iloc[i]["Mis"],
                   "Rating": potential
            }
            gk_data.append(table)
            gk_table = pd.DataFrame(gk_data)
            j=j+1
        elif g3.iloc[i]["Pos"]=="GK":
            j=j+1
        if g3.iloc[i]["Pos"]=="DF" and int(g3.iloc[i]["90s"])>10:
            potential = get_rating_df(g4.iloc[i]["Cmp%"], round((g7.iloc[i]["Tkl+Int"]/g7.iloc[i]["90s"]), 1), round((g4.iloc[i]["PrgP"])/g4.iloc[i]["90s"],1),
                                      round(g8.iloc[i]["PrgC"]/g4.iloc[i]["90s"],1), round((g7.iloc[i]["Blocks"]/g7.iloc[i]["90s"]),1), round(g9.iloc[i]['Won']/g7.iloc[i]["90s"],1),
                                      (g9.iloc[i]["CrdY"]+(g9.iloc[i]["CrdR"])*5+(g9.iloc[i]["2CrdY"])*3+(g9.iloc[i]["PKcon"])*3), g7.iloc[i]["Err"])
            table = {"Team": g3.iloc[i]["Team"], "Player": g3.iloc[i]["Player"], "Age": g3.iloc[i]["Age"], "Matches": g3.iloc[i]["90s"],
                     "Cmp%": g4.iloc[i]["Cmp%"], "Progressive Paces": round((g4.iloc[i]["PrgP"])/g4.iloc[i]["90s"],1), "Progressive Carries":round(g8.iloc[i]["PrgC"]/g4.iloc[i]["90s"],1),
                     "Tackles+Interception": round((g7.iloc[i]["Tkl+Int"]/g7.iloc[i]["90s"]), 1), "Blocks":round((g7.iloc[i]["Blocks"]/g7.iloc[i]["90s"]),1), "Aerial Won":round(g9.iloc[i]['Won']/g7.iloc[i]["90s"],1),
                     "Fouls Commited":round(g9.iloc[i]["Fls"]/g9.iloc[i]["90s"],1), "Dangerous Fouls":(g9.iloc[i]["CrdY"]+(g9.iloc[i]["CrdR"])*5+(g9.iloc[i]["2CrdY"])*3+(g9.iloc[i]["PKcon"])*3), "Errors":g7.iloc[i]["Err"],
                     "Rating": potential
                     }
            df_data.append(table)
            df_table=pd.DataFrame(df_data)
        if g3.iloc[i]["Pos"]=="MF" and int(g3.iloc[i]["90s"])>10:
            potential= get_rating_mf(round((g4.iloc[i]["PrgP"])/g4.iloc[i]["90s"],1), round(g8.iloc[i]["PrgC"]/g4.iloc[i]["90s"],1), g3.iloc[i]["G-xG"], round(g4.iloc[i]["xAG"]/g4.iloc[i]["90s"],2),
                                     round(g4.iloc[i]["KP"]/g4.iloc[i]["90s"],1), round(g4.iloc[i]["1/3"]/g4.iloc[i]["90s"],1), g6.iloc[i]["SCA90"], g6.iloc[i]["GCA90"], round((g7.iloc[i]["Tkl+Int"]/g7.iloc[i]["90s"]), 1),
                                     round((g8.iloc[i]["Succ"]/g7.iloc[i]["90s"]), 1), round((g8.iloc[i]["1/3"]/g7.iloc[i]["90s"]), 1))
            potential=potential++g3.iloc[i]["Gls"]//3+g4.iloc[i]["Ast"]//3
            table = {"Team": g3.iloc[i]["Team"], "Player": g3.iloc[i]["Player"], "Age": g3.iloc[i]["Age"], "Matches": g3.iloc[i]["90s"],
                     "Progressive Paces": round((g4.iloc[i]["PrgP"])/g4.iloc[i]["90s"],1), "Progressive Carries":round(g8.iloc[i]["PrgC"]/g4.iloc[i]["90s"],1),
                     "Goal realization":g3.iloc[i]["G-xG"], "xAG/90":round(g4.iloc[i]["xAG"]/g4.iloc[i]["90s"],2), "Cmp/90":round(g4.iloc[i]["Cmp"]/g4.iloc[i]["90s"],1), "Key passes":round(g4.iloc[i]["KP"]/g4.iloc[i]["90s"],1), "Passes into 1/3":round(g4.iloc[i]["1/3"]/g4.iloc[i]["90s"],1),
                     "Shot-Creating Actions":g6.iloc[i]["SCA90"], "Goal-Creating Actions":g6.iloc[i]["GCA90"], "Tackles+Interception": round((g7.iloc[i]["Tkl+Int"]/g7.iloc[i]["90s"]), 1), "Dribbling":round((g8.iloc[i]["Succ"]/g7.iloc[i]["90s"]), 1),
                     "Carriers into 1/3":round((g8.iloc[i]["1/3"]/g7.iloc[i]["90s"]), 1), "Fouls Commited":round(g9.iloc[i]["Fls"]/g9.iloc[i]["90s"],1),
                     "Rating": potential
                     }
            mf_data.append(table)
            mf_table=pd.DataFrame(mf_data)
        if g3.iloc[i]["Pos"]=="FW" and int(g3.iloc[i]["90s"])>10:
            potential=get_rating_fw(round((g4.iloc[i]["PrgP"])/g4.iloc[i]["90s"],1), round(g8.iloc[i]["PrgC"]/g4.iloc[i]["90s"],1),
                                    g3.iloc[i]["G-xG"], round(g4.iloc[i]["xAG"]/g4.iloc[i]["90s"],2), round(g4.iloc[i]["KP"]/g4.iloc[i]["90s"],1),
                                    g6.iloc[i]["SCA90"], g6.iloc[i]["GCA90"], round((g8.iloc[i]["Succ"]/g7.iloc[i]["90s"]), 1))
            potential=potential+g3.iloc[i]["Gls"]//5+g4.iloc[i]["Ast"]//3
            table = {"Team": g3.iloc[i]["Team"], "Player": g3.iloc[i]["Player"], "Age": g3.iloc[i]["Age"], "Matches": g3.iloc[i]["90s"],  "Goals":g3.iloc[i]["Gls"],
                     "Goal realization":g3.iloc[i]["G-xG"], "Sh/90":g3.iloc[i]["Sh/90"], "xAG/90":round(g4.iloc[i]["xAG"]/g4.iloc[i]["90s"],2), "Cmp/90":round(g4.iloc[i]["Cmp"]/g4.iloc[i]["90s"],1),
                     "Progressive Paces": round((g4.iloc[i]["PrgP"]) / g4.iloc[i]["90s"], 1), "Progressive Carries": round(g8.iloc[i]["PrgC"] / g4.iloc[i]["90s"], 1), "Key passes":round(g4.iloc[i]["KP"]/g4.iloc[i]["90s"],1),
                     "Dribbling":round((g8.iloc[i]["Succ"]/g7.iloc[i]["90s"]), 1), "Shot-Creating Actions": g6.iloc[i]["SCA90"], "Goal-Creating Actions":g6.iloc[i]["GCA90"],
                     "Rating": potential
                     }
            fw_data.append(table)
            fw_table=pd.DataFrame(fw_data)

    gk_table= gk_table.sort_values("Rating", ascending=False)
    df_table= df_table.sort_values("Rating", ascending=False)
    mf_table= mf_table.sort_values("Rating", ascending=False)
    fw_table= fw_table.sort_values("Rating", ascending=False)
    gk_table.to_html("templates/gk.html", index=False)
    df_table.to_html("templates/df.html", index=False)
    mf_table.to_html("templates/mf.html", index=False)
    fw_table.to_html("templates/fw.html", index=False)

make_data()