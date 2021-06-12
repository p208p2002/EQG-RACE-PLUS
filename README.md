# EQG-RACE-PLUS
This work align [RACE](https://www.aclweb.org/anthology/D17-1082.pdf) and [EQG-RACE](https://arxiv.org/pdf/2012.06106.pdf), for divide question by three types(General, Cloze, and Specific)

## Dataset Download
- [Google Drive](https://drive.google.com/file/d/1wXGyEjzwDpvG1TCv6C8JfUwDJmOiBwOr/view?usp=sharing)
- [GitHub Release](https://github.com/p208p2002/EQG-RACE-PLUS/releases)

## Example Data
```json
{
    "id": "high12026.txt",
    "answers": [
        "D",
        "C",
        "D",
        "C"
    ],
    "options": [
        [
            "introduce herself to John",
            "talk about her bad year",
            "ask for some advice",
            "express her thanks"
        ],
        [
            "didn't like her boyfriend",
            "spent a lot of time online",
            "wasn't satisfied with her job",
            "received very good education"
        ],
        [
            "He is a very famous writer.",
            "He used to live a very negative life.",
            "He doesn't like sharing his life stories.",
            "He likes helping others through writing positive blogs."
        ],
        [
            "Practice makes perfect.",
            "Bad luck doesn't exist long.",
            "A positive attitude is rewarding.",
            "A friend in need is a friend indeed."
        ]
    ],
    "article": "Dear John,\nMy name is Amber and I want to share my story ...",
    "questions": [
        "Amber wrote the letter mainly to  _",
        "We can infer from the passage that Amber  _",
        "What is implied about John in the letter?",
        "What does Amber's change tell us?"
    ],
    "specific_questions": [
        "What is implied about John in the letter?"
    ],
    "cloze_questions": [
        "Amber wrote the letter mainly to  _",
        "We can infer from the passage that Amber  _"
    ],
    "general_questions": [
        "What does Amber's change tell us?"
    ]
}
```
