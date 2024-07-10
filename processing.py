"""Back end processing of application."""
import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime


# Line breaks between containers
def nl(num_of_lines):
    for i in range(num_of_lines):
        st.write(" ")


# Select appropriate topics based on user-selected topics
def filter_topics_by_stages(topics, stages):
    relevant_topics = []
    if "Planning and Design" in stages:
        relevant_topics.extend(topics[:3])
    if "Data collection and model building" in stages:
        relevant_topics.extend(topics[3:6])
    if "Deployment" in stages:
        relevant_topics.extend(topics[6:])
    return relevant_topics


# Extract info from form answers
def process_statement_answers(name):
    for topic in ss['current_quiz']:
        scores = []
        # Aggregate scores from all three metrics
        coverage_key = f"coverage_{topic.name}"
        robustness_key = f"robustness_{topic.name}"
        inputdiversity_key = f"inputdiversity_{topic.name}"
        scores.extend([ss[coverage_key],
                       ss[robustness_key],
                       ss[inputdiversity_key]])
     
        # Aggregate rationales
        rationale_key = f"{topic.name}_rationale"
        ss['user_rationales'].append(ss[rationale_key])

        # Calculate total score
        score = sum(3 if rating == "High"
                    else (2 if rating == "Medium" else 1) for rating in scores)

        # Select appropriate conversion based on raw score
        if score == 3:
            ss['user_answers'].append(1)
        elif score in (4, 5):
            ss['user_answers'].append(2)
        elif score in (6, 7):
            ss['user_answers'].append(3)
        elif score == 8:
            ss['user_answers'].append(4)
        elif score == 9:
            ss['user_answers'].append(5)
 
    return process_answers(name)


# Aggregate scores/rationales
def process_topic_answers(name):
    for topic in ss['current_quiz']:
        ss['user_answers'].append(ss[topic.name])
        rationale_key = str(topic.name) + "_rationale"
        ss['user_rationales'].append(ss[rationale_key])
    return process_answers(name)


def process_answers(name):
    # Initialize dictionaries to store answers and counts
    pillar_answers = {
        "MAP": 0,
        "MEA": 0,
        "MAN": 0,
        "GOV": 0
    }
    dimension_answers = {
        "Ecology": 0,
        "IP_Copyright": 0,
        "Accuracy": 0,
        "Fairness": 0,
        "Human Oversight": 0,
        "Security": 0,
        "Privacy": 0
    }
    pillar_counts = {
        "MAP": 0,
        "MEA": 0,
        "MAN": 0,
        "GOV": 0
    }
    dimension_counts = {
        "Ecology": 0,
        "IP_Copyright": 0,
        "Accuracy": 0,
        "Fairness": 0,
        "Human Oversight": 0,
        "Security": 0,
        "Privacy": 0
    }

    # Iterate over topics in current_quiz
    for idx, topic in enumerate(ss['current_quiz']):
        # Separate scores into NIST pillars
        for pillar in topic.pillars_list:
            pillar_answers[pillar] += ss['user_answers'][idx]
            pillar_counts[pillar] += 1

        # Separate scores into risk dimensions
        for dimension in topic.dimensions_list:
            dimension_answers[dimension] += ss['user_answers'][idx]
            dimension_counts[dimension] += 1

    # Calculate averages and update ss averages
    for pillar in pillar_answers:
        if pillar_counts[pillar] != 0:
            average = pillar_answers[pillar] / pillar_counts[pillar]
            ss[f'{pillar.lower()}_average'] += average

    for dimension in dimension_answers:
        if dimension_counts[dimension] != 0:
            average = dimension_answers[dimension] / dimension_counts[dimension]
            ss[f'{dimension.lower().replace(" ", "_")}_average'] += average

    return topic_radar_chart(name)


# Create radar chart
def topic_radar_chart(name):
    fig1 = go.Figure()
    # Adding trace for the NIST Pillars
    title_name = name + " Scores by NIST Pillars"
    fig1.add_trace(go.Scatterpolar(
        r=[ss['gov_average'], ss['map_average'], ss['mea_average'],
            ss['man_average'], ss['gov_average']],
        theta=['GOVERN', 'MAP', 'MEASURE', 'MANAGE', 'GOVERN'],
        fill='toself',
        name='NIST Pillars'
    ))
    # Update layout of the radar chart
    fig1.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[1, 5]
            ),
        ),
        showlegend=False,
        title=title_name
    )

    fig2 = go.Figure()
    # Adding trace for the NIST Pillars
    title_name2 = name + " Scores by Responsibility Dimensions"
    fig2.add_trace(go.Scatterpolar(
        r=[ss['ecology_average'], ss['security_average'], ss['accuracy_average'],
            ss['privacy_average'], ss['human_oversight_average'],
            ss['ip_copyright_average'], ss['fairness_average'], ss['ecology_average']],
        theta=['Ecology', 'Security', 'Accuracy', 'Privacy', 'Human Oversight',
               'IP & Copyright', 'Fairness', 'Ecology'],
        fill='toself',
        name='Responsibility Dimensions'
    ))
    # Update layout of the radar chart
    fig2.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[1, 5]
            ),
        ),
        showlegend=False,
        title=title_name2
    )
    return fig1, fig2


# Aggregate responses and save to csv
def save_results_to_csv(system_name):
    # Create a list to hold the data
    data = []

    # Loop through the current quiz to collect the results
    for idx, topic in enumerate(ss['current_quiz']):
        topic_name = topic.name
        score = ss['user_answers'][idx]
        rationale = ss['user_rationales'][idx]
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Append a dictionary of the results
        data.append({
            "Date": timestamp,
            "System Name": system_name,
            "Topic Name": topic_name,
            "Score": score,
            "Rationale": rationale
        })

    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data)

    # Convert the DataFrame to a CSV string
    csv = df.to_csv(index=False)
    return csv


# Session state variables
ss = st.session_state
keys_to_initialize = [
    'current_quiz', 'user_answers', 'user_rationales',
    'gov_average', 'map_average', 'mea_average', 'man_average',
    'ecology_average', 'ip_copyright_average', 'privacy_average',
    'security_average', 'accuracy_average', 'fairness_average',
    'human_oversight_average'
]
for key in keys_to_initialize:
    if key not in ss:
        if key in ['user_answers', 'user_rationales', 'current_quiz']:
            ss[key] = []  # Initialize as empty lists for storing multiple values
        else:
            ss[key] = 0  # Initialize other keys as necessary