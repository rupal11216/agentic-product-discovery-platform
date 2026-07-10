import os
import tempfile

import streamlit as st

from shopping_agent import agent

# ---------------------------------------------------------------------
# Page configuration
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="AI Shopping Assistant",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🛒 AI Shopping Assistant")

st.markdown(
    """
Search products using natural language or upload an image to discover similar products.

**Capabilities**

- Product Search
- Visual Product Search
- Product Comparison
- Ratings & Reviews
- Order Assistance
"""
)

st.divider()

# ---------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------
with st.sidebar:

    st.header("📷 Visual Search")

    with st.container(border=True):

        st.write(
            "Upload a product image to search for visually similar items available in the store."
        )

        uploaded_file = st.file_uploader(
            "Upload Image",
            type=["jpg", "jpeg", "png", "webp"],
        )

        if uploaded_file:
            st.success("Image uploaded successfully.")
            st.image(uploaded_file, use_container_width=True)

        if uploaded_file and st.button(
            "Find Similar Products",
            use_container_width=True,
        ):

            suffix = os.path.splitext(uploaded_file.name)[1] or ".jpg"

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=suffix,
            ) as tmp:

                tmp.write(uploaded_file.getvalue())
                image_path = tmp.name

            prompt = (
                "I uploaded a product image. "
                "Please analyze it and find similar products in the store. "
                f"Image path: {image_path}"
            )

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt,
                }
            )

            st.session_state.pending_image = uploaded_file.name

            st.rerun()

# ---------------------------------------------------------------------
# Chat state
# ---------------------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------------------------------------------------------
# Welcome card
# ---------------------------------------------------------------------
if not st.session_state.messages:

    st.info(
        """
### Welcome

Try asking questions like:

- Wireless headphones under $100
- Best gaming keyboard
- Compare two smartphones
- Organic honey with 4★ rating

Or upload a product image using the sidebar.
"""
    )

# ---------------------------------------------------------------------
# Chat history
# ---------------------------------------------------------------------
for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        if (
            msg["role"] == "user"
            and msg["content"].startswith("I uploaded a product image")
        ):

            st.markdown("📷 **Searching using uploaded product image...**")

        else:

            st.markdown(msg["content"].replace("$", r"\$"))

# ---------------------------------------------------------------------
# Image search
# ---------------------------------------------------------------------
if (
    st.session_state.messages
    and st.session_state.messages[-1]["role"] == "user"
    and "pending_image" in st.session_state
):

    with st.chat_message("assistant"):

        with st.spinner(
            "Analyzing image • Searching catalog • Ranking products..."
        ):

            result = agent.invoke(
                {"messages": st.session_state.messages}
            )

            response = result["messages"][-1].content.replace("`", "")

        with st.container(border=True):

            st.markdown(response.replace("$", r"\$"))

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    del st.session_state.pending_image

    st.rerun()

# ---------------------------------------------------------------------
# Chat input
# ---------------------------------------------------------------------
if prompt := st.chat_input(
    "Ask about products, prices, ratings or recommendations..."
):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Searching products..."):

            result = agent.invoke(
                {"messages": st.session_state.messages}
            )

            response = result["messages"][-1].content.replace("`", "")

        with st.container(border=True):

            st.markdown(response.replace("$", r"\$"))

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )

    st.rerun()
