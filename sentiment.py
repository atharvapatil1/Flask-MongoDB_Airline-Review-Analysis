def sentiment(review):
    positive_words = set([
    "good",
    "like",
    "refund",
    "friendly",
    "comfortable",
    "well",
    "better",
    "nice",
    "great",
    "recommend",
    "free",
    "clean",
    "available",
    "helpful",
    "work",
    "excellent",
    "enough",
    "best",
    "pleasant",
    "hot",
    "fine",
    "efficient",
    "right",
    "smooth",
    "pretty",
    "polite",
    "support",
    "comfort",
    "easy",
    "worth",
    "attentive",
    "top",
    "decent",
    "reasonable",
    "fast",
    "happy",
    "clear",
    "impressed",
    "clearly",
    "worked",
    "helped",
    "complimentary",
    "adequate",
    "amazing",
    "super",
    "warm",
    "smile",
    "refunded",
    "courteous",
    "modern",
    "proper",
    "promised",
    "ready",
    "positive",
    "cheaper",
    "soft",
    "perfect",
    "wonderful",
    "delicious",
    "lovely",
    "fairly",
    "spacious",
    "important",
    "fantastic",
    "recommended",
    "respect",
    "properly",
    "enjoyed",
    "willing",
    "improved",
    "thank",
    "lucky",
    "safe",
    "improve",
    "welcome",
    "works",
    "outstanding",
    "smiling",
    "pleasantly",
    "enjoyable",
    "enjoy",
    "fair",
    "fresh",
    "love",
    "quiet",
    "upgraded",
    "reasonably",
    "incredibly",
    "perfectly",
    "improvement",
    "appreciated",
    "lowcost",
    "luck",
    "beautiful",
    "correct",
    "helping",
    "convenient",
    "reliable",
    "punctual",
    "pleased",
    "won",
    "prefer",
    "generous",
    "exceptional",
    "satisfied",
    "wonder",
    "interesting",
    "smoothly",
    "fun",
    "cheapest",
    "promptly",
    "sufficient",
    "sweet",
    "breeze",
    "cheerful",
    "pleasure",
    "trust",
    "appreciate",
    "comfy",
    "smiles",
    "significant",
    "safely",
    "impressive",
    "amenity",
    "satisfactory",
    "superb",
    "cleared",
    "awesome",
    "flexible",
    "calm",
    "liked",
    "seamless",
    "prompt",
    "grateful",
    "honest",
    "responsive",
    "variety",
    "exceeded",
    "ample",
    "solid",
    "loved",
    "patient",
    "orderly",
    "superior",
    "empathy",
    "led",
    "spotless",
    "affordable",
    "understandable",
    "tough",
    "easier",
    "favor",
    "successfully",
    "strong",
    "consistently",
    "cleanliness",
    "brilliant",
    "competitive",
    "nicely",
    "efficiently",
    "roomy",
    "afford",
    "faster",
    "loyalty",
    "success",
    "dedicated",
    "approval",
    "successful",
    "nicer",
    "convenience",
    "bright",
    "happily",
    "patience",
    "incredible",
    "confidence",
    "glad",
    "friendliness",
    "promise",
    "quicker",
    "regard",
    "timely",
    "gold",
    "loyal",
    "reputation",
    "relaxed",
    "favour",
    "improvements",
    "ease",
    "wise",
    "fortunately",
    "advantage",
    "progress",
    "useful",
    "excited",
    "compassion",
    "improving",
    "benefit",
    "exceptionally",
    "cool",
    "honor",
    "hospitable",
    "bonus",
    "keen",
    "amazed",
    "decency",
    "appropriate",
    "tidy",
    "enjoying",
    "correctly",
    "effectively",
    "complementary",
    "sparkling",
    "pure",
    "guarantee",
    "lead",
    "smart",
    "benefits",
    "leading",
    "consistent",
    "reputable",
    "favorite",
    "flexibility",
    "patiently",
    "savings",
    "secure",
    "bargain",
    "promises",
    "entertaining",
    "effective",
    "comfortably",
    "refreshing",
    "genuine",
    "accurate",
    "kindness",
    "valuable",
    "capable",
    "plentiful",
    "terrific",
    "premier",
    "swift",
    "conveniently",
    "luxury",
    "entertain",
    "engaging",
    "ideal",
    "speedy",
    "delightful",
    "commitment",
    "suitable",
    "memorable",
    "impeccable",
    "satisfying",
    "positively",
    "fancy",
    "encourage",
    "proactive",
    "faith",
    "adjustable",
    "immaculate",
    "gladly",
    "enthusiastic",
    "painless",
    "relief",
    "politeness",
    "gratitude",
    "likes",
    "spectacular",
    "warmth",
    "grace",
    "respectful",
    "logical",
    "attractive",
    "sharp",
    "supportive",
    "rectify",
    "immaculately",
    "modest",
    "straightforward",
    "silent",
    "compliment",
    "flawless",
    "exceed",
    "thankful",
    "joy",
    "recover",
    "privilege",
    "trusted",
    "compact",
    "proud",
    "recommendation",
    "honesty",
    "protection",
    "considerate",
    "goodness",
    "recovery",
    "preferable",
    "cooperative",
    "exciting",
    "fluent",
    "refreshed",
    "worthy",
    "fortune",
    "grand",
    "positives",
    "cleaner",
    "qualified",
    "famous",
    "kindly",
    "sincerely",
    "pleasing",
    "charm",
    "extraordinary",
    "remarkable",
    "praise",
    "healthy",
    "knowledgeable",
    "proven",
    "peaceful",
    "appealing",
    "redeeming",
    "promising",
    "quieter",
    "motivated",
    "peace",
    "phenomenal",
    "redemption",
    "reward",
    "paradise",
    "qualify",
    "fortunate",
    "foremost",
    "instantly",
    "proving",
    "assure",
    "honored",
    "exceeding",
    "dignity",
    "commend",
    "supported",
    "slick",
    "sensitive",
    "eager",
    "charming",
    "gentle",
    "fairness",
    "elite",
    "elegant",
    "classic",
    "humble",
    "patriotic",
    "faultless",
    "reclaim",
    "fabulous",
    "miracle",
    "neat",
    "delight",
    "happier",
    "win",
    "clarity",
    "lighter",
    "exemplary",
    "leads",
    "sincere",
    "redeem",
    "compliant",
    "realistic",
    "highquality",
    "remedy",
    "brandnew",
    "tollfree",
    "fastest",
    "confident",
    "renewed",
    "sufficiently",
    "supporting",
    "beautifully",
    "truthful",
    "satisfy",
    "thoughtful",
    "warmly",
    "smoothest",
    "inexpensive",
    "advanced",
    "smartly",
    "succeed",
    "comprehensive",
    "precisely",
    "kudos",
    "advantages",
    "splendid",
    "pleasurable",
    "hardworking",
    "wow",
    "polished",
    "shiny",
    "comforting",
    "stunned",
    "pride",
    "luxurious",
    "refined",
    "avid",
    "generously",
    "greatest",
    "remarkably",
    "economical",
    "reachable",
    "excitement",
    "sleek",
    "topnotch",
    "magical",
    "joyful",
    "award",
    "accomplished",
    "uncomplicated",
    "classy",
    "stellar",
    "firstclass",
    "preferring",
    "lean",
    "assurance",
    "precious",
    "cute",
    "smoother",
    "audible",
    "defeats",
    "nicest",
    "seasoned",
    "willingness",
    "striking",
    "awards",
    "accessible",
    "mercy",
    "delighted",
    "readily",
    "respectable",
    "gorgeous",
    "diligent",
    "perfection",
    "scenic",
    "wholeheartedly",
    "unlimited",
    "calming",
    "authentic",
    "astounded",
    "celebrate",
    "hilarious",
    "amazingly",
    "continuity",
    "stylish",
    "sublime",
    "robust",
    "desirable",
    "exceeds",
    "abundant",
    "finest",
    "convincing",
    "loves",
    "awarded",
    "rightly",
    "celebration",
    "respectfully",
    "optimal",
    "exquisite",
    "ideally",
    "exceedingly",
    "personalized",
    "restructuring",
    "usable",
    "steady",
    "saver",
    "priceless",
    "userfriendly",
    "tolerable",
    "assurances",
    "approve",
    "restored",
    "handy",
    "snappy",
    "abundance",
    "easiest",
    "popular",
    "cheer",
    "charismatic",
    "intelligence",
    "passionate",
    "beauty",
    "impressively",
    "powerful",
    "pampered",
    "golden",
    "commendable",
    "magic",
    "intelligent",
    "survival",
    "cleanest",
    "rapid",
    "lavish",
    "eased",
    "trusting",
    "jovial",
    "liking",
    "gained",
    "stable",
    "roomier",
    "heaven",
    "inspire",
    "fascinating",
    "tender",
    "stunning",
    "energetic",
    "gracious",
    "tops",
    "beneficial",
    "hero",
    "applaud",
    "overtake",
    "divine",
    "enthusiasm",
    "impeccably",
    "immense",
    "complement",
    "dependable",
    "colorful",
    "awe",
    "warmer",
    "astounding",
    "openly",
    "cozy",
    "transparent",
    "outstandingly",
    "magnificent",
    "fans",
    "guidance",
    "renowned",
    "mercifully",
    "profound",
    "appeal",
    "concise",
    "agile",
    "recommendations",
    "reliably",
    ])
    
    negative_words = set([

    "delayed",
    "delay",
    "bad",
    "worst",
    "lost",
    "rude",
    "poor",
    "problem",
    "issue",
    "missed",
    "delays",
    "terrible",
    "refused",
    "issues",
    "problems",
    "cheap",
    "uncomfortable",
    "lack",
    "limited",
    "expensive",
    "horrible",
    "miss",
    "worse",
    "hard",
    "awful",
    "fault",
    "disappointed",
    "broken",
    "wrong",
    "cold",
    "impossible",
    "complaint",
    "dirty",
    "unable",
    "stuck",
    "disappointing",
    "emergency",
    "slow",
    "nightmare",
    "cramped",
    "difficult",
    "ridiculous",
    "joke",
    "complaints",
    "denied",
    "mistake",
    "negative",
    "tired",
    "inconvenience",
    "lie",
    "complain",
    "useless",
    "unfriendly",
    "sorry",
    "frustrating",
    "unhelpful",
    "error",
    "unfortunately",
    "unacceptable",
    "unpleasant",
    "overweight",
    "excuse",
    "trouble",
    "lose",
    "incompetent",
    "ruined",
    "failed",
    "chaos",
    "waste",
    "mess",
    "complained",
    "shame",
    "chaotic",
    "scam",
    "hassle",
    "disgusting",
    "stress",
    "bother",
    "upset",
    "concern",
    "damaged",
    "limit",
    "shocked",
    "disappointment",
    "disaster",
    "poorly",
    "crowded",
    "hung",
    "risk",
    "annoying",
    "unreliable",
    "strike",
    "uneventful",
    "downside",
    "angry",
    "losing",
    "pain",
    "pathetic",
    "concerned",
    "confusion",
    "bothered",
    "refuse",
    "lied",
    "warning",
    "appalling",
    "blame",
    "loss",
    "worn",
    "mediocre",
    "noisy",
    "worried",
    "miserable",
    "confused",
    "loud",
    "badly",
    "wasted",
    "regret",
    "bumped",
    "stressful",
    "sad",
    "incompetence",
    "frustrated",
    "excuses",
    "insult",
    "hang",
    "failure",
    "refusing",
    "lacking",
    "unnecessary",
    "stupid",
    "disgrace",
    "annoyed",
    "overpriced",
    "unbelievable",
    "nasty",
    "strange",
    "damage",
    "broke",
    "concerns",
    "sick",
    "odd",
    "ignore",
    "fell",
    "trash",
    "break",
    "frustration",
    "lousy",
    "noise",
    "warned",
    "penalty",
    "spite",
    "rubbish",
    "disabled",
    "worry",
    "filthy",
    "smell",
    "hell",
    "doubt",
    "disrespectful",
    "unfortunate",
    "dreadful",
    "nervous",
    "unhappy",
    "unwilling",
    "rejected",
    "bland",
    "disgusted",
    "unexpected",
    "disorganized",
    "arrogant",
    "difficulties",
    "hate",
    "dark",
    "desert",
    "garbage",
    "weird",
    "injury",
    "delaying",
    "horrendous",
    "disinterested",
    "crazy",
    "refuses",
    "aggressive",
    "inefficient",
    "shocking",
    "sadly",
    "atrocious",
    "indifferent",
    "falling",
    "errors",
    "exhausted",
    "difficulty",
    "irresponsible",
    "die",
    "complaining",
    "unavailable",
    "confusing",
    "randomly",
    "scary",
    "pity",
    "freezing",
    "disgraceful",
    "strict",
    "grumpy",
    "false",
    "painful",
    "careless",
    "screwed",
    "lying",
    "suffer",
    "stale",
    "mistakes",
    "afraid",
    "severe",
    "funny",
    "ashamed",
    "inadequate",
    "struggling",
    "frozen",
    "excessive",
    "unknown",
    "incorrect",
    "fuss",
    "ignorant",
    "ordeal",
    "bored",
    "loose",
    "death",
    "unbearable",
    "ridiculously",
    "lazy",
    "rough",
    "ripped",
    "expired",
    "mad",
    "utterly",
    "wasting",
    "unusual",
    "boring",
    "panic",
    "shabby",
    "anxiety",
    "shock",
    "bumpy",
    "scared",
    "beware",
    "shameful",
    "messed",
    "fall",
    "split",
    "abysmal",
    "plague",
    "impolite",
    "fail",
    "furious",
    "misleading",
    "criticism",
    "trapped",
    "reluctantly",
    "suspect",
    "disregard",
    "unethical",
    "limits",
    "fraud",
    "dispute",
    "unsafe",
    "troubles",
    "headache",
    "negligence",
    "audacity",
    "discomfort",
    "lacked",
    "faulty",
    "irritating",
    "helpless",
    "downhill",
    "scrambling",
    "ruin",
    "terribly",
    "hurt",
    "misfortune",
    "suffered",
    "clueless",
    "fear",
    "apprehensive",
    "appalled",
    "bump",
    "inconsistent",
    "dead",
    "inability",
    "embarrassing",
    "absence",
    "gripe",
    "unclear",
    "upsetting",
    "steep",
    "outrageous",
    "dismay",
    "insane",
    "dismissive",
    "critical",
    "costly",
    "fragile",
    "struggle",
    "nonsense",
    "condescending",
    "criminal",
    "stolen",
    "anger",
    "cheated",
    "unbelievably",
    "unlikely",
    "challenging",
    "vice",
    "rip",
    "slowly",
    "shrug",
    "disturbing",
    "damn",
    "shambles",
    "inattentive",
    "urgent",
    "infuriating",
    "insufficient",
    "desperate",
    "complicated",
    "impatient",
    "illegal",
    "inexperienced",
    "bothering",
    "pricey",
    "anxious",
    "crisis",
    "ignorance",
    "cry",
    "unforeseen",
    "bug",
    "vague",
    "dishonest",
    "crashed",
    "disastrous",
    "weak",
    "worthless",
    "unsure",
    "unreasonable",
    "fussy",
    "abruptly",
    "stealing",
    "negatives",
    "wary",
    "sucks",
    "sink",
    "threatening",
    "curt",
    "hostile",
    "horrific",
    "awkward",
    "suffering",
    "virus",
    "restriction",
    "drag",
    "overwhelmed",
    "allergic",
    "exorbitant",
    "propaganda",
    "breaking",
    "deceptive",
    "deaf",
    "fried",
    "begging",
    "glitch",
    "scramble",
    "inconsiderate",
    "silly",
    "pretend",
    "lengthy",
    "petty",
    "inappropriate",
    "restricted",
    "dislike",
    "incapable",
    "bitter",
    "strangely",
    "beg",
    "uncaring",
    "fat",
    "inferior",
    "attack",
    "downgrade",
    "unkind",
    "breakdown",
    "mystery",
    "smoke",
    "painfully",
    "suspicious",
    "stiff",
    "harassed",
    "insulting",
    "tiring",
    "picky",
    "stranger",
    "cumbersome",
    "humiliating",
    "absurd",
    "dump",
    "complains",
    "smelly",
    "damages",
    "harsh",
    "vain",
    "distress",
    "worries",
    "irritated",
    "nuisance",
    "crushed",
    "substandard",
    "failing",
    "denying",
    "decline",
    "neglected",
    "lies",
    "misery",
    "cracked",
    "shoddy",
    "unlucky",
    "drunk",
    "crash",
    "horrid",
    "drain",
    "liable",
    "bulky",
    "needless",
    "problematic",
    "embarrassment",
    "nonexistent",
    "congested",
    "disruption",
    "abrupt",
    "fake",
    "inflexible",
    "dissatisfied",
    "unfamiliar",
    "conflicting",
    "wound",
    "messy",
    "harassment",
    "strictly",
    "invalid",
    "insulted",
    "louder",
    "deny",
    "tricky",
    "unsatisfactory",
    "drawback",
    "shortage",
    "fails",
    "crashing",
    "incorrectly",
    "hangs",
    "bumping",
    "smelled",
    "ripoff",
    "blind",
    "suck",
    "hectic",
    "lame",
    "disrespect",
    "reluctant",
    "blatant",
    "congestion",
    "adamant",
    "oversize",
    "discontinued",
    "stuffy",
    "struggled",
    "moody",
    "disappoint",
    "scrambled",
    "threat",
    "fiasco",
    "overloaded",
    "disgruntled",
    "unpredictable",
    "unappealing",
    "denial",
    "unprepared",
    "tentative",
    "subjected",
    "losses",
    "greedy",
    "shortcomings",
    "flimsy",
    "dizzy",
    "hefty",
    "struggles",
    "pitiful",
    "pointless",
    "sketchy",
    "extortion",
    "torture",
    "discourage",
    "slowest",
    "discouraging",
    "abuse",
    "stains",
    "desperately",
    "greasy",
    "unclean",
    "conflict",
    "worrying",
    "dirt",
    "deplorable",
    "faults",
    "traumatic",
    "mistakenly",
    "forbidden",
    "cheating",
    "ruining",
    "negligent",
    "skeptical",
    "outbreak",
    "outraged",
    "expire",
    "dissatisfaction",
    "poorest",
    "abrasive",
    "excessively",
    "arbitrary",
    "irritation",
    "questionable",
    "hopeless",
    "smells",
    "unreachable",
    "cruel",
    "rail",
    "danger",
    "remorse",
    "hated",
    "irrelevant",
    "unusable",
    "inhumane",
    "disgust",
    "dumped",
    "frantically",
    "uncertain",
    "grumble",
    "indifference",
    "tedious",
    "idiot",
    "dull",
    "dubious",
    "illness",
    "lacks",
    "stole",
    "fever",
    "overwhelming",
    "messing",
    "displeasure",
    "failures",
    "deceiving",
    "erratic",
    "crack",
    "stingy",
    "mislead",
    "burning",
    "madness",
    "oversight",
    "distressing",
    "invisible",
    "shockingly",
    "agony",
    "poorer",
    "apathetic",
    "threaten",
    "scolded",
    "rigid",
    "rattled",
    "deficient",
    "crooks",
    "tragic",
    "shake",
    "allergy",
    "bogus",
    "violation",
    "intolerable",
    "impending",
    "bully",
    "unexplained",
    "bullying",
    "sticky",
    "burden",
    "dangerous",
    "frantic",
    "hostility",
    "limitations",
    "despicable",
    "ironic",
    "unthinkable",
    "humiliation",
    "dismal",
    "unintelligible",
    "cheaply",
    "sceptical",
    "dragging",
    "exorbitantly",
    "weary",
    "dragged",
    "arrogance",
    "intrusive",
    "distressed",
    "discrimination",
    "sore",
    "rage",
    "uncomfortably",
    "steal",
    "inaccurate",
    "taxing",
    "perfunctory",
    "clogged",
    "insensitive",
    "laughable",
    "antiquated",
    "breach",
    "allergies",
    "reject",
    "defect",
    "unresponsive",
    "obscure",
    "fooled",
    "jerk",
    "detract",
    "annoy",
    "futile",
    "idle",
    "miserably",
    "stern",
    "toll",
    "revolting",
    "abusive",
    "overlook",
    "forbid",
    "darkness",
    "objection",
    "scratch",
    "accusing",
    "stumbled",
    "stampede",
    "sour",
    "confront",
    "disturb",
    "shady",
    "measly",
    "struck",
    "lackluster",
    "fuzzy",
    "draconian",
    "marginal",
    "inept",
    "redundant",
    "impertinent",
    "confrontational",
    "liability",
    "criticize",
    "isolated",
    "irate",
    "unusually",
    "smelt",
    "cloudy",
    "resistance",
    "gross",
    "attacks",
    "cons",
    "adverse",
    "disputed",
    "grossly",
    "needy",
    "grievances",
    "mistaken",
    "notorious",
    "punish",
    "stupidly",
    "contempt",
    "infested",
    "drawbacks",
    "wild",
    "disruptive",
    "disturbed",
    "brazen",
    "exaggeration",
    "scarce",
    "bothersome",
    "disarray",
    "hoax",
    "unscrupulous",
    "fright",
    "corrupt",
    "involuntary",
    "stodgy",
    "protest",
    "blurred",
    "apprehension",
    "impose",
    "loser",
    "obnoxious",
    "untrue",
    "sober",
    "interference",
    "repetitive",
    "insanely",
    "discriminatory",
    "quibble",
    "bizarre",
    "cheapen",
    "frustrations",
    "unexpectedly",
    "unspecified",
    "offensive",
    "complication",
    "sullen",
    "disagree",
    "lagging",
    "cranky",
    "foul",
    "inordinate",
    "meager",
    "plight",
    "criticisms",
    "debacle",
    "fraudulent",
    "chatter",
    "regretted",
    "freezes",
    "dust",
    "wedge",
    "irregularity",
    "indignation",
    "archaic",
    "cracks",
    "headaches",
    "ugly",
    "ineffective",
    "desperation",
    "unwelcome",
    "unimportant",
    "disproportionate",
    "unwillingness",
    "overdone",
    "scratched",
    "pittance",
    "leak",
    "abnormal",
    "restless",
    "junk",
    "unimaginable",
    "flaws",
    "unhealthy",
    "condemned",
    "unjustified",
    "snag",
    "dread",
    "stringent",
    "shameless",
    "unfit",
    "wrongly",
    "troublesome",
    "embarrassingly",
    "infection",
    "scrap",
    "bitterly",
    "frightfully",
    "ghastly",
    "panicking",
    "absurdly",
    "subpar",
    "scold",
    "defective",
    "unruly",
    "annoys",
    "dusty",
    "inaudible",
    "slower",
    "inexcusable",
    "conflicts",
    "inefficiency",
    "incomplete",
    "scare",
    "dumb",
    "unsuccessful",
    "harass",
    "lure",
    "stupidity",
    "burned",
    "inconsistency",
    "furiously",
    "negativity",
    "freaking",
    "mishap",
    "aborted",
    "ludicrous",
    "disdain",
    "displeased",
    "commotion",
    "insignificant",
    "drastic",
    "disapointed",
    "clumsy",
    "bust",
    "abort",
    "egregious",
    ])
    
    sentiment_score = 0
    words = review.lower().split()
    total_words = len(words)

    for word in words:
        if word in positive_words:
            sentiment_score += 1
        elif word in negative_words:
            sentiment_score -= 1

    # Normalizing the sentiment score by the total number of words
    if total_words > 0:
        normalized_sentiment = sentiment_score / (total_words * 0.25)
    else:
        normalized_sentiment = 0  # Handle case with empty review or no relevant words

    return round(normalized_sentiment, 4)

# Example usage
# score = sentiment("This was an amazing flight with great service.")
# print(score)
