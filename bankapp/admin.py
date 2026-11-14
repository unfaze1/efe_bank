
import streamlit as st
import pandas as pd
import hmac

st.title("🔐 EFE BANK Admin Panel")

# Admin login state
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# Login screen
if not st.session_state.admin_logged_in:

    username = st.text_input("Admin Username")
    password = st.text_input("Admin Password", type="password")

    if st.button("Login"):

        correct_username = st.secrets["admin"]["username"]
        correct_password = st.secrets["admin"]["password"]

        if (
            hmac.compare_digest(username, correct_username)
            and hmac.compare_digest(password, correct_password)
        ):
            st.session_state.admin_logged_in = True
            st.rerun()
        else:
            st.error("Incorrect username or password!")

# Admin dashboard
else:

    st.success("Welcome, Administrator!")

    if st.button("Logout"):
        st.session_state.admin_logged_in = False
        st.rerun()

    st.divider()

    # Read users
    df = pd.read_csv("user.csv")

    # Never display passwords
    safe_df = df.drop(columns=["Password"], errors="ignore")

    st.subheader("Registered Users")

    st.metric("Total Users", len(df))

    st.dataframe(safe_df, use_container_width=True)

    # Download user information without passwords
    csv = safe_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        "Download User Data",
        data=csv,
        file_name="users.csv",
        mime="text/csv"
    )


