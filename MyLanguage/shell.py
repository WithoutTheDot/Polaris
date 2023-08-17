import basic
import basic
import sys
def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]


if len(sys.argv)>1:
	result, error = basic.run(sys.argv[1], f'RUN("{sys.argv[1]}")')
	if error:
		print(remove_last_line_from_string(remove_last_line_from_string(error.as_string())))
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
	sys.exit()


while True:
	fn = '<stdin>'
	text = input('basic > ')
	if text.strip() == "QUIT": break
	if text.strip().startswith("#"):continue
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
