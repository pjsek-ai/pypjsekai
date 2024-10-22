from typing import Optional
from mitmproxy import contentviews, flow, ctx, http
# from json import dumps
from pjsekai.utilities import msgpack, unmsgpack, encrypt, decrypt


class ViewProjectSekai(contentviews.View):
    name = "pjsekai"

    def __call__(
        self,
        data: bytes,
        *,
        content_type: Optional[str] = None,
        flow: Optional[flow.Flow] = None,
        http_message: Optional[http.Message] = None,
        **unknown_metadata,
    ) -> contentviews.TViewResult:
        if ctx.options.pjsekai_key is None or ctx.options.pjsekai_iv is None:
            return "pjsekai", contentviews.format_text("")
        try:
            plaintext: bytes = decrypt(
                data, 
                str(ctx.options.pjsekai_key).encode(), 
                str(ctx.options.pjsekai_iv).encode()
            )
            plaintextDict: Optional[dict] = unmsgpack(plaintext)
            # plaintextJson: str = dumps(
            #     plaintextDict, indent=2, ensure_ascii=False)
            return "pjsekai", contentviews.json.format_json(plaintextDict)
        except Exception as e:
            return "pjsekai", contentviews.format_text(e)

    def render_priority(
        self,
        data: bytes,
        *,
        content_type: Optional[str] = None,
        flow: Optional[flow.Flow] = None,
        http_message: Optional[http.Message] = None,
        **unknown_metadata,
    ) -> float:
        if ctx.options.pjsekai_key is None or ctx.options.pjsekai_iv is None:
            return 0
        try:
            _ = decrypt(
                data, 
                str(ctx.options.pjsekai_key).encode(), 
                str(ctx.options.pjsekai_iv).encode()
            )
            return 1
        except Exception as e:
            return 0


view = ViewProjectSekai()


def load(loader):
    loader.add_option(
        name="pjsekai_key",
        typespec=Optional[str],
        default=None,
        help="AES key to decrypt Project Sekai",
    )
    loader.add_option(
        name="pjsekai_iv",
        typespec=Optional[str],
        default=None,
        help="AES iv to decrypt Project Sekai",
    )
    loader.add_option(
        name="pjsekai_time_travel_destination",
        typespec=Optional[int],
        default=None,
        help="Unix timestemp to time travel to for Project Sekai",
    )
    contentviews.add(view)


def done():
    contentviews.remove(view)


def response(flow: http.HTTPFlow) -> None:
    if ctx.options.pjsekai_key is not None and ctx.options.pjsekai_iv is not None and ctx.options.pjsekai_time_travel_destination is not None:
        if flow.request.pretty_url.endswith("/api/system"):
            plaintext: bytes = decrypt(
                flow.response.content,
                ctx.options.pjsekai_key.encode(), 
                ctx.options.pjsekai_iv.encode()
            )
            plaintext_dict: Optional[dict] = unmsgpack(plaintext)
            if plaintext_dict is not None:
                plaintext_dict["serverDate"] = ctx.options.pjsekai_time_travel_destination * 1000
            modified_msgpack: bytes = msgpack(plaintext_dict)
            ciphertext: bytes = encrypt(
                modified_msgpack, 
                ctx.options.pjsekai_key.encode(), 
                ctx.options.pjsekai_iv.encode()
            )
            flow.response.content = ciphertext
