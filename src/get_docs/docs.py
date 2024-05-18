from __future__ import annotations
from bs4 import BeautifulSoup
from langchain_community.document_loaders.recursive_url_loader import (
    RecursiveUrlLoader,
)


class Docs:
    def __init__(
        self,
        url: str,
        max_depth: int = 20,
        sort_results: bool = True,
        reverse_results: bool = True,
    ):
        self.url = url
        self.max_depth = max_depth
        self.loader = RecursiveUrlLoader(
                url=url,
                max_depth=max_depth,
                extractor=lambda x: BeautifulSoup(x, "html.parser").text,
            )
        self.sort_results = sort_results
        self.reverse_results = reverse_results

    def get_docs(self):
        # listdoclist = [loader.load() for loader in self.recursive_loader]
        # docs = [doc for doclist in listdoclist for doc in doclist]

        docs = self.loader.load()

        if self.sort_results:
            docs = sorted(docs, key=lambda x: x.metadata["source"])

        if self.reverse_results:
            docs = list(reversed(docs))

        return docs

    def concatenate_docs(self):
        docs = self.get_docs()
        return "\n\n === \n\n".join([doc.page_content for doc in docs])

    def save_docs(self, path: str):
        docs = self.get_docs()
        with open(path, "w") as f:
            f.write("\n\n === \n\n".join([doc.page_content for doc in docs]))
