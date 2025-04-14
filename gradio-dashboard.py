import pandas as pd
import numpy as np
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter

import gradio as gr
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
load_dotenv()

books = pd.read_csv("books_with_emotion.csv")
books['large_thumbnail'] = books['thumbnail'] + "&fife=w800"
books['large_thumbnail'] = np.where(
    books['large_thumbnail'].isna(),
    'cover-not-found.jpg',
    books['large_thumbnail'],
)

raw_documents = TextLoader("tagged_description.txt", encoding='utf-8').load()
text_splitter = CharacterTextSplitter(separator="\n", chunk_size=0, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)
db_books = Chroma.from_documents(documents, embedding=embedding_model)

def retrieve_semantic_recommendations(
        query: str,
        category: str = None,
        tone: str = None,
        initial_top_k: int = 50,
        final_top_k: int = 16,
) -> pd.DataFrame:

    recs = db_books.similarity_search(query, k=initial_top_k)
    books_list = [rec.page_content.split()[0] for rec in recs]
    book_recs = books[books['isbn13'].astype(str).isin(books_list)].head(final_top_k)

    if category != "ALL":
        book_recs = book_recs[book_recs['simple_category'] == category][:final_top_k]
    else:
        book_recs = book_recs.head(final_top_k)

    if tone == "Happy":
        book_recs.sort_values(by='joy', ascending=False, inplace=True)
    elif tone == "Angry":
        book_recs.sort_values(by='anger', ascending=False, inplace=True)
    elif tone == "Surprising":
        book_recs.sort_values(by='surprise', ascending=False, inplace=True)
    elif tone == "Suspenseful":
        book_recs.sort_values(by='fear', ascending=False, inplace=True)
    elif tone == "Sad":
        book_recs.sort_values(by='sadness', ascending=False, inplace=True)

    return book_recs

def recommend_books(
        query: str,
        category: str,
        tone: str
):
    recommendations = retrieve_semantic_recommendations(query, category, tone)
    results = []

    for _, row in recommendations.iterrows():
        description = row['description']
        truncated_desc_split = description.split()
        truncated_description = " ".join(truncated_desc_split[:40]) + "..."

        author_split = row['authors'].split(';')
        if len(author_split) == 2:
            author_str = f"{author_split[0]} and {author_split[1]}."
        elif len(author_split) >2:
            author_str = f"{', '.join(author_split[:-1])} and {author_split[-1]}."
        else:
            author_str = row["authors"]

        caption = f"{row['title']} by {author_str}: {truncated_description}"
        results.append((row['large_thumbnail'], caption))

    return results

categories = ["ALL"] + sorted(books['simple_category'].unique())
tones = ["ALL", "Happy", "Surprising", "Angry","Suspenseful", "Sad"]

with gr.Blocks(theme = gr.themes.Glass()) as dashboard:
    gr.Markdown("# Book Recommendation System")

    with gr.Row():
        user_query = gr.Textbox(label="Enter the description of book",
                                placeholder="e.g. A mind provoking story")
        category_dropdown = gr.Dropdown(choices = categories, label="Select a category", value = "ALL")
        tone_dropdown = gr.Dropdown(choices = tones, label="Select a tone", value = "ALL")
        submit_button = gr.Button("Find Recommendations")

    gr.Markdown("## Recommended Books")
    output = gr.Gallery(label="Recommended Books", columns=8, rows = 2)

    submit_button.click(fn = recommend_books,
                        inputs = [user_query,category_dropdown, tone_dropdown],
                        outputs =  output)

if __name__ == "__main__":
    dashboard.launch()