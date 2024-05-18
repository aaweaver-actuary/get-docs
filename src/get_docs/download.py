from bs4 import BeautifulSoup
from langchain_community.document_loaders.recursive_url_loader import RecursiveURLLoader


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
        self.loader = RecursiveURLLoader(
            url=url,
            max_depth=max_depth,
            extractor=lambda x: BeautifulSoup(x, "html.parser").text,
        )
        self.sort_results = sort_results
        self.reverse_results = reverse_results

    def get_docs(self):
        docs = self.loader().load()

        if self.sort_results:
            docs = sorted(docs, key=lambda x: x.metadata["source"])

        if self.reverse_results:
            docs = list(reversed(docs))

        return docs

    def concatenate_docs(self):
        docs = self.get_docs()
        return "\n\n === \n\n".join([doc.page_content for doc in docs])

    