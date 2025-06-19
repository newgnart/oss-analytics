import os
import dlt
from dlt.sources.helpers.rest_client import RESTClient
from dlt.sources.helpers.rest_client.auth import BearerTokenAuth
from dlt.sources.helpers.rest_client.paginators import HeaderLinkPaginator

BASE_URL = "https://api.github.com/repos"


@dlt.resource()
def paginated_getter(repo: str, endpoint: str, token: str):
    client = RESTClient(
        base_url=f"{BASE_URL}/{repo}",
        auth=BearerTokenAuth(token=token),
        paginator=HeaderLinkPaginator(links_next_key="next"),
    )

    for page in client.paginate(endpoint):
        yield page
