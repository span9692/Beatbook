from app.models import db, Like

def seed_likes():
    post1 = Like(user_id=2, post_id=1)
    post2 = Like(user_id=13, post_id=1)
    post3 = Like(user_id=4, post_id=1)
    post4 = Like(user_id=2, post_id=2)
    post5 = Like(user_id=13, post_id=2)
    post6 = Like(user_id=12, post_id=2)
    post7 = Like(user_id=8, post_id=2)
    post8 = Like(user_id=13, post_id=2)
    post9 = Like(user_id=7, post_id=3)
    post10 = Like(user_id=8, post_id=3)
    post11 = Like(user_id=9, post_id=3)
    post12 = Like(user_id=10, post_id=3)
    post13 = Like(user_id=11, post_id=3)
    post14 = Like(user_id=12, post_id=3)
    post15 = Like(user_id=13, post_id=3)
    post16 = Like(user_id=14, post_id=3)
    post17 = Like(user_id=12, post_id=4)
    post18 = Like(user_id=15, post_id=4)
    post19 = Like(user_id=16, post_id=5)
    post20 = Like(user_id=17, post_id=5)
    post21 = Like(user_id=16, post_id=6)
    post22 = Like(user_id=15, post_id=6)
    post23 = Like(user_id=14, post_id=6)
    post24 = Like(user_id=13, post_id=7)
    post25 = Like(user_id=12, post_id=8)
    post26 = Like(user_id=11, post_id=8)
    post27 = Like(user_id=10, post_id=8)
    post28 = Like(user_id=9, post_id=9)
    post29 = Like(user_id=8, post_id=9)
    post30 = Like(user_id=7, post_id=10)
    post31 = Like(user_id=8, post_id=11)
    post32 = Like(user_id=7, post_id=11)
    post33 = Like(user_id=6, post_id=11)
    post34 = Like(user_id=17, post_id=12)
    post35 = Like(user_id=14, post_id=12)
    post36 = Like(user_id=9, post_id=13)
    post37 = Like(user_id=15, post_id=14)
    post38 = Like(user_id=16, post_id=14)
    post39 = Like(user_id=2, post_id=15)
    post40 = Like(user_id=7, post_id=16)
    post41 = Like(user_id=9, post_id=16)
    post42 = Like(user_id=9, post_id=17)
    post43 = Like(user_id=7, post_id=17)
    post44 = Like(user_id=12, post_id=18)
    post45 = Like(user_id=13, post_id=19)
    post46 = Like(user_id=14, post_id=19)
    post47 = Like(user_id=15, post_id=19)
    post48 = Like(user_id=16, post_id=20)
    post49 = Like(user_id=17, post_id=20)
    post50 = Like(user_id=6, post_id=21)
    post51 = Like(user_id=8, post_id=22)
    post52 = Like(user_id=17, post_id=22)
    post53 = Like(user_id=7, post_id=23)
    post54 = Like(user_id=3, post_id=23)
    post55 = Like(user_id=11, post_id=24)
    post56 = Like(user_id=11, post_id=25)
    post57 = Like(user_id=18, post_id=25)
    post58 = Like(user_id=8, post_id=26)
    post59 = Like(user_id=14, post_id=27)
    post60 = Like(user_id=6, post_id=27)
    post61 = Like(user_id=9, post_id=28)
    post62 = Like(user_id=10, post_id=28)
    post63 = Like(user_id=11, post_id=28)
    post64 = Like(user_id=12, post_id=28)
    post65 = Like(user_id=13, post_id=28)
    post66 = Like(user_id=14, post_id=28)
    post67 = Like(user_id=3, post_id=29)
    post68 = Like(user_id=18, post_id=30)
    post69 = Like(user_id=7, post_id=30)
    post70 = Like(user_id=6, post_id=30)
    post71 = Like(user_id=4, post_id=30)
    post72 = Like(user_id=3, post_id=31)
    post73 = Like(user_id=4, post_id=31)
    post74 = Like(user_id=6, post_id=32)
    post75 = Like(user_id=9, post_id=32)
    post76 = Like(user_id=4, post_id=33)
    post77 = Like(user_id=14, post_id=33)
    post78 = Like(user_id=14, post_id=34)
    post79 = Like(user_id=16, post_id=34)
    post80 = Like(user_id=5, post_id=35)
    post81 = Like(user_id=17, post_id=36)
    post82 = Like(user_id=11, post_id=37)
    post83 = Like(user_id=13, post_id=37)
    post84 = Like(user_id=14, post_id=38)
    post85 = Like(user_id=3, post_id=38)
    post86 = Like(user_id=14, post_id=39)
    post87 = Like(user_id=4, post_id=39)
    post88= Like(user_id=14, post_id=40)
    post89 = Like(user_id=12, post_id=40)
    post90 = Like(user_id=15, post_id=40)
    post91 = Like(user_id=16, post_id=41)
    post92 = Like(user_id=11, post_id=41)
    post93 = Like(user_id=5, post_id=42)
    post94 = Like(user_id=16, post_id=43)
    post95 = Like(user_id=18, post_id=43)
    post96 = Like(user_id=4, post_id=44)
    post97 = Like(user_id=16, post_id=45)
    post98 = Like(user_id=11, post_id=45)
    post99 = Like(user_id=2, post_id=46)
    post100 = Like(user_id=17, post_id=46)
    post101 = Like(user_id=16, post_id=46)
    post102 = Like(user_id=3, post_id=47)
    post103 = Like(user_id=2, post_id=47)
    post104 = Like(user_id=1, post_id=47)
    post105 = Like(user_id=3, post_id=48)
    post106 = Like(user_id=12, post_id=48)
    post107 = Like(user_id=17, post_id=48)
    post108 = Like(user_id=16, post_id=49)
    post109 = Like(user_id=15, post_id=49)
    post110 = Like(user_id=15, post_id=50)
    post111 = Like(user_id=2, post_id=51)
    post112 = Like(user_id=3, post_id=51)
    post113 = Like(user_id=5, post_id=51)
    post114 = Like(user_id=6, post_id=52)
    post115 = Like(user_id=8, post_id=53)
    post116 = Like(user_id=17, post_id=54)
    post117 = Like(user_id=15, post_id=55)
    post118 = Like(user_id=12, post_id=55)
    post119 = Like(user_id=15, post_id=56)
    post120 = Like(user_id=14, post_id=56)
    post121 = Like(user_id=13, post_id=56)
    post122 = Like(user_id=12, post_id=56)
    post123 = Like(user_id=11, post_id=56)
    post124 = Like(user_id=10, post_id=56)
    post125 = Like(user_id=12, post_id=57)
    post126 = Like(user_id=15, post_id=57)
    post127 = Like(user_id=18, post_id=58)
    post128 = Like(user_id=17, post_id=58)
    post129 = Like(user_id=1, post_id=59)
    post130 = Like(user_id=3, post_id=59)
    post131 = Like(user_id=4, post_id=60)
    post132 = Like(user_id=13, post_id=61)
    post133 = Like(user_id=14, post_id=61)
    post134 = Like(user_id=2, post_id=62)
    post135 = Like(user_id=12, post_id=63)
    post136 = Like(user_id=13, post_id=63)
    post137 = Like(user_id=12, post_id=64)
    post138 = Like(user_id=17, post_id=65)
    post139 = Like(user_id=16, post_id=65)
    post140 = Like(user_id=15, post_id=65)
    post141 = Like(user_id=1, post_id=66)
    post142 = Like(user_id=15, post_id=66)
    post143 = Like(user_id=7, post_id=67)
    post144 = Like(user_id=17, post_id=68)
    post145 = Like(user_id=15, post_id=69)
    post146 = Like(user_id=14, post_id=69)
    post147 = Like(user_id=13, post_id=69)
    post148 = Like(user_id=12, post_id=69)
    post149 = Like(user_id=11, post_id=69)
    post150 = Like(user_id=18, post_id=70)
    post151 = Like(user_id=5, post_id=71)
    post152 = Like(user_id=6, post_id=71)
    post153 = Like(user_id=4, post_id=72)
    post154 = Like(user_id=3, post_id=73)
    post155 = Like(user_id=2, post_id=73)
    post156 = Like(user_id=17, post_id=74)
    post157 = Like(user_id=11, post_id=75)
    post158 = Like(user_id=10, post_id=75)
    post159 = Like(user_id=3, post_id=75)
    post160 = Like(user_id=4, post_id=76)
    post161 = Like(user_id=6, post_id=77)
    post162 = Like(user_id=10, post_id=77)
    post163 = Like(user_id=14, post_id=77)
    post164 = Like(user_id=3, post_id=78)
    post165 = Like(user_id=1, post_id=79)
    post166 = Like(user_id=14, post_id=79)
    post167 = Like(user_id=10, post_id=79)
    post168 = Like(user_id=4, post_id=80)
    post169 = Like(user_id=5, post_id=80)
    post170 = Like(user_id=10, post_id=80)
    post171 = Like(user_id=11, post_id=80)
    post172 = Like(user_id=13, post_id=80)
    post173 = Like(user_id=17, post_id=80)
    post174 = Like(user_id=17, post_id=81)
    post175 = Like(user_id=15, post_id=81)
    post176 = Like(user_id=6, post_id=81)
    post177 = Like(user_id=6, post_id=82)
    post178 = Like(user_id=7, post_id=82)
    post179 = Like(user_id=18, post_id=82)
    post180 = Like(user_id=11, post_id=83)
    post181 = Like(user_id=2, post_id=83)
    post182 = Like(user_id=5, post_id=83)
    post183 = Like(user_id=17, post_id=83)








    comment1 = Like(user_id=6, comment_id=1)
    comment2 = Like(user_id=7, comment_id=1)
    comment3 = Like(user_id=4, comment_id=5)
    comment4 = Like(user_id=6, comment_id=6)
    comment5 = Like(user_id=5, comment_id=7)
    comment6 = Like(user_id=6, comment_id=8)
    comment7 = Like(user_id=4, comment_id=8)
    comment8 = Like(user_id=8, comment_id=8)
    comment9 = Like(user_id=9, comment_id=8)
    comment10 = Like(user_id=5, comment_id=9)
    comment11 = Like(user_id=6, comment_id=9)
    comment12 = Like(user_id=10, comment_id=9)
    comment13 = Like(user_id=7, comment_id=9)
    comment14 = Like(user_id=8, comment_id=9)
    comment15 = Like(user_id=13, comment_id=10)
    comment16 = Like(user_id=11, comment_id=10)
    comment17 = Like(user_id=18, comment_id=11)
    comment18 = Like(user_id=7, comment_id=12)
    comment19 = Like(user_id=16, comment_id=14)
    comment20 = Like(user_id=17, comment_id=14)
    comment21 = Like(user_id=11, comment_id=14)
    comment22 = Like(user_id=7, comment_id=15)
    comment23 = Like(user_id=6, comment_id=16)
    comment24 = Like(user_id=16, comment_id=18)
    comment25 = Like(user_id=18, comment_id=20)
    comment26 = Like(user_id=11, comment_id=20)
    comment27 = Like(user_id=10, comment_id=20)
    comment28 = Like(user_id=3, comment_id=20)
    comment29 = Like(user_id=10, comment_id=20)
    comment30 = Like(user_id=2, comment_id=23)
    comment31 = Like(user_id=3, comment_id=23)
    comment32 = Like(user_id=4, comment_id=23)
    comment33 = Like(user_id=10, comment_id=25)
    comment34 = Like(user_id=11, comment_id=26)
    comment35 = Like(user_id=18, comment_id=26)
    comment36 = Like(user_id=10, comment_id=29)
    comment37 = Like(user_id=16, comment_id=29)
    comment38= Like(user_id=15, comment_id=29)
    comment39 = Like(user_id=10, comment_id=31)
    comment40 = Like(user_id=12, comment_id=33)
    comment41 = Like(user_id=16, comment_id=34)
    comment42 = Like(user_id=5, comment_id=36)
    comment43 = Like(user_id=6, comment_id=36)
    comment44 = Like(user_id=11, comment_id=38)
    comment45 = Like(user_id=12, comment_id=39)
    comment46 = Like(user_id=12, comment_id=40)
    comment47 = Like(user_id=10, comment_id=42)
    comment48 = Like(user_id=17, comment_id=43)
    comment49 = Like(user_id=18, comment_id=43)
    comment50 = Like(user_id=12, comment_id=44)
    comment51 = Like(user_id=10, comment_id=45)
    comment52 = Like(user_id=12, comment_id=48)
    comment53 = Like(user_id=14, comment_id=48)
    comment54 = Like(user_id=10, comment_id=48)
    comment55 = Like(user_id=2, comment_id=49)
    comment56 = Like(user_id=3, comment_id=49)
    comment57 = Like(user_id=12, comment_id=52)
    comment58 = Like(user_id=5, comment_id=53)
    comment59 = Like(user_id=6, comment_id=53)
    comment60 = Like(user_id=7, comment_id=54)
    comment61 = Like(user_id=17, comment_id=57)
    comment62 = Like(user_id=15, comment_id=57)
    comment63 = Like(user_id=3, comment_id=62)
    comment64 = Like(user_id=4, comment_id=62)
    comment65 = Like(user_id=7, comment_id=63)
    comment66 = Like(user_id=8, comment_id=63)
    comment67 = Like(user_id=9, comment_id=63)
    comment68 = Like(user_id=15, comment_id=64)
    comment69 = Like(user_id=12, comment_id=64)
    comment70 = Like(user_id=7, comment_id=65)
    comment71 = Like(user_id=11, comment_id=66)
    comment72 = Like(user_id=12, comment_id=67)
    comment73 = Like(user_id=17, comment_id=68)
    comment74 = Like(user_id=12, comment_id=68)
    comment75 = Like(user_id=11, comment_id=68)
    comment76 = Like(user_id=7, comment_id=70)
    comment77 = Like(user_id=3, comment_id=71)
    comment78 = Like(user_id=13, comment_id=72)
    comment79 = Like(user_id=14, comment_id=73)
    comment80 = Like(user_id=4, comment_id=73)
    comment81 = Like(user_id=18, comment_id=73)
    comment82 = Like(user_id=3, comment_id=74)
    comment83 = Like(user_id=18, comment_id=75)
    comment84 = Like(user_id=10, comment_id=75)
    comment85 = Like(user_id=3, comment_id=77)
    comment86 = Like(user_id=10, comment_id=79)
    comment87 = Like(user_id=8, comment_id=79)
    comment88 = Like(user_id=7, comment_id=79)
    comment89 = Like(user_id=2, comment_id=81)
    comment90 = Like(user_id=3, comment_id=81)
    comment91 = Like(user_id=5, comment_id=82)
    comment92 = Like(user_id=6, comment_id=82)
    comment93 = Like(user_id=11, comment_id=83)
    comment94 = Like(user_id=12, comment_id=83)
    comment95 = Like(user_id=16, comment_id=84)
    comment96 = Like(user_id=17, comment_id=84)
    comment97 = Like(user_id=3, comment_id=86)
    comment98 = Like(user_id=15, comment_id=89)
    comment99 = Like(user_id=14, comment_id=89)
    comment100 = Like(user_id=12, comment_id=89)
    comment101 = Like(user_id=9, comment_id=91)
    comment102 = Like(user_id=7, comment_id=91)
    comment103 = Like(user_id=3, comment_id=94)
    comment104 = Like(user_id=6, comment_id=94)
    comment105 = Like(user_id=10, comment_id=94)
    comment106 = Like(user_id=11, comment_id=96)
    comment107 = Like(user_id=17, comment_id=96)
    comment108 = Like(user_id=3, comment_id=97)
    comment109 = Like(user_id=6, comment_id=97)
    comment110 = Like(user_id=13, comment_id=101)
    comment111 = Like(user_id=14, comment_id=101)
    comment112 = Like(user_id=15, comment_id=101)
    comment113 = Like(user_id=16, comment_id=101)
    comment114 = Like(user_id=17, comment_id=101)
    comment115 = Like(user_id=4, comment_id=101)
    comment116 = Like(user_id=17, comment_id=103)
    comment117 = Like(user_id=17, comment_id=104)
    comment118 = Like(user_id=11, comment_id=104)
    comment119 = Like(user_id=10, comment_id=104)
    comment120 = Like(user_id=8, comment_id=104)
    comment121 = Like(user_id=2, comment_id=105)
    comment122 = Like(user_id=9, comment_id=105)
    comment123 = Like(user_id=8, comment_id=106)
    comment124 = Like(user_id=18, comment_id=106)
    comment125 = Like(user_id=16, comment_id=106)
    comment126 = Like(user_id=15, comment_id=106)
    comment127 = Like(user_id=8, comment_id=107)
    comment128 = Like(user_id=8, comment_id=108)
    comment129 = Like(user_id=9, comment_id=108)
    comment130 = Like(user_id=8, comment_id=109)
    comment131 = Like(user_id=18, comment_id=109)
    comment132 = Like(user_id=9, comment_id=109)
    comment133 = Like(user_id=8, comment_id=110)
    comment134 = Like(user_id=18, comment_id=112)
    comment135 = Like(user_id=16, comment_id=112)
    comment136 = Like(user_id=14, comment_id=112)
    comment137 = Like(user_id=12, comment_id=112)
    comment138 = Like(user_id=8, comment_id=114)
    comment139 = Like(user_id=10, comment_id=114)
    comment140 = Like(user_id=4, comment_id=114)
    comment141 = Like(user_id=3, comment_id=114)
    comment142 = Like(user_id=2, comment_id=114)
    comment143 = Like(user_id=16, comment_id=114)
    comment144 = Like(user_id=18, comment_id=114)
    comment145 = Like(user_id=17, comment_id=114)
    comment146 = Like(user_id=15, comment_id=114)
    comment147 = Like(user_id=14, comment_id=114)
    comment148 = Like(user_id=13, comment_id=115)
    comment149 = Like(user_id=18, comment_id=116)
    comment150 = Like(user_id=3, comment_id=116)
    comment151 = Like(user_id=9, comment_id=116)
    comment152 = Like(user_id=9, comment_id=117)
    comment153 = Like(user_id=16, comment_id=117)






    db.session.add(post1)
    db.session.add(post2)
    db.session.add(post3)
    db.session.add(post4)
    db.session.add(post5)
    db.session.add(post6)
    db.session.add(post7)
    db.session.add(post8)
    db.session.add(post9)
    db.session.add(post10)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post13)
    db.session.add(post14)
    db.session.add(post15)
    db.session.add(post16)
    db.session.add(post17)
    db.session.add(post18)
    db.session.add(post19)
    db.session.add(post20)
    db.session.add(post21)
    db.session.add(post22)
    db.session.add(post23)
    db.session.add(post24)
    db.session.add(post25)
    db.session.add(post26)
    db.session.add(post27)
    db.session.add(post28)
    db.session.add(post29)
    db.session.add(post30)
    db.session.add(post31)
    db.session.add(post32)
    db.session.add(post33)
    db.session.add(post34)
    db.session.add(post35)
    db.session.add(post36)
    db.session.add(post37)
    db.session.add(post38)
    db.session.add(post39)
    db.session.add(post40)
    db.session.add(post41)
    db.session.add(post42)
    db.session.add(post43)
    db.session.add(post44)
    db.session.add(post45)
    db.session.add(post46)
    db.session.add(post47)
    db.session.add(post48)
    db.session.add(post49)
    db.session.add(post50)
    db.session.add(post51)
    db.session.add(post52)
    db.session.add(post53)
    db.session.add(post54)
    db.session.add(post55)
    db.session.add(post56)
    db.session.add(post57)
    db.session.add(post58)
    db.session.add(post59)
    db.session.add(post60)
    db.session.add(post61)
    db.session.add(post62)
    db.session.add(post63)
    db.session.add(post64)
    db.session.add(post65)
    db.session.add(post66)
    db.session.add(post67)
    db.session.add(post68)
    db.session.add(post69)
    db.session.add(post70)
    db.session.add(post71)
    db.session.add(post72)
    db.session.add(post73)
    db.session.add(post74)
    db.session.add(post75)
    db.session.add(post76)
    db.session.add(post77)
    db.session.add(post78)
    db.session.add(post79)
    db.session.add(post80)
    db.session.add(post81)
    db.session.add(post82)
    db.session.add(post83)
    db.session.add(post84)
    db.session.add(post85)
    db.session.add(post86)
    db.session.add(post87)
    db.session.add(post88)
    db.session.add(post89)
    db.session.add(post104)
    db.session.add(post91)
    db.session.add(post92)
    db.session.add(post93)
    db.session.add(post94)
    db.session.add(post95)
    db.session.add(post96)
    db.session.add(post97)
    db.session.add(post98)
    db.session.add(post99)
    db.session.add(post100)
    db.session.add(post101)
    db.session.add(post102)
    db.session.add(post103)
    db.session.add(post90)
    db.session.add(post105)
    db.session.add(post106)
    db.session.add(post107)
    db.session.add(post108)
    db.session.add(post109)
    db.session.add(post100)
    db.session.add(post101)
    db.session.add(post102)
    db.session.add(post103)
    db.session.add(post104)
    db.session.add(post105)
    db.session.add(post106)
    db.session.add(post107)
    db.session.add(post108)
    db.session.add(post109)
    db.session.add(post110)
    db.session.add(post111)
    db.session.add(post112)
    db.session.add(post113)
    db.session.add(post114)
    db.session.add(post115)
    db.session.add(post116)
    db.session.add(post117)
    db.session.add(post118)
    db.session.add(post119)
    db.session.add(post120)
    db.session.add(post121)
    db.session.add(post122)
    db.session.add(post123)
    db.session.add(post124)
    db.session.add(post125)
    db.session.add(post126)
    db.session.add(post127)
    db.session.add(post128)
    db.session.add(post129)
    db.session.add(post130)
    db.session.add(post131)
    db.session.add(post132)
    db.session.add(post133)
    db.session.add(post134)
    db.session.add(post135)
    db.session.add(post136)
    db.session.add(post137)
    db.session.add(post138)
    db.session.add(post139)
    db.session.add(post140)
    db.session.add(post141)
    db.session.add(post142)
    db.session.add(post143)
    db.session.add(post144)
    db.session.add(post145)
    db.session.add(post146)
    db.session.add(post147)
    db.session.add(post148)
    db.session.add(post149)
    db.session.add(post150)
    db.session.add(post151)
    db.session.add(post152)
    db.session.add(post153)
    db.session.add(post154)
    db.session.add(post155)
    db.session.add(post156)
    db.session.add(post157)
    db.session.add(post158)
    db.session.add(post159)
    db.session.add(post160)
    db.session.add(post161)
    db.session.add(post162)
    db.session.add(post163)
    db.session.add(post164)
    db.session.add(post165)
    db.session.add(post166)
    db.session.add(post167)
    db.session.add(post168)
    db.session.add(post169)
    db.session.add(post170)
    db.session.add(post171)
    db.session.add(post172)
    db.session.add(post173)
    db.session.add(post174)
    db.session.add(post175)
    db.session.add(post176)
    db.session.add(post177)
    db.session.add(post178)
    db.session.add(post179)
    db.session.add(post180)
    db.session.add(post181)
    db.session.add(post182)
    db.session.add(post183)


    db.session.add(comment1)
    db.session.add(comment2)
    db.session.add(comment3)
    db.session.add(comment4)
    db.session.add(comment5)
    db.session.add(comment6)
    db.session.add(comment7)
    db.session.add(comment8)
    db.session.add(comment9)
    db.session.add(comment10)
    db.session.add(comment11)
    db.session.add(comment12)
    db.session.add(comment13)
    db.session.add(comment14)
    db.session.add(comment15)
    db.session.add(comment16)
    db.session.add(comment17)
    db.session.add(comment18)
    db.session.add(comment19)
    db.session.add(comment20)
    db.session.add(comment21)
    db.session.add(comment22)
    db.session.add(comment23)
    db.session.add(comment24)
    db.session.add(comment25)
    db.session.add(comment26)
    db.session.add(comment27)
    db.session.add(comment28)
    db.session.add(comment29)
    db.session.add(comment30)
    db.session.add(comment31)
    db.session.add(comment32)
    db.session.add(comment33)
    db.session.add(comment34)
    db.session.add(comment35)
    db.session.add(comment36)
    db.session.add(comment37)
    db.session.add(comment38)
    db.session.add(comment39)
    db.session.add(comment40)
    db.session.add(comment41)
    db.session.add(comment42)
    db.session.add(comment43)
    db.session.add(comment44)
    db.session.add(comment45)
    db.session.add(comment46)
    db.session.add(comment47)
    db.session.add(comment48)
    db.session.add(comment49)
    db.session.add(comment50)
    db.session.add(comment51)
    db.session.add(comment52)
    db.session.add(comment53)
    db.session.add(comment54)
    db.session.add(comment55)
    db.session.add(comment56)
    db.session.add(comment57)
    db.session.add(comment58)
    db.session.add(comment59)
    db.session.add(comment60)
    db.session.add(comment61)
    db.session.add(comment62)
    db.session.add(comment63)
    db.session.add(comment64)
    db.session.add(comment65)
    db.session.add(comment66)
    db.session.add(comment67)
    db.session.add(comment68)
    db.session.add(comment69)
    db.session.add(comment70)
    db.session.add(comment71)
    db.session.add(comment72)
    db.session.add(comment73)
    db.session.add(comment74)
    db.session.add(comment75)
    db.session.add(comment76)
    db.session.add(comment77)
    db.session.add(comment78)
    db.session.add(comment79)
    db.session.add(comment80)
    db.session.add(comment81)
    db.session.add(comment82)
    db.session.add(comment83)
    db.session.add(comment84)
    db.session.add(comment85)
    db.session.add(comment86)
    db.session.add(comment87)
    db.session.add(comment88)
    db.session.add(comment89)
    db.session.add(comment90)
    db.session.add(comment91)
    db.session.add(comment92)
    db.session.add(comment93)
    db.session.add(comment94)
    db.session.add(comment95)
    db.session.add(comment96)
    db.session.add(comment97)
    db.session.add(comment98)
    db.session.add(comment99)
    db.session.add(comment100)
    db.session.add(comment101)
    db.session.add(comment102)
    db.session.add(comment103)
    db.session.add(comment104)
    db.session.add(comment105)
    db.session.add(comment106)
    db.session.add(comment107)
    db.session.add(comment108)
    db.session.add(comment109)
    db.session.add(comment110)
    db.session.add(comment111)
    db.session.add(comment112)
    db.session.add(comment113)
    db.session.add(comment114)
    db.session.add(comment115)
    db.session.add(comment116)
    db.session.add(comment117)
    db.session.add(comment118)
    db.session.add(comment119)
    db.session.add(comment120)
    db.session.add(comment121)
    db.session.add(comment122)
    db.session.add(comment123)
    db.session.add(comment124)
    db.session.add(comment125)
    db.session.add(comment126)
    db.session.add(comment127)
    db.session.add(comment128)
    db.session.add(comment129)
    db.session.add(comment130)
    db.session.add(comment131)
    db.session.add(comment132)
    db.session.add(comment133)
    db.session.add(comment134)
    db.session.add(comment135)
    db.session.add(comment136)
    db.session.add(comment137)
    db.session.add(comment138)
    db.session.add(comment139)
    db.session.add(comment140)
    db.session.add(comment141)
    db.session.add(comment142)
    db.session.add(comment143)
    db.session.add(comment144)
    db.session.add(comment145)
    db.session.add(comment146)
    db.session.add(comment147)
    db.session.add(comment148)
    db.session.add(comment149)
    db.session.add(comment150)
    db.session.add(comment151)
    db.session.add(comment152)
    db.session.add(comment153)


    db.session.commit()


def undo_likes():
    db.session.execute('TRUNCATE likes RESTART IDENTITY CASCADE;')
    db.session.commit()
