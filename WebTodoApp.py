import streamlit as st
import WebFileFunctions as wff
import os

filepath = "todo.txt"
todo_list = []


def todo_add():
    todo_value = st.session_state["Todo_I"]
    todo_list_local = wff.get_filedata(filepath)
    try:
        if todo_list_local.index(todo_value + "\n") >= 0:
            st.write("Duplicate Value")
    except ValueError:
        todo_list_local.append(todo_value + "\n")
        wff.write_filedata(filepath, todo_list_local)


def todo_selected(index):
    todo_list_local = wff.get_filedata(filepath)
    session_items = st.session_state.items()
    for key, value in enumerate(session_items):
        if value[1] == True:
            todo_list_local.pop(index)
            wff.write_filedata(filepath, todo_list_local)


if os.path.exists(filepath):
    print("false")
    todo_list = wff.get_filedata(filepath)
else:
    print("true")
    wff.create_file(filepath_arg=filepath)

st.title("To Do App - run from Apps folder")
st.subheader("Add items")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        wff.write_filedata(filepath, todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter to do", key="Todo_I", placeholder="Add to do..")
st.button(label="Add", on_click=todo_add, key="Todo_B")

st.session_state
