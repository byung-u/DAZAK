#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##########################################
# 출처
# 원본: http://highthroughput.org/wp/
# 원본참고: http://pinkwink.kr/1005
##########################################
# 관련 개념
"""
# zip
 >>> x = [1, 2, 3]
 >>> y = [4, 5, 6]
 >>> zipped = zip(x, y)
 >>> list(zipped)
 [(1, 4), (2, 5), (3, 6)]
 >>> x2, y2 = zip(*zip(x, y))
 >>> x == list(x2) and y == list(y2)
 True

# pandas.DataFrame.pivot
>>> df = pd.DataFrame({'foo': ['one','one','one','two','two','two'],
                       'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'baz': [1, 2, 3, 4, 5, 6]})
>>> df
    foo   bar  baz
0   one   A    1
1   one   B    2
2   one   C    3
3   two   A    4
4   two   B    5
5   two   C    6
>>> df.pivot(index='foo', columns='bar', values='baz')
     A   B   C
one  1   2   3
two  4   5   6
>>> df.pivot(index='foo', columns='bar')['baz']
     A   B   C
one  1   2   3
two  4   5   6

# numpy masked array
>>> import numpy as np
>>> import numpy.ma as ma
>>> x = np.array([1, 2, 3, -1, 5])
# -1 만 제외하고 구하고 싶을 때
# 아래처럼 -1에 대해서만 마스킹하여 처리
>>> mx = ma.masked_array(x, mask=[0, 0, 0, 1, 0])
>>> mx.mean()
2.75

# color map
cmaps = [('Perceptually Uniform Sequential',
                            ['viridis', 'inferno', 'plasma', 'magma']),
         ('Sequential',     ['Blues', 'BuGn', 'BuPu',
                             'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
                             'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
                             'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
         ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
                             'copper', 'gist_heat', 'gray', 'hot',
                             'pink', 'spring', 'summer', 'winter']),
         ('Diverging',      ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
                             'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
                             'seismic']),
         ('Qualitative',    ['Accent', 'Dark2', 'Paired', 'Pastel1',
                             'Pastel2', 'Set1', 'Set2', 'Set3', 'Vega10',
                             'Vega20', 'Vega20b', 'Vega20c']),
         ('Miscellaneous',  ['gist_earth', 'terrain', 'ocean', 'gist_stern',
                             'brg', 'CMRmap', 'cubehelix',
                             'gnuplot', 'gnuplot2', 'gist_ncar',
                             'nipy_spectral', 'jet', 'rainbow',
                             'gist_rainbow', 'hsv', 'flag', 'prism'])]
"""
##########################################
# CODE
##########################################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


BORDER_LINES = [
    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)],  # 인천
    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)],  # 서울
    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
     (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)],  # 경기도
    [(9, 12), (9, 10), (8, 10)],  # 강원도
    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
     (13, 4), (14, 4), (14, 2)],  # 충청남도
    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
     (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)],  # 충청북도
    [(14, 4), (15, 4), (15, 6)],  # 대전시
    [(14, 7), (14, 9), (13, 9), (13, 11), (13, 13)],  # 경상북도
    [(14, 8), (16, 8), (16, 10), (15, 10),
     (15, 11), (14, 11), (14, 12), (13, 12)],  # 대구시
    [(15, 11), (16, 11), (16, 13)],  # 울산시
    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)],  # 전라북도
    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)],  # 광주시
    [(18, 5), (20, 5), (20, 6)],  # 전라남도
    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)],  # 부산시
]

"""
# ziped BORDER_LINES
>>>    for path in BORDER_LINES:
>>>        ys, xs = zip(*path)

(3, 5, 5, 9, 9) (2, 2, 3, 3, 1)
(2, 3, 3, 8, 8, 7, 7, 4, 4, 1) (5, 5, 4, 4, 7, 7, 9, 9, 7, 7)
(1, 1, 3, 3, 8, 8, 9, 9, 10, 10, 9, 9) (6, 9, 9, 10, 10, 9, 9, 8, 8, 5, 5, 3)
(9, 9, 8) (12, 10, 10)
(10, 11, 11, 12, 12, 13, 13, 14, 14) (5, 5, 4, 4, 5, 5, 4, 4, 2)
(11, 12, 12, 15, 15, 13, 13, 11, 11, 10, 10) (5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 8)
(14, 15, 15) (4, 4, 6)
(14, 14, 13, 13, 13) (7, 9, 9, 11, 13)
(14, 16, 16, 15, 15, 14, 14, 13) (8, 8, 10, 10, 11, 11, 12, 12)
(15, 16, 16) (11, 11, 13)
(17, 17, 18, 18, 15) (1, 3, 3, 6, 6)
(19, 19, 21, 21, 22, 22, 19) (2, 4, 4, 3, 3, 2, 2)
(18, 20, 20) (5, 5, 6)
(16, 18, 18, 19, 19, 20, 20) (9, 9, 8, 8, 9, 9, 10)
"""


