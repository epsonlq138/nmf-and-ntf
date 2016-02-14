#!/usr/bins/python
# -*- coding:utf-8 -*-
'''
Created on 2015/08/03

@author: drumichiro
'''
from numpy import nan


LARGE_AREA = {"北海道": "0 北海道",
              "東北": "1 東北",
              "関東": "2 関東",
              "北信越": "3 北信越",
              "東海": "4 東海",
              "関西": "5 関西",
              "中国": "6 中国",
              "四国": "7 四国",
              "九州・沖縄": "8 九州・沖縄"}


PREFECTURE = {"北海道": "00 北海道",
              "青森県": "01 青森県",
              "岩手県": "02 岩手県",
              "宮城県": "03 宮城県",
              "秋田県": "04 秋田県",
              "山形県": "05 山形県",
              "福島県": "06 福島県",
              "茨城県": "07 茨城県",
              "栃木県": "08 栃木県",
              "群馬県": "09 群馬県",
              "埼玉県": "10 埼玉県",
              "千葉県": "11 千葉県",
              "東京都": "12 東京都",
              "神奈川県": "13 神奈川県",
              "新潟県": "14 新潟県",
              "富山県": "15 富山県",
              "石川県": "16 石川県",
              "福井県": "17 福井県",
              "山梨県": "18 山梨県",
              "長野県": "19 長野県",
              "岐阜県": "20 岐阜県",
              "静岡県": "21 静岡県",
              "愛知県": "22 愛知県",
              "三重県": "23 三重県",
              "滋賀県": "24 滋賀県",
              "京都府": "25 京都府",
              "大阪府": "26 大阪府",
              "兵庫県": "27 兵庫県",
              "奈良県": "28 奈良県",
              "和歌山県": "29 和歌山県",
              "鳥取県": "30 鳥取県",
              "島根県": "31 島根県",
              "岡山県": "32 岡山県",
              "広島県": "33 広島県",
              "山口県": "34 山口県",
              "徳島県": "35 徳島県",
              "香川県": "36 香川県",
              "愛媛県": "37 愛媛県",
              "高知県": "38 高知県",
              "福岡県": "39 福岡県",
              "佐賀県": "40 佐賀県",
              "長崎県": "41 長崎県",
              "熊本県": "42 熊本県",
              "大分県": "43 大分県",
              "宮崎県": "44 宮崎県",
              "鹿児島県": "45 鹿児島県",
              "沖縄県": "46 沖縄県",
              "無登録": "47 無登録",
              nan: "47 無登録"}


SMALL_AREA = {"北海道": "00 北海道",
              "青森": "01 青森",
              "岩手": "02 岩手",
              "宮城": "03 宮城",
              "秋田": "04 秋田",
              "山形": "05 山形",
              "福島": "06 福島",
              "茨城": "07 茨城",
              "栃木": "08 栃木",
              "群馬": "09 群馬",
              "埼玉": "10 埼玉",
              "千葉": "11 千葉",
              "新宿・高田馬場・中野・吉祥寺": "12 新宿・高田馬場・中野・吉祥寺",
              "恵比寿・目黒・品川": "13 恵比寿・目黒・品川",
              "銀座・新橋・東京・上野": "14 銀座・新橋・東京・上野",
              "渋谷・青山・自由が丘": "15 渋谷・青山・自由が丘",
              "池袋・神楽坂・赤羽": "16 池袋・神楽坂・赤羽",
              "赤坂・六本木・麻布": "17 赤坂・六本木・麻布",
              "立川・町田・八王子他": "18 立川・町田・八王子他",
              "川崎・湘南・箱根他": "19 川崎・湘南・箱根他",
              "横浜": "20 横浜",
              "新潟": "21 新潟",
              "富山": "22 富山",
              "石川": "23 石川",
              "福井": "24 福井",
              "山梨": "25 山梨",
              "長野": "26 長野",
              "岐阜": "27 岐阜",
              "静岡": "28 静岡",
              "愛知": "29 愛知",
              "三重": "30 三重",
              "滋賀": "31 滋賀",
              "京都": "32 京都",
              "キタ": "33 キタ",
              "ミナミ他": "34 ミナミ他",
              "兵庫": "35 兵庫",
              "奈良": "36 奈良",
              "和歌山": "37 和歌山",
              "鳥取": "38 鳥取",
              "島根": "39 島根",
              "岡山": "40 岡山",
              "広島": "41 広島",
              "山口": "42 山口",
              "徳島": "43 徳島",
              "香川": "44 香川",
              "愛媛": "45 愛媛",
              "高知": "46 高知",
              "福岡": "47 福岡",
              "佐賀": "48 佐賀",
              "長崎": "49 長崎",
              "熊本": "50 熊本",
              "大分": "51 大分",
              "宮崎": "52 宮崎",
              "鹿児島": "53 鹿児島",
              "沖縄": "54 沖縄"}


