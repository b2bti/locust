from codecs import encode
import json

boundary = "wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T"

def converter_para_form_data(body={}):
	i = 0
	body_em_lista = []

	chaves = body.keys()
	valores = list(body.values())
	for chave in chaves:
		body_em_lista.append(encode('--' + boundary))
		body_em_lista.append(encode('Content-Disposition: form-data; name=' + chave +';'))
		body_em_lista.append(encode('Content-Type: {}'.format('text/plain')))
		body_em_lista.append(encode(''))
		body_em_lista.append(encode(valores[i]))
		i = i + 1
	body_form_data = b'\r\n'.join(body_em_lista)
	return body_form_data