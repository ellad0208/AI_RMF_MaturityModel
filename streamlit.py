"""Streamlit front end."""
import streamlit as st
import streamlit_nested_layout
import plotly.graph_objects as go
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from quiz import topics, statements
from processing import *

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

# Replace with your credentials file path
CREDENTIALS_FILE = 'credentials.json'

# Replace with your Google Sheet URL
SHEET_URL = "https://docs.google.com/spreadsheets/d/1jnvgjUBggHgx5lVTD8Sc4AbBVez3-XoJn5thg2A589A/edit?gid=0#gid=0"

def save_feedback_data(name, email, feedback):
    gc = gspread.service_account(filename=CREDENTIALS_FILE)
    spreadsheet = gc.open_by_url(SHEET_URL)
    sheet = spreadsheet.sheet1  # Get the first sheet
    data = [name, email, feedback]
    st.write(data)
    sheet.append_row(data)
    st.success("Feedback submitted successfully.")

#Page introduction
st.set_page_config(page_title="NIST AI Maturity Assessment", page_icon=":control_knobs:", layout="centered", initial_sidebar_state="auto", menu_items=None)
st.title("NIST AI RMF Maturity Model Assessment Tool")
paper_url = "https://arxiv.org/abs/2401.15229"
nist_url = "https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF"
"This tool implements the NIST AI Risk Management Framework maturity model put forth by Ravit Dotan, Borhane Blili-Hamelin, Ravi Madhavan, Jeanna Matthews, and Joshua Scarpino in their paper \"[Evolving AI Risk Management: A Maturity Model based on the NIST AI Risk Management Framework](%s)\". his assessment is not meant to be objective,  but rather to communicate evaluations and reasons for those evaluations that can help organizations understand where they are and how they can improve." %paper_url
"I hope to facilitate the collection of further feedback on the maturity model and make the model easier to access for organizations who may choose to use it. Fill out the model, receive personalized insights and charts, give your feedback, and save your answers and the results to track progression over time."
st.markdown("[:violet[Learn more about the National Institute of Standards and Technology's AI Risk Management Framework.]](%s)" %nist_url)
nl(1)

#Assessment settings
stages = st.multiselect(
    "What stages are relevant to your AI system?",
    ["Planning and Design", "Data collection and model building", "Deployment"],
    placeholder="Select options...")
granularity = st.selectbox(
    "Please select your desired level of granularity.",
    ("Topics (up to 9 questions)", "Statements (up to 27 questions)"),
    index = None,
    placeholder="Choose an option...")


#Grabbing correct questions
ss['current_quiz'] = filter_topics_by_stages(topics, stages)

