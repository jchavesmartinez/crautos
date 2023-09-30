import streamlit as st

# Function to add values to the selectbox
def add_values_to_selectbox():
    # Add your logic to fetch or generate new values
    new_values = ["Option 1", "Option 2", "Option 3"]
    return new_values

# Streamlit app
def main():
    st.title("Dynamic Selectbox Example")

    # Initial set of values for the selectbox
    initial_values = ["Option A", "Option B", "Option C"]

    # Create a selectbox with initial values
    selected_option = st.selectbox("Select an option", initial_values)

    # Button to trigger the update of selectbox values
    if st.button("Add Values"):
        # Get new values
        new_values = add_values_to_selectbox()

        # Update selectbox with new values
        selected_option = st.selectbox("Select an option", initial_values + new_values)

    # Display the selected option
    st.write("You selected:", selected_option)

if __name__ == "__main__":
    main()