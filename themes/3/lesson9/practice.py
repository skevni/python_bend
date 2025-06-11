

from hashlib import sha256


class MarsURLEncoder:

    def __init__(self):
        self.urls = {}

    def encode(self, long_url: str):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        short_url = ('https://ma.rs/' +
                     hashlib.sha256(long_url.encode("utf-8")).hexdigest())
        self.urls[short_url] = long_url

    def decode(self, short_url: str):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        return self.urls.get(short_url)


mr = MarsURLEncoder()
mr.encode("https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html")
print(mr.decode(
    "https://ma.rs/dcc6ad2289b63dba7c0c14b86786f825db7b1da6e41cdb0924454093591bfd35"
    )
)
