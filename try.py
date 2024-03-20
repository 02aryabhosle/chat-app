import streamlit as st
def main():
    st.title('Query Response System')
    
    user_input = st.text_input("Please enter your query", "")
    
    if st.button('Submit'):
        if user_input:
            st.write(f'You asked: {user_input}')
            st.write('Here is your response: ...')  # Add your response logic here
        else:
            st.write('Please enter a query.')

if __name__ == "__main__":
    main()