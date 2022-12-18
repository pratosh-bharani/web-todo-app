import streamlit as st
import functions

todos = functions.get_todos()

st.set_page_config(layout="wide")
def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    functions.write_todos(todos)



st.title('My Todo App')
st.subheader('This is my Todo App')
st.write('This App is to increase your productivity')

for index, todo in enumerate(todos):
    key_todo = f"{todo}_{str(index)}"
    checkbox = st.checkbox(todo, key=key_todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[key_todo]
        st.experimental_rerun()

st.text_input(label="", placeholder = "Add new todo...",
              on_change=add_todo, key="new_todo")

