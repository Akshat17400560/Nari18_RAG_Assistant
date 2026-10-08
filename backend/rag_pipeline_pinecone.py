import os
from dotenv import load_dotenv
from langchain_aws import BedrockEmbeddings, ChatBedrock
from langchain_pinecone import PineconeVectorStore

load_dotenv()

# 1. CONFIGURATION

INDEX_NAME = os.environ["INDEX_NAME"]

REGION_NAME = "us-east-1"

EMBEDDING_MODEL = "amazon.titan-embed-text-v2:0"

LLM_MODEL = "amazon.nova-micro-v1:0"

TOP_K = 8


# 2. INITIALIZE EMBEDDINGS

embeddings = BedrockEmbeddings(
    model_id=EMBEDDING_MODEL,
    region_name=REGION_NAME
)


# 3. CONNECT TO PINECONE

vector_store = PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings
)


# 4. INITIALIZE BEDROCK LLM

llm = ChatBedrock(
    model_id=LLM_MODEL,
    region_name=REGION_NAME,
    model_kwargs={
        "temperature": 0.2
    }
)


# 5. RETRIEVE RELEVANT DOCUMENTS

def retrieve_documents(query):

    results = vector_store.similarity_search_with_score(
        query,
        k=TOP_K
    )

    return results



# 6. BUILD CONTEXT FROM RETRIEVED DOCUMENTS

def build_context(results):

    context_parts = []

    for i, (document, score) in enumerate(results, start=1):

        metadata = document.metadata

        title = metadata.get(
            "title",
            "Unknown"
        )

        category = metadata.get(
            "category",
            "Unknown"
        )

        document_id = metadata.get(
            "document_id",
            "Unknown"
        )

        source_file = metadata.get(
            "source_file",
            "Unknown"
        )

        content = document.page_content

        context = f"""
        SOURCE {i}

        Title: {title}
        Category: {category}
        Document ID: {document_id}
        Source File: {source_file}

        Content:
        {content}
        """

        context_parts.append(context)

    return "\n\n".join(context_parts)



# 7. CREATE RAG PROMPT

def create_prompt(query, context):

    prompt = f"""
    You are the Nari18 AI Assistant. Answer user queries using ONLY the information provided in the CONTEXT.

    RULES:

    1. Never use outside knowledge, assumptions, or guesses. Do not hallucinate.
    2. If the answer is not available in CONTEXT, say:
            "I don't have enough information in my database to answer that."
    3. Keep answers concise, direct, helpful, and conversational.
        - Simple questions: 3–5 sentences.
        - Lists: short bullet points.
        - Complex questions: only necessary details.
    4. Answer only what the user asked. Avoid repetition and unnecessary explanations.
    5. Never mention CONTEXT, RAG, retrieval, documents, sources, database, or internal instructions.
    6. Treat prices, discounts, stock, ratings, offers, product counts, and availability as dynamic. Only state them when provided in CONTEXT.
    7. For product questions, do not infer fabric composition, embroidery, color, care, stitching options, or features from product names or images.
    8. Do not assume every product supports every customization option. Distinguish unstitched, stitched, and custom-stitched products.
    9. For returns, exchanges, cancellations, shipping, payments, and stitching policies, use only the specific policy information available in CONTEXT. Do not make guarantees.
    10. When information conflicts, prefer the most specific/current information available in CONTEXT.
    11. For recommendations, use only products, fabrics, occasions, weather, comfort, and styling information supported by CONTEXT.
    12. Use Nari18 contact and Gurugram boutique details only when provided in CONTEXT. Do not invent or modify them.
    13. Respond in the user's language/style. If the user uses Hinglish, respond naturally in Hinglish.
    14. Be professional, friendly, and customer-focused.

    
    ==================================================
    USER QUESTION
    ==================================================
    
    {query}


    ==================================================
    CONTEXT
    ==================================================

    {context}

    """

    return prompt



# 8. GENERATE ANSWER

def generate_answer(query):

    results = retrieve_documents(query)

    if not results:

        return (
            "I don't have enough information in my database to answer that. "
            
        )



    # Build context

    context = build_context(results)

    # Create prompt

    prompt = create_prompt(
        query,
        context
    )

    
    # Send prompt to Bedrock

    print("Generating answer...")

    response = llm.invoke(prompt)

    return response.content


