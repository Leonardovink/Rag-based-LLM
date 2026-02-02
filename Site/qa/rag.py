from .get_embedding_function import get_embedding_function
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama

CHROMA_PATH = "qa/chroma"

PROMPT_TEMPLATE = """
    You are a medical assistant.
    Answer the question using ONLY the context below.
    If the answer is not contained in the context, say:
    "I dont know based on the provided documents."

    Context:    
    {context}

    ---

    Answer the question based on the above context: {question}
    """
def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=embedding_function
    )
    
    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)
    print(response_text)
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text, sources