import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','django_movie.settings')

import django
django.setup()
from myapp.models import ClassifyModel, MovieModel

def populate():
    
    comedy_movies = [
        {
            "id": 1,
            "name": "King of Comedy",
            "detail": "Yin Tianqiu (Zhou Xingchi) has been fascinated by drama and wants to be an actor. In addition to running a dragon, he will also set up an actor training class in the Kaifang Welfare Association. At this time, Miss Dance Liu fluttered in the leadership of Mama Sang and asked to learn to play. It turned out that Liu fluttering had a very unpleasant experience. In the process of Yin Tianqiu\u2019s guidance to her, Liu fluttering grew up against Yin Tianqiu. Feelings, she also became a popular lady in the nightclub. After Yin Tianqiu received a lot of white eyes, he finally got the appreciation of the big star sister (Mo Wenwei), carrying him to play the leading role in the new play, but did not expect to suddenly change his role and disappoint him. No. The identity of the undercover police officer (Wu Mengda) who was on the spot was recognized, and Yin Tianqiu\u2019s help was broken. After that, Yin Tianqiu continued to be active in the actor training class of the Kaifang Welfare Association.",
            "pic": "image/GGSJGP_QR7DZM1B13L.png",
            "actor": "Stephen Chow / Cecilia Cheung",
            "duration": 85,
            "star": 5,
            "publish_time": "1992-02-13T12:00:00Z",
            "create_time": "2019-03-14T22:06:53.899Z",
        },
        {
            "id": 6,
            "name": "Goodbye Mr.Loser",
            "detail": "In the wedding of the first love Qiu Ya (Wang Zhi ornaments) in the student era, after eating, the soft rice was eaten by his wife, Xialuo (Shen Teng), and he was full of ugliness. He was also married by his wife Ma Dongmei (Ma Li) Debunking temper. In the midst of chaos, Charlotte unexpectedly traveled through time and space and returned to the classroom of the 1997 student era. He ignorant, thought it was a dream of realism, so he screamed at Wang, kissed Qiuya, and tried to jump off the building to wake himself up. When the injured he woke up from his bed, he realized that he really crossed the time and space. Since there is a chance to come back, it is better to toss it back. He bravely pursued Qiu Ya, the fallen superior student Yuan Hua (Yin Zheng ornaments), and refused Ma Dongmei's stalker. Later, Charlotte entered the entertainment circle with the famous songs of \u201cCreating\u201d Pu Shu and Dou Wei.\r\nHis life has undergone tremendous changes, but somewhere in the heart, he feels more and more empty...",
            "pic": "image/5.png",
            "actor": "Shen Teng / Ma Li",
            "duration": 104,
            "star": 5,
            "publish_time": "2015-09-30T00:00:00Z",
            "create_time": "2019-03-14T22:32:54.008Z",
        },
        {
            "id": 10,
            "name": "Hello Mr. Billionaire",
            "detail": "Wang Duoyu (Shen Teng), the goalkeeper of the Xiangxiang team of Xihong City, was fired by the coach because of the loss of the game. Wang Duoyu suddenly received the invitation of the mysterious person Jin Bo (Zhang Chenguang) and was told that he was It turned out to be the sole heir to the insurance tycoon Wang Laotai (Li Liqun), with a legacy of up to 10 billion! However, Wang Laotai gave a very wonderful condition, that is, Wang Duoyu was asked to spend one billion yuan in a month, and he could not tell the people around him, otherwise he would lose the inheritance right. Wang Duoyu did not hesitate to sign the \"military order\", and together with his friend Zhuang Qiang (Zhang Yiming) and the financial Xiazhu (Song Yihua), he opened the \"golden journey\" and will soon become the richest man in Xihong City. For the first time, I felt the happiness of being a rich man. I also found that it is not so simple to spend money!",
            "pic": "image/91.jpeg",
            "actor": "Shen Teng / Song Yihua",
            "duration": 118,
            "star": 5,
            "publish_time": "2018-07-27T00:00:00Z",
            "create_time": "2019-03-14T22:40:21.423Z",
        },
    ]

    action_movies = [
        {
            "id": 3,
            "name": "Fast & Furious 7",
            "detail": "After a thrilling London war, Dominique Torreto (Van Diesel) and his friends returned to a peaceful life, but the grace and resentment of the rivers and lakes never allowed them to take it easy. . The tricky rival, Owen Shaw, was in the hospital and couldn't move. His brother Dyke Shaw (Jason Stantham) vowed to avenge his brother. Dyke was the ace of the US special forces, not only with stunts, but also with a slap in the face. He killed the Korean who was far away from Tokyo, and almost sent the inspector Luke Hobbs (Dwayne Johnson) to another world. Even the home of Dominica was blown up by the other side.",
            "pic": "image/2.png",
            "actor": "Van Diesel / Paul Walker",
            "duration": 137,
            "star": 5,
            "publish_time": "2014-05-12T18:00:00Z",
            "create_time": "2019-03-14T22:26:07.793Z",
        },
        {
            "id": 4,
            "name": "New Police Story",
            "detail": "The group of police officers of Chen Guorong (Cheng Long) is the elite of the police force and has solved numerous crimes. Azu (Wu Yanzu) is the son of the chief police officer, but has colluded with several high-ranking children (Jiang Yizhen, Yin Ziwei, An Zhijie, Ye Shanhao) to challenge the police. When they went to the bank to rob, the alarm bell rang when the police arrived, they brought Arong and the team members into an empty warehouse that had already been designed. The police officers were trapped in the game program that had been designed by the gangsters, and they were cruelly killed. Even the brother of Arong\u2019s girlfriend (Yang Caini) was not spared. Arong was suspended from this, and he broke up with the guilt. Ah Rong, who was drunk all day, met A Feng (Xie Weifeng) at the bar. In order to cheer up Arong, Ah Feng decided to pretend that the police told Arong that he was a new police officer sent by the boss to ask Arong to help turn the case. Arong met the group of criminals who attacked him. They fought bravely with them. With the help of police flower salsa (Cai Zhuoyu), they knew that the incidents of the criminals were compiled into a game, and they also knew what intelligence was in the year. The cause of the leak",
            "pic": "image/3.png",
            "actor": "Jackie Chan / Nicholas Tse",
            "duration": 123,
            "star": 5,
            "publish_time": "2014-09-12T12:00:00Z",
            "create_time": "2019-03-14T22:27:45.113Z",
        }
    ]

    romantic_movies = [
        {
            "id": 7,
            "name": "You're The Apple Of My Eyes",
            "detail": "Youth is a heavy rain. Even if I have a cold, I look forward to seeing it again. Life is a constant battle. When you have not been favored by the goddess, the left hand is always only an aid! ! !\r\nKe Jingteng (Ke Zhendong) and his group of friends, who love to play handsome but always frustrated Lao Cao (ao quan), can not stop the erection, so called the erection of erection (sheng yu), want to use funny to win but always fail On the side (Cai Changxian), the fat-loving master of the fat world, Ahe (hao shao wen), has been an eternal party from the middle to the high school. They all have a tangled feeling towards Ban Hua Shen Jiayi (Chen Yuxi). On the one hand, they look down on the girls who only study hard, and on the other hand they dumped her good temperament. Because of poor academic performance, Ke Jingteng was arranged by the teacher to sit in front of Shen Jiayi. Because his hero saved the beauty, she began to help him with his homework in a compulsory way. This incident made other brothers envy and hate, but everyone did not say it. After graduation, Ke Jingteng and Shen Jiayi maintained a lover-like connection at their respective universities. It wasn't until he held the free fighting game that things changed. This series of friends, who were originally unmoved, are also...",
            "pic": "image/6.png",
            "actor": "Ke Zhendong / Chen Yuxi",
            "duration": 110,
            "star": 5,
            "publish_time": "2012-01-06T18:00:00Z",
            "create_time": "2019-03-14T22:35:43.517Z",
        },
        {
            "id": 8,
            "name": "Soul Mate",
            "detail": "The first acquaintance of July (Ma Sichun) and An Sheng (Zhou Dongyu) was at the age of thirteen. One of them was a \"wild child\" who was a maverick, and a \"prostitute\" who was simply gentle and disciplined. At the beginning of the year, July and Ansheng were almost inseparable. She was her light. She was her shadow. Until one day, a teenager named Su Jiaming (Li Chengbin) appeared in July and fell in love in July.\r\nAnsheng decided to go to Beijing to discuss his life. Before leaving, in July, he unexpectedly discovered that Yu Jiaming, who was wearing Sujiaming, appeared in the collar of Ansheng. An Sheng left, and the relationship between Su Jiaming and Su Jiaming continued in July. They were admitted to the same university and agreed to get married as soon as they graduated. However, things did not develop as I imagined in July, and the relationship between her and Su Jiaming also produced new variables because of the return of An Sheng.",
            "pic": "image/7.png",
            "actor": "Zhou Dongyu / Ma Sichun",
            "duration": 109,
            "star": 5,
            "publish_time": "2016-09-14T22:37:00Z",
            "create_time": "2019-03-14T22:37:18.348Z",
        }
    ]

    science_movies = [
        {
            "id": 2,
            "name": "Iron Man",
            "detail": "Stark Arms is the world's largest supplier of arms to the world, and its new head, Tony Stark (Robert Downey Jr.), is a talented and talented person. He worked with the company's veteran, Obadia Stein (Jeff Briggis Jeff Bridges), to bring Stark's business to the top. Tony in the real life is keen to collect expensive sports cars and make some inventions and creations. Of course, the marriage of dew is even more essential. Fortunately, he had a good assistant like Virginia Potts (Gwyneth Paltrow) to take care of everything, so that he was free to live the life of your son.",
            "pic": "image/1.png",
            "actor": "Art Macomb / Matt Holloway",
            "duration": 126,
            "star": 5,
            "publish_time": "2008-05-02T22:24:00Z",
            "create_time": "2019-03-14T22:24:17.814Z",
        },
        {
            "id": 12,
            "name": "Captain Marvel",
            "detail": "Captain Marvel is a 2019 American superhero film based on the Marvel Comics character Carol Danvers. Produced by Marvel Studios and distributed by Walt Disney Studios Motion Pictures, it is the twenty-first film in the Marvel Cinematic Universe (MCU). The film is written and directed by Anna Boden and Ryan Fleck, with Geneva Robertson-Dworet also contributing to the screenplay. Brie Larson stars as Danvers, alongside Samuel L. Jackson, Ben Mendelsohn, Djimon Hounsou, Lee Pace, Lashana Lynch, Gemma Chan, Annette Bening, Clark Gregg, and Jude Law. Set in 1995, the story follows Danvers as she becomes Captain Marvel after Earth is caught in the center of a galactic conflict between two alien worlds.",
            "pic": "image/12.jpg",
            "actor": "Brie Larson / Samuel L. Jackson",
            "duration": 124,
            "star": 5,
            "publish_time": "2019-02-27T23:35:32Z",
            "create_time": "2019-03-16T23:35:40.539Z",
        },
        {
            "id": 13,
            "name": "Avengers: Endgame",
            "detail": "Avengers: Endgame is an upcoming American superhero film based on the Marvel Comics superhero team the Avengers, produced by Marvel Studios and set for distribution by Walt Disney Studios Motion Pictures. It is the direct sequel to 2018's Avengers: Infinity War, a sequel to 2012's Marvel's The Avengers and 2015's Avengers: Age of Ultron, and the 22nd film in the Marvel Cinematic Universe (MCU). The film is directed by Anthony and Joe Russo with a screenplay by Christopher Markus and Stephen McFeely and features an ensemble cast including Robert Downey Jr., Chris Evans, Mark Ruffalo, Chris Hemsworth, Scarlett Johansson, Jeremy Renner, Don Cheadle, Paul Rudd, Brie Larson, Karen Gillan, Danai Gurira, Benedict Wong, Jon Favreau, Bradley Cooper, Gwyneth Paltrow, and Josh Brolin. In the film, the surviving members of the Avengers work to reverse the damage caused by Thanos in Infinity War.",
            "pic": "image/13.jpg",
            "actor": "Robert Downey Jr. / Chris Evans",
            "duration": 120,
            "star": 5,
            "publish_time": "2019-04-26T23:41:10Z",
            "create_time": "2019-03-16T23:41:13.631Z",
        },
        {
            "id": 20,
            "name": "Wonder Woman",
            "detail": "Wonder Woman is a 2017 American superhero film based on the DC Comics character of the same name, produced by DC Entertainment in association with RatPac Entertainment and Chinese company Tencent Pictures, and distributed by Warner Bros. Pictures. It is the fourth installment in the DC Extended Universe (DCEU).[6] Directed by Patty Jenkins from a screenplay by Allan Heinberg and a story by Heinberg, Zack Snyder, and Jason Fuchs, Wonder Woman stars Gal Gadot in the title role, alongside Chris Pine, Robin Wright, Danny Huston, David Thewlis, Connie Nielsen, and Elena Anaya. It is the second live action theatrical film featuring Wonder Woman following her debut in 2016's Batman v Superman: Dawn of Justice.[7] In Wonder Woman, the Amazon princess Diana sets out to stop World War I, believing the conflict was started by the longtime enemy of the Amazons, Ares, after American pilot and spy Steve Trevor crash-lands on their island Themyscira and informs her about it.",
            "pic": "image/20.jpg",
            "actor": "Gal Gadot",
            "duration": 141,
            "star": 5,
            "publish_time": "2017-03-15T22:07:31Z",
            "create_time": "2019-03-17T22:07:51.653Z",
        }
    ]

    horror_movies = [
        {
            "id": 5,
            "name": "Saw",
            "detail": "The waking Adam (Leigh Whannell) found himself trapped in an abandoned toilet. He was opposite Lawrence (Cary Elwes), who was tied up with chains and was surprised to find a horrible dead man in the middle of the two. The blood of the dead is dripping, and the left hand is holding the gun in the right hand of the recorder. Adam put a tape in his pocket and he quickly put it in the recorder. The tape said that Lawrence must kill Adam before 6 o'clock tonight, otherwise the two will die together, and Lawrence's family will not be spared. The blood flowing out of the dead in front of him is extremely poisonous. A bloody death game begins. In the remaining time, they must find clues and escape from hell. At the last minute, when they thought they would see the sky again, a new round of nightmare was just beginning.",
            "pic": "image/4.png",
            "actor": "Ray Warner / Gary Elvis",
            "duration": 103,
            "star": 5,
            "publish_time": "2004-01-19T22:29:00Z",
            "create_time": "2019-03-14T22:29:47.987Z",
        },
        {
            "id": 11,
            "name": "The Conjuring",
            "detail": "The Conjuring is a 2013 American supernatural horror film directed by James Wan and written by Chad Hayes and Carey W. Hayes. It is the inaugural film in The Conjuring Universe franchise.[3] Patrick Wilson and Vera Farmiga star as Ed and Lorraine Warren, paranormal investigators and authors associated with prominent cases of haunting. Their purportedly real-life reports inspired The Amityville Horror story and film franchise.[4] The Warrens come to the assistance of the Perron family, who experienced increasingly disturbing events in their farmhouse in Rhode Island in 1971",
            "pic": "image/11.jpg",
            "actor": "Patrick Wilson, Vera Farmiga",
            "duration": 112,
            "star": 5,
            "publish_time": "2013-07-15T23:30:28Z",
            "create_time": "2019-03-16T23:30:30.021Z",
        },
        {
            "id": 16,
            "name": "The Conjuring 2",
            "detail": "The Conjuring 2 (also known as The Conjuring 2: The Enfield Case)[4][5] is a 2016 American supernatural horror film, directed by James Wan. The screenplay is by Chad Hayes, Carey W. Hayes, Wan, and David Leslie Johnson. It is the sequel to 2013's The Conjuring, the second installment in The Conjuring series, and the third installment in the Conjuring Universe franchise. Patrick Wilson and Vera Farmiga reprise their roles as paranormal investigators and authors Ed and Lorraine Warren from the first film. The film follows the Warrens as they travel to Britain to assist the Hodgson family, who are experiencing poltergeist activity at their Enfield council house in 1977 which later became referred to as the Enfield Poltergeist.",
            "pic": "image/16.jpg",
            "actor": "Patrick Wilson / Vera Farmiga",
            "duration": 134,
            "star": 5,
            "publish_time": "2016-06-07T21:10:21Z",
            "create_time": "2019-03-17T21:10:25.656Z",
        }
    ]

    adventure_movies = [
        {
            "id": 9,
            "name": "Avatar",
            "detail": "Jack Nasri (Sam Worthington), a former navy warrior who was wounded in battle and decided to go to the dead compatriot, came to Pandora to control Dr. Grace (Sigourney Weaver) The \"Avatar\" hybrid creature created by the combination of human genes and local Nami tribe genes. Jack's goal was to break into the Nazi tribes, and diplomacy persuaded them to voluntarily leave their homes for generations, so that SecFor could cut down the area's virgin forests and mine expensive \"unreachable\" mines. In the process of exploring Pandora, Jack met the Princess Natyre (Ze Saldana) and learned about Na's survival skills and attitude towards nature. At the same time, SecFor's manager and military representative, Colonel Miles (St. Stephen Stephen Lang), gradually lost patience and decided to resort to force to drive the Na'vi..",
            "pic": "image/8.png",
            "actor": "Sam Worthington / Zoe Saldana",
            "duration": 162,
            "star": 5,
            "publish_time": "2010-01-04T00:00:00Z",
            "create_time": "2019-03-14T22:38:44.979Z",
        },
    ]

    tokusatsu_movies = [
        {
            "id":14,
            "name": "Ultraman Zero: The Revenge of Belial",
            "detail": "Ultraman Zero THE MOVIE Super Decisive Battle! Belial Galactic Empire (\u30a6\u30eb\u30c8\u30e9\u30de\u30f3\u30bc\u30ed THE MOVIE \u8d85\u6c7a\u6226\uff01\u30d9\u30ea\u30a2\u30eb\u9280\u6cb3\u5e1d\u56fd Urutoraman Zero THE MOVIE: Ch\u014dkessen! Beriaru Ginga Teikoku, lit. \"Ultraman Zero The Movie: Super Deciding Fight! The Belial Galactic Empire\") is a 2010 Japanese superhero film in the Ultra Series to celebrate the franchise's 45th anniversary.[1] It serves as a sequel to Mega Monster Battle: Ultra Galaxy Legend The Movie. The catchphrases for the movie are \"Kaiser Belial descent. Zero, fight with light!\" and \"This is our light!\".",
            "pic": "image/14.jpg",
            "actor": "\u5c0f\u67f3 \u53cb / \u6ff1\u7530 \u9f8d\u81e3",
            "duration": 100,
            "star": 5,
            "publish_time": "2010-12-23T23:51:22Z",
            "create_time": "2019-03-16T23:51:25.976Z",
        },
        {
            "id":15,
            "name": "Ultraman Saga",
            "detail": "Ultraman Saga (\u30a6\u30eb\u30c8\u30e9\u30de\u30f3\u30b5\u30fc\u30ac Urutoraman S\u0101ga) is a 2012 Japanese tokusatsu, superhero and kaiju film in the Ultra Series to celebrate the franchise's 45th anniversary. It serves as a sequel to Ultraman Zero: The Revenge of Belial. The catchphrase for the movie is \"We Still Have Glittering Hope!!\" (\u50d5\u3089\u306b\u306f\u307e\u3060\u3001\u8f1d\u304f\u5e0c\u671b\u304c\u3042\u308b!! Bokura ni wa Mada, Kagayaku Kib\u014d ga Aru!!). The film features Ultraman Zero, Ultraman Dyna, and Ultraman Cosmos as well as the five Ultra Brothers facing a new ultimate threat, Hyper Zetton (\u30cf\u30a4\u30d1\u30fc\u30bc\u30c3\u30c8\u30f3 Haip\u0101 Zetton) and the monster army created by the evil Alien Bat (\u30d0\u30c3\u30c8\u661f\u4eba Batto Seijin). The film also features a new Ultraman known as Ultraman Saga (\u30a6\u30eb\u30c8\u30e9\u30de\u30f3\u30b5\u30fc\u30ac Urutoraman S\u0101ga). The movie is set in the world of Ultraman Dyna, taking place 15 years after the series and features much of the supporting cast returning. A selection of members from the idol group AKB48 has been chosen to portray the characters of Team-U, a special monster attack team part of the fictional Earth Defense Force.",
            "pic": "image/15.jpg",
            "actor": "\u30bf\u30a4\u30ac\u30fb\u30ce\u30be\u30e0 / \u30a2\u30b9\u30ab\u30fb\u30b7\u30f3",
            "duration": 90,
            "star": 5,
            "publish_time": "2012-03-24T23:53:42Z",
            "create_time": "2019-03-16T23:53:47.161Z",
        },
        {
            "id":19,
            "name": "Ultraman Orb The Movie",
            "detail": "Ultraman Orb The Movie (\u5287\u5834\u7248 \u30a6\u30eb\u30c8\u30e9\u30de\u30f3\u30aa\u30fc\u30d6 \u7d46\u306e\u529b\u3001\u304a\u304b\u308a\u3057\u307e\u3059\uff01 Gekij\u014dban Urutoraman \u014cbu Kizuna no Chikara, Okarishimasu!, also called \"Ultraman Orb The Movie: I'm Borrowing the Power of Your Bonds!\") is a Japanese superhero and Kaiju film, serving as the film adaptation of the 2016 Ultra Series television series Ultraman Orb. It was released in March 11, 2017, in celebration to the 50th anniversary of Ultra Seven where the titular character himself and his son Ultraman Zero is set to appear.[1] Both Blu-Ray and the DVD is set to be released on 28 July 2017.",
            "pic": "image/19.jpg",
            "actor": "\u77f3\u9ed2 \u82f1\u96c4",
            "duration": 72,
            "star": 5,
            "publish_time": "2017-03-11T21:51:26Z",
            "create_time": "2019-03-17T21:51:30.517Z",
        },

    ]

    literary_movies = [
        {
            "id":17,
            "name": "The Legend of 1900",
            "detail": "The Legend of 1900 (Italian: La leggenda del pianista sull'oceano, \"The Legend of the Pianist on the Ocean\") is a 1998 Italian drama film directed by Giuseppe Tornatore and starring Tim Roth, Pruitt Taylor Vince and M\u00e9lanie Thierry. It was Tornatore's first English-language film.[2] The film is inspired by Novecento, a monologue by Alessandro Baricco. The film was nominated for a variety of awards worldwide, winning several for its soundtrack.",
            "pic": "image/17.jpg",
            "actor": "Tim Roth",
            "duration": 125,
            "star": 5,
            "publish_time": "1998-10-28T21:33:39Z",
            "create_time": "2019-03-17T21:35:00.348Z",

        },
        {
            "id":18,
            "name": "The Truman Show",
            "detail": "The Truman Show is a 1998 American satirical science fiction film[4] directed by Peter Weir, produced by Scott Rudin, Andrew Niccol, Edward S. Feldman, and Adam Schroeder, and written by Niccol. The film stars Jim Carrey as Truman Burbank, adopted and raised by a corporation inside a simulated television show revolving around his life, until he discovers it and decides to escape. Additional roles are performed by Laura Linney, Noah Emmerich, Natascha McElhone, Holland Taylor, Ed Harris, and Brian Delate.",
            "pic": "image/18.jpg",
            "actor": "Jim Carrey / Laura Linney",
            "duration": 103,
            "star": 5,
            "publish_time": "1998-06-01T21:41:32Z",
            "create_time": "2019-03-17T21:41:37.524Z",
        },
    ]



    classifies = {
        "Comedy": {"movies": comedy_movies},
        "Action": {"movies": action_movies},
        "Romantic": {"movies": romantic_movies},
        "Science fiction":{"movies": science_movies},
        "Horror":{"movies": horror_movies},
        "Adventure":{"movies": adventure_movies},
        "Tokusatsu":{"movies": tokusatsu_movies},
        "Literary":{"movies": literary_movies},
    }


    for cla, cla_data in classifies.items():
        c = add_cla(cla)
        for p in cla_data["movies"]:
            add_movie(p["id"], p["name"],p["detail"],p["pic"],p["actor"],p["duration"],p["star"],p["publish_time"],p["create_time"],c)
    
    for c in ClassifyModel.objects.all():
        for p in MovieModel.objects.filter(classify=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_movie(id, name, detail, pic, actor, duration, star, publish_time, create_time, classify):
    p = MovieModel.objects.get_or_create(id=id, name=name,duration=duration,star=star, publish_time = publish_time, classify = classify)[0]
    p.detail = detail
    p.pic = pic
    p.actor = actor
    
    p.create_time = create_time
    p.save()
    return p

def add_cla(name):
    c = ClassifyModel.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting AngryPotato population script...")
    populate()