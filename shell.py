import basic
import basic

while True:
	fn = '<stdin>'
	text = input('basic > ')
	if text == "QUIT": break
	if text.strip().startswith("RUN"):
		fn = f"""'{text.strip()[5:].replace('")', '')}'"""
	if text.strip() == "": continue
	result, error = basic.run(fn, text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