PREFECTURE_TO_LARGE_AREA = \
    {"北海道": "北海道",
     "青森県": "東北",
     "岩手県": "東北",
     "宮城県": "東北",
     "秋田県": "東北",
     "山形県": "東北",
     "福島県": "東北",
     "茨城県": "関東",
     "栃木県": "関東",
     "群馬県": "関東",
     "埼玉県": "関東",
     "千葉県": "関東",
     "東京都": "関東",
     "神奈川県": "関東",
     "新潟県": "北信越",
     "富山県": "北信越",
     "石川県": "北信越",
     "福井県": "北信越",
     "山梨県": "北信越",
     "長野県": "北信越",
     "岐阜県": "東海",
     "静岡県": "東海",
     "愛知県": "東海",
     "三重県": "東海",
     "滋賀県": "関西",
     "京都府": "関西",
     "大阪府": "関西",
     "兵庫県": "関西",
     "奈良県": "関西",
     "和歌山県": "関西",
     "鳥取県": "中国",
     "島根県": "中国",
     "岡山県": "中国",
     "広島県": "中国",
     "山口県": "中国",
     "徳島県": "四国",
     "香川県": "四国",
     "愛媛県": "四国",
     "高知県": "四国",
     "福岡県": "九州・沖縄",
     "佐賀県": "九州・沖縄",
     "長崎県": "九州・沖縄",
     "熊本県": "九州・沖縄",
     "大分県": "九州・沖縄",
     "宮崎県": "九州・沖縄",
     "鹿児島県": "九州・沖縄",
     "沖縄県": "九州・沖縄",
     "無登録": "無登録"}


PREFECTURE_TO_SMALL_AREA = \
    {"北海道": "北海道",
     "青森県": "青森",
     "岩手県": "岩手",
     "宮城県": "宮城",
     "秋田県": "秋田",
     "山形県": "山形",
     "福島県": "福島",
     "茨城県": "茨城",
     "栃木県": "栃木",
     "群馬県": "群馬",
     "埼玉県": "埼玉",
     "千葉県": "千葉",
     "東京都": "新宿・高田馬場・中野・吉祥寺",
     "神奈川県": "横浜",
     "新潟県": "新潟",
     "富山県": "富山",
     "石川県": "石川",
     "福井県": "福井",
     "山梨県": "山梨",
     "長野県": "長野",
     "岐阜県": "岐阜",
     "静岡県": "静岡",
     "愛知県": "愛知",
     "三重県": "三重",
     "滋賀県": "滋賀",
     "京都府": "京都",
     "大阪府": "キタ",
     "兵庫県": "兵庫",
     "奈良県": "奈良",
     "和歌山県": "和歌山",
     "鳥取県": "鳥取",
     "島根県": "島根",
     "岡山県": "岡山",
     "広島県": "広島",
     "山口県": "山口",
     "徳島県": "徳島",
     "香川県": "香川",
     "愛媛県": "愛媛",
     "高知県": "高知",
     "福岡県": "福岡",
     "佐賀県": "佐賀",
     "長崎県": "長崎",
     "熊本県": "熊本",
     "大分県": "大分",
     "宮崎県": "宮崎",
     "鹿児島県": "鹿児島",
     "沖縄県": "沖縄",
     "無登録": "無登録"}


