# agentic-product-discovery-platform

An **Agentic AI-powered retail assistant** that enables intelligent product discovery through natural language conversations and visual search. The application combines Large Language Models (LLMs), tool calling, multimodal reasoning, and structured product retrieval to deliver personalized shopping recommendations and streamline the retail purchasing workflow.

---

## Overview

Traditional e-commerce platforms rely heavily on keyword-based search and static filters, making product discovery inefficient for users with complex requirements. This project demonstrates how an **Agentic AI system** can understand user intent, autonomously coordinate multiple tools, retrieve structured product information, analyze uploaded product images, and guide users through an end-to-end shopping experience.

The assistant supports conversational product search, visual product discovery, product comparison, customer rating retrieval, order placement, and graceful handling of out-of-scope queries through an intuitive Streamlit interface.

---

## Key Features

- Agentic AI workflow with autonomous tool selection
- Natural language product search
- Multimodal product discovery using text and images
- Image-based product understanding with Vision LLMs
- Intelligent product recommendations
- Product comparison
- Customer ratings and review retrieval
- Price and organic-product filtering
- Conversational shopping experience
- Order placement workflow
- Graceful handling of out-of-scope and unsupported queries
- Interactive Streamlit interface

---

## Tech Stack

### Languages & Frameworks

- Python
- Streamlit
- LangChain

### AI Technologies

- Agentic AI
- Large Language Models (LLMs)
- Vision Language Models
- Tool Calling
- Multimodal AI

### Database

- SQLite

### Development

- uv

---

## System Architecture

```
                     User
                       │
                       ▼
              Streamlit Interface
                       │
                       ▼
          Agentic AI Shopping Assistant
                       │
         ┌─────────────┼─────────────┐
         ▼             ▼             ▼
 Product Search   Ratings Engine  Vision Analysis
         │             │             │
         └─────────────┼─────────────┘
                       ▼
           SQLite Product Database
                       │
                       ▼
      Personalized Recommendations
                       │
                       ▼
             Purchase Confirmation
```

---

## Example Queries

- Wireless headphones under $100
- Organic honey with a rating above 4.5
- Compare gaming keyboards
- Find products similar to this uploaded image
- Order the second product

---

## Project Highlights

- Built an **Agentic AI application** capable of autonomously selecting and coordinating multiple tools to satisfy complex shopping requests.
- Integrated multimodal reasoning to support both natural language and image-based product discovery.
- Combined structured database retrieval with LLM reasoning to generate personalized product recommendations.
- Implemented an end-to-end retail workflow including product search, ratings retrieval, image analysis, and purchase assistance.
- Designed the assistant to recognize and appropriately respond to out-of-domain or unsupported user requests while maintaining a coherent conversational experience.

---

## Repository Notes

- Local environment variables (`.env`) have been intentionally excluded from the repository to protect API credentials.
- The project was developed using **uv** for dependency and environment management. Local environment configuration and lock files have been intentionally omitted to keep the repository focused on the application code.
- Create a `.env` file with the required API credentials before running the application.

---

## Future Enhancements

- Personalized recommendations based on user preferences
- Shopping cart and wishlist management
- Inventory availability tracking
- Hybrid semantic and keyword search
- User authentication
- Multi-agent retail workflows
- Recommendation explanations and reasoning
