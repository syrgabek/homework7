import hashlib
from aiogram import types, Dispatcher
from youtube_search import YoutubeSearch

# def finder(text):
#     result = YoutubeSearch(text, max_results=10).to_dict()
#     return result
#
# async def inline_youtube_handler(query: types.InlineQuery):
#     text = query.query or "echo"
#     links = finder(text)
#     articles = [
#         types.InlineQueryResultArticle(
#             id=hashlib.md5(f"{link['id']}".encode()).hexdigest(),
#             title=f"{link['title']}",
#             url=f"https://youtube.com/watch?v={link['id']}",
#             thumb_url=f"{link['thumbnails'][0]}",
#             input_message_content=types.InputTextMessageContent(
#                 message_text=f"https://youtube.com/watch?v={link['id']}"
#             )
#         ) for link in links
#     ]
#     await query.answer(articles, cache_time=60, is_personal=True)
#
# async def inline_wiki(query: types.InlineQuery):
#     text = query.query or "echo"
#     links= "https://en.wikipedia.org/wiki/" + text
#     result_id: str = hashlib.md5(text.encode()).hexdigest()
#     articles = [
#         types.InlineQueryResultArticle(
#             id=result_id,
#             title="Wikipedia:",
#             url=links,
#             input_message_content=types.InputTextMessageContent(
#                 message_text=links
#
#             )
#         )
#     ]
#     await query.answer(articles, cache_time=2, is_personal=True)



async def inline_google(query: types.InlineQuery):
    text = query.query or "echo"
    links= "https://www.google.com/search?q=" + text
    result_id: str = hashlib.md5(text.encode()).hexdigest()
    articles = [
        types.InlineQueryResultArticle(
            id=result_id,
            title="Google:",
            url=links,
            input_message_content=types.InputTextMessageContent(
                message_text=links

            )
        )
    ]
    await query.answer(articles, cache_time=2, is_personal=True)

def register_handlers_inline(dp: Dispatcher):
    # dp.register_inline_handler(inline_youtube_handler)
    dp.register_inline_handler(inline_google)
