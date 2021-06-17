# RACE for QGG
This dataset is a subset of RACE, which contains three types(Factoid, Cloze and Summarization) of questions.

## Dataset Download
> preparing

## Data Statistics
|Types|Examples|Train|Dev|Test|
|---|---|---|---|---|
|Cloze|Yingying is Wangwang's  _ .|43167|2405|2462|
|Factiod|What can Mimi do?|18405|1030|944|
|Summarization|According to this passage we know that _ .|3004|175|184|

## Example Data
```json
{
    "answers": [
        "D",
        "A",
        "B",
        "C"
    ],
    "options": [
        [
            "States",
            "Doubts",
            "Confirms",
            "Removes"
        ],
        [
            "shows the kind of male birds females seek out.",
            "indicates the wandering albatross is the most faithful.",
            "is based on Professor Stutchbury's 20 years' research.",
            "suggests that female birds select males near their home."
        ],
        [
            "young birds' quality depends on their feather.",
            "some male birds care for others' young as their own.",
            "female birds go to find males as soon as autumn comes.",
            "female birds are responsible for feeding the hungry babies."
        ],
        [
            "A book about love-birds.",
            "Birds' living habits and love life",
            "The fact that birds don't love their mates forever.",
            "The factors that influence birds to look for another mate."
        ]
    ],
    "questions": [
        "What does the underline word \"dispels\" mean?",
        "The book The Private Lives of Birds  _  .",
        "According to the passage, we can infer that  _  .",
        "What is the passage mainly about?"
    ],
    "article": "\"Birds are not as loyal to their partners as you might think ...",
    "id": "high11327.txt",
    "factiod_questions": [
        "What does the underline word \"dispels\" mean?"
    ],
    "cloze_questions": [
        "The book The Private Lives of Birds  _  ."
    ],
    "summarization_questions": [
        "According to the passage, we can infer that  _  ."
    ]
}
```
