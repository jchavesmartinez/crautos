import streamlit as st
from session_state import get

# Function to initialize session state
def init_session():
    return get(cost=0.0)

# Function to update the cost
def update_cost(session, new_cost):
    session.cost += new_cost

# Main app
def main():
    # Initialize session state
    session_state = init_session()

    # Display initial cost
    st.write(f"Initial Cost: ${session_state.cost:.2f}")

    # Add a new cost
    new_cost = st.number_input("Enter New Cost:", step=0.01, format="%f")
    
    if st.button("Add Cost"):
        update_cost(session_state, new_cost)

    # Display updated cost
    st.write(f"Updated Cost: ${session_state.cost:.2f}")

if __name__ == "__main__":
    main()