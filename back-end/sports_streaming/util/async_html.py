from requests_html import AsyncHTMLSession
import pyppeteer


# https://github.com/psf/requests-html/issues/293#issuecomment-536320351
class AsyncHTMLSessionFixed(AsyncHTMLSession):
  """
  pip3 install websockets==6.0 --force-reinstall
  """
  def __init__(self, **kwargs):
    super(AsyncHTMLSessionFixed, self).__init__(**kwargs)
    self.__browser_args = kwargs.get("browser_args", ["--no-sandbox"])

  @property
  async def browser(self):
    if not hasattr(self, "_browser"):
      self._browser = await pyppeteer.launch(
        ignoreHTTPSErrors=not(self.verify),
        headless=True, handleSIGINT=False,
        handleSIGTERM=False, handleSIGHUP=False,
        args=self.__browser_args
      )
    return self._browser
