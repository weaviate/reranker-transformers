import unittest
import requests
import time

class SmokeTest(unittest.TestCase):
    def _waitForStartup(self):
        url = 'http://localhost:8000/.well-known/ready'

        for i in range(0, 100):
            try:
                res = requests.get(url)
                if res.status_code == 204:
                    return
                else:
                    raise Exception(
                            "status code is {}".format(res.status_code))
            except Exception as e:
                print("Attempt {}: {}".format(i, e))
                time.sleep(1)

        raise Exception("did not start up")

    def testVectorizing(self):
        self._waitForStartup()
        url = 'http://localhost:8000/answers/'

        req_body = {'text': 'John is 20 years old', 'question': 'how old is john?'}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        self.assertTrue("20" in str(resBody['answer']).strip())
        self.assertGreaterEqual(resBody['certainty'], 0.01)
        self.assertGreaterEqual(len(str(resBody['answer']).strip()), 2)
        print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {'text': 'John is 20 years old', 'question': 'this is wrong question'}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['certainty'] != None:
            self.assertLessEqual(resBody['certainty'], 0.5)

        req_body = {'text': 'John is 20 years old', 'question': 'This question has no meaning or has it?'}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['answer'] != None:
            print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {"question": "how old is john?", "text": "Praesent pulvinar semper feugiat. Sed eros nisl, volutpat ut dolor et, consectetur finibus libero. Aenean molestie, neque vel aliquet ultrices, nisl magna molestie justo, id fringilla neque urna a orci. Curabitur a leo sed enim blandit bibendum. Sed a risus in tortor varius tristique ut ac purus. Proin vitae bibendum magna. Donec sit amet fermentum arcu. Nulla pharetra hendrerit elementum. In varius pretium leo, a auctor tortor. Phasellus rutrum lacus quis imperdiet sagittis. Proin et scelerisque eros. Suspendisse convallis at erat et condimentum... Donec eu orci eu nibh ullamcorper varius a ut quam. Mauris tempus semper tincidunt. Aliquam eu justo vestibulum, semper sapien ut, sollicitudin justo. Suspendisse potenti. Proin ultricies feugiat tortor non viverra. Aliquam eleifend mollis orci ut lacinia. Etiam tincidunt sem velit, vel consequat arcu finibus nec. Donec tincidunt sem quam, eu lacinia orci blandit at. Donec fermentum, lacus eu congue viverra, nisl risus hendrerit ex, et feugiat metus nisi nec dui. In in elit a nunc elementum ullamcorper. In non nunc in dolor placerat malesuada vitae sed nulla. In vitae metus sed mi laoreet ultricies eget in quam. Quisque consectetur ipsum in lorem congue porta. Maecenas scelerisque, mauris ac molestie malesuada, eros orci blandit quam, vitae vulputate lectus eros sit amet sem. Duis luctus venenatis risus ut lacinia. Aenean sed enim volutpat, elementum elit eget, semper augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aenean feugiat tellus odio, aliquam dignissim odio placerat vel. Curabitur id dolor sed mi scelerisque dictum. Sed tempus varius dolor id condimentum. Etiam rutrum vestibulum odio. Ut a convallis arcu, eu porta magna. Fusce eu euismod justo, at malesuada quam. Duis dignissim id ipsum a interdum. Proin et urna faucibus tellus accumsan bibendum id sed erat. Ut at eros ac nibh faucibus sollicitudin. Ut scelerisque arcu libero, eu finibus felis porta in. Phasellus varius gravida massa. Nulla tortor augue, eleifend et orci non, venenatis scelerisque ex. Sed quis diam eu lorem pretium lobortis. Morbi malesuada, leo id egestas ultrices, magna justo euismod enim, et lacinia magna nulla eu ex. There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc. John is 20 years old. Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32. The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from \"de Finibus Bonorum et Malorum\" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham. Duis euismod odio a dolor porttitor, sit amet imperdiet enim lacinia. Vestibulum mattis gravida metus, at vulputate metus consequat eleifend. Nunc quis risus leo. Nullam at augue eget odio tincidunt facilisis sed in sem. Pellentesque consectetur, ex quis maximus sagittis, felis tortor suscipit tortor, a sagittis nisl arcu quis sem. Sed finibus, eros quis suscipit elementum, est sapien gravida purus, non ullamcorper mauris arcu quis nulla. Suspendisse at felis vitae neque finibus lobortis sed eu urna. Ut suscipit laoreet erat, vitae hendrerit lorem gravida vel. Proin quis risus nec tortor facilisis mollis eu nec urna. In at ullamcorper purus. Aenean ac ligula orci. Mauris porta fermentum ante, ut tempor nisi dignissim ac. Vivamus pulvinar a velit et interdum. Donec dolor dui, pellentesque quis vestibulum egestas, dapibus non erat. Praesent vitae euismod turpis. Proin efficitur rutrum ante, at posuere enim ultricies ac. Pellentesque sed finibus lorem. Morbi dapibus posuere lacus, vitae luctus libero suscipit ut. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Fusce lacus diam, bibendum eu suscipit quis, hendrerit sit amet quam. Nam eget sodales leo. Vivamus varius nec purus ut facilisis. In erat diam, rutrum et quam id, vestibulum sollicitudin ligula. Sed luctus porttitor diam elementum faucibus. Phasellus pellentesque purus vitae nulla sodales, a efficitur felis fermentum. Mauris vulputate dapibus metus commodo maximus. Nulla eget sapien eu nibh efficitur porttitor nec nec massa. Nullam rutrum lorem ut justo viverra blandit. Praesent a erat lorem. Ut eget quam id ipsum venenatis condimentum auctor et turpis. Nullam et bibendum ipsum. Duis varius et nisi eget maximus. Duis commodo feugiat porttitor. Sed sed rutrum erat. Morbi auctor urna a porta suscipit. Maecenas eget maximus nisi, at euismod eros."}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        self.assertGreaterEqual(len(str(resBody['answer']).strip()), 5)
        self.assertGreaterEqual(resBody['certainty'], 0.1)
        print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {'text': '', 'question': ''}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        self.assertIsNone(resBody['answer'])
        self.assertIsNone(resBody['certainty'])

        req_body = {'question': 'What was Michael Brecker\'s first saxophone?', 'text': 'Early in his career, Brecker played a Selmer Super Balanced Action saxophone (serial number 39xxx), later moving to a lacquer-finished Selmer Mark VI tenor saxophone (serial number 86351, manufactured in 1960) with silver-plated neck (serial number 92203), fitted with a Dave Guardala MB1 mouthpiece and LaVoz medium reeds. His earlier mouthpieces included a metal Otto Link \'New York\' STM (during the mid-1970s) and a metal Dukoff in the late 1970s and early 1980s. Brecker also played the drums as he often talked about time, or rhythm, being musically the most important. He displayed his drum prowess during shows with his own ensembles or accompanying students during masterclasses. '}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['certainty'] != None:
            self.assertGreaterEqual(resBody['certainty'], 0.01)
        self.assertGreaterEqual(len(str(resBody['answer']).strip()), 5)
        print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {'question': 'Who was influenced by Brian Wilson?', 'text': 'Best known for primarily using a plectrum or pick, McCartney occasionally plays fingerstyle. He was strongly influenced by Motown artists, in particular James Jamerson, whom McCartney called a hero for his melodic style. He was also influenced by Brian Wilson, as he commented: \"because he went to very unusual places\". Another favourite bassist of his is Stanley Clarke.: The influence of Motown and James Jamerson, : Stanley Clarke. McCartney\'s skill as a bass player has been acknowledged by bassists including Sting, Dr. Dre bassist Mike Elizondo, and Colin Moulding of XTC. During McCartney\'s early years with the Beatles, he primarily used a Höfner 500/1 bass, although from 1965, he favoured his Rickenbacker 4001S for recording. While typically using Vox amplifiers, by 1967, he had also begun using a Fender Bassman for amplification.: Höfner 500/1, : Rickenbacker 4001, : Vox amplifiers; : Fender Bassman. During the late 1980s and early 1990s, he used a Wal 5-String, which he said made him play more thick-sounding basslines, in contrast to the much lighter Höfner, which inspired him to play more sensitively, something he considers fundamental to his playing style. He changed back to the Höfner around 1990 for that reason. He uses Mesa Boogie bass amplifiers while performing live. MacDonald identified \"She\'s a Woman\" as the turning point when McCartney\'s bass playing began to evolve dramatically, and Beatles biographer Chris Ingham singled out Rubber Soul as the moment when McCartney\'s playing exhibited significant progress, particularly on \"The Word\".: \"She\'s a Woman\"; : \"began to come into its own\". Bacon and Morgan agreed, calling McCartney\'s groove on the track \"a high point in pop bass playing and ... the first proof on a recording of his serious technical ability on the instrument.\": Rubber Soul as the starting point for McCartney\'s bass improvement, : \"a high point in pop bass playing\". MacDonald inferred the influence of James Brown\'s \"Papa\'s Got a Brand New Bag\" and Wilson Pickett\'s \"In the Midnight Hour\", American soul tracks from which McCartney absorbed elements and drew inspiration as he \"delivered his most spontaneous bass-part to date\". Bacon and Morgan described his bassline for the Beatles song \"Rain\" as \"an astonishing piece of playing ... [McCartney] thinking in terms of both rhythm and \'lead bass\' ... [choosing] the area of the neck ... he correctly perceives will give him clarity for melody without rendering his sound too thin for groove.\" MacDonald identified the influence of Indian classical music in \"exotic melismas in the bass part\" on \"Rain\" and described the playing as \"so inventive that it threatens to overwhelm the track\". By contrast, he recognised McCartney\'s bass part on the Harrison-composed \"Something\" as creative but overly busy and \"too fussily extemporised\". McCartney identified Sgt. Pepper\'s Lonely Hearts Club Band as containing his strongest and most inventive bass playing, particularly on \"Lucy in the Sky with Diamonds\". '}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['certainty'] != None:
            self.assertGreaterEqual(resBody['certainty'], 0.1)
        self.assertGreaterEqual(len(str(resBody['answer']).strip()), 3)
        print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {'question': 'Who was the bass player of The Beatles?', 'text': 'Best known for primarily using a plectrum or pick, McCartney occasionally plays fingerstyle. He was strongly influenced by Motown artists, in particular James Jamerson, whom McCartney called a hero for his melodic style. He was also influenced by Brian Wilson, as he commented: \"because he went to very unusual places\". Another favourite bassist of his is Stanley Clarke.: The influence of Motown and James Jamerson, : Stanley Clarke. McCartney\'s skill as a bass player has been acknowledged by bassists including Sting, Dr. Dre bassist Mike Elizondo, and Colin Moulding of XTC. During McCartney\'s early years with the Beatles, he primarily used a Höfner 500/1 bass, although from 1965, he favoured his Rickenbacker 4001S for recording. While typically using Vox amplifiers, by 1967, he had also begun using a Fender Bassman for amplification.: Höfner 500/1, : Rickenbacker 4001, : Vox amplifiers; : Fender Bassman. During the late 1980s and early 1990s, he used a Wal 5-String, which he said made him play more thick-sounding basslines, in contrast to the much lighter Höfner, which inspired him to play more sensitively, something he considers fundamental to his playing style. He changed back to the Höfner around 1990 for that reason. He uses Mesa Boogie bass amplifiers while performing live. MacDonald identified \"She\'s a Woman\" as the turning point when McCartney\'s bass playing began to evolve dramatically, and Beatles biographer Chris Ingham singled out Rubber Soul as the moment when McCartney\'s playing exhibited significant progress, particularly on \"The Word\".: \"She\'s a Woman\"; : \"began to come into its own\". Bacon and Morgan agreed, calling McCartney\'s groove on the track \"a high point in pop bass playing and ... the first proof on a recording of his serious technical ability on the instrument.\": Rubber Soul as the starting point for McCartney\'s bass improvement, : \"a high point in pop bass playing\". MacDonald inferred the influence of James Brown\'s \"Papa\'s Got a Brand New Bag\" and Wilson Pickett\'s \"In the Midnight Hour\", American soul tracks from which McCartney absorbed elements and drew inspiration as he \"delivered his most spontaneous bass-part to date\". Bacon and Morgan described his bassline for the Beatles song \"Rain\" as \"an astonishing piece of playing ... [McCartney] thinking in terms of both rhythm and \'lead bass\' ... [choosing] the area of the neck ... he correctly perceives will give him clarity for melody without rendering his sound too thin for groove.\" MacDonald identified the influence of Indian classical music in \"exotic melismas in the bass part\" on \"Rain\" and described the playing as \"so inventive that it threatens to overwhelm the track\". By contrast, he recognised McCartney\'s bass part on the Harrison-composed \"Something\" as creative but overly busy and \"too fussily extemporised\". McCartney identified Sgt. Pepper\'s Lonely Hearts Club Band as containing his strongest and most inventive bass playing, particularly on \"Lucy in the Sky with Diamonds\". '}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])

        req_body = {'question': 'What science fiction movie did Stanley Kubrick direct?', 'text': 'Prior to shooting Fear and Desire, Kubrick was a Look photographer who had directed two short documentaries in 1951, Day of the Fight and Flying Padre. Both films were acquired for theatrical release by RKO Radio Pictures. From his experiences in creating short films, Kubrick felt he was ready to make a narrative feature film.Duncan, Paul. \"Stanley Kubrick: The Complete Films.\" Taschen, 2008.  Kubrick quit his full-time job with Look and set forth to create Fear and Desire. The screenplay was written by Howard Sackler, a classmate of Kubrick\'s at William Howard Taft High School in the Bronx, New York; Sackler later won the Pulitzer Prize for his 1968 drama The Great White Hope. Virginia Leith, who played The Girl in this film, would soon play Jan in the 1962 cult classic The Brain That Wouldn\'t Die. Paul Mazursky, who would later receive recognition as the director of such films as Harry and Tonto and An Unmarried Woman, was cast as the soldier who kills the captive peasant. Funds for Fear and Desire were raised from Kubrick\'s family and friends, with most of it coming from Martin Perveler, Kubrick\'s uncle and the owner of a profitable pharmacy. The film\'s original budget has been estimated at $10,000. The production team consisted of 15 people: the director, five actors (Paul Mazursky, Frank Silvera, Kenneth Harp, Steve Coit, and Virginia Leith), five crew members (including Kubrick\'s first wife, Toba Metz) and three Mexican laborers who transported the film equipment around California\'s San Gabriel Mountains, where the film was shot. Due to budget limitations, Kubrick improvised in the use of his equipment. To create fog, Kubrick used a crop sprayer, but the cast and crew was nearly asphyxiated because the machinery still contained the insecticide used for its agricultural work. For tracking shots, Paul Mazursky recalled how Kubrick came up with a novel substitute: \"There was no dolly track, just a baby carriage to move the camera\", he told an interviewer. To reduce production costs, Kubrick had intended to make it a silent picture, but in the end the adding of sounds, effects and music brought the production over budget to around $53,000, and had to be bailed out by producer Richard de Rochemont, on condition that he help in de Rochemont\'s production of a five-part program about Abraham Lincoln for the educational TV series Omnibus, filmed on location in Hodgenville, Kentucky. Kubrick also ran into difficulty in editing a key scene where one of the soldiers throws a plate of beans to the floor and enters the frame from the wrong side. Kubrick\'s blocking of the crucial scene was faulty, and his actors accidentally crossed the so-called \"stage line\"; this required the negative to be flipped in the printing process to preserve continuity, which was another expense.Buchanan, Larry. \"It Came From Hunger!\" McFarland & Co., 1996.'}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['answer'] != None:
            self.assertGreaterEqual(len(str(resBody['answer']).strip()), 5)
            print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

        req_body = {'question': 'what does cabernet sauvignon taste like?', 'text': 'Cabernet Sauvignon is a very bold and assertive wine that has potential to overwhelm light and delicate dishes. The wine\'s high tannin content as well as the oak influences and high alcohol levels associated with many regional styles play important roles in influencing how well the wine matches with different foods. When Cabernet Sauvignon is young, all those elements are at their peak, but as the wine ages it mellows; possibilities for different food pairings open up. In most circumstances, matching the weight (alcohol level and body) of the wine to the heaviness of the food is an important consideration. Cabernet Sauvignons with high alcohol levels do not pair well with spicy foods due to hotness levels of the capsaicins present in spices like chili peppers being enhanced by the alcohol with the heat accentuating the bitterness of the tannins. Milder spices, such as black pepper, pair better due to their ability to minimize the perception of tannins—such as in the classic pairings of Cabernet Sauvignon with steak au poivre and pepper-crusted ahi tuna. Fats and proteins reduce the perception of tannins on the palate. When Cabernet Sauvignon is paired with steak or dishes with a heavy butter cream sauce, the tannins are neutralized, allowing the fruits of the wine to be more noticeable. In contrast, starches such as pastas and rice will have little effect on tannins. The bitterness of the tannins can also be counterbalanced by the use of bitter foods, such as radicchio and endive, or with cooking methods that involve charring like grilling. As the wine ages and the tannins lessen, more subtle and less bitter dishes will pair better with Cabernet Sauvignon. The oak influences of the wine can be matched with cooking methods that have similar influences on the food—such as grilling, smoking and plank roasting. Dishes that include oak-influenced flavors and aromas normally found in Cabernet Sauvignon—such as dill weed, brown sugar, nutmeg and vanilla—can also pair well. The different styles of Cabernet Sauvignon from different regions can also influence how well the wine matches up with certain foods. Old World wines, such as Bordeaux, have earthier influences and will pair better with mushrooms. Wines from cooler climates that have noticeable vegetal notes can be balanced with vegetables and greens. New World wines, with bolder fruit flavors that may even be perceived as sweet, will pair well with bolder dishes that have lots of different flavor influences. While Cabernet Sauvignon has the potential to pair well with bitter dark chocolate, it will not pair well with sweeter styles such as milk chocolate. The wine can typically pair well with a variety of cheeses, such as Cheddar, mozzarella and Brie, but full flavored or blue cheeses will typically compete too much with the flavors of Cabernet Sauvignon to be a complementary pairing. '}
        res = requests.post(url, json=req_body)
        resBody = res.json()

        self.assertEqual(200, res.status_code)
        self.assertEqual(req_body['text'], resBody['text'])
        self.assertEqual(req_body['question'], resBody['question'])
        if resBody['answer'] != None:
            self.assertGreaterEqual(len(str(resBody['answer']).strip()), 5)
            print(f"{req_body['question']} : {resBody['answer']} : {resBody['certainty']}")

if __name__ == "__main__":
    unittest.main()