if granularity and stages:
    #Topic-level assessment
    if granularity == "Topics (up to 9 questions)":
        nl(1)
        #FAQ
        with st.expander(label = ":red[If this is your first time using the assessment tool, please consider reading these guidelines.]"):
            with st.expander("What metrics am I evaluating?"):
                "When scoring, each evaluated statement should be ranked on a scale of 1-5, where 1 is the lowest and 5 is the highest, based on how well it satisfies three metrics:"
                st.markdown("*1. Coverage of RMF subcategories:* the scoring of the topic statement should reflect the coverage of all the individual statements included in that topic. All substatements are listed below the topic statement.")
                st.markdown("*2. Robustness:* - The risk management activities are")
                st.write("""(1) Regular - Performed in a routine manner  
                (2) Systematic - Follow policies that are well-defined and span company-wide  
                (3) Trained Personnel - Performed by people who are properly trained and whose roles in the activities are clearly defined  
                (4) Sufficiently Resourced - Supported by sufficient resources, including budget, time, compute power, and cutting-edge tools  
                (5) Adaptive - Adapting to changes in the landscape and product, including regular reviews and effective contingency processes to respond to failure  
                (6) Cross-functional - Involve all core business units and senior management. They are informed of the outcomes and contribute to decision-making, strategy, and resource allocation related to the activities (core business units include finance, customer support, HR, marketing, sales, etc).""")
                st.markdown("*3. Input diversity:* A low level of input diversity means that the relevant activities receive input from relatively few kinds of stakeholders, while high levels of input diversity mean that the activities receive input from diverse internal and external stakeholders, such as civil society organizations, customers, and employees.")
            with st.expander("How should I quantify those metrics?"):
                """
                Scores ranges between 1-5, where 1 is the lowest and 5 is the highest. We developed the following as a rule of thumb for determining scores:
                5: HHH. All three metrics are satisfied to a high degree.
                4: HHM. Two of the metrics are satisfied to a high degree and one to a medium degree.
                3: HMM, HHL, HML, or MMM. One of the following is the case: 
                - Two of the metrics are satisfied to a medium degree and one to a high degree;
                - Two of the metrics are satisfied to a high degree and one to a low degree;
                - One metric is satisfied to a high degree, one to a medium degree, and one to a low degree;
                - All metrics are satisfied to a medium degree.
                2: MML, MLL, or HLL. One of the following is the case: 
                - Two of the metrics are satisfied to a medium degree and one to a low degree;
                - One metric is satisfied to a medium degree and two to a low degree;
                - One of the metrics is satisfied to a high degree and two to a low degree.
                1: LLL. All metrics are satisfied to a low or nonexistent degree.
                """
            with st.expander("Are these scores \"objective\"?"):
                st.write("Scoring AI responsibility involves a great degree of personal judgment. The goal is not to produce “objective” scores but rather to communicate evaluations and reasons for those evaluations that can help organizations understand where they are and how they can improve. These scoring guidelines are designed to facilitate this kind of evaluation by guiding evaluators to provide evidence-based, well-reasoned evaluations that are based on expectations drawn from NIST’s work.")
            with st.expander("Why am I asked to provide evidence/rationale?"):
                st.write("Providing evidence encourages accountability in the evaluation process because it requires the evaluator to base the scoring on information that others can assess, too. Moreover, requiring evaluators to provide evidence also encourages accountability on the part of the evaluated companies, because it encourages them to ensure that such evidence is available. Companies can do so, for example, by documenting key processes and their outcomes. Providing evidence for scoring improves the usefulness of the evaluation because it contextualizes and explains the reason for the score. Numbers on their own don’t offer much information about the company, what they currently do, what is missing, and how they can improve. The evidence an evaluator cites helps others understand how the evaluator interprets the scoring guidelines and what a given score means to that evaluator. This can help companies understand what they are doing right and how to do better.")
        nl(1)

        #form to collect answers
        with st.form(key = "topic_form", border = False):
            #Topic template
            system_name = st.text_input(":red[Label your system:]")
            for topic in ss['current_quiz']:
                with st.container(border = True):
                    st.markdown(f"##### Topic {topic.name}: {topic.sentence}")
                    for statement in topic.statements:
                        st.markdown(f"- *{statement.sentence}*")
                    st.write("Assign a score based on coverage of the above statements, robustness, and input diversity.")
                    topic_slider = st.slider("Score", 1, 5, 3, key = topic.name, help = "5 = HHH. 4 = HHM. 3 = HMM, HHL, HML, or MMM. 2 = MML, MLL, or HLL. 1 = LLL.")
                    rationale_key = str(topic.name) + "_rationale"
                    st.text_area(label= "Explanation/Rationale", key = rationale_key, help = "Evidence includes information about what organizations do, about what they don’t do, and reports of lack of evidence. For example, evidence may include describing artifacts that indicate that the company is engaged in the relevant activities or the evaluator’s first-hand experience in the company. E.g., they may describe which company documents contain the relevant information and how detailed that information is, the evaluator’s first-hand knowledge about the execution of the relevant tasks, and so on. Evidence may also include indications that certain activities are not performed, which may happen, for example, when company documents imply that these activities are outside of the company’s current scope. Further, evidence discussions may also include pointing out a lack of evidence. We ask evaluators to note in their comments a distinction between lack of any evidence and presence of evidence to the contrary.")
            submitted = st.form_submit_button("Submit")
        done = False
        if submitted: 
            done = True
            if system_name:
                topic_csv = save_results_to_csv(system_name)
                filename = system_name + "_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
                st.download_button("Download CSV of Results", data=topic_csv, file_name=filename, mime='text/csv')
            else:
                st.warning("Please label your system to download the results.")
            fig1, fig2 = process_topic_answers(system_name)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
            
        if done:
            with st.form(key = "feedback_form"):
                st.write("Your personal data will only be shared with the creator of this web app (Ella Duus) and the maturity model study authors (Ravit Dotan, Borhane Blili-Hamelin, Ravi Madhavan, Jeanna Matthews, and Joshua Scarpino) to facilitate the improvement of the maturity model. Your aggregated anonymized feedback data may be shared in an academic context")
                name = st.text_input("Please enter your name (optional)")
                email = st.text_input("Please enter your email (optional)")
                feedback = st.text_area("Please give your feedback on this maturity model")
                submit = st.form_submit_button("Submit")
            if submit:
                save_feedback_data(name, email, feedback)
        
        
    #Statement-level assessment
    elif granularity == "Statements (up to 27 questions)":
        nl(1)
        #FAQ
        with st.expander(label = ":red[If this is your first time using the assessment tool, please consider reading these guidelines.]"):
            with st.expander("What metrics am I evaluating?"):
                "When scoring, each evaluated statement should be ranked on a scale of 1-5, where 1 is the lowest and 5 is the highest, based on how well it satisfies three metrics:"
                st.markdown("*1. Coverage of RMF subcategories:* the scoring of the topic statement should reflect the coverage of all the individual statements included in that topic. All substatements are listed below the topic statement.")
                st.markdown("*2. Robustness:* - The risk management activities are")
                st.write("""(1) Regular - Performed in a routine manner  
                (2) Systematic - Follow policies that are well-defined and span company-wide  
                (3) Trained Personnel - Performed by people who are properly trained and whose roles in the activities are clearly defined  
                (4) Sufficiently Resourced - Supported by sufficient resources, including budget, time, compute power, and cutting-edge tools  
                (5) Adaptive - Adapting to changes in the landscape and product, including regular reviews and effective contingency processes to respond to failure  
                (6) Cross-functional - Involve all core business units and senior management. They are informed of the outcomes and contribute to decision-making, strategy, and resource allocation related to the activities (core business units include finance, customer support, HR, marketing, sales, etc).""")
                st.markdown("*3. Input diversity:* A low level of input diversity means that the relevant activities receive input from relatively few kinds of stakeholders, while high levels of input diversity mean that the activities receive input from diverse internal and external stakeholders, such as civil society organizations, customers, and employees.")
            with st.expander("How should I quantify those metrics?"):
                """
                Please rate the coverage, robustness, and input diversity based on how well they are satisfied, using the following scale: low, medium, or high.
                """
            with st.expander("Are these scores \"objective\"?"):
                st.write("Scoring AI responsibility involves a great degree of personal judgment. The goal is not to produce “objective” scores but rather to communicate evaluations and reasons for those evaluations that can help organizations understand where they are and how they can improve. These scoring guidelines are designed to facilitate this kind of evaluation by guiding evaluators to provide evidence-based, well-reasoned evaluations that are based on expectations drawn from NIST’s work.")
            with st.expander("Why am I asked to provide evidence/rationale?"):
                st.write("Providing evidence encourages accountability in the evaluation process because it requires the evaluator to base the scoring on information that others can assess, too. Moreover, requiring evaluators to provide evidence also encourages accountability on the part of the evaluated companies, because it encourages them to ensure that such evidence is available. Companies can do so, for example, by documenting key processes and their outcomes. Providing evidence for scoring improves the usefulness of the evaluation because it contextualizes and explains the reason for the score. Numbers on their own don’t offer much information about the company, what they currently do, what is missing, and how they can improve. The evidence an evaluator cites helps others understand how the evaluator interprets the scoring guidelines and what a given score means to that evaluator. This can help companies understand what they are doing right and how to do better.")
        nl(1)
        with st.form(key = "statement_form", border = False):
            system_name = st.text_input(":red[Label your system:]")
            for topic in ss['current_quiz']:
                with st.container(border = True):
                    st.markdown(f"##### Topic {topic.name}: {topic.sentence}")
                    for statement in topic.statements:
                        st.markdown(f"- *{statement.sentence}*")
                    coverage_key = f"coverage_{topic.name}"
                    robustness_key = f"robustness_{topic.name}"
                    inputdiversity_key = f"inputdiversity_{topic.name}"
                    coverage_slider = st.select_slider("Coverage Level",options = ["Low", "Medium", "High"], key = coverage_key, value = "Medium", help = "The scoring of the topic statement should reflect coverage of all the individual statements included in that topic. For example, companies that evaluate and document security but not fairness risks satisfy this metric to a degree lower than companies that address both.")
                    robustness_slider = st.select_slider("Robustness Level",options = ["Low", "Medium", "High"], key = robustness_key, value = "Medium", help = "Robustness - The risk management activities are \n(1) Regular - Performed in a routine manner \n(2) Systematic - Follow policies that are well-defined and span company-wide \n(3) Trained Personnel - Performed by people who are properly trained and whose roles in the activities are clearly defined \n(4) Sufficiently Resourced - Supported by sufficient resources, including budget, time, compute power, and cutting-edge tools \n(5) Adaptive - Adapting to changes in the landscape and product, including regular reviews and effective contingency processes to respond to failure \n(6) Cross-functional - Involve all core business units and senior management. They are informed of the outcomes and contribute to decision-making, strategy, and resource allocation related to the activities (core business units include finance, customer support, HR, marketing, sales, etc)")
                    inputdiversity_slider = st.select_slider("Input Diversity Level",options = ["Low", "Medium", "High"], value = "Medium", key = inputdiversity_key, help = "Input diversity means that risk management activities receive input from diverse internal and external stakeholders. A low level of input diversity means that the relevant activities receive input from relatively few kinds of stakeholders.  High levels of input diversity mean that the activities receive input from diverse internal and external stakeholders. For example, suppose that a company chooses its fairness metrics in consultation with civil society organizations, surveys of diverse customers administered by the customer success team, and conversations with diverse employees in the company. In that case, the company demonstrates a high level of input diversity with regard to the statement \"We evaluate and document bias and fairness issues related to this AI system\"")
                    rationale_key = str(topic.name) + "_rationale"
                    st.text_area(label= "Explanation/Rationale", key = rationale_key, help = "Evidence includes information about what organizations do, about what they don’t do, and reports of lack of evidence. For example, evidence may include describing artifacts that indicate that the company is engaged in the relevant activities or the evaluator’s first-hand experience in the company. E.g., they may describe which company documents contain the relevant information and how detailed that information is, the evaluator’s first-hand knowledge about the execution of the relevant tasks, and so on. Evidence may also include indications that certain activities are not performed, which may happen, for example, when company documents imply that these activities are outside of the company’s current scope. Further, evidence discussions may also include pointing out a lack of evidence. We ask evaluators to note in their comments a distinction between lack of any evidence and presence of evidence to the contrary.")
            submitted = st.form_submit_button("Submit")
        done = False
        if submitted:
            if system_name:
                topic_csv = save_results_to_csv(system_name)
                filename = system_name + "_" + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + ".csv"
                st.download_button("Download CSV of Results", data=topic_csv, file_name=filename, mime='text/csv')
            else:
                st.warning("Please label your system to download the results.")
            done = True
            fig1, fig2 = process_statement_answers(system_name)
            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
        if done:
            with st.form(key = "feedback_form"):
                st.write("Your personal data will only be shared with the creator of this web app (Ella Duus) and the maturity model study authors (Ravit Dotan, Borhane Blili-Hamelin, Ravi Madhavan, Jeanna Matthews, and Joshua Scarpino) to facilitate the improvement of the maturity model. Your aggregated anonymized feedback data may be shared in an academic context")
                name = st.text_input("Please enter your name (optional)")
                email = st.text_input("Please enter your email (optional)")
                feedback = st.text_area("Please give your feedback on this maturity model")
                submit = st.form_submit_button("Submit")
            if submit:
                save_feedback_data(name, email, feedback)

