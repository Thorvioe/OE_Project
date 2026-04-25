Task Decomposition Document:

Project: Internship Opportunity Finder:

1. Objective

The goal of this project is to build an AI-powered system that:

Accepts a user query (e.g., “Data Science internships”)
Searches real-time internship listings
Uses AI to filter and structure results
Returns clean, relevant opportunities

2. Task Breakdown (File-wise Mapping)

Task 1: User Input Handling
File: app.py

Subtasks:

Accept user query (role, domain, location)
Validate input
Pass query to agent layer
Display formatted results

Responsibility:
Acts as the entry point and controller


Task 2: AI Processing & Orchestration
File: agent.py

Subtasks:

Receive query from app.py
Call internship search function
Process results using LLM
Filter irrelevant listings
Format output (clean structure)

Responsibility:
Handles core intelligence of system


Task 3: Internship Search Function
🔧 Function: search_internships()

Subtasks:

Build API query
Send request to Tavily API
Fetch raw job listings
Return unstructured data

Responsibility:
Handles data retrieval

Task 4: External API Integration
APIs Used:
Tav
ily API
LLM API (Google GenAI / OpenAI)

Subtasks:

Connect APIs securely using keys
Handle API responses
Manage errors (timeouts, invalid keys)


Task 5: Configuration Management
File: .env

Subtasks:

Store API keys securely
Load environment variables in code
File: requirement.txt

Subtasks:

List all dependencies
Ensure reproducibility


Task 6: Documentation
File: README.md

Subtasks:

Project description
Setup instructions
Usage guide
Architecture overview


3. Workflow Decomposition
Step 1: User enters query
Step 2: app.py receives input
Step 3: agent.py processes query
Step 4: search_internships() fetches data
Step 5: Tavily API returns raw listings
Step 6: LLM filters + structures data
Step 7: Clean results returned to user

4. Functional Decomposition
Module	Function	Description
app.py	Input/Output	Handles interaction
agent.py	Processing	AI logic & orchestration
search_internships	Data Fetching	Retrieves internships
APIs	External Services	Provide data + intelligence
.env	Config	Secure keys
requirement.txt	Dependency	Environment setup
README.md	Documentation	Project explanation


5. Non-Functional Tasks
Security → API keys in .env
Performance → Efficient API calls
Scalability → Add more agents later
Modularity → Separate files for each task


6. Future Task Decomposition
Add multi-agent system (listing, critic, ranking)
Add database (store internships)
Build frontend UI
Add recommendation system

7. Final Summary (Use in Report)

The system is decomposed into modular tasks including input handling, AI processing, data retrieval, and external API integration, ensuring scalability, maintainability, and efficient internship discovery.