# -*- coding:utf-8 -*-
import sys
import numpy as np
import collections
import math
import re

def read_file(filename):
    with open(filename, "r") as f:
        lines = [line.replace("\n", "").split() for line in f]
    return lines


def read_vector(filename):
    lines = read_file(filename)
    vector_dict = collections.OrderedDict({})
    # 初めの一行目はベクトルの行数と次元なのでスキップ
    for l in lines[1:]:
        vector_dict[l[0]] = np.array([float(w) for w in l[1:]])
    return vector_dict

# dictionaryのkey:value入れ替え
def invert_dict(dictionary):
    return {v:k for k, v in dictionary.items()}

# 辞書のvalueでソート。デフォルトは降順
def sort_dict(dic, sort_type="DESC"):
    counter = collections.Counter(dic)
    if sort_type == "ASC":
        count_pairs = sorted(counter.items(), key=lambda x: x[1])
    elif sort_type == "DESC":
        count_pairs = sorted(counter.items(), key=lambda x: -x[1])
    key, value = list(zip(*count_pairs))
    return (key, value)



def concatenate_sequence(seq, id_to_word=None):
    if id_to_word:
        return ' '.join([id_to_word[word_id] for word_id in seq])
    else:
        return ' '.join([str(word) for word in seq])


# 単語のid列を文に変更してprint
def print_sequence(seq, id_to_word=None):
    if id_to_word:
        for word_id in seq:
            print id_to_word[word_id],
        print ''
    else:
        for word in seq:
            print word,
        print ''

# argparserの文字列をboolに変換
def str_to_bool(str_):
    bool_ = True
    if str_ in ["True", "true", "1"]:
        bool_ = True
    elif str_ in ["False", "false", "0"]:
        bool_ = False
    else:
        print("Irregular bool string")
        exit(1)
    return bool_


def separate_path_and_filename(file_path):
    m = re.match('^(.+)/(.+)$', file_path)
    return m.group(1) , m.group(2)


