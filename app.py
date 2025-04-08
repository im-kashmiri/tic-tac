# tic_tac_toe_app.py

import streamlit as st

# Session state for game state
if 'board' not in st.session_state:
    st.session_state.board = [" "] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

def check_winner(board):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]
    return None

def reset_game():
    st.session_state.board = [" "] * 9
    st.session_state.turn = "X"
    st.session_state.winner = None

st.title("🎮 Tic Tac Toe")

cols = st.columns(3)
for i in range(9):
    if st.session_state.board[i] == " " and not st.session_state.winner:
        if cols[i % 3].button(" ", key=i):
            st.session_state.board[i] = st.session_state.turn
            st.session_state.winner = check_winner(st.session_state.board)
            if not st.session_state.winner:
                st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
    else:
        cols[i % 3].button(st.session_state.board[i], key=i, disabled=True)

if st.session_state.winner:
    st.success(f"🎉 Player {st.session_state.winner} wins!")
elif " " not in st.session_state.board:
    st.info("It's a draw!")

st.button("🔁 Reset", on_click=reset_game)
