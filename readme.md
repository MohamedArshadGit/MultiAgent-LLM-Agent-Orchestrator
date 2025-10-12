This repo contains multiple LLM and Agentic AI experiments — including OpenAI, Ollama, LangGraph, LangChain, and Groq integrations. Each folder or file explores a specific use case or toolchain


** multi_agent_cordination_basic.ipynb **

Loads API keys for OpenAI, Google Gemini, Groq, and Ollama.

Generates a challenging question using OpenAI.

Sends the question to multiple LLMs (OpenAI, Gemini, Groq, Ollama) to get their answers.

Collects all answers and formats them nicely for comparison.

Uses an OpenAI model as a judge to rank the answers of all competitors.

Outputs the final ranking of models in JSON format and prints readable results.

Demonstrates multi-agent coordination and evaluation in an LLM workflow.