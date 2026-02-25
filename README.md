# Hakemusbotti

Hakemusbotti auttaa asiakkaittaan kehittämään työnhakutaitojaan. Erityisesti hakemuskirjeiden kirjoittaminen on vaikeaa ja aikaa vievää.

Botille voi syöttää CV:n ja tarkemman kuvauksen erilaisista työtehtävistä joissa olet toiminut, sekä vanhoja hakemuksia tyylinäytteeksi

Näiden avulla, kun annat avoimen työpaikan kuvauksen, botti osaa hallusinoimatta auttaa sinua hakemuksen kirjottamisessa esimerkiksi etsimällä relevanteimmat työkokemukset ja taidot paikkaan ja auttamalla kirjoittamaan aidosti itsesi näköistä tekstiä.

# How to run

Miten ajetaan, lisää myöhemmin

# Project structure



app-pilot/
├── data/ # Your raw "Source of Truth"
│ ├── work_history.json
│ ├── style_samples.json
│ └── desired_future.json
├── storage/ # Where LlamaIndex saves your Vector DB (auto-generated)
├── app/
│ ├── **init**.py
│ ├── main.py # FastAPI entry point
│ ├── cli.py # "Value-First" script entry point
│ ├── core/
│ │ ├── **init**.py
│ │ ├── engine.py # The RAG / LlamaIndex orchestration logic
│ │ └── prompt_templates.py # Specialized prompts for style/facts
│ ├── models/
│ │ ├── **init**.py
│ │ └── schemas.py # Pydantic models (WorkExperience, JobReq, etc.)
│ ├── services/
│ │ ├── **init**.py
│ │ ├── vector_db.py # Interface/Implementation for ChromaDB/LlamaIndex
│ │ └── llm_service.py # Logic for calling OpenAI/Anthropic
├── tests/ # Recruiters LOVE to see a tests folder
│ └── test_rag_logic.py
├── .env # API Keys (OpenAI, etc.) - DO NOT COMMIT THIS
├── requirements.txt # Dependencies (fastapi, llamaindex, pydantic)
└── README.md # The most important file for your portfolio
