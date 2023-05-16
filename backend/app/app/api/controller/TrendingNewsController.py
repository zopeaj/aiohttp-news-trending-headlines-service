from aiohttp.web import RouteTableDef
from fastapi import status



trendingnewsroutes = RouteTableDef()


@trendingnewsroutes.get("/trending-news")
