import os
import json

from variety.plugins.IQuoteSource import IQuoteSource

import logging

logger = logging.getLogger("variety")

class QwqSource(IQuoteSource):
	
	file_log:bool = False
	
	def __init__(self):
		super(IQuoteSource, self).__init__()
		self.quotes = []
	
	@classmethod
	def get_info(cls):
		return {
			"name": "Quotes qwq",
			"description": (
					"Show your loved quotes channel message in Telegram.\n"
					"\n"
					"you can simply export a Telegram channel message as the quote source:\n"
					"  just export as JSON file,\n"
					"  then rename it, make sure the file extension is `.tg.json`,\n"
					"  then put it to plugin's config folder: \"~/.config/variety/pluginconfig/quotes-qwq/\",\n"
					"  now you have your favorite quote message in your variety!\n"
					"there's also 10 built-in qwq quotes:\n"
					"  enable it by `touch quotes_qwq.config.built_in_quotes` in config folder."
			),
			"author": "ANNIe Eyre",
			"version": "1.0",
		}
	
	def needs_internet(self):
		return False
	
	def supports_search(self):
		return True
	
	def activate(self):
		
		if self.active:
			return
		
		super(QwqSource, self).activate()
		logger.info("QuotesQwq: Quotes Qwq activated")
		self.echo_log("Quotes Qwq activated")
		
		self.quotes = []
		
		load_built_in:bool = False
		load_test:bool = False
		load_found:bool = False
		logger.info(f"QuotesQwq: finding quotes data in {self.qwq_configs()}")
		self.echo_log(f"finding quotes data in {self.qwq_configs()}")
		# self.echo_log(str.join(" // ", os.listdir(config_path)))
		for f in os.listdir(self.qwq_configs()):
			logger.debug(f"QuotesQwq: checking file {f}")
			self.echo_log(f"checking file {f}")
			if (f.endswith(".tg.json")):
				self.load_tg_source(os.path.join(self.qwq_configs(), f))
				load_found = True
			if (f == "quotes_qwq.config.built_in_quotes"):
				logger.info(f"QuotesQwq: built in quotes enabled by local config.")
				self.echo_log(f"built in quotes enabled by local config.")
				load_built_in = True
				load_found = True
		
		if load_built_in: self.load_inset_resource()
		if load_test: self.load_test_resource()
		
	
	def load_tg_source (self, file_path: str):
		counting: int = 0
		with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
			try:
				content = json.loads(f.read())
				if content["messages"]:
					for message in content["messages"]:
						if message["type"] == "message":
							try:
								quote:str = ""
								author:str = None
								sourceName:str = None
								link:str = None
								for txt_obj in message["text_entities"]:
									quote += txt_obj["text"]
								try: author = message["forwarded_from"]
								except: author = f"<{message['from']}>"
								sourceName = os.path.basename(file_path)
								link = f"https://t.me/c/{content['id']}/{message['id']}"
								self.quotes.append({"quote": quote, "author": author, "sourceName": sourceName, "link": link})
								counting += 1
							except Exception:
								logger.warn(f"QuotesQwq: parse TG Quotes in {os.path.basename(file_path)}, id {message['id']} failed: {Exception}")
								self.echo_log(f"parse TG Quotes in {os.path.basename(file_path)}, id {message['id']} failed: {Exception}")
			except Exception:
				logger.warn(f"QuotesQwq: parse TG Quotes File failed: {Exception}")
				self.echo_log(f"parse TG Quotes File failed: {Exception}")
		logger.info(f"QuotesQwq: load tg data {os.path.basename(file_path)} complete, {counting} quotes added.")
		self.echo_log(f"load tg data {os.path.basename(file_path)} complete, {counting} quotes added.")
	
	# ???????????????????????????????????????
	# ????????? tg ?????? @hESUchan (https://t.me/hESUchan) ???????????????
	# ??????????????????????????????????????????????????????
	def load_test_resource(self):
		self.quotes.append({"quote": "??????502 bad gateway???x", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		self.quotes.append({"quote": "?????????bra???mai??????", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		self.quotes.append({"quote": "?????????????????????x", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		self.quotes.append({"quote": "??????hrh????????????bushi", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		self.quotes.append({"quote": "?????????z???????????????????????????", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		self.quotes.append({"quote": "???????????????????????????????????????", "author": "qwq", "sourceName": "QwqSource Test Inset"})
		logger.debug("load <telegram @hESUchan> test use inset resource")
		self.echo_log("load <telegram @hESUchan> test use inset resource")
	
	# ??????????????????????????? telegram @hasuchanbot (tg://user?id=1014656686) ??????????????????????????????
	# (??????????????? ?????? page#4 (31 - 40))
	def load_inset_resource(self):
		self.quotes.append({"quote": "????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "????????????????????????????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "?????????????????????????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "??????????????????????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "???????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "????????????piggy??????????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		self.quotes.append({"quote": "???????????????", "author": "qwq", "sourceName": "QwqSource Inset"})
		logger.info("QuotesQwq: load <telegram @hasuchanbot> inset resource")
		self.echo_log("load <telegram @hasuchanbot> inset resource")
	
	def deactivate(self):
		self.quotes = []
		logger.info("QuotesQwq: Quotes Qwq deactivated")
		self.echo_log("Quotes Qwq deactivated")
	
	def get_random(self):
		return self.quotes
	
	def get_for_author(self, author):
		return [q for q in self.quotes if q["author"] and q["author"].lower().find(author.lower()) >= 0]
	
	def get_for_keyword(self, keyword):
		return self.get_for_author(keyword) + \
				[q for q in self.quotes if q["quote"].lower().find(keyword.lower()) >= 0]
	
	def qwq_configs (self):
		return os.path.join(self.get_config_folder(), "..", "quotes-qwq")
	
	def echo_log (self, msg: str):
		if self.file_log:
			with open(os.path.join(self.qwq_configs(), "quotes_qwq.log"), "a", encoding="utf-8", errors="ignore") as file:
				file.write(msg+"\n")
		return

