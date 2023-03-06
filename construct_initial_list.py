#!/usr/bin/env python3
"""Construct initial list of vocabulary from the Google Doc.
"""

import pandas as pd
import json
import re


def construct_vocab_list(english, yiddish, pronouns, word_category):
    """Convert lists of English, Yiddish, and pronouns into a dataframe
    """
    if len(english) != len(yiddish):
        raise Exception("English and Yiddish aren't the same length!")
    if len(english) != len(pronouns):
        raise Exception("English and Pronouns aren't the same length!")
    unhappy = ['*' in e for e in english]
    constructed = ['+' in e for e in english]
    english = [e.replace('*', '').replace('+', '') for e in english]
    literal = [re.findall(r'\([lL]it\.(.*)\)', e) for e in english]
    literal = [l[0].strip() if l else '' for l in literal ]
    english = [re.sub(r'\([lL]it\.(.*)\)', '', e) for e in english]
    english = [e.replace('־', '-') for e in english]
    yiddish = [y.replace('־', '-') for y in yiddish]
    df = pd.DataFrame([{'english': e, 'yiddish': y, 'pronoun': p, 'unhappy': u,
                        'constructed': c,  'category': word_category, 'literal': l}
                       for e,y,p,u,c,l in
                       zip(english, yiddish, pronouns, unhappy, constructed, literal)])
    df['alternative_yiddish'] = ''
    return df


def create_full_list():
    with open('from_google_doc.json') as f:
        words = json.load(f)
    dfs = []
    for k, v in words.items():
        tmp = construct_vocab_list(**v, word_category=k)
        if k == 'character sheet':
            tmp.loc[19, 'alternative_yiddish'] = 'שטאַם'
            tmp.loc[19, 'yiddish'] = tmp.loc[19, 'yiddish'].split('(')[0].strip()
        elif k == 'optional character sheet':
            tmp.loc[4, 'alternative_yiddish'] = 'כּישופֿל -עך'
        elif k == 'character creation':
            tmp.loc[20, 'alternative_yiddish'] = 'האַלבניק'
        elif k == 'items':
            tmp.loc[27, 'alternative_yiddish'] = 'קאַרטע'
        elif k == 'monsters':
            tmp.loc[9, 'alternative_yiddish'] = 'גײַסט'
            tmp.loc[10, 'alternative_yiddish'] = 'שד, שׂטן'
            tmp.loc[8, 'alternative_yiddish'] = 'דער ריז, די גוג-ומגוג'
        dfs.append(tmp)
    dfs = pd.concat(dfs)
    with open('vocab.json', 'w') as f:
        json.dump(dfs.to_dict('records'), f, ensure_ascii=False, indent=3)


if __name__ == '__main__':
    create_full_list()
