from Statement import Statement
from Topic import Topic

def populatePillarsList(topic):
    for statement in topic.statements:
        topic.pillars_list.extend(statement.pillar)

def populateDimensionsList(topic):
    for statement in topic.statements:
        topic.dimensions_list.append(statement.responsibility_dimension)

# Topic 1 - Mapping impacts
statement1a = Statement(
    sentence="We document the goals, scope, and methods of this AI system.",
    topic=1,
    name = "1a",
    responsibility_dimension="Human Oversight",
    pillar=["MAP", "MAP", "MAP", "MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1b = Statement(
    sentence="We document the benefits and potential positive impacts of this AI system, including the likelihood and magnitude.",
    topic=1,
    name = "1b",
    responsibility_dimension="Human Oversight",
    pillar=["MAP", "MAP", "MAP", "GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1c = Statement(
    sentence="We document the business value of this AI system.",
    topic=1,
    name = "1c",
    responsibility_dimension="Human Oversight",
    pillar=["MAP", "MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1d = Statement(
    sentence="We document the possible negative impacts of this AI system, including the likelihood and magnitude.",
    topic=1,
    name = "1d",
    responsibility_dimension="Human Oversight",
    pillar=["GOV", "GOV", "GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1e = Statement(
    sentence="We document the potential costs of malfunctions of this AI system, including non-monetary costs such as decreased trustworthiness.",
    topic=1,
    name = "1e",
    responsibility_dimension="Human Oversight",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1f = Statement(
    sentence="We implement processes to integrate input about unexpected impacts.",
    topic=1,
    name = "1f",
    responsibility_dimension="Human Oversight",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement1g = Statement(
    sentence="We document the methods and tools we use for mapping impacts.",
    topic=1,
    name = "1g",
    responsibility_dimension="Human Oversight",
    pillar=["MAP", "MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic1 = Topic(
    sentence="We document what the AI will do and its potential impacts.",
    rationale="",
    evaluation="",
    stage=1,
    statements=[statement1a, statement1b, statement1c, statement1d, statement1e, statement1f, statement1g],
    name = 1
)

# Topic 2 - Documenting requirements
statement2a = Statement(
    sentence="We document the human oversight processes the system needs.",
    topic=2,
    name = "2a",
    responsibility_dimension="Human Oversight",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement2b = Statement(
    sentence="We document the technical standards and certifications the system will need to satisfy.",
    topic=2,
    name = "2b",
    responsibility_dimension="Accuracy",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement2c = Statement(
    sentence="We document AI legal requirements that apply to this AI system.",
    topic=2,
    name = "2c",
    responsibility_dimension="AP & Copyright",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic2 = Topic(
    sentence="We document basic requirements the system must meet.",
    rationale="",
    evaluation="",
    stage=1,
    statements=[statement2a, statement2b, statement2c],
    name = 2
)

# Topic 3 - Culture
statement3a = Statement(
    sentence="We write policies and guidelines about AI ethics.",
    topic=3,
    name = "3a",
    responsibility_dimension="Fairness",
    pillar=["GOV", "GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement3b = Statement(
    sentence="We document roles, responsibilities, and lines of communication related to AI risk management.",
    topic=3,
    name = "3b",
    responsibility_dimension="Human Oversight",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement3c = Statement(
    sentence="We provide training about AI ethics to relevant personnel.",
    topic=3,
    name = "3c",
    responsibility_dimension="Fairness",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement3d = Statement(
    sentence="We implement practices to foster critical thinking about AI risks.",
    topic=3,
    name = "3d",
    responsibility_dimension="Human Oversight",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic3 = Topic(
    sentence="We cultivate AI ethics mindsets.",
    rationale="",
    evaluation="",
    stage=1,
    statements=[statement3a, statement3b, statement3c, statement3d],
    name = 3
)

# Topic 4 - Measuring risk
statement4a = Statement(
    sentence="We document and periodically re-evaluate our strategy for measuring the impacts of this AI system. It includes choosing which impacts we measure. It also includes how we will approach monitoring unexpected impacts and impacts that can’t be captured with existing metrics.",
    topic=4,
    name = "4a",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4b = Statement(
    sentence="We document the methods and tools we use to measure the impacts of this AI system.  It includes which metrics and datasets we use",
    topic=4,
    name = "4b",
    responsibility_dimension="Human Oversight",
    pillar=["MEA", "MEA", "MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4c = Statement(
    sentence="We document the effectiveness of our measurement processes.",
    topic=4,
    name = "4c",
    responsibility_dimension="Accuracy",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4d = Statement(
    sentence="We regularly evaluate and document the performance of this AI system in conditions similar to deployment.",
    topic=4,
    name = "4d",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4e = Statement(
    sentence="We regularly evaluate and document bias and fairness issues related to this AI system.",
    topic=4,
    name = "4e",
    responsibility_dimension="Fairness",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4f = Statement(
    sentence="We regularly evaluate and document privacy issues related to this AI system.",
    topic=4,
    name = "4f",
    responsibility_dimension="Privacy",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4g = Statement(
    sentence="We regularly evaluate and document environmental impacts related to this AI system.",
    topic=4,
    name = "4g",
    responsibility_dimension="Ecology",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4h = Statement(
    sentence="We regularly evaluate and document transparency and accountability issues related to this AI system.",
    topic=4,
    name = "4h",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4i = Statement(
    sentence="We regularly evaluate and document security and resilience issues related to this AI system.",
    topic=4,
    name = "4i",
    responsibility_dimension="Security",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4j = Statement(
    sentence="We regularly evaluate and document explainability issues related to this AI system.",
    topic=4,
    name = "4j",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4k = Statement(
    sentence="We regularly evaluate and document third-party issues, such as IP infringement, related to this AI system.",
    topic=4,
    name = "4k",
    responsibility_dimension="IP & Copyright",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4l = Statement(
    sentence="We regularly evaluate and document other impacts related to this AI system.",
    topic=4,
    name = "4l",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement4m = Statement(
    sentence="If evaluations use human subjects, they are representative and meet appropriate requirements.",
    topic=4,
    name = "4m",
    responsibility_dimension="Fairness",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic4 = Topic(
    sentence="We measure our potential negative impacts.",
    rationale="",
    evaluation="",
    stage=2,
    statements=[statement4a, statement4b, statement4c, statement4d, statement4e, statement4f, statement4g, statement4h, statement4i, statement4j, statement4k, statement4l, statement4m],
    name=4
)

# Topic 5 - Transparency
statement5a = Statement(
    sentence="We document information about the system’s limitations and options for human oversight related to this AI system. The documentation is good enough to assist those who need to make decisions based on the system’s outputs.",
    topic=5,
    name = "5a",
    responsibility_dimension="Human Oversight",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement5b = Statement(
    sentence="We document the system risk controls, including in third-party components.",
    topic=5,
    name = "5b",
    responsibility_dimension="Human Oversight",
    pillar=["MAP"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement5c = Statement(
    sentence="We explain the model to ensure responsible use.",
    topic=5,
    name = "5c",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement5d = Statement(
    sentence="We inventory information about this AI system in a repository of our AI systems.",
    topic=5,
    name = "5d",
    responsibility_dimension="Human Oversight",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic5 = Topic(
    sentence="We document information about the system’s limitations and risk control.",
    rationale="",
    evaluation="",
    stage=2,
    statements=[statement5a, statement5b, statement5c, statement5d],
    name = 5
)

# Topic 6 - Management plan
statement6a = Statement(
    sentence="We plan and document how we will respond to the risks caused by this AI system. The response options can include mitigating, transferring, avoiding, or accepting risks.",
    topic=6,
    name = "6a",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement6b = Statement(
    sentence="We prioritize the responses to the risks of this AI system based on impact, likelihood, available resources or methods, and the organization’s risk tolerance.",
    topic=6,
    name = "6b",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement6c = Statement(
    sentence="We document the residual risks of this AI system (the risks that we do not mitigate). The documentation includes risks to buyers and users of the system.",
    topic=6,
    name = "6c",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement6d = Statement(
    sentence="We have a plan for addressing unexpected risks related to this AI system as they come up.",
    topic=6,
    name = "6d",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic6 = Topic(
    sentence="We plan how we will respond to risks.",
    rationale="",
    evaluation="",
    stage=2,
    statements=[statement6a, statement6b, statement6c, statement6d],
    name = 6
)

# Topic 7 - Risk mitigation
statement7a = Statement(
    sentence="We proactively evaluate whether this system meets its stated objectives and whether its development or deployment should proceed.",
    topic=7,
    name = "7a",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7b = Statement(
    sentence="We ensure this AI’s bias and fairness performance stays meets our standards.",
    topic=7,
    name = "7b",
    responsibility_dimension="Fairness",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7c = Statement(
    sentence="We ensure this AI’s privacy performance meets our standards.",
    topic=7,
    name = "7c",
    responsibility_dimension="Privacy",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7d = Statement(
    sentence="We ensure this AI’s environmental performance meets our standards.",
    topic=7,
    name = "7d",
    responsibility_dimension="Ecology",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7e = Statement(
    sentence="We ensure this AI’s transparency and accountability meets our standards.",
    topic=7,
    name = "7e",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7f = Statement(
    sentence="We ensure this AI’s security and resilience meets our standards.",
    topic=7,
    name = "7f",
    responsibility_dimension="Security",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7g = Statement(
    sentence="We ensure this AI’s explainability performance meets our standards.",
    topic=7,
    name = "7g",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7h = Statement(
    sentence="We ensure this AI’s third-party impacts, such as IP infringement, meet our standards.",
    topic=7,
    name = "7h",
    responsibility_dimension="IP & Copyright",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7i = Statement(
    sentence="We implement processes for human oversight related to this AI system.",
    topic=7,
    name = "7i",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7j = Statement(
    sentence="We implement processes for appeal related to this AI system.",
    topic=7,
    name = "7j",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7k = Statement(
    sentence="We maintain end-of-life mechanisms to supersede, disengage, or deactivate this AI system if its performance or outcomes are inconsistent with the intended use.",
    topic=7,
    name = "7k",
    responsibility_dimension="Human Oversight",
    pillar=["MAN", "GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7l = Statement(
    sentence="We address all other risks prioritized in our plans related to this system by conducting measurable activities.",
    topic=7,
    name = "7l",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7m = Statement(
    sentence="We address unexpected risks related to this system by conducting measurable activities.",
    topic=7,
    name = "7m",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement7n = Statement(
    sentence="We track and respond to errors and incidents related to this system by conducting measurable activities.",
    topic=7,
    name = "7n",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic7 = Topic(
    sentence="We act to minimize the risks we identify.",
    rationale="",
    evaluation="",
    stage=2,
    statements=[statement7a, statement7b, statement7c, statement7d, statement7e, statement7f, statement7g, statement7h, statement7i, statement7j, statement7k, statement7l, statement7m, statement7n],
    name = 7
)

# Topic 8 - Pre-deployment checks
statement8a = Statement(
    sentence="We demonstrate that this system is valid, reliable, and meets our standards. We document the conditions under which it falls short.",
    topic=8,
    name = "8a",
    responsibility_dimension="Accuracy",
    pillar=["MEA", "MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic8 = Topic(
    sentence="We only release versions that meet our AI ethics standards.",
    rationale="",
    evaluation="",
    stage=3,
    statements=[statement8a],
    name = 8
)

# Topic 9 - Monitoring
statement9a = Statement(
    sentence="We plan how to monitor risks related to this system post-deployment.",
    topic=9,
    name = "9a",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9b = Statement(
    sentence="We monitor this system’s functionality and behavior post-deployment.",
    topic=9,
    name = "9b",
    responsibility_dimension="Human Oversight",
    pillar=["MEA"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9c = Statement(
    sentence="We apply mechanisms to sustain the value of this AI system post-deployment.",
    topic=9,
    name = "9c",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9d = Statement(
    sentence="We capture and evaluate input from users about this system post-deployment.",
    topic=9,
    name = "9d",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9e = Statement(
    sentence="We monitor appeal and override processes related to this system post-deployment.",
    topic=9,
    name = "9e",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9f = Statement(
    sentence="We monitor incidents related to this system and responses to them post-deployment.",
    topic=9,
    name = "9f",
    responsibility_dimension="Human Oversight",
    pillar=["MAN", "MAN", "MAN", "MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9g = Statement(
    sentence="We monitor incidents related to high-risk third-party components and respond to them.",
    topic=9,
    name = "9g",
    responsibility_dimension="Human Oversight",
    pillar=["GOV"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9h = Statement(
    sentence="We implement all other components of our post-deployment monitoring plan for this system.",
    topic=9,
    name = "9h",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
statement9i = Statement(
    sentence="We monitor issues that would trigger our end-of-life mechanisms for this system, and we take the system offline if issues come up.",
    topic=9,
    name = "9i",
    responsibility_dimension="Human Oversight",
    pillar=["MAN"],
    robust_eval="",
    diverse_eval="",
    rationale=""
)
topic9 = Topic(
    sentence="We monitor and resolve issues as they arise.",
    rationale="",
    evaluation="",
    stage=3,
    statements=[statement9a, statement9b, statement9c, statement9d, statement9e, statement9f, statement9g, statement9h, statement9i],
    name=9
)

topics = [topic1, topic2, topic3, topic4, topic5, topic6, topic7, topic8, topic9]
for topic in topics:
    populatePillarsList(topic)
    populateDimensionsList(topic)

# Creating a list of all statements
statements = [
    statement1a, statement1b, statement1c, statement1d, statement1e, statement1f, statement1g,
    statement2a, statement2b, statement2c,
    statement3a, statement3b, statement3c, statement3d,
    statement4a, statement4b, statement4c, statement4d, statement4e, statement4f, statement4g, statement4h, statement4i, statement4j, statement4k, statement4l, statement4m,
    statement5a, statement5b, statement5c, statement5d,
    statement6a, statement6b, statement6c, statement6d,
    statement7a, statement7b, statement7c, statement7d, statement7e, statement7f, statement7g, statement7h, statement7i, statement7j, statement7k, statement7l, statement7m, statement7n,
    statement8a,
    statement9a, statement9b, statement9c, statement9d, statement9e, statement9f, statement9g, statement9h, statement9i
]





