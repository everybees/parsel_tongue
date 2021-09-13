import random

scroll = {
"quiz" :["Who found water in the wilderness when pastured the donkeys. Ans: Anah.", 
"According to the Genesis creation narrative, what was created by God to separate the “waters above” the earth from the “waters below” the earth. Ans: Sky",
"Who is the son of Anah. Ans: Dishon."
"Which is the city of Bela Edom. Ans: Dinhabah."
"Who was reigned the country of Dinhabah after Bela. Ans: Jobab.",
"In Genesis 1:27, God created what in his own image. Ans: Man.",
"To whom sold Joseph by Midianites. Ans: To Potiphar (He is the guard of Pharaoh).",
"The wife of Judah? Ans: Daughter of Shua, a Canaanite.",
"Who was the mother of Zerah. Ans: Tamar.",
"Which region was surrounded by the river Pishon. Ans: The land of Havilah",
"Name the second river from Eden which passes through Cush land. Ans: Gihon.",
"Who was interpreted the dream, dreamed by Pharaoh in Egypt. Ans: Joseph.",
"What was the name Pharaoh called to Joseph. Ans: Zaphnath-paaneah.",
"The Bible says “she shall be called Woman” and why. Ans: Because she was taken out of Man",
"Which creature was subtle than any beast of the field that the LORD God had made. Ans: Serpent",
"Which are the supply cities built by Egyptians to Pharaoh. Ans: Pithom, Rameses.",
"Who is the child of Israel received from the Nile River. Ans: Moses.",
"When man ate the fruit of the tree of knowledge, what did he gain Ans: Ability to know good and evils.",
"Who is the son of Moses. Ans: Gershom.",
"According to the Bible, what was Abel's occupation. Ans: Sheep keeper.",
"Who was the priest of Midian. Ans: Jethro.",
"Where did God appear to Moses. Ans: Mount Sinai.",
"After Abel’s murder, Cain went to .... Ans: Land of Nod.",
"How many books are in the New Testament? Ans: 27",
"Who is the author of the Book of Revelation Ans: John the Beloved"
"What tribe is Paul from. Ans: Benjamin"
"Name the place where Jesus walked on water. Ans: Sea of Galilee"
"Who said: How long will you waver between two opinions. Ans(Elijah on Mount Carmel)",
"Which commander had leprosy. Ans: Naemann",
"For which type of tree was Lebanon well known. Ans: Cedar",
"What were the names of Abraham’s brothers. Ans: Nahor, Haran",
"What was Priscilla’s husband called; which job did he have. Ans: Aquila, tent maker",
"Who was Bernice. Ans: The wife of king Agrippa)",
"Who was Zippora. Ans: Moses’ wife",
"What was Timothy grandmother called. Ans: Lois",
"What does Jahwe-Schammah mean. Ans: God himself/Ezekiel 48,35",
"When was Passover celebrated? Day and month. Ans: 14th day of the 1st month",
"What was Job’s mother called. Ans: Zeruja/2 Samuel 2,13",
"The high priest of Jerusalem that put Jesus on trial, what was his name. Ans Caiaphas",
"Who took Judas Iscariot’s place as a disciple. Ans: Matthias."
"Apostle Paul wrote how many books. Ans: 13 books"
]
}
print("Welcome to Rabbi. Enter 'Start Quiz' to begin quiz.\nEnter 'Next Quiz' for the next question")

while True:
    print()
    Prompt = input().split()
    if ["Done"] == Prompt:
        print("Exiting...")
        break

    for word in Prompt:
        if word.lower() in scroll.keys():
            print(random.choice (scroll[word.lower()]))