# target_data는 .csv 파일의 카테고리
# blocked_map은 pandas DataFrame
# d1
# d2
# cmapname: color map name
def drawKorea(target_data, blocked_map, d1, d2, cmapname):

    vmin = min(blocked_map[target_data])  # target_data의 최소값 (인구수가 가장 적은 값)
    vmax = max(blocked_map[target_data])  # target_data의 최대값 (인구수가 가장 많은 값)
    white_label_min = (vmax - vmin) * 0.25 + vmin

    # .csv에서 받아온 정보에서 사용하기 좋게 pivot
    map_data = blocked_map.pivot(index='y', columns='x', values=target_data)

    # np.isnan(map_data)는 Nan이면 True, 나머지는 False 리턴해주고
    # 이것을 바탕으로 마스킹 배열 생성
    masked_mapdata = np.ma.masked_where(condition=np.isnan(map_data), a=map_data, copy=True)  # numpy masked array

    plt.figure(figsize=(8, 13))  # width, height tuple in inches

    # create a pseudocolor plot of a 2-D array.
    # plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)
    plt.pcolormesh(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)

    # 지역 이름 표시
    for idx, row in blocked_map.iterrows():  # rows에 대한 반복 처리
        # 인구수: row[target_data]
        annocolor = 'white' if row[target_data] > white_label_min else 'black'

        # 광역시도: row[d1]
        # 행정구역: row[d2]

        # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. (중구, 서구)
        # XX시로 끝나지만 세종시가 아닌 것들만 예외처리
        if row[d1].endswith('시') and not row[d1].startswith('세종'):
            # row[d1] : 서울특별시, 부산광역시...  row[d1][:2] : 서울, 부산...
            # row[d2] : 서대문구, 서초구, 중구 ... row[d2][:-1] : 서대문, 서초, 중 ...
            dispname = '{}\n{}'.format(row[d1][:2], row[d2][:-1])
            if len(row[d2]) <= 2:
                # 중, 서, ... -> 중구, 서구, ...
                dispname += row[d2][-1]
        else:
            # 제주특별자치도, 전라남도, 경상북도, ...
            dispname = row[d2][:-1]

        # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
        if len(dispname.splitlines()[-1]) >= 3:
            fontsize, linespacing = 9.5, 1.5
        else:
            fontsize, linespacing = 11, 1.2

        # '서울/n강남'에 대한 annotating
        plt.annotate(s=dispname,
                     xy=(row['x'] + 0.5, row['y'] + 0.5),
                     fontweight='bold', fontsize=fontsize,
                     horizontalalignment='center',
                     verticalalignment='center',
                     color=annocolor,
                     linespacing=linespacing)

    for path in BORDER_LINES:
        ys, xs = zip(*path)
        # plot xs, ys
        plt.plot(xs, ys, color='black', linewidth=4)

    plt.gca().invert_yaxis()  # x, y 뒤집어야 함
    plt.gca().set_aspect(aspect='equal')

    plt.axis('off')

    # 우측에 컬러바를 통해서 색상에 따라 수치를 파악할 수 있음
    # shirink: 컬러바의 전반적인 크기 조절
    # aspect: 컬러바의 폭 조절
    cb = plt.colorbar(shrink=0.1, aspect=10)
    cb.set_label(label=target_data)

    plt.tight_layout()
    plt.show()


def main():
    plt.rcParams["font.family"] = "AppleGothic"  # font setting

    # http://en.wikipedia.org/wiki/Plus_and_minus_signs#Character_codes
    plt.rcParams['axes.unicode_minus'] = False  # use hypen '-' (True: use unicode minus)

    data_draw_korea = pd.read_csv('./data_draw_korea.csv', index_col=0, encoding='UTF-8')
    data_draw_korea.head()  # return first row

    drawKorea('인구수', data_draw_korea, '광역시도', '행정구역', 'Blues')


if __name__ == '__main__':
    main()