SMALL_AREA_TO_PREFECTURE = \
    {"北海道": "北海道",
     "青森": "青森県",
     "岩手": "岩手県",
     "宮城": "宮城県",
     "秋田": "秋田県",
     "山形": "山形県",
     "福島": "福島県",
     "茨城": "茨城県",
     "栃木": "栃木県",
     "群馬": "群馬県",
     "埼玉": "埼玉県",
     "千葉": "千葉県",
     "新宿・高田馬場・中野・吉祥寺": "東京都",
     "恵比寿・目黒・品川": "東京都",
     "銀座・新橋・東京・上野": "東京都",
     "渋谷・青山・自由が丘": "東京都",
     "池袋・神楽坂・赤羽": "東京都",
     "赤坂・六本木・麻布": "東京都",
     "立川・町田・八王子他": "東京都",
     "川崎・湘南・箱根他": "神奈川県",
     "横浜": "神奈川県",
     "新潟": "新潟県",
     "富山": "富山県",
     "石川": "石川県",
     "福井": "福井県",
     "山梨": "山梨県",
     "長野": "長野県",
     "岐阜": "岐阜県",
     "静岡": "静岡県",
     "愛知": "愛知県",
     "三重": "三重県",
     "滋賀": "滋賀県",
     "京都": "京都府",
     "キタ": "大阪府",
     "ミナミ他": "大阪府",
     "兵庫": "兵庫県",
     "奈良": "奈良県",
     "和歌山": "和歌山県",
     "鳥取": "鳥取県",
     "島根": "島根県",
     "岡山": "岡山県",
     "広島": "広島県",
     "山口": "山口県",
     "徳島": "徳島県",
     "香川": "香川県",
     "愛媛": "愛媛県",
     "高知": "高知県",
     "福岡": "福岡県",
     "佐賀": "佐賀県",
     "長崎": "長崎県",
     "熊本": "熊本県",
     "大分": "大分県",
     "宮崎": "宮崎県",
     "鹿児島": "鹿児島県",
     "沖縄": "沖縄県",
     "無登録": "無登録"}


CAPSULE = {"グルメ": "00 グルメ",
           "エステ": "01 エステ",
           "ビューティ": "02 ビューティー",
           "ビューティー": "02 ビューティー",
           "ネイル・アイ": "03 ネイル・アイ",
           "ヘアサロン": "04 ヘアサロン",
           "健康・医療": "05 健康・医療",
           "リラクゼーション": "06 リラクゼーション",
           "レジャー": "07 レジャー",
           "貸別荘": "08 貸別荘",
           "ロッジ": "09 ロッジ",
           "ゲストハウス": "10 ゲストハウス",
           "ペンション": "11 ペンション",
           "公共の宿": "12 公共の宿",
           "民宿": "13 民宿",
           "旅館": "14 旅館",
           "ホテル": "15 ホテル ",
           "レッスン": "16 レッスン",
           "通信講座": "17 通信講座",
           "通学レッスン": "18 通学レッスン",
           "宅配": "19 宅配",
           "ギフトカード": "20 ギフトカード",
           "WEBサービス": "21 WEBサービス",
           "イベント": "22 イベント",
           "その他": "23 その他"}


GENRE = {"グルメ": "00 グルメ",
         "エステ": "01 エステ",
         "ビューティー": "02 ビューティー",
         "ネイル・アイ": "03 ネイル・アイ",
         "ヘアサロン": "04 ヘアサロン",
         "健康・医療": "05 健康・医療",
         "リラクゼーション": "06 リラクゼーション",
         "レジャー": "07 レジャー",
         "ホテル・旅館": "08 ホテル・旅館",
         "レッスン": "09 レッスン",
         "宅配": "10 宅配",
         "ギフトカード": "11 ギフトカード",
         "その他のクーポン": "12 その他のクーポン"}


SEX_TYPE = {"m": "00 男性", "f": "01 女性"}