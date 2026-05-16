from PythonInteligênciaArtificialAplicada.ManipulandoStringComIA.IaComPython import perguntar_ia,client

prompt = input("Digite sua pergunta: ")

chat = client.chats.create(model="gemini-3-flash-preview")

while prompt != "1":
    resposta_stream = perguntar_ia(prompt)
    print(resposta_stream)

    print("\n")
    print("Se desejar finalizar, digite 1.")
    prompt = input("Digite sua pergunta: ")


print("Encerrando Chat...")
