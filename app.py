import streamlit as st
import random

# App title
st.title("Random Kink Selector 🔥")

st.markdown("""
Edit the list of kinks below (one per line), adjust how many to select,  
and hit the button for random suggestions!
""")

# Default list of kinks (one per line for easy editing)
default_kinks = """Bondage
Discipline
Dominance
Submission
Sadism
Masochism
Roleplay
Age play
Pet play
Hand fetish
Spanking
Whipping
Gagging
Blindfolding
Wax play
Ice play
Edge play
Impact play
Voyeurism
Exhibitionism
Public play
Humiliation
Degradation
Praise kink
Orgasm denial
Forced orgasm
Anal play
Double penetration
Cum play
Watersports
Body worship
Sensation play
Temperature play
Food play
Objectification
Blackmail fetish
Consensual non-consent (CNC)
Kidnapping fantasy
Interrogation play
Home invasion fantasy
Stalker roleplay
Ravishment fantasy
Somnophilia
Free use
Dubcon (dubious consent)
Fear play
Pain play
Nipple torture
Clamps and clips
Verbal humiliation
Slut training
Pet training
Slave training
Orgasm control
Speech restriction
Collar fetish
Wet and messy (WAM)
Puppy play
Primal play
Predator/prey
Wrestling fetish
Erotic fighting
Breath control
Erotic photography
Clothing Fetish
StripTease Play
Doctor Patient RP
Insertion Play
Chemical Play
Oil Play
Time Play
Dirty Talk
Assistant/Maid Play
Boss Secretary
Spit Play
Outdoor sex (Car , Train ,Plane etc)
Tease Play
Landlord /Tenant RP
Body Writing"""

# Text area for editing the kink list
kinks_text = st.text_area(
    "Edit your kink list (one kink per line):",
    value=default_kinks,
    height=400
)

# Parse the text into a list, removing empty lines
kinks = [line.strip() for line in kinks_text.splitlines() if line.strip()]

# Sidebar controls
st.sidebar.header("Settings")
num_to_select = st.sidebar.slider("How many kinks to select?", min_value=1, max_value=10, value=3)

if st.sidebar.button("Generate Random Kinks"):
    if len(kinks) == 0:
        st.warning("Your kink list is empty! Add some kinks first.")
    elif len(kinks) < num_to_select:
        st.warning(f"Only {len(kinks)} kink(s) available. Selecting all.")
        selected = kinks
        random.shuffle(selected)
    else:
        selected = random.sample(kinks, num_to_select)
    
    st.success("Your randomly selected kinks are:")
    for i, kink in enumerate(selected, 1):
        st.markdown(f"**{i}.** {kink}")
    
    # Fun extra touch
    st.balloons()
else:
    st.info(f"Current list has **{len(kinks)}** kinks. Ready to generate when you click the button!")

# Optional: show count
st.caption(f"Total kinks in list: {len(kinks)}")
