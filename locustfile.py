from locust import task, between
from locust.contrib.fasthttp import FastHttpUser
import Common.formatacoes


class usuarioFinalQueFazLogin(FastHttpUser):
	host = "https://apidev.sga.bet"

	@task
	def login_usuario_final_mm(self):
		body = {
			"login": "jessicaPersona",
			"password": "mnbvcxz1",
			"operator_code": "Sys"
		}
		with self.rest(
			"POST", 
			"/player/user/login", 
			headers={"x-api-key": "02ff96c8f50ce6a488812146d448a04b2e2358dd45d0dbb59824",
				"gmt": "-03:00",
				"Content-Type": "multipart/form-data; boundary={}".format(Common.formatacoes.boundary),
			}, 
			data=Common.formatacoes.converter_para_form_data(body)
		) as resposta:
			if resposta.status_code == 200:
				print("MM\n")
