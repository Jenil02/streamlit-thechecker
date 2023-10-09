import streamlit as st

st.text('Welcome to Streamlit! ')

def form_callback():
    st.write(st.session_state.my_text)
    st.write(st.session_state.my_text_2)

num_tags = st.number_input("Select number of errors", 0, 300)

with st.form(key='my_form'):
    error_text, corr_text = st.columns(2)
    with error_text:
        st.image('/Users/jenil/Desktop/Pasted_graphic_1.png')

    with corr_text:
        st.write('This is the right column')

    tags = []
    sizes = []
    st.header("Corrections")
    col1, col2 = st.columns(2)


    for i in range(1, 1+num_tags):
        tag = col1.text_input(f"Error {i}", key=f"tag_{i}")
        size = col2.text_input(f"Correction {i}", key=f"size_{i}")
        tags.append(tag)
        sizes.append(size)
    
    submit_button = st.form_submit_button(label='Submit', on_click=form_callback)

# if 'sum' not in st.session_state:
#     st.session_state.sum = ''

# col1,col2 = st.columns(2)
# col1.title('Sum:')
# if isinstance(st.session_state.sum, float):
#     col2.title(f'{st.session_state.sum:.2f}')

# with st.form('addition'):
#     a = st.number_input('a')
#     b = st.number_input('b')
#     submit = st.form_submit_button('add')

# The value of st.session_state.sum is updated at the end of the script rerun,
# so the displayed value at the top in col2 does not show the new sum. Trigger
# a second rerun when the form is submitted to update the value above.
# st.session_state.sum = a + b
# if submit:
#     st.rerun()



# with st.form(key='my_form'):
#     on = form.toggle('Activate feature')

#     if on:
#         col1, col2 = st.columns(2)
#         with col1:
#             text_input = st.text_input(
#             "Error line 👇",
#         )
#         with col2:
#             text_input = st.text_input(
#             "Corrected line 👇",
#             )
    
#     submitted = st.form_submit_button("Submit